# Originally written by petrascyll
# Thanks to Leotorrez, CaveRabbit, and SilentNightSound for help
# Join AGMG: discord.gg/agmg

# 1.6 Hashes updated by HammyCatte
# 1.7 Hashes updated by shaojiang

# 2.5 update with dyanmic character data overhaul by ConfoundedHermit

# Last Updated: 2026-06-22
# Game Version at time of update: 3.0

import os
import re
import time
import struct
import argparse
import traceback

from dataclasses import dataclass, field
from pathlib import Path

# extra precaution to not 'fix' 
# the same buffer multiple times
global_modified_buffers: dict[str, list[str]] = {}


def main():
    parser = argparse.ArgumentParser(
        prog="ZZZ Fix 3.0 by ConfoundedHermit",
        description=('')
    )

    parser.add_argument('ini_filepath', nargs='?', default=None, type=str)
    args = parser.parse_args()

    if args.ini_filepath:
        if args.ini_filepath.endswith('.ini'):
            print('Passed .ini file:', args.ini_filepath)
            upgrade_ini(args.ini_filepath)
        else:
            raise Exception('Passed file is not an Ini')

    else:
        # Change the CWD to the directory this script is in
        # Nuitka: "Onefile: Finding files" in https://nuitka.net/doc/user-manual.pdf 
        # I'm not using Nuitka anymore but this distinction (probably) also applies for pyinstaller
        # os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
        print('CWD: {}'.format(os.path.abspath('.')))
        process_folder('.')

    print('Done!')


# SHAMELESSLY (mostly) ripped from genshin fix script
def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.upper().startswith('DISABLED') and filename.lower().endswith('.ini'):
            continue
        if filename.upper().startswith('DESKTOP'):
            continue

        filepath = os.path.join(folder_path, filename)
        if os.path.isdir(filepath):
            process_folder(filepath)
        elif filename.endswith('.ini'):
            print('Found .ini file:', filepath)
            upgrade_ini(filepath)


def upgrade_ini(filepath):
    try:
        # Errors occuring here is fine as no write operations to the ini nor any buffers are performed
        ini = Ini(filepath).upgrade()
    except Exception as x:
        print('Error occurred: {}'.format(x))
        print('No changes have been applied to {}!'.format(filepath))
        print()
        print(traceback.format_exc())
        print()
        return False

    try:
        # Content of the ini and any modified buffers get written to disk in this function
        # Since the code for this function is more concise and predictable, the chance of it failing
        # is low, but it can happen if Windows doesn't want to cooperate and write for whatever reason.
        ini.save()
    except Exception as X:
        print('Fatal error occurred while saving changes for {}!'.format(filepath))
        print('Its likely that your mod has been corrupted. You must redownload it from the source before attempting to fix it again.')
        print()
        print(traceback.format_exc())
        print()
        return False

    return True


