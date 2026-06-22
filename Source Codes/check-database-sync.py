#!/usr/bin/env python3
import os
import re
import json
import importlib
import sys
from pathlib import Path
from collections import Counter

# DATABASE VERSION CONFIGURATION (Change this for future versions)
DATABASE_VERSION = "3.0"

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def parse_json_structure(json_path):
    ib_hashes = set()
    other_hashes = set()
    hex_pattern = re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE)
    
    def walk(d):
        if isinstance(d, dict):
            for k, v in d.items():
                if k.lower() == 'ib' and isinstance(v, str) and hex_pattern.match(v):
                    ib_hashes.add(v.lower())
                elif isinstance(v, str) and hex_pattern.match(v):
                    other_hashes.add(v.lower())
                else:
                    walk(v)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, str) and hex_pattern.match(item):
                    other_hashes.add(item.lower())
                else:
                    walk(item)
                    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            walk(data)
    except Exception as e:
        print(f"{Colors.RED}Failed to read {json_path}: {e}{Colors.RESET}")
    return ib_hashes, other_hashes

def parse_txt_transitions(txt_path):
    transitions = []
    try:
        content = txt_path.read_text(encoding='utf-8')
    except Exception:
        try:
            content = txt_path.read_text(encoding='gb2312')
        except Exception:
            return []
            
    lines = content.splitlines()
    current_char = ""
    for line in lines:
        char_match = re.match(r'^\s*([^,:\s]+)', line)
        if char_match:
            potential_char = char_match.group(1)
            if not any(word in potential_char for word in ["以下", "新增", "头发", "NormalMap", "Diffuse", "LightMap", "MaterialMap", "Position", "Texcoord", "Blend"]):
                current_char = potential_char
        
        matches = re.findall(r'([a-f0-9]{8})\s*->\s*([a-f0-9]{8})', line, re.IGNORECASE)
        for old_h, new_h in matches:
            transitions.append({
                'char_hint': current_char,
                'old': old_h.lower(),
                'new': new_h.lower(),
                'line': line.strip()
            })
    return transitions

