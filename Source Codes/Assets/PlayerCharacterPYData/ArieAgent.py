"""
ArieAgent Character Hash Commands
ZZZ Mod Fixer v2.8
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns ArieAgent's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'1173ff78': [(log, ('2.8: ArieAgent Hair IB Hash',)),                    (add_ib_check_if_missing,)],
'046400d3': [(log, ('2.8: ArieAgent Body IB Hash',)),                    (add_ib_check_if_missing,)],
'ffa703e8': [(log, ('2.8: ArieAgent Face IB Hash',)),                    (add_ib_check_if_missing,)],
'db7c8d25': [(log, ('2.8: ArieAgent Eye IB Hash',)),                     (add_ib_check_if_missing,)],
'62cc8d20': [(log, ('2.8: ArieAgent Weapon IB Hash',)),                  (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'5bbaca72': [(log, ('2.8: ArieAgent Hair draw_vb',)),                    (add_section_if_missing, ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n'))],
'42a4622f': [(log, ('2.8: ArieAgent Hair position_vb',)),                (add_section_if_missing, ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n'))],
'23629315': [(log, ('2.8: ArieAgent Hair texcoord_vb',)),                (add_section_if_missing, ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n'))],
'468e532f': [(log, ('2.8: ArieAgent Hair blend_vb',)),                   (add_section_if_missing, ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n'))],

# Body
'a28a907a': [(log, ('2.8: ArieAgent Body draw_vb',)),                    (add_section_if_missing, ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n'))],
'608bff86': [(log, ('2.8: ArieAgent Body position_vb',)),                (add_section_if_missing, ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n'))],
'b019dae2': [(log, ('2.8: ArieAgent Body texcoord_vb',)),                (add_section_if_missing, ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n'))],
'7c85654d': [(log, ('2.8: ArieAgent Body blend_vb',)),                   (add_section_if_missing, ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n'))],

# Face
'f0c79e51': [(log, ('2.8: ArieAgent Face draw_vb',)),                    (add_section_if_missing, ('ffa703e8', 'ArieAgent.Face.IB', 'match_priority = 0\n'))],
'b62f2772': [(log, ('2.8: ArieAgent Face position_vb',)),                (add_section_if_missing, ('ffa703e8', 'ArieAgent.Face.IB', 'match_priority = 0\n'))],
'9772ccda': [(log, ('2.8: ArieAgent Face texcoord_vb',)),                (add_section_if_missing, ('ffa703e8', 'ArieAgent.Face.IB', 'match_priority = 0\n'))],
'ea540ea2': [(log, ('2.8: ArieAgent Face blend_vb',)),                   (add_section_if_missing, ('ffa703e8', 'ArieAgent.Face.IB', 'match_priority = 0\n'))],

# Eye
'390a4a23': [(log, ('2.8: ArieAgent Eye draw_vb',)),                     (add_section_if_missing, ('db7c8d25', 'ArieAgent.Eye.IB', 'match_priority = 0\n'))],
'cf12b575': [(log, ('2.8: ArieAgent Eye position_vb',)),                 (add_section_if_missing, ('db7c8d25', 'ArieAgent.Eye.IB', 'match_priority = 0\n'))],
'22b99744': [(log, ('2.8: ArieAgent Eye texcoord_vb',)),                 (add_section_if_missing, ('db7c8d25', 'ArieAgent.Eye.IB', 'match_priority = 0\n'))],
'71fabd1a': [(log, ('2.8: ArieAgent Eye blend_vb',)),                    (add_section_if_missing, ('db7c8d25', 'ArieAgent.Eye.IB', 'match_priority = 0\n'))],

# Weapon
'380bb1a8': [(log, ('2.8: ArieAgent Weapon draw_vb Hash',)),             (add_section_if_missing, ('62cc8d20', 'ArieAgent.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'6611eaa1': [(log, ('2.0 -> 2.8: ArieAgent Face Diffuse [Legacy]',)),      (update_hash, ('741d7c8f',))],
'f0aec120': [(log, ('2.0 -> 2.8: ArieAgent Hair Diffuse [Legacy]',)),      (update_hash, ('be70c507',))],
'9e2e56b3': [(log, ('2.0 -> 2.8: ArieAgent Hair LightMap [Legacy]',)),     (update_hash, ('41124010',))],
'002360e1': [(log, ('2.0 -> 2.8: ArieAgent Hair MaterialMap [Legacy]',)),  (update_hash, ('01087a99',))],
'702063c7': [(log, ('2.0 -> 2.8: ArieAgent Body Diffuse [Legacy]',)),      (update_hash, ('859bb461',))],
'a588ea59': [(log, ('2.0 -> 2.8: ArieAgent Body LightMap [Legacy]',)),     (update_hash, ('ba534b39',))],
'0a8badcd': [(log, ('2.0 -> 2.8: ArieAgent Body MaterialMap [Legacy]',)),  (update_hash, ('14aa84e5',))],
'5ec4228a': [(log, ('2.0 -> 2.8: ArieAgent Weapon Diffuse [Legacy]',)),   (update_hash, ('f797551b',))],
'e180bd1c': [(log, ('2.0 -> 2.8: ArieAgent Weapon LightMap [Legacy]',)),  (update_hash, ('6c620c16',))],
'777472dd': [(log, ('2.0 -> 2.8: ArieAgent Weapon MaterialMap [Legacy]',)), (update_hash, ('9e9d8560',))],
'ebac056e': [(log, ('2.8: ArieAgent Shared NormalMap Hash [Legacy]',)),   (update_hash, ('798adba3',))],

# === Face Textures (v2.8 Target) ===
'741d7c8f': [
        (log,                           ('2.8: ArieAgent FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('ffa703e8', 'ArieAgent.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures (v2.8 Target) ===
'be70c507': [
        (log,                           ('2.8: ArieAgent HairA Diffuse Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n')),
    ],
'41124010': [
        (log,                           ('2.8: ArieAgent HairA LightMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n')),
    ],
'01087a99': [
        (log,                           ('2.8: ArieAgent HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (v2.8 Target) ===
'859bb461': [
        (log,                           ('2.8: ArieAgent BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n')),
    ],
'ba534b39': [
        (log,                           ('2.8: ArieAgent BodyA LightMap Hash',)),
        (add_section_if_missing,        ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n')),
    ],
'14aa84e5': [
        (log,                           ('2.8: ArieAgent BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'f797551b': [
        (log,                           ('2.8: ArieAgent WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgent.Weapon.IB', 'match_priority = 0\n')),
    ],
'6c620c16': [
        (log,                           ('2.8: ArieAgent WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgent.Weapon.IB', 'match_priority = 0\n')),
    ],
'9e9d8560': [
        (log,                           ('2.8: ArieAgent WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgent.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: ArieAgent Shared NormalMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgent.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('046400d3', 'ArieAgent.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgent.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ArieAgent',
    'game_versions': ['2.8'],
}