# MARK: Ini
class Ini():
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.content  = Path(self.filepath).read_text(encoding='utf-8')
            self.encoding = 'utf-8'
        except UnicodeDecodeError:
            self.content  = Path(self.filepath).read_text(encoding='gb2312')
            self.encoding = 'gb2312'
        

        # The random ordering of sets is annoying
        # Use a list for the hashes that will be iterated on
        # and a set for the hashes I already iterated on
        self._hashes = []
        self._touched = False
        self._done_hashes = set()

        # Only write the modified buffers at the very end after the ini is saved, since
        # the ini can be backed up, while backing up buffers is not not reasonable.
        # Buffer with multiple fixes: will be read from the mod directory for the first
        # fix, and from this dict in memory for subsequent fixes 
        self.modified_buffers = {
            # buffer_filepath: buffer_data
        }

        # Get all (uncommented) hashes in the ini
        pattern = re.compile(r'\n\s*hash\s*=\s*([a-f0-9]*)', flags=re.IGNORECASE)
        self._hashes = pattern.findall(self.content)
    
    def upgrade(self):
        while len(self._hashes) > 0:
            hash = self._hashes.pop()
            if hash not in self._done_hashes:
                if hash in hash_commands:
                    print(f'\tProcessing {hash}:')
                    default_args = DefaultArgs(hash=hash, ini=self, data={}, tabs=2)
                    self.execute(hash_commands[hash], default_args)
                else:
                    print(f'\tSkipping {hash}: No tasks available')
            else:
                print(f'\tSkipping {hash}: Already Checked/Processed')

            self._done_hashes.add(hash)

        # Auto-detect Jane Doe mods and run blend fix if applicable
        # PENGAMAN 1: Only trigger if hash is ACTIVE (not in comment) - check with regex
        jane_indicators = ('e42171df', 'd06a9206', '33a09cfe', '82e7c056', 'fa617c9a')
        has_active_jane = False
        for indicator in jane_indicators:
            # Check if hash appears as ACTIVE assignment (not preceded by ;)
            if re.search(r'(?<![;\w])' + indicator + r'(?!\w)', self.content, re.IGNORECASE):
                # Double-check: it's in a proper hash = xxx line, not commented
                if re.search(r'^\s*hash\s*=\s*' + indicator + r'\s*$', self.content, re.IGNORECASE | re.MULTILINE):
                    has_active_jane = True
                    break
        if has_active_jane:
            print('\tApplying Jane Doe specific fixes (legacy mod compatibility)...')
            
            # 1. Run blend auto-scan
            scanner = jane_blend_auto_scan()
            result = scanner.execute(DefaultArgs(hash='', ini=self, data={}, tabs=2))
            self._touched = self._touched or result.touched
            
            # 2. Swap vb0/vb2 in section headers named "JaneHairPosition" or "JaneHairBlend"
            #    to match the standard: vb0 = Position, vb2 = Blend
            #    This only affects sections with "Jane" in the title
            swap_count = 0
            swap_pattern = re.compile(
                r'^\[(TextureOverrideJane\w*Position)\]\s*\n'  # section with "Position"
                r'((.|\n)*?)'                                    # body
                r'^\s*vb0\s*=\s*(Resource\w+)\s*$'               # vb0 = something
                r'((.|\n)*?)'
                r'^\s*vb2\s*=\s*(Resource\w+)\s*$'               # vb2 = something
                r'((.|\n)*?)(?=^\[|\Z)',
                re.MULTILINE | re.IGNORECASE
            )
            new_content = swap_pattern.sub(
                lambda m: '[' + m.group(1).replace('Position', 'Blend') + ']\n' +
                          m.group(2) +
                          'vb2 = ' + m.group(3) + '\n' +   # swap: old vb0 becomes vb2
                          m.group(4) +
                          'vb0 = ' + m.group(6) + '\n' +   # swap: old vb2 becomes vb0
                          m.group(7),
                self.content
            )
            if new_content != self.content:
                swap_count += 1
                self.content = new_content
                self._touched = True
                print('\t  ✓ Swapped vb0/vb2 in Jane section')
            
            # 3. Duplicate HairBlend.buf → ArmsBlend.buf if needed
            #    Also add corresponding Resource section in .ini
            ini_dir = Path(self.filepath).parent
            hair_blend_path = ini_dir / 'JaneHairBlend.buf'
            arms_blend_path = ini_dir / 'JaneArmsBlend.buf'
            if hair_blend_path.exists() and not arms_blend_path.exists():
                try:
                    import shutil
                    shutil.copy2(str(hair_blend_path), str(arms_blend_path))
                    print('\t  ✓ Duplicated JaneHairBlend.buf → JaneArmsBlend.buf')
                    # Also add Resource section for ArmsBlend to .ini if not already present
                    if 'ResourceJaneArmsBlend' not in self.content:
                        arms_section = '\n[ResourceJaneArmsBlend]\ntype = Buffer\nstride = 32\nfilename = JaneArmsBlend.buf\n'
                        self.content += arms_section
                        self._touched = True
                        print('\t  ✓ Added ResourceJaneArmsBlend section to .ini')
                except Exception as e:
                    print(f'\t  ⚠ Failed to duplicate .buf: {e}')

        # Auto-detect Dialyn mods and run blend fix if applicable
        # PENGAMAN 1: Only trigger if hash is ACTIVE (not in comment)
        dialyn_indicators = ('3d7e53cf', 'ff36809b')
        has_active_dialyn = False
        for indicator in dialyn_indicators:
            if re.search(r'(?<![;\w])' + indicator + r'(?!\w)', self.content, re.IGNORECASE):
                if re.search(r'^\s*hash\s*=\s*' + indicator + r'\s*$', self.content, re.IGNORECASE | re.MULTILINE):
                    has_active_dialyn = True
                    break
        if has_active_dialyn:
            print('\tApplying Dialyn specific fixes (legacy mod compatibility)...')
            
            # Run blend auto-scan
            scanner = dialyn_blend_auto_scan()
            result = scanner.execute(DefaultArgs(hash='', ini=self, data={}, tabs=2))
            self._touched = self._touched or result.touched

        return self

    def execute(self, commands, default_args):
        for command in commands:
            clss = command[0]
            args = command[1] if len(command) > 1 else {}
            instance = clss(**args) if type(args) is dict else clss(*args) 
            result: ExecutionResult = instance.execute(default_args)

            self._touched = self._touched or result.touched
            if result.failed:
                print()
                return

            if result.queue_hashes:
                # Only add the hashes that I haven't already iterated on
                self._hashes.extend(set(result.queue_hashes).difference(self._done_hashes))

            if result.queue_commands:
                # sub_default_args = DefaultArgs(
                #     hash = default_args.hash,
                #     ini  = default_args.ini,
                #     data = default_args.data,
                #     tabs = default_args.tabs
                # )
                self.execute(result.queue_commands, default_args)

            if result.signal_break:
                return

        return default_args

    def save(self):
        if self._touched:
            basename = os.path.basename(self.filepath).split('.ini')[0]
            
            backup_dir = None
            
            current_path = Path(self.filepath).parent.resolve()
            for parent in [current_path] + list(current_path.parents):
                test_path = parent / 'Data' / 'ZZMI'
                if test_path.is_dir():
                    backup_dir = test_path / '(.ini) Caches'
                    break
                if parent.name.upper() == 'ZZMI':
                    backup_dir = parent / '(.ini) Caches'
                    break
                test_path_direct = parent / 'ZZMI'
                if test_path_direct.is_dir():
                    backup_dir = test_path_direct / '(.ini) Caches'
                    break
            
            if not backup_dir:
                import string
                for letter in string.ascii_uppercase:
                    drive = f"{letter}:\\"
                    if os.path.exists(drive):
                        test_path1 = Path(drive) / 'XXMI' / 'Data' / 'ZZMI'
                        if test_path1.is_dir():
                            backup_dir = test_path1 / '(.ini) Caches'
                            break
                        test_path2 = Path(drive) / 'Data' / 'ZZMI'
                        if test_path2.is_dir():
                            backup_dir = test_path2 / '(.ini) Caches'
                            break
                        test_path3 = Path(drive) / 'XXMI' / 'ZZMI'
                        if test_path3.is_dir():
                            backup_dir = test_path3 / '(.ini) Caches'
                            break
                        test_path4 = Path(drive) / 'XXMI Launcher' / 'ZZMI'
                        if test_path4.is_dir():
                            backup_dir = test_path4 / '(.ini) Caches'
                            break
                        test_path5 = Path(drive) / 'ZZMI'
                        if test_path5.is_dir():
                            backup_dir = test_path5 / '(.ini) Caches'
                            break

            
            if backup_dir:
                backup_dir = str(backup_dir.absolute())
            else:
                
                backup_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
            
            try:
                os.makedirs(backup_dir, exist_ok=True)
            except Exception as e:
                print(f"⚠  Failed to create external backup folder at '{backup_dir}': {e}")
                backup_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
            
            
            backup_filename = f'DISABLED_BACKUP_{int(time.time())}_{basename}.txt'
            backup_fullpath = os.path.join(backup_dir, backup_filename)

            try:
                import shutil
                shutil.move(self.filepath, backup_fullpath)
                print(f'Created Backup: {backup_filename} at {backup_dir}')
            except Exception as e:
                print(f"⚠  Failed to relocate backup externally (Different Drive/Access): {e}")
                
                try:
                    backup_fallback_filename = f'DISABLED_BACKUP_{int(time.time())}.{basename}.txt'
                    backup_fallback_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
                    backup_fallback_path = os.path.join(backup_fallback_dir, backup_fallback_filename)
                    
                    with open(self.filepath, 'r', encoding=self.encoding) as original_file:
                        original_content = original_file.read()
                    with open(backup_fallback_path, 'w', encoding=self.encoding) as backup_file:
                        backup_file.write(original_content)
                    print(f'Created Backup (Emergency): {backup_fallback_filename} at {backup_fallback_dir}')
                except Exception as ex:
                    print(f"✖ Failed to create emergency backup: {ex}")

            with open(self.filepath, 'w', encoding=self.encoding) as updated_ini:
                updated_ini.write(self.content)

            if len(self.modified_buffers) > 0:
                print('Writing updated buffers')
                # PENGAMAN 2: Backup .buf files BEFORE overwriting
                # Find backup directory same pattern as (.ini) Caches but for (.buf) Backup
                buf_backup_dir = None
                current_path = Path(self.filepath).parent.resolve()
                for parent in [current_path] + list(current_path.parents):
                    test_path = parent / 'Data' / 'ZZMI'
                    if test_path.is_dir():
                        buf_backup_dir = test_path / '(.buf) Backup'
                        break
                    if parent.name.upper() == 'ZZMI':
                        buf_backup_dir = parent / '(.buf) Backup'
                        break
                    test_path_direct = parent / 'ZZMI'
                    if test_path_direct.is_dir():
                        buf_backup_dir = test_path_direct / '(.buf) Backup'
                        break
                
                if not buf_backup_dir:
                    import string
                    for letter in string.ascii_uppercase:
                        drive = f"{letter}:\\"
                        if os.path.exists(drive):
                            test_path1 = Path(drive) / 'XXMI' / 'Data' / 'ZZMI'
                            if test_path1.is_dir():
                                buf_backup_dir = test_path1 / '(.buf) Backup'
                                break
                            test_path2 = Path(drive) / 'Data' / 'ZZMI'
                            if test_path2.is_dir():
                                buf_backup_dir = test_path2 / '(.buf) Backup'
                                break
                            test_path3 = Path(drive) / 'XXMI' / 'ZZMI'
                            if test_path3.is_dir():
                                buf_backup_dir = test_path3 / '(.buf) Backup'
                                break
                            test_path4 = Path(drive) / 'XXMI Launcher' / 'ZZMI'
                            if test_path4.is_dir():
                                buf_backup_dir = test_path4 / '(.buf) Backup'
                                break
                            test_path5 = Path(drive) / 'ZZMI'
                            if test_path5.is_dir():
                                buf_backup_dir = test_path5 / '(.buf) Backup'
                                break
                
                for filepath, data in self.modified_buffers.items():
                    # Backup original file before overwriting
                    original_path = Path(filepath)
                    if original_path.exists():
                        # Determine backup filepath
                        if buf_backup_dir:
                            # Preserve relative folder structure
                            try:
                                relative = original_path.relative_to(Path(self.filepath).parent)
                                backup_file = Path(str(buf_backup_dir)) / relative
                            except ValueError:
                                backup_file = Path(str(buf_backup_dir)) / original_path.name
                        else:
                            # Fallback: same folder as mod
                            backup_file = original_path.parent / f'DISABLED_BACKUP_{int(time.time())}_{original_path.name}'
                        
                        try:
                            os.makedirs(str(backup_file.parent), exist_ok=True)
                            import shutil
                            shutil.copy2(str(original_path), str(backup_file))
                            print(f'\tBacked up: {original_path.name} -> {backup_file}')
                        except Exception as be:
                            print(f"\t⚠  Failed to backup {original_path.name}: {be}")
                    
                    # Write the new buffer
                    with open(filepath, 'wb') as f:
                        f.write(data)
                    print('\tSaved: {}'.format(filepath))

            print('Updates applied')
        else:
            print('No changes applied')
        print()

    def has_hash(self, hash):
        return (
            (hash in self._hashes)
            or (hash in self._done_hashes)
        )


