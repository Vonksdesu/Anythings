# ZZZ-Mod-Fixer

A comprehensive tool to automatically update and fix Zenless Zone Zero (ZZZ) character mods for compatibility with newer game versions.

## Overview

ZZZ-Mod-Fixer is designed to address the common issue of character mods breaking after game updates. When Zenless Zone Zero receives updates, the game's internal hash values, texture coordinate formats, and buffer structures often change, rendering older mods incompatible. This tool automatically detects and applies the necessary fixes to bring your mods up to date.

### How It Works

The mod fixer operates through a multi-step process:

1. **Hash Detection**: Scans `.ini` files (3DMigoto mod configuration files) to identify hash values that reference specific game assets and shaders.

2. **Version Mapping**: Compares detected hashes against a comprehensive database of known hash changes across game versions. Each character has dedicated data modules that map old hashes to new ones.

3. **Intelligent Transformation**: Applies version-specific fixes including:
   - **Hash Updates**: Replaces outdated hash values with current ones
   - **Texture Coordinate Remapping**: Converts buffer formats (e.g., 4B→4f conversions for color data, 2e→2f for float precision changes)
   - **Buffer Stride Adjustments**: Updates stride values when data structure sizes change
   - **Blend Index Updates**: Remaps bone/vertex group indices for skeletal animations
   - **Section Management**: Adds missing texture override sections or removes obsolete ones
   - **Index Buffer Handling**: Manages match_first_index properties for multi-mesh characters

4. **Safe Modification**: Creates timestamped backups of all modified files before applying changes, allowing easy rollback if needed.

5. **Binary Buffer Processing**: Directly modifies binary `.buf` files when texture coordinate format changes require data structure transformations.

### Key Features

- **Automatic Version Detection**: Identifies which game version(s) a mod was designed for based on hash patterns
- **Character-Specific Fixes**: Over 60 playable characters supported with dedicated fix modules
- **Non-Destructive**: Always creates backups before modifying files
- **Batch Processing**: Can process entire mod folders recursively
- **Smart Section Handling**: Adds missing sections, multiplies sections when multiple resolutions are needed, and comments out obsolete sections
- **Buffer Format Conversion**: Handles complex binary buffer transformations for texture coordinate remapping

## Usage

### Basic Usage - Folder Mode

The simplest way to use the mod fixer is to place the executable in your mod folder (or any parent folder) and run it:

```bash
# Windows: Double-click the executable or run from command line
zzz-mod-fixer.exe
```

The tool will:
- Recursively scan all subdirectories from the current location
- Process all `.ini` files found (except those prefixed with `DISABLED`)
- Display progress for each hash being processed
- Create backup files with the naming pattern: `DISABLED_BACKUP_{timestamp}.{original_name}.ini`

### Advanced Usage - Single File Mode

To process a specific `.ini` file:

```bash
zzz-mod-fixer.exe path\to\your\mod.ini
```

### Python Script Usage

If running from source:

```bash
# Process current directory
python zzz-mod-fixer.py

# Process specific file
python zzz-mod-fixer.py path\to\mod.ini
```

## Understanding the Output

When processing mods, you'll see detailed console output:

```
Found .ini file: ./Anby_Mod/Anby.ini
	Processing 5c0240db:
		1.0: Anby Hair IB Hash
		/ Skipping `run = CommandListSkinTexture` Addition
	Processing cc114f4f:
		1.5 -> 1.6: Anby HeadA Diffuse 1024p Hash
		+ Updating 1 hash(es) to 692c6d2b
		+ Multiplying Section - 05d7b504 - [...Anby.HeadA.Diffuse.2048]
Created Backup: DISABLED_BACKUP_1736734565.Anby.ini at C:\Path\To\Mod
Updates applied
```

**Status Indicators:**
- `+` = Adding or updating something
- `-` = Removing or commenting out something
- `/` = Skipping (already correct or not needed)
- `X` = Warning or issue detected