def build_py_hash_index(py_data_path, mock_command_classes):
    init_file = py_data_path / '__init__.py'
    if not init_file.exists():
        return {}, {}, {}
        
    try:
        content = init_file.read_text(encoding='utf-8')
    except Exception:
        content = init_file.read_text(encoding='gb2312')
        
    characters_match = re.search(r'CHARACTERS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not characters_match:
        return {}, {}, {}
        
    registered_chars = re.findall(r"['\"](.*?)['\"]", characters_match.group(1))
    
    hash_to_module = {}
    module_to_hashes = {}
    module_to_char_info = {}
    
    sys.path.insert(0, str(py_data_path.parent))
    try:
        for character_name in registered_chars:
            try:
                module = importlib.import_module(f'PlayerCharacterPYData.{character_name}')
                py_commands = module.get_hash_commands(**mock_command_classes)
                py_hashes = {h.lower() for h in py_commands.keys()}
                
                module_to_hashes[character_name] = py_hashes
                for h in py_hashes:
                    if h not in hash_to_module:
                        hash_to_module[h] = []
                    hash_to_module[h].append(character_name)
                    
                char_info = getattr(module, 'CHARACTER_INFO', None)
                if char_info and isinstance(char_info, dict):
                    module_to_char_info[character_name] = char_info
                else:
                    module_to_char_info[character_name] = {}
            except Exception:
                module_to_hashes[character_name] = set()
                module_to_char_info[character_name] = {}
                continue
    finally:
        sys.path.remove(str(py_data_path.parent))
        
    return hash_to_module, module_to_hashes, module_to_char_info

def longest_common_substring_length(s1, s2):
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
    longest = 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                longest = max(longest, m[x][y])
    return longest

def clean_name(name):
    name_no_ext = Path(name).stem
    # Extract only letters and digits (removing Chinese characters, spaces, and punctuation)
    latin_and_digits = "".join(re.findall(r'[a-zA-Z0-9]+', name_no_ext))
    return latin_and_digits.lower()

def has_name_match(json_name, mod_name, module_to_char_info=None):
    c1 = clean_name(json_name)
    
    # Generate all possible name candidates for the module to check against
    candidates = [mod_name]
    if module_to_char_info and mod_name in module_to_char_info:
        info = module_to_char_info[mod_name]
        if 'name' in info:
            candidates.append(info['name'])
        if 'display_name' in info:
            candidates.append(info['display_name'])
        if 'base_character' in info:
            candidates.append(info['base_character'])
            
    for candidate in candidates:
        c2 = clean_name(candidate)
        if not c2:
            continue
            
        # 1. Direct substring match (e.g., "wise" in "wiseoathofskies")
        if c1 in c2 or c2 in c1:
            return True
            
        # 2. Common prefix match (e.g., "janeskin" and "janedoenocturneoflight" share "jane")
        common_prefix_len = 0
        for i in range(min(len(c1), len(c2))):
            if c1[i] == c2[i]:
                common_prefix_len += 1
            else:
                break
                
        min_len = min(len(c1), len(c2))
        required_prefix_len = min(min_len, 3) # Using 3 to support short names like "Ben"
        if common_prefix_len >= required_prefix_len:
            return True
            
    return False

def find_associated_modules(json_filename, json_ib_hashes, json_all_hashes, hash_to_module, module_to_hashes, module_to_char_info):
    associated = set()
    methods = []
    
    ib_matches = set()
    for h in json_ib_hashes:
        if h in hash_to_module:
            ib_matches.update(hash_to_module[h])
    if ib_matches:
        associated.update(ib_matches)
        methods.append("IB Hash Trail (Highly Accurate)")
    
    name_matches = set()
    for character_name in module_to_hashes.keys():
        if has_name_match(json_filename, character_name, module_to_char_info):
            name_matches.add(character_name)
    if name_matches:
        associated.update(name_matches)
        methods.append("Name Similarity (Accurate)")
        
    if not associated:
        component_matches = set()
        for h in json_all_hashes:
            if h in hash_to_module:
                if len(hash_to_module[h]) <= 2:
                    component_matches.update(hash_to_module[h])
        if component_matches:
            associated.update(component_matches)
            methods.append("Component Hash Trail (Accurate)")
            
    # Strict name filtering based on prefix similarity
    if len(associated) > 1:
        strict_associated = set()
        for mod_name in associated:
            if has_name_match(json_filename, mod_name, module_to_char_info):
                strict_associated.add(mod_name)
        if strict_associated:
            associated = strict_associated
            
    # Unique IB Hash Disambiguation (Intelligent Outfit/Skin Splitting)
    # Automatically splits distinct outfits while keeping same-outfit split files grouped
    if len(associated) > 1:
        unique_ib_counts = {mod_name: 0 for mod_name in associated}
        for h in json_ib_hashes:
            defining_mods = [mod for mod in associated if h in module_to_hashes[mod]]
            if len(defining_mods) == 1:
                unique_ib_counts[defining_mods[0]] += 1
                
        max_unique = max(unique_ib_counts.values()) if unique_ib_counts else 0
        if max_unique > 0:
            associated = {mod_name for mod_name, count in unique_ib_counts.items() if count == max_unique}
            
    return list(associated), " + ".join(methods) if methods else "Unidentified"

def check_sync():
    base_path = Path('.')
    py_data_path = base_path / 'Assets' / 'PlayerCharacterPYData'
    json_folder = base_path / 'ZZZHashIDCharactersDatabase' / f'Database_{DATABASE_VERSION}'
    
    if not json_folder.exists():
        print(f"{Colors.RED}✖ Error: Database folder not found at: {json_folder.resolve()}{Colors.RESET}")
        return
        
    def log(*args, **kwargs): pass
    def update_hash(*args, **kwargs): pass
    def comment_sections(*args, **kwargs): pass
    def comment_commandlists(*args, **kwargs): pass
    def remove_section(*args, **kwargs): pass
    def remove_indexed_sections(*args, **kwargs): pass
    def capture_section(*args, **kwargs): pass
    def create_new_section(*args, **kwargs): pass
    def transfer_indexed_sections(*args, **kwargs): pass
    def multiply_section_if_missing(*args, **kwargs): pass
    def add_ib_check_if_missing(*args, **kwargs): pass
    def add_section_if_missing(*args, **kwargs): pass
    def zzz_13_remap_texcoord(*args, **kwargs): pass
    def zzz_12_shrink_texcoord_color(*args, **kwargs): pass
    def update_buffer_blend_indices(*args, **kwargs): pass
    
    command_classes = {
        'log': log,
        'update_hash': update_hash,
        'comment_sections': comment_sections,
        'comment_commandlists': comment_commandlists,
        'remove_section': remove_section,
        'remove_indexed_sections': remove_indexed_sections,
        'capture_section': capture_section,
        'create_new_section': create_new_section,
        'transfer_indexed_sections': transfer_indexed_sections,
        'multiply_section_if_missing': multiply_section_if_missing,
        'add_ib_check_if_missing': add_ib_check_if_missing,
        'add_section_if_missing': add_section_if_missing,
        'zzz_13_remap_texcoord': zzz_13_remap_texcoord,
        'zzz_12_shrink_texcoord_color': zzz_12_shrink_texcoord_color,
        'update_buffer_blend_indices': update_buffer_blend_indices
    }

    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} ZZZ Mod Fixer - Database Synchronization Analysis {DATABASE_VERSION} (FLEXIBLE){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    
    hash_to_module, module_to_hashes, module_to_char_info = build_py_hash_index(py_data_path, command_classes)
    
    critical_errors = 0
    serious_errors = 0
    missing_hashes_count = 0

    # Tracking set to avoid redundant printing
    flagged_swapped_modules = set()
    
    for json_file in sorted(json_folder.glob('*.json')):
        filename = json_file.name
        
        ib_hashes, other_hashes = parse_json_structure(json_file)
        all_json_hashes = ib_hashes | other_hashes
        
        associated_modules, method = find_associated_modules(filename, ib_hashes, all_json_hashes, hash_to_module, module_to_hashes, module_to_char_info)
        
        is_missing_or_empty = False
        if not associated_modules:
            is_missing_or_empty = True
        else:
            total_hashes = sum(len(module_to_hashes.get(mod, set())) for mod in associated_modules)
            if total_hashes == 0:
                is_missing_or_empty = True

        if is_missing_or_empty:
            critical_errors += 1
            print(f"{Colors.RED}[✖ MISSING MODULE OR EMPTY CHARACTER PYTHON FILE] Database file: '{filename}'{Colors.RESET}")
            print(f"{Colors.YELLOW}                                                     No matching physical Python file or empty Python file in your project!\n{Colors.RESET}")
            continue
            
        swapped_modules_in_group = set()
        safe_modules_in_group = []
        
        for mod in associated_modules:
            char_info = module_to_char_info.get(mod, {})
            declared_name = char_info.get('name')
            is_this_swapped = False
            
            if declared_name:
                if mod.lower() != declared_name.lower():
                    is_this_swapped = True
                    swapped_modules_in_group.add(mod)
                    if mod not in flagged_swapped_modules:
                        flagged_swapped_modules.add(mod)
                        serious_errors += 1
                        print(f"{Colors.RED}[✖ CHARACTER FILE HASH CONTENT SWAPPED WITH ANOTHER CHARACTER] Module: {mod}.py{Colors.RESET}")
                        print(f"                                                                Name in file: '{mod}'")
                        print(f"                                                                Name in CHARACTER_INFO: '{declared_name}'")
                        print(f"{Colors.YELLOW}                                                                Please fix the content of your Python file first!\n{Colors.RESET}")
                    break
            
            if not is_this_swapped:
                safe_modules_in_group.append(mod)
        
        if not safe_modules_in_group:
            continue

        combined_py_hashes = set()
        for mod in safe_modules_in_group:
            if mod in module_to_hashes:
                combined_py_hashes.update(module_to_hashes[mod])
                
        missing_hashes = all_json_hashes - combined_py_hashes
        if missing_hashes:
            missing_hashes_count += 1
            modules_display = ", ".join([f"{m}.py" for m in sorted(safe_modules_in_group)])
            
            if len(safe_modules_in_group) > 1:
                module_type_label = "Group Module"
            else:
                module_type_label = "Individual Module"
                
            print(f"{Colors.RED}[✖ UNSYNCHRONIZED HASH] {module_type_label}: {modules_display}{Colors.RESET}")
            print(f"                        Matches with: {filename} via {Colors.BLUE}{method}{Colors.RESET}")
            print(f"                        Found {Colors.YELLOW}{len(missing_hashes)}{Colors.RESET} hashes missing from your Python file group:")
            for h in sorted(missing_hashes):
                print(f"                        - {Colors.YELLOW}{h}{Colors.RESET}")
            print()
            
    if critical_errors == 0 and serious_errors == 0 and missing_hashes_count == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] JSON VERIFICATION SUCCESS: All model database .json files are synchronized and secure with your Python files!\n{Colors.RESET}")

    print(f"\n{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} ZZZ Mod Fixer - Change Log Synchronization Analysis (.txt){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    
    txt_errors = 0
    for txt_file in sorted(json_folder.parent.glob('*.txt')):
        if "说明" in txt_file.name or "readme" in txt_file.name.lower():
            continue
            
        transitions = parse_txt_transitions(txt_file)
        if not transitions:
            continue
            
        print(f"\nAnalyzing transition log: {Colors.BLUE}'{txt_file.name}'{Colors.RESET} ({Colors.BOLD}{len(transitions)}{Colors.RESET} transitions found)")
        
        for trans in transitions:
            old_h = trans['old']
            new_h = trans['new']
            
            target_mods = set()
            if new_h in hash_to_module:
                target_mods.update(hash_to_module[new_h])
            if old_h in hash_to_module:
                target_mods.update(hash_to_module[old_h])
                
            if not target_mods and trans['char_hint']:
                clean_hint = clean_name(trans['char_hint'])
                for character_name in module_to_hashes.keys():
                    clean_mod = clean_name(character_name)
                    if clean_hint in clean_mod or clean_mod in clean_hint:
                        target_mods.add(character_name)
                        
            if not target_mods:
                continue
                
            for character_name in target_mods:
                try:
                    sys.path.insert(0, str(py_data_path.parent))
                    module = importlib.import_module(f'PlayerCharacterPYData.{character_name}')
                    py_commands = module.get_hash_commands(**command_classes)
                    sys.path.remove(str(py_data_path.parent))
                    
                    if old_h not in py_commands:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ MISSING TRANSITION] Module: {character_name}.py{Colors.RESET}")
                        print(f"                     Old hash '{Colors.YELLOW}{old_h}{Colors.RESET}' not found in Python file!")
                        print(f"                     Log: {trans['line']}")
                        continue
                        
                    commands_list = py_commands[old_h]
                    has_update_call = False
                    correct_target = False
                    actual_target = None
                    
                    for cmd in commands_list:
                        if isinstance(cmd, tuple) and len(cmd) >= 1:
                            func = cmd[0]
                            if hasattr(func, '__name__') and func.__name__ == 'update_hash':
                                has_update_call = True
                                if len(cmd) >= 2 and isinstance(cmd[1], tuple) and len(cmd[1]) >= 1:
                                    actual_target = cmd[1][0].lower()
                                    if actual_target == new_h:
                                        correct_target = True
                                        break
                                        
                    if not has_update_call:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ INCORRECT TRANSITION] Module: {character_name}.py{Colors.RESET}")
                        print(f"                     Hash '{Colors.YELLOW}{old_h}{Colors.RESET}' is registered, but does not have 'update_hash' command!")
                        print(f"                     Log: {trans['line']}")
                    elif not correct_target:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ INCORRECT TARGET] Module: {character_name}.py{Colors.RESET}")
                        print(f"                   Hash '{Colors.YELLOW}{old_h}{Colors.RESET}' updates to '{Colors.RED}{actual_target}{Colors.RESET}',")
                        print(f"                   should point to '{Colors.GREEN}{new_h}{Colors.RESET}' according to log!")
                        print(f"                   Log: {trans['line']}")
                        
                except Exception as e:
                    print(f"{Colors.RED}[✖] Failed to analyze module {character_name} for transition: {e}{Colors.RESET}")
                    
    if txt_errors == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] TXT VERIFICATION SUCCESS: All transition logs .txt are successfully validated in your Python files!\n{Colors.RESET}")

    print(f"\n{Colors.BOLD}{Colors.CYAN}=========================== CONCLUSION ==========================={Colors.RESET}")
    if critical_errors == 0 and serious_errors == 0 and missing_hashes_count == 0 and txt_errors == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] SYNCHRONIZATION SUCCESS: All your Python modules are perfectly synchronized with the JSON & .txt logs!{Colors.RESET}")
    else:
        print(f"{Colors.BOLD}{Colors.RED}[✖] SYNCHRONIZATION FAILED:{Colors.RESET}")
        if critical_errors > 0:
            print(f"    - Found {Colors.RED}{critical_errors}{Colors.RESET} cases of Missing Module or Empty Python file.")
        if serious_errors > 0:
            print(f"    - Found {Colors.RED}{serious_errors}{Colors.RESET} cases of Python file hash content swapped with another character.")
        if missing_hashes_count > 0:
            print(f"    - Found {Colors.RED}{missing_hashes_count}{Colors.RESET} groups of Python modules with hashes out of sync with the JSON database.")
        if txt_errors > 0:
            print(f"    - Found {Colors.RED}{txt_errors}{Colors.RESET} transition synchronization errors in .txt log.")
        print(f"\n    {Colors.YELLOW}Please fix the mismatches listed above for successful synchronization.{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")

if __name__ == '__main__':
    check_sync()