# MARK: Commands

def get_critical_content(section):
    hash = None
    match_first_index = None
    critical_lines = []
    pattern = re.compile(r'^\s*(.*?)\s*=\s*(.*?)\s*$', flags=re.IGNORECASE)

    for line in section.splitlines():
        line_match = pattern.match(line)
        
        if line.strip().startswith('['):
            continue
        elif line_match and line_match.group(1).lower() == 'hash':
            hash = line_match.group(2)
        elif line_match and line_match.group(1).lower() == 'match_first_index':
            match_first_index = line_match.group(2)
        else:
            critical_lines.append(line)

    return '\n'.join(critical_lines), hash, match_first_index


# Returns all resources used by a commandlist
# Hardcoded to only return vb1 i.e. texcoord resources for now
# (TextureOverride sections are special commandlists)
def process_commandlist(ini_content: str, commandlist: str, target: str):
    line_pattern = re.compile(r'^\s*(run|{})\s*=\s*(.*)\s*$'.format(target), flags=re.IGNORECASE)
    resources = []

    for line in commandlist.splitlines():
        line_match = line_pattern.match(line)
        if not line_match: continue

        if line_match.group(1) == target:
            resources.append(line_match.group(2))

        # Must check the commandlists that are run within the
        # the current commandlist for the resource as well
        # Recursion yay
        elif line_match.group(1) == 'run':
            commandlist_title = line_match.group(2)
            pattern = get_section_title_pattern(commandlist_title)
            commandlist_match = pattern.search(ini_content + '\n[')
            if commandlist_match:
                sub_resources = process_commandlist(ini_content, commandlist_match.group(1), target)
                resources.extend(sub_resources)

    return resources


@dataclass
class DefaultArgs():
    hash : str
    ini  : Ini
    tabs : int
    data : dict[str, str]


@dataclass
class ExecutionResult():
    touched        : bool = False
    failed         : bool = False
    signal_break   : bool = False
    queue_hashes   : tuple[str] = None
    queue_commands : tuple[str] = None


@dataclass(init=False)
class log():
    text: tuple[str]

    def __init__(self, *text):
        self.text = text

    def execute(self, default_args: DefaultArgs):
        tabs        = default_args.tabs

        info  = self.text[0]
        hash  = self.text[1] if len(self.text) > 1 else ''
        title = self.text[2] if len(self.text) > 2 else ''
        rest  = self.text[3:] if len(self.text) > 3 else []

        s = '{}{:34}'.format('\t'*tabs, info)
        if hash  : s += ' - {:8}'.format(hash)
        if title : s += ' - {}'.format(title) 
        if rest  : s += ' - '.join(rest)

        print(s)

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass
class update_hash():
    new_hash: str

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash

        pattern = re.compile(r'(\n\s*)(hash\s*=\s*{})'.format(active_hash), flags=re.IGNORECASE)
        ini.content, sub_count = pattern.subn(r'\1hash = {}\n; \2'.format(self.new_hash), ini.content)

        default_args.hash = self.new_hash

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (self.new_hash,),
            queue_commands = (
                (log, ('+ Updating {} hash(es) to {}'.format(sub_count, self.new_hash),)),
            )
        )


@dataclass
class comment_sections():

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash

        pattern = get_section_hash_pattern(hash)
        new_ini_content = ''   # ini content with all matching sections commented

        prev_j = 0
        commented_count = 0
        section_matches = pattern.finditer(ini.content)
        for section_match in section_matches:
            i, j = section_match.span(1)
            commented_section = '\n'.join(['; ' + line for line in section_match.group(1).splitlines()])
            commented_count  += 1

            new_ini_content += ini.content[prev_j:i] + commented_section
            prev_j = j

        new_ini_content += ini.content[prev_j:]
        
        ini.content = new_ini_content

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (log, ('- Commented {} relevant section(s)'.format(commented_count),)),
            )
        )