## File Organization

The mod fixer expects the following structure:

```
ZZZ-Mod-Fixer/
├── zzz-mod-fixer.py (or .exe)
├── Assets/
│   └── PlayerCharacterPYData/
│       ├── __init__.py
│       ├── Anby.py
│       ├── Ellen.py
│       ├── Miyabi.py
│       └── ... (additional character modules)
└── README.md
```

**Note:** The `Assets` folder is bundled into compiled executables automatically.

## Supported Characters

The tool includes fix data for all playable characters through version 2.5, including:
- Launch characters (Anby, Billy, Nicole, Corin, etc.)
- Limited characters (Ellen, Zhu Yuan, Jane Doe, Miyabi, etc.)
- Alternate skins and forms (Ellen Campus, Soldier 0, etc.)
- Upcoming characters with known hash data

## Backup and Recovery

### Backup Files

All backups are created with the pattern:
```
DISABLED_BACKUP_{unix_timestamp}.{original_filename}.ini
```

The `DISABLED` prefix ensures 3DMigoto won't load the backup file.

### Restoring from Backup

To restore a mod:
1. Delete or rename the current `.ini` file
2. Remove the `DISABLED_BACKUP_{timestamp}.` prefix from the backup file
3. Restore any original `.buf` files if needed (buffer backups are not created automatically)

### Important Notes

- **Buffer files (.buf) are modified in-place** - Keep original mod archives as backups
- **Multiple runs are safe** - The tool won't re-fix already fixed hashes
- **Failed fixes are non-destructive** - If a fix fails, the original files remain unchanged

## Troubleshooting

### "No changes applied"
This is normal if your mod is already compatible with the current game version. The tool detected no outdated hashes.

### "Section substitution failed"
This indicates a complex mod structure that may require manual fixing. Check for emoji characters (🍰, 🌲, 🤍) in the console output - these are placeholder indicators that couldn't be resolved.

### "Expected buffer stride X but got Y instead"
The tool will show a warning but continue processing. This occurs when texture coordinate buffer formats don't match expectations but can usually be safely overridden.

### Mod still doesn't work after fixing
- Ensure you're running the latest version of 3DMigoto
- Check that the game version matches what the fix targets
- Verify all `.buf` files are present alongside the `.ini` file
- Some mods may require game-side updates beyond what automated fixing can provide

## Technical Details

### Hash Command System

Each character has a dedicated Python module that defines hash commands - transformation rules that specify how to fix each known hash:

- `update_hash`: Replace an old hash with a new one
- `zzz_13_remap_texcoord`: Remap texture coordinate buffer formats
- `add_section_if_missing`: Add required sections for proper texture loading
- `multiply_section_if_missing`: Duplicate sections for multi-resolution support
- `transfer_indexed_sections`: Reorganize indexed buffer sections
- `update_buffer_blend_indices`: Remap skeletal animation bone indices

### Character Module Format

Character modules return hash command dictionaries:

```python
def get_hash_commands(**command_classes):
    return {
        'old_hash': [
            (log, ('Version info',)),
            (update_hash, ('new_hash',)),
            (zzz_13_remap_texcoord, {'id': 'char', 'old_format': ('4B','2e'), 'new_format': ('4B','2f')}),
        ],
        # ... more hashes
    }
```

## Contributing

To add support for new characters or game versions:

1. Create a new module in `Assets/PlayerCharacterPYData/`
2. Define the `get_hash_commands()` function with appropriate transformations
3. Follow the existing character module patterns
4. Add a references to the new module in `zzz-mod-fixer.spec` and `Assets\PlayerCharacterPYData\__init__.py`
4. Test thoroughly with real mod files

## Credits

- Originally written by **petrascyll**
- 1.6 updates by **HammyCatte**
- 1.7 updates by **shaojiang**

Join the AGMG community: [discord.gg/agmg](https://discord.gg/agmg)

## License

See [LICENSE](LICENSE) file for details.
