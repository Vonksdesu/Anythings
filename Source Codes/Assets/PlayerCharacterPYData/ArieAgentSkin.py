"""
ArieAgentSkin Character Hash Commands
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
    Returns ArieAgentSkin's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'1173ff78': [(log, ('2.8: ArieAgentSkin Hair IB Hash',)),        (add_ib_check_if_missing,)],
'046400d3': [(log, ('2.8: ArieAgentSkin Body IB Hash',)),        (add_ib_check_if_missing,)],
'ac9c2ebb': [(log, ('2.8: ArieAgentSkin Decoration IB Hash',)),  (add_ib_check_if_missing,)],
'ffa703e8': [(log, ('2.8: ArieAgentSkin Face IB Hash',)),        (add_ib_check_if_missing,)],
'db7c8d25': [(log, ('2.8: ArieAgentSkin Eye IB Hash',)),         (add_ib_check_if_missing,)],
'62cc8d20': [(log, ('2.8: ArieAgentSkin Weapon IB Hash',)),      (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'5bbaca72': [(log, ('2.8: ArieAgentSkin Hair draw_vb',)),                (add_section_if_missing, ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n'))],
'42a4622f': [(log, ('2.8: ArieAgentSkin Hair position_vb',)),            (add_section_if_missing, ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n'))],
'23629315': [(log, ('2.8: ArieAgentSkin Hair texcoord_vb',)),            (add_section_if_missing, ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n'))],
'468e532f': [(log, ('2.8: ArieAgentSkin Hair blend_vb',)),               (add_section_if_missing, ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n'))],

# Body
'a28a907a': [(log, ('2.8: ArieAgentSkin Body draw_vb',)),                (add_section_if_missing, ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n'))],
'608bff86': [(log, ('2.8: ArieAgentSkin Body position_vb',)),            (add_section_if_missing, ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n'))],
'b019dae2': [(log, ('2.8: ArieAgentSkin Body texcoord_vb',)),            (add_section_if_missing, ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n'))],
'7c85654d': [(log, ('2.8: ArieAgentSkin Body blend_vb',)),               (add_section_if_missing, ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n'))],

# Decoration
'8e2e89dc': [(log, ('2.8: ArieAgentSkin Decoration draw_vb',)),          (add_section_if_missing, ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n'))],
'09998ea7': [(log, ('2.8: ArieAgentSkin Decoration position_vb',)),      (add_section_if_missing, ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n'))],
'9f6fa4fe': [(log, ('2.8: ArieAgentSkin Decoration texcoord_vb',)),      (add_section_if_missing, ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n'))],
'624d99aa': [(log, ('2.8: ArieAgentSkin Decoration blend_vb',)),         (add_section_if_missing, ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n'))],

# Face
'f0c79e51': [(log, ('2.8: ArieAgentSkin Face draw_vb',)),                (add_section_if_missing, ('ffa703e8', 'ArieAgentSkin.Face.IB', 'match_priority = 0\n'))],
'b62f2772': [(log, ('2.8: ArieAgentSkin Face position_vb',)),            (add_section_if_missing, ('ffa703e8', 'ArieAgentSkin.Face.IB', 'match_priority = 0\n'))],
'9772ccda': [(log, ('2.8: ArieAgentSkin Face texcoord_vb',)),            (add_section_if_missing, ('ffa703e8', 'ArieAgentSkin.Face.IB', 'match_priority = 0\n'))],
'ea540ea2': [(log, ('2.8: ArieAgentSkin Face blend_vb',)),               (add_section_if_missing, ('ffa703e8', 'ArieAgentSkin.Face.IB', 'match_priority = 0\n'))],

# Eye
'390a4a23': [(log, ('2.8: ArieAgentSkin Eye draw_vb',)),                 (add_section_if_missing, ('db7c8d25', 'ArieAgentSkin.Eye.IB', 'match_priority = 0\n'))],
'cf12b575': [(log, ('2.8: ArieAgentSkin Eye position_vb',)),             (add_section_if_missing, ('db7c8d25', 'ArieAgentSkin.Eye.IB', 'match_priority = 0\n'))],
'22b99744': [(log, ('2.8: ArieAgentSkin Eye texcoord_vb',)),             (add_section_if_missing, ('db7c8d25', 'ArieAgentSkin.Eye.IB', 'match_priority = 0\n'))],
'71fabd1a': [(log, ('2.8: ArieAgentSkin Eye blend_vb',)),                (add_section_if_missing, ('db7c8d25', 'ArieAgentSkin.Eye.IB', 'match_priority = 0\n'))],

# Weapon
'380bb1a8': [(log, ('2.8: ArieAgentSkin Weapon draw_vb Hash',)),         (add_section_if_missing, ('62cc8d20', 'ArieAgentSkin.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'28466273': [(log, ('2.0 -> 2.8: ArieAgentSkin Face Diffuse [Legacy]',)), (update_hash, ('6b11a215',))],
'fc3231cd': [(log, ('2.0 -> 2.8: ArieAgentSkin Hair Diffuse A [Legacy]',)), (update_hash, ('fb2c3964',))],
'f0aec120': [(log, ('2.0 -> 2.8: ArieAgentSkin Hair Diffuse B [Legacy]',)), (update_hash, ('be70c507',))],
'380fbecb': [(log, ('2.0 -> 2.8: ArieAgentSkin Hair LightMap A [Legacy]',)), (update_hash, ('21aac04f',))],
'9e2e56b3': [(log, ('2.0 -> 2.8: ArieAgentSkin Hair LightMap B [Legacy]',)), (update_hash, ('41124010',))],
'8f3cfb68': [(log, ('2.0 -> 2.8: ArieAgentSkin Hair MaterialMap A [Legacy]',)), (update_hash, ('e1ccfca4',))],
'002360e1': [(log, ('2.0 -> 2.8: ArieAgentSkin Hair MaterialMap B [Legacy]',)), (update_hash, ('01087a99',))],
'1bf43198': [(log, ('2.0 -> 2.8: ArieAgentSkin Body/Deco Diffuse [Legacy]',)), (update_hash, ('282c7753',))],
'99f9094c': [(log, ('2.0 -> 2.8: ArieAgentSkin Body/Deco LightMap [Legacy]',)), (update_hash, ('263f8811',))],
'ab411caa': [(log, ('2.0 -> 2.8: ArieAgentSkin Body/Deco MaterialMap [Legacy]',)), (update_hash, ('f5b45cc2',))],
'2c3a5d8d': [(log, ('2.0 -> 2.8: ArieAgentSkin Weapon Diffuse [Legacy]',)), (update_hash, ('adbfa4c4',))],
'4a0da1fb': [(log, ('2.0 -> 2.8: ArieAgentSkin Weapon LightMap [Legacy]',)), (update_hash, ('71966d3f',))],
'825f0b0b': [(log, ('2.0 -> 2.8: ArieAgentSkin Weapon MaterialMap [Legacy]',)), (update_hash, ('328592b5',))],
'ebac056e': [(log, ('2.8: ArieAgentSkin Shared NormalMap Hash [Legacy]',)),(update_hash, ('798adba3',))],

# === Face Textures ===
'6b11a215': [
        (log,                           ('2.8: ArieAgentSkin FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('ffa703e8', 'ArieAgentSkin.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Skin Textures (v2.8 Target) ===
'fb2c3964': [
        (log,                           ('2.8: ArieAgentSkin HairA Diffuse Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'be70c507': [
        (log,                           ('2.8: ArieAgentSkin HairB Diffuse Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'21aac04f': [
        (log,                           ('2.8: ArieAgentSkin HairA LightMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'41124010': [
        (log,                           ('2.8: ArieAgentSkin HairB LightMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'e1ccfca4': [
        (log,                           ('2.8: ArieAgentSkin HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'01087a99': [
        (log,                           ('2.8: ArieAgentSkin HairB MaterialMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body & Decoration Shared Textures (v2.8 Target) ===
'282c7753': [
        (log,                           ('2.8: ArieAgentSkin Body, Decoration Diffuse Hash',)),
        (add_section_if_missing,        ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n')),
    ],
'263f8811': [
        (log,                           ('2.8: ArieAgentSkin Body, Decoration LightMap Hash',)),
        (add_section_if_missing,        ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n')),
    ],
'f5b45cc2': [
        (log,                           ('2.8: ArieAgentSkin Body, Decoration MaterialMap Hash',)),
        (add_section_if_missing,        ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n')),
    ],

# === Weapon Skin Textures (v2.8 Target) ===
'adbfa4c4': [
        (log,                           ('2.8: ArieAgentSkin WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgentSkin.Weapon.IB', 'match_priority = 0\n')),
    ],
'71966d3f': [
        (log,                           ('2.8: ArieAgentSkin WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgentSkin.Weapon.IB', 'match_priority = 0\n')),
    ],
'328592b5': [
        (log,                           ('2.8: ArieAgentSkin WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgentSkin.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: ArieAgentSkin Shared NormalMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'ArieAgentSkin.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('046400d3', 'ArieAgentSkin.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'ArieAgentSkin.Decoration.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62cc8d20', 'ArieAgentSkin.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ArieAgentSkin',
    'game_versions': ['2.8'],
}