@dataclass
class comment_commandlists():
    commandlist_title: str

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        pattern = get_section_title_pattern(self.commandlist_title)
        new_ini_content = ''   # ini content with matching commandlist commented out

        prev_j = 0
        commented_count = 0
        commandlist_matches = pattern.finditer(ini.content)
        for commandlist_match in commandlist_matches:
            i, j = commandlist_match.span(1)
            commented_commandlist = '\n'.join(['; ' + line for line in commandlist_match.group(1).splitlines()])
            commented_count  += 1

            new_ini_content += ini.content[prev_j:i] + commented_commandlist
            prev_j = j

        new_ini_content += ini.content[prev_j:]
        
        ini.content = new_ini_content

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (log, ('- Commented {} relevant commandlist(s)'.format(commented_count),)),
            )
        )


@dataclass(kw_only=True)
class remove_section():
    capture_content : str = None
    capture_position: str = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash
        data        = default_args.data

        pattern = get_section_hash_pattern(active_hash)
        section_match = pattern.search(ini.content)
        if not section_match: raise Exception('Bad regex')
        start, end = section_match.span(1)

        if self.capture_content:
            data[self.capture_content] = get_critical_content(section_match.group(1))[0]
        if self.capture_position:
            data[self.capture_position] = str(start)

        ini.content = ini.content[:start] + ini.content[end:]

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class remove_indexed_sections():
    capture_content         : str = None
    capture_indexed_content : str = None
    capture_position        : str = None

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        data = default_args.data
        
        pattern = get_section_hash_pattern(hash)
        new_ini_content = ''   # ini with ib sections removed
        position        = -1   # First Occurence Deletion Start Position
        prev_end         = 0

        section_matches = pattern.finditer(ini.content)
        for section_match in section_matches:
            if re.search(r'\n\s*match_first_index\s*=', section_match.group(1), flags=re.IGNORECASE):
                if self.capture_indexed_content:
                    critical_content, _, match_first_index = get_critical_content(section_match.group(1))
                    placeholder = '{}{}{}'.format(self.capture_indexed_content, match_first_index, self.capture_indexed_content)
                    data[placeholder] = critical_content
            else:
                if self.capture_content:
                    critical_content = get_critical_content(section_match.group(1))[0]
                    placeholder = self.capture_content
                    data[placeholder] = critical_content

            start, end = section_match.span()
            if position == -1:
                position = start

            new_ini_content += ini.content[prev_end:start]
            prev_end = end

        new_ini_content += ini.content[prev_end:]
        ini.content = new_ini_content

        if self.capture_position:
            data[self.capture_position] = str(position)

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class capture_section():
    capture_content  : str = None
    capture_position : str = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash
        data        = default_args.data

        pattern = get_section_hash_pattern(active_hash)
        section_match = pattern.search(ini.content)
        if not section_match: raise Exception('Bad regex')
        _, end = section_match.span(1)

        if self.capture_content:
            data[self.capture_content] = get_critical_content(section_match.group(1))[0]
        if self.capture_position:
            data[self.capture_position] = str(end + 1)

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class create_new_section():
    section_content  : str
    saved_position   : str = None
    capture_position : str = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        data        = default_args.data

        pos = -1
        if self.saved_position and self.saved_position in data:
            pos = int(data[self.saved_position])

        for placeholder, value in data.items():
            if placeholder.startswith('_'):
                # conditions are not to be used for substitution
                continue
            self.section_content = self.section_content.replace(placeholder, value)

        # Half broken/fixed mods' ini will not have the object indices we're expecting
        # Could also be triggered due to a typo in the hash commands
        for emoji in ['🍰', '🌲', '🤍']:
            if emoji in self.section_content:
                print('Section substitution failed')
                print(self.section_content)
                return ExecutionResult(
                    touched        = False,
                    failed         = True,
                    signal_break   = False,
                    queue_hashes   = None,
                    queue_commands = None
                )
  
        if self.capture_position:
            data[self.capture_position] = str(len(self.section_content) + pos)

        ini.content = ini.content[:pos] + self.section_content + ini.content[pos:]

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class transfer_indexed_sections():
    trg_indices: tuple[str] = None
    transfer_indexed_sections: tuple[str] = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash
        data        = default_args.data

        title = None
        p = get_section_hash_pattern(hash)
        ib_matches = p.findall(ini.content)
        indexed_ib_count = 0
        for m in ib_matches:
            if re.search(r'\n\s*match_first_index\s*=', m):
                indexed_ib_count += 1
                if not title: title = re.match(r'^\[TextureOverride(.*?)\]', m, flags=re.IGNORECASE).group(1)[:-1]
            else:
                if not title: title = re.match(r'^\[TextureOverride(.*?)\]', m, flags=re.IGNORECASE).group(1)[:-2]

        if indexed_ib_count == 0:
            return ExecutionResult()

        unindexed_ib_content = '\n'.join([
            f'[TextureOverride{title}IB]',
            f'hash = {hash}',
            '🍰',
            '',
            ''
        ])

        alpha = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        content = ''
        for i, (trg_index, src_index) in enumerate(zip(self.trg_indices, self.src_indices)):
            content += '\n'.join([
                f'[TextureOverride{title}{alpha[i]}]',
                f'hash = {hash}',
                f'match_first_index = {trg_index}',
                f'🤍{src_index}🤍' if src_index != '-1' else 'ib = null',
                '',
                ''
            ])

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (remove_indexed_sections, {'capture_content': '🍰', 'capture_indexed_content': '🤍', 'capture_position': '🌲'}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': content}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': unindexed_ib_content}),
            ) if indexed_ib_count < len(ib_matches) else (
                (remove_indexed_sections, {'capture_indexed_content': '🤍', 'capture_position': '🌲'}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': content}),
            ),
        )


@dataclass()
class multiply_section_if_missing():
    equiv_hashes: tuple[str] | str
    extra_title : tuple[str]

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        if (type(self.equiv_hashes) is not tuple):
            self.equiv_hashes = (self.equiv_hashes,)
        for equiv_hash in self.equiv_hashes:
            if ini.has_hash(equiv_hash):
                return ExecutionResult(
                    touched        = False,
                    failed         = False,
                    signal_break   = False,
                    queue_hashes   = None,
                    queue_commands = (
                        (log, ('/ Skipping Section Multiplication',  f'{equiv_hash}', f'[...{self.extra_title}]',)),
                    ),
                )
        equiv_hash = self.equiv_hashes[0]

        content = '\n'.join([
            '',
            f'[TextureOverride{self.extra_title}]',
            f'hash = {equiv_hash}',
            '🍰',
            '',
        ])

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (equiv_hash,),
            queue_commands = (
                (log,                ('+ Multiplying Section', f'{equiv_hash}', f'[...{self.extra_title}]')),
                (capture_section,    {'capture_content': '🍰', 'capture_position': '🌲'}),
                (create_new_section, {'saved_position': '🌲', 'section_content': content}),
            ),
        )


@dataclass()
class add_ib_check_if_missing():

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        
        pattern         = get_section_hash_pattern(hash)
        section_matches = pattern.finditer(ini.content)

        needs_check       = False
        new_sections      = ''
        unindexed_section = ''

        for section_match in section_matches:
            if not re.search(r'\n\s*match_first_index\s*=', section_match.group(1), flags=re.IGNORECASE):
                unindexed_section = section_match.group()
                continue

            if re.search(r'\n\s*run\s*=\s*CommandListSkinTexture', section_match.group(1), flags=re.IGNORECASE):
                new_sections += section_match.group()
                continue

            needs_check = True
            new_sections += re.sub(
                r'\n\s*match_first_index\s*=.*?\n',
                r'\g<0>run = CommandListSkinTexture\n',
                section_match.group(),
                flags=re.IGNORECASE, count=1
            )


        if unindexed_section and not new_sections:
            if not re.search(r'\n\s*run\s*=\s*CommandListSkinTexture', unindexed_section, flags=re.IGNORECASE):
                needs_check = True
                unindexed_section = re.sub(
                    r'\n\s*hash\s*=.*?\n',
                    r'\g<0>run = CommandListSkinTexture\n',
                    unindexed_section,
                    flags=re.IGNORECASE, count=1
                )

        new_sections = unindexed_section + new_sections

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (log,                     ('+ Adding `run = CommandListSkinTexture`',)),
                (remove_indexed_sections, {'capture_position': '🌲'}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': new_sections}),
            ) if needs_check else (
                (log,                     ('/ Skipping `run = CommandListSkinTexture` Addition',)),
            ),
        )


@dataclass
class add_section_if_missing():
    equiv_hashes    : tuple[str] | str
    section_title   : str = None
    section_content : str = field(default='')

    def execute(self, default_args: DefaultArgs):
        ini = default_args.ini

        if (type(self.equiv_hashes) is not tuple):
            self.equiv_hashes = (self.equiv_hashes,)
        for equiv_hash in self.equiv_hashes:
            if ini.has_hash(equiv_hash):
                return ExecutionResult(
                    touched        = False,
                    failed         = False,
                    signal_break   = False,
                    queue_hashes   = None,
                    queue_commands = (
                        (log, ('/ Skipping Section Addition', equiv_hash, f'[...{self.section_title}]',)),
                    ),
                )
        equiv_hash = self.equiv_hashes[0]

        section = '\n[TextureOverride{}]\n'.format(self.section_title)
        section += 'hash = {}\n'.format(equiv_hash)
        section += self.section_content

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (equiv_hash,),
            queue_commands = (
                (log,                ('+ Adding Section', equiv_hash, f'[...{self.section_title}]',)),
                (capture_section,    {'capture_position': '🌲'}),
                (create_new_section, {'saved_position': '🌲', 'section_content': section}),
            ),
        )


@dataclass
class zzz_13_remap_texcoord():
    id: str
    old_format: tuple[str] # = ('4B','2e','2f','2e')
    new_format: tuple[str] # = ('4B','2f','2f','2f')

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        tabs = default_args.tabs

        # Precompute new buffer strides and offsets
        # Check if existing buffer stride matches our expectations
        # before remapping it
        if (len(self.old_format) != len(self.new_format)): raise Exception()
        old_stride = struct.calcsize('<' + ''.join(self.old_format))
        new_stride = struct.calcsize('<' + ''.join(self.new_format))

        offset = 0
        offsets = [0]
        for format_chunk in self.old_format:
            offset += struct.calcsize(f'<{format_chunk}')
            offsets.append(offset)

        # Need to find all Texcoord Resources used by this hash directly
        # through TextureOverrides or run through Commandlists... 
        pattern = get_section_hash_pattern(hash)
        section_match = pattern.search(ini.content)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb1')

        # - Match Resource sections to find filenames of buffers 
        # - Update stride value of resources early instead of iterating again later
        buffer_filenames = set()
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match: continue

            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if not line_match:
                    modified_resource_section.append(line)

                # Capture buffer filename
                elif line_match.group(1) == 'filename':
                    modified_resource_section.append(line)
                    buffer_filenames.add(line_match.group(2))

                # Update stride value of resource in ini
                elif line_match.group(1) == 'stride':
                    stride = int(line_match.group(2))
                    if stride != old_stride:
                        print('{}X WARNING [{}]! Expected buffer stride {} but got {} instead. Overriding and continuing.'.format('\t'*tabs, resource, old_stride, stride))
                    #     raise Exception('Remap failed for {}! Expected buffer stride {} but got {} instead.'.format(resource, old_stride, stride))

                    modified_resource_section.append('stride = {}'.format(new_stride))
                    modified_resource_section.append(';'+line)

            # Update ini
            modified_resource_section = '\n'.join(modified_resource_section)
            i, j = resource_section_match.span(1)
            ini.content = ini.content[:i] + modified_resource_section + ini.content[j:]

        global global_modified_buffers
        for buffer_filename in buffer_filenames:
            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in global_modified_buffers:
                global_modified_buffers[buffer_dict_key] = []
            fix_id = f'{self.id}-texcoord_remap'
            if fix_id in global_modified_buffers[buffer_dict_key]: continue
            else: global_modified_buffers[buffer_dict_key].append(fix_id)

            if buffer_dict_key not in ini.modified_buffers:
                buffer = buffer_filepath.read_bytes()
            else:
                buffer = ini.modified_buffers[buffer_dict_key]

            vcount = len(buffer) // stride
            new_buffer = bytearray()
            for i in range(vcount):
                for j, (old_chunk, new_chunk) in enumerate(zip(self.old_format, self.new_format)):

                    if offsets[j] < stride and offsets[j+1] <= stride:

                        if old_chunk != new_chunk:
                            # HardCode VColor Remap
                            if (j == 0 and old_chunk == '4B' and new_chunk == '4f'):
                                new_buffer.extend(struct.pack('<4f', *[b/255 for b in struct.unpack_from('<4B', buffer, i*stride + 0)]))
                            elif (j == 0 and old_chunk == '4f' and new_chunk == '4B'):
                                new_buffer.extend(struct.pack('<4B', *[max(0, min(255, int(b * 255))) if b == b else 0 for b in struct.unpack_from('<4f', buffer, i*stride + 0)]))

                            # General Element Remap
                            else:
                                new_buffer.extend(struct.pack(f'<{new_chunk}', *struct.unpack_from(f'<{old_chunk}', buffer, i*stride+offsets[j])))

                        # No Element Remap Needed
                        else:
                            new_buffer.extend(buffer[i*stride + offsets[j]: i*stride + offsets[j+1]])

                    # Mod texcoord vertex data does not saturate the expected old stride
                    else: # cope
                        new_buffer.extend(struct.pack(f'<{new_chunk}', *([0] * int(new_chunk[0]))))
            
            ini.modified_buffers[buffer_dict_key] = new_buffer    

        return ExecutionResult(
            touched=True
        )


# Deprecated. Use generalized remap_texcoord instead
@dataclass
class zzz_12_shrink_texcoord_color():
    id: str

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        tabs = default_args.tabs        

        # Need to find all Texcoord Resources used by this hash directly
        # through TextureOverrides or run through Commandlists... 
        pattern = get_section_hash_pattern(hash)
        section_match = pattern.search(ini.content)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb1')

        # - Match Resource sections to find filenames of buffers 
        # - Update stride value of resources early instead of iterating again later
        buffer_filenames = set()
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match: continue

            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if not line_match:
                    modified_resource_section.append(line)

                # Capture buffer filename
                elif line_match.group(1) == 'filename':
                    modified_resource_section.append(line)
                    buffer_filenames.add(line_match.group(2))

                # Update stride value of resource in ini
                elif line_match.group(1) == 'stride':
                    stride = int(line_match.group(2))
                    modified_resource_section.append('stride = {}'.format(stride - 12))
                    modified_resource_section.append(';'+line)

            # Update ini
            modified_resource_section = '\n'.join(modified_resource_section)
            i, j = resource_section_match.span(1)
            ini.content = ini.content[:i] + modified_resource_section + ini.content[j:]

        global global_modified_buffers
        for buffer_filename in buffer_filenames:
            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in global_modified_buffers:
                global_modified_buffers[buffer_dict_key] = []
            fix_id = f'{self.id}-zzz_12_shrink_texcoord_color'
            if fix_id in global_modified_buffers[buffer_dict_key]: continue
            else: global_modified_buffers[buffer_dict_key].append(fix_id)

            if buffer_dict_key not in ini.modified_buffers:
                buffer = buffer_filepath.read_bytes()
            else:
                buffer = ini.modified_buffers[buffer_dict_key]

            vcount = len(buffer) // stride
            new_buffer = bytearray()
            for i in range(vcount):
                # print(*[ int((f*255)) for f in struct.unpack_from('<4f', buffer, i*stride + 0)])
                new_buffer.extend(struct.pack(
                        '<4B',
                        *[
                            max(0, min(255, int(f * 255))) if f == f else 0
                            for f in struct.unpack_from('<4f', buffer, i*stride + 0)
                        ]
                    ))
                new_buffer.extend(buffer[i*stride + 16: i*stride + stride])
            
            ini.modified_buffers[buffer_dict_key] = new_buffer            

        return ExecutionResult(
            touched=True
        )

@dataclass
class update_buffer_blend_indices():
    hash       : str
    old_indices: tuple[int]
    new_indices: tuple[int]

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        # Need to find all Texcoord Resources used by this hash directly
        # through TextureOverrides or run through Commandlists... 
        pattern = get_section_hash_pattern(self.hash)
        section_match = pattern.search(ini.content)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb2')

        # - Match Resource sections to find filenames of buffers 
        # - Update stride value of resources early instead of iterating again later
        buffer_filenames = set()
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match: continue

            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if not line_match:
                    modified_resource_section.append(line)

                # Capture buffer filename
                elif line_match.group(1) == 'filename':
                    modified_resource_section.append(line)
                    buffer_filenames.add(line_match.group(2))

        for buffer_filename in buffer_filenames:
            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in ini.modified_buffers:
                buffer = buffer_filepath.read_bytes()
            else:
                buffer = ini.modified_buffers[buffer_dict_key]
    
            new_buffer = bytearray()
            blend_stride = 32
            vertex_count = len(buffer)//blend_stride
            for i in range(vertex_count):
                blend_weights  = struct.unpack_from('<4f', buffer, i*blend_stride + 0)
                blend_indices  = struct.unpack_from('<4I', buffer, i*blend_stride + 16)

                new_buffer.extend(struct.pack('<4f4I', *blend_weights, *[
                    vgx if vgx not in self.old_indices
                    else self.new_indices[self.old_indices.index(vgx)]
                    for vgx in blend_indices
                ]))

            ini.modified_buffers[buffer_dict_key] = new_buffer

        return ExecutionResult(
            touched=True
        )

@dataclass
# MARK: Jane Doe Blend Remapper
class jane_blend_auto_scan():
    """
    Scans ALL vb2 resources in the .ini file and remaps blend indices
    for Jane Doe character. This handles legacy mods that don't have
    separate blend_vb hashes (e42171df / d06a9206) in their .ini files.

    Works like Satan1c's Jane.remapper: finds any vb2=ResourceXXX binding,
    checks if the .buf file has stride 32, and applies the hair/hand remapping.
    """
    # Hair bone mappings (old_index -> new_index)
    HAIR_MAPPING = {
        26: 4, 27: 5, 28: 6, 29: 7, 30: 8, 31: 9, 32: 10, 33: 11, 34: 12, 35: 13,
        36: 14, 37: 15, 38: 16, 39: 17, 40: 19, 41: 20, 42: 18, 43: 22, 44: 23,
        45: 24, 46: 25, 47: 26, 48: 27, 49: 28, 50: 21, 51: 29, 52: 30, 53: 31,
        90: 33, 91: 34, 92: 32, 93: 36, 94: 37, 95: 35, 96: 38, 97: 39, 98: 40,
        99: 41, 100: 42, 101: 44, 102: 45, 103: 46, 104: 48, 105: 47, 106: 43,
        107: 49, 108: 52, 109: 53, 110: 54, 111: 55, 112: 50, 113: 51, 114: 56,
        115: 57, 116: 58, 117: 59, 118: 60, 119: 61, 120: 62, 121: 63, 122: 64,
        123: 65, 124: 66, 125: 67, 126: 68
    }
    # Hand bone mappings (old_index -> new_index)
    HAND_MAPPING = {
        4: 0, 5: 1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6, 11: 7, 12: 8, 13: 9, 14: 10,
        15: 11, 16: 12, 17: 13, 18: 14, 19: 15, 20: 16, 21: 17, 22: 18, 23: 19,
        24: 20, 25: 21, 54: 22, 55: 23, 56: 24, 57: 25, 58: 26, 59: 27, 60: 28,
        61: 29, 62: 30, 63: 31, 64: 32, 65: 33, 66: 34, 67: 35, 68: 36, 69: 37,
        70: 38, 71: 39, 72: 40, 73: 41, 74: 42, 75: 43, 76: 44, 77: 45, 78: 46,
        79: 47, 80: 48, 81: 49, 82: 50, 83: 51, 84: 52, 85: 53, 86: 54, 87: 55,
        88: 56, 89: 57, 127: 58, 128: 59, 129: 60
    }

    def execute(self, default_args: DefaultArgs):
        ini = default_args.ini
        content = ini.content
        ini_dir = Path(ini.filepath).parent

        # Find all vb2 = ResourceXXX bindings in the ini
        # First, find all section headers with their content
        section_pattern = re.compile(
            r'^\[([^\]]+)\]\s*((?:(?!^\[)[^\n]*\n?)*)',
            flags=re.MULTILINE | re.IGNORECASE
        )

        blend_resources = []  # list of (resource_name, section_name, hash_or_context)

        for section_match in section_pattern.finditer(content):
            section_name = section_match.group(1).strip()
            section_body = section_match.group(2)

            # Skip non-TextureOverride sections for hash lookup, but keep all for vb2 scan
            vb2_match = re.search(r'^\s*vb2\s*=\s*Resource([a-zA-Z0-9_]+)\s*$', section_body, re.IGNORECASE | re.MULTILINE)
            if vb2_match:
                resource_name = vb2_match.group(1)
                # Find the hash in this section
                hash_match = re.search(r'^\s*hash\s*=\s*([a-f0-9]{8})\s*$', section_body, re.IGNORECASE | re.MULTILINE)
                context_hash = hash_match.group(1).lower() if hash_match else 'unknown'
                blend_resources.append((resource_name, section_name, context_hash))

        if not blend_resources:
            print(f'\t\tNo vb2 resources found in ini')
            return ExecutionResult(touched=False)

        # Find the Resource section for each blend resource
        touched = False
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)

        for res_name, sec_name, ctx_hash in blend_resources:
            # Find Resource section
            res_pattern = re.compile(
                r'^\[Resource' + re.escape(res_name) + r'\]\s*((?:(?!^\[)[^\n]*\n?)*)',
                flags=re.MULTILINE | re.IGNORECASE
            )
            res_match = res_pattern.search(content)
            if not res_match:
                continue

            res_body = res_match.group(1)

            # Check stride
            stride_match = re.search(r'^\s*stride\s*=\s*(\d+)\s*$', res_body, re.IGNORECASE | re.MULTILINE)
            if not stride_match:
                continue
            stride = int(stride_match.group(1))
            if stride != 32:
                print(f'\t\tSkipping Resource{res_name}: stride={stride} != 32 (not a blend buffer)')
                continue

            # Get filename
            filename_match = re.search(r'^\s*filename\s*=\s*(.+)\s*$', res_body, re.IGNORECASE | re.MULTILINE)
            if not filename_match:
                continue
            buf_filename = filename_match.group(1).strip()
            buf_path = ini_dir / buf_filename

            if not buf_path.exists():
                print(f'\t\tSkipping {buf_filename}: file not found')
                continue

            # Determine which mapping to use based on context
            # ONLY remap if we know the exact bone mapping
            # HAIR: hash e42171df or position hash 33a09cfe / fa617c9a
            # HAND: hash d06a9206 or position hash 82e7c056 / 6d482e21
            if ctx_hash in ('e42171df', '33a09cfe', 'fa617c9a'):
                mapping = self.HAIR_MAPPING
                mapping_name = 'HAIR'
            elif ctx_hash in ('d06a9206', '82e7c056', '6d482e21'):
                mapping = self.HAND_MAPPING
                mapping_name = 'HAND'
            else:
                # Unknown context - try to deduce from filename
                name_lower = buf_filename.lower()
                if 'hair' in name_lower or 'head' in name_lower:
                    mapping = self.HAIR_MAPPING
                    mapping_name = 'HAIR (auto-detect)'
                elif 'hand' in name_lower or 'finger' in name_lower or 'accessor' in name_lower:
                    mapping = self.HAND_MAPPING
                    mapping_name = 'HAND (auto-detect)'
                else:
                    print(f'\t\tSkipping {buf_filename}: unknown mapping context (hash={ctx_hash})')
                    continue

            # Read buffer
            buf_dict_key = str(buf_path.absolute())
            if buf_dict_key in ini.modified_buffers:
                buffer = ini.modified_buffers[buf_dict_key]
            else:
                buffer = buf_path.read_bytes()

            # Verify plausible blend buffer (vertex count)
            vertex_count = len(buffer) // stride
            if vertex_count == 0:
                continue

            # Remap
            new_buffer = bytearray(len(buffer))
            for v in range(vertex_count):
                offset = v * stride
                # Copy weights (first 16 bytes) unmodified
                new_buffer[offset:offset+16] = buffer[offset:offset+16]
                # Remap indices (next 16 bytes: 4 uint32)
                indices = struct.unpack_from('<4I', buffer, offset + 16)
                mapped = [mapping.get(idx, idx) for idx in indices]
                new_buffer[offset + 16:offset + 32] = struct.pack('<4I', *mapped)

            ini.modified_buffers[buf_dict_key] = new_buffer
            print(f'\t\t✓ Jane blend remapped ({mapping_name}): {buf_filename}')
            touched = True

        if not touched:
            print(f'\t\tNo blend buffers needed remapping')

        return ExecutionResult(
            touched=touched
        )


# MARK: Dialyn Blend Remapper
class dialyn_blend_auto_scan():
    """
    Scans ALL vb2 resources in the .ini file and remaps blend indices
    for Dialyn character. This handles legacy mods that need the
    updated bone mapping for Dialyn's 3D model structure.

    Based on Dialyn.remapper.cs by Satan1c.
    """
    BLEND_MAPPING = {
        18: 20, 19: 18, 20: 19,
        54: 62, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59, 61: 60, 62: 61,
        69: 71, 70: 72, 71: 70, 72: 69,
        91: 98, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97,
        113: 114, 114: 113,
        128: 129, 129: 128, 130: 132, 131: 130, 132: 131,
        188: 189, 189: 188,
    }
    POSITION_TO_BLEND = {
        'ff36809b': '3d7e53cf',
    }

    def execute(self, default_args: DefaultArgs):
        ini = default_args.ini
        content = ini.content
        ini_dir = Path(ini.filepath).parent

        section_pattern = re.compile(
            r'^\[([^\]]+)\]\s*((?:(?!^\[)[^\n]*\n?)*)',
            flags=re.MULTILINE | re.IGNORECASE
        )

        blend_resources = []

        for section_match in section_pattern.finditer(content):
            section_name = section_match.group(1).strip()
            section_body = section_match.group(2)

            vb2_match = re.search(r'^\s*vb2\s*=\s*Resource([a-zA-Z0-9_]+)\s*$', section_body, re.IGNORECASE | re.MULTILINE)
            if vb2_match:
                resource_name = vb2_match.group(1)
                hash_match = re.search(r'^\s*hash\s*=\s*([a-f0-9]{8})\s*$', section_body, re.IGNORECASE | re.MULTILINE)
                context_hash = hash_match.group(1).lower() if hash_match else 'unknown'
                blend_resources.append((resource_name, section_name, context_hash))

        if not blend_resources:
            print(f'\t\tNo vb2 resources found in ini')
            return ExecutionResult(touched=False)

        touched = False
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)

        for res_name, sec_name, ctx_hash in blend_resources:
            res_pattern = re.compile(
                r'^\[Resource' + re.escape(res_name) + r'\]\s*((?:(?!^\[)[^\n]*\n?)*)',
                flags=re.MULTILINE | re.IGNORECASE
            )
            res_match = res_pattern.search(content)
            if not res_match:
                continue

            res_body = res_match.group(1)

            stride_match = re.search(r'^\s*stride\s*=\s*(\d+)\s*$', res_body, re.IGNORECASE | re.MULTILINE)
            if not stride_match:
                continue
            stride = int(stride_match.group(1))
            if stride != 32:
                print(f'\t\tSkipping Resource{res_name}: stride={stride} != 32 (not a blend buffer)')
                continue

            filename_match = re.search(r'^\s*filename\s*=\s*(.+)\s*$', res_body, re.IGNORECASE | re.MULTILINE)
            if not filename_match:
                continue
            buf_filename = filename_match.group(1).strip()
            buf_path = ini_dir / buf_filename

            if not buf_path.exists():
                print(f'\t\tSkipping {buf_filename}: file not found')
                continue

            # Determine which mapping to use
            mapping = self.BLEND_MAPPING
            mapping_name = 'DIALYN'

            buf_dict_key = str(buf_path.absolute())
            if buf_dict_key in ini.modified_buffers:
                buffer = ini.modified_buffers[buf_dict_key]
            else:
                buffer = buf_path.read_bytes()

            vertex_count = len(buffer) // stride
            if vertex_count == 0:
                continue

            new_buffer = bytearray(len(buffer))
            for v in range(vertex_count):
                offset = v * stride
                new_buffer[offset:offset+16] = buffer[offset:offset+16]
                indices = struct.unpack_from('<4I', buffer, offset + 16)
                mapped = [mapping.get(idx, idx) for idx in indices]
                new_buffer[offset + 16:offset + 32] = struct.pack('<4I', *mapped)

            ini.modified_buffers[buf_dict_key] = new_buffer
            print(f'\t✓ Dialyn blend remapped ({mapping_name}): {buf_filename}')
            touched = True

        if not touched:
            print(f'\t\tNo blend buffers needed remapping')

        return ExecutionResult(
            touched=touched
        )


# MARK: Character Data Loader
def load_character_modules():
    """
    Dynamically loads all character modules from PlayerCharacterPYData folder.
    Returns merged hash_commands dictionary.
    """
    import importlib
    import sys
    from pathlib import Path
    
    # Determine the base path (handles both script and PyInstaller executable)
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_path = Path(sys._MEIPASS) / 'Assets'
    else:
        # Running as script
        base_path = Path(__file__).parent / 'Assets'
    
    character_data_path = base_path / 'PlayerCharacterPYData'
    
    # Prepare command classes to pass to character modules
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
        'update_buffer_blend_indices': update_buffer_blend_indices,
        'jane_blend_auto_scan': jane_blend_auto_scan,
        'dialyn_blend_auto_scan': dialyn_blend_auto_scan,
    }
    
    merged_commands = {}
    
    # Add PlayerCharacterPYData to Python path
    sys.path.insert(0, str(character_data_path.parent))
    
    try:
        # Get all .py files in the directory (excluding __init__.py)
        character_files = [f for f in character_data_path.glob('*.py') 
                          if f.name != '__init__.py']
        
        print(f'Loading {len(character_files)} character modules...')
        
        for char_file in sorted(character_files):
            char_name = char_file.stem
            try:
                # Import the character module
                module = importlib.import_module(f'PlayerCharacterPYData.{char_name}')
                
                # Get hash commands from the module
                if hasattr(module, 'get_hash_commands'):
                    char_commands = module.get_hash_commands(**command_classes)
                    
                    # Check for hash collisions
                    collisions = set(merged_commands.keys()) & set(char_commands.keys())
                    if collisions:
                        print(f'  Warning: {char_name} has hash collisions: {collisions}')
                    
                    # Merge commands
                    merged_commands.update(char_commands)
                    print(f'  ✓ Loaded {char_name}: {len(char_commands)} hashes')
                else:
                    print(f'  X Skipped {char_name}: missing get_hash_commands()')
                    
            except Exception as e:
                print(f'  X Failed to load {char_name}: {e}')
        
        print(f'Total hashes loaded: {len(merged_commands)}\n')
        
    finally:
        # Clean up sys.path
        sys.path.remove(str(character_data_path.parent))
    
    return merged_commands


# Load all character data dynamically
try:
    hash_commands = load_character_modules()
except Exception as e:
    print(f'\nFATAL ERROR: Failed to load character modules!')
    print(f'Error: {e}')
    print('\nAll character data must be loaded from individual module files.')
    print('Please ensure the Assets/PlayerCharacterPYData directory exists and contains valid character modules.')
    print(traceback.format_exc())
    input('\nPress "Enter" to quit...\n')
    raise SystemExit(1)

# MARK: Regex
# Using VERBOSE flag to ignore whitespace
# https://docs.python.org/3/library/re.html#re.VERBOSE
def get_section_hash_pattern(hash) -> re.Pattern:
    return re.compile(
        r'''
            ^(
                [ \t]*?\[(?:Texture|Shader)Override.*\][ \t]*
                (?:\n
                    (?![ \t]*?(?:\[|hash\s*=))
                    .*$
                )*?
                (?:\n\s*hash\s*=\s*{}[ \t]*)
                (?:
                    (?:\n(?![ \t]*?\[).*$)*
                    (?:\n[\t ]*?[\$\w].*$)
                )?
            )\s*
        '''.format(hash),
        flags=re.VERBOSE|re.IGNORECASE|re.MULTILINE
    )


def get_section_title_pattern(title) -> re.Pattern:
    return re.compile(
        r'''
            ^(
                [ \t]*?\[{}\]
                (?:
                    (?:\n(?![ \t]*?\[).*$)*
                    (?:\n[\t ]*?[\$\w].*$)
                )?
            )\s*
        '''.format(title),
        flags=re.VERBOSE|re.IGNORECASE|re.MULTILINE
    )

# MARK: RUN
if __name__ == '__main__':
    try: main()
    except Exception as x:
        print('\nError Occurred: {}\n'.format(x))
        print(traceback.format_exc())
    finally:
        input('\nPress "Enter" to quit...\n')