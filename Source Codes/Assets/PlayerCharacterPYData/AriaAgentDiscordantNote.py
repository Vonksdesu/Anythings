"""
AriaAgentDiscordantNote Character Hash Commands
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
    Returns AriaAgentDiscordantNote's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'1173ff78': [(log, ('2.8: AriaAgentDiscordantNote Hair IB Hash',)),        (add_ib_check_if_missing,)],
'046400d3': [(log, ('2.8: AriaAgentDiscordantNote Body IB Hash',)),        (add_ib_check_if_missing,)],
'ac9c2ebb': [(log, ('2.8: AriaAgentDiscordantNote Decoration IB Hash',)),  (add_ib_check_if_missing,)],
'ffa703e8': [(log, ('2.8: AriaAgentDiscordantNote Face IB Hash',)),        (add_ib_check_if_missing,)],
'db7c8d25': [(log, ('2.8: AriaAgentDiscordantNote Eye IB Hash',)),         (add_ib_check_if_missing,)],
'62cc8d20': [(log, ('2.8: AriaAgentDiscordantNote Weapon IB Hash',)),      (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'5bbaca72': [(log, ('2.8: AriaAgentDiscordantNote Hair draw_vb',)),                (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n'))],
'42a4622f': [(log, ('2.8: AriaAgentDiscordantNote Hair position_vb',)),            (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n'))],
'23629315': [(log, ('2.8: AriaAgentDiscordantNote Hair texcoord_vb',)),            (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n'))],
'468e532f': [(log, ('2.8: AriaAgentDiscordantNote Hair blend_vb',)),               (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n'))],

# Body
'a28a907a': [(log, ('2.8: AriaAgentDiscordantNote Body draw_vb',)),                (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n'))],
'608bff86': [(log, ('2.8: AriaAgentDiscordantNote Body position_vb',)),            (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n'))],
'b019dae2': [(log, ('2.8: AriaAgentDiscordantNote Body texcoord_vb',)),            (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n'))],
'7c85654d': [(log, ('2.8: AriaAgentDiscordantNote Body blend_vb',)),               (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n'))],

# Decoration
'8e2e89dc': [(log, ('2.8: AriaAgentDiscordantNote Decoration draw_vb',)),          (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n'))],
'09998ea7': [(log, ('2.8: AriaAgentDiscordantNote Decoration position_vb',)),      (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n'))],
'9f6fa4fe': [(log, ('2.8: AriaAgentDiscordantNote Decoration texcoord_vb',)),      (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n'))],
'624d99aa': [(log, ('2.8: AriaAgentDiscordantNote Decoration blend_vb',)),         (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n'))],

# Face
'f0c79e51': [(log, ('2.8: AriaAgentDiscordantNote Face draw_vb',)),                (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n'))],
'b62f2772': [(log, ('2.8: AriaAgentDiscordantNote Face position_vb',)),            (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n'))],
'9772ccda': [(log, ('2.8: AriaAgentDiscordantNote Face texcoord_vb',)),            (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n'))],
'ea540ea2': [(log, ('2.8: AriaAgentDiscordantNote Face blend_vb',)),               (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n'))],

# Eye
'390a4a23': [(log, ('2.8: AriaAgentDiscordantNote Eye draw_vb',)),                 (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n'))],
'cf12b575': [(log, ('2.8: AriaAgentDiscordantNote Eye position_vb',)),             (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n'))],
'22b99744': [(log, ('2.8: AriaAgentDiscordantNote Eye texcoord_vb',)),             (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n'))],
'71fabd1a': [(log, ('2.8: AriaAgentDiscordantNote Eye blend_vb',)),                (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n'))],

# Weapon
'380bb1a8': [(log, ('2.8: AriaAgentDiscordantNote Weapon draw_vb Hash',)),         (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'28466273': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Face Diffuse [Legacy]',)), (update_hash, ('6b11a215',))],
'fc3231cd': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Hair Diffuse A [Legacy]',)), (update_hash, ('fb2c3964',))],
'f0aec120': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Hair Diffuse B [Legacy]',)), (update_hash, ('be70c507',))],
'380fbecb': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Hair LightMap A [Legacy]',)), (update_hash, ('21aac04f',))],
'9e2e56b3': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Hair LightMap B [Legacy]',)), (update_hash, ('41124010',))],
'8f3cfb68': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Hair MaterialMap A [Legacy]',)), (update_hash, ('e1ccfca4',))],
'002360e1': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Hair MaterialMap B [Legacy]',)), (update_hash, ('01087a99',))],
'1bf43198': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Body/Deco Diffuse [Legacy]',)), (update_hash, ('282c7753',))],
'99f9094c': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Body/Deco LightMap [Legacy]',)), (update_hash, ('263f8811',))],
'ab411caa': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Body/Deco MaterialMap [Legacy]',)), (update_hash, ('f5b45cc2',))],
'2c3a5d8d': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Weapon Diffuse [Legacy]',)), (update_hash, ('adbfa4c4',))],
'4a0da1fb': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Weapon LightMap [Legacy]',)), (update_hash, ('71966d3f',))],
'825f0b0b': [(log, ('2.0 -> 2.8: AriaAgentDiscordantNote Weapon MaterialMap [Legacy]',)), (update_hash, ('328592b5',))],
'ebac056e': [(log, ('2.8: AriaAgentDiscordantNote Shared NormalMap Hash [Legacy]',)),(update_hash, ('798adba3',))],

# === Face Textures ===
'6b11a215': [
        (log,                           ('2.8: AriaAgentDiscordantNote FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Skin Textures (v2.8 Target) ===
'fb2c3964': [
        (log,                           ('2.8: AriaAgentDiscordantNote HairA Diffuse Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'be70c507': [
        (log,                           ('2.8: AriaAgentDiscordantNote HairB Diffuse Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'21aac04f': [
        (log,                           ('2.8: AriaAgentDiscordantNote HairA LightMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'41124010': [
        (log,                           ('2.8: AriaAgentDiscordantNote HairB LightMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'e1ccfca4': [
        (log,                           ('2.8: AriaAgentDiscordantNote HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'01087a99': [
        (log,                           ('2.8: AriaAgentDiscordantNote HairB MaterialMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body & Decoration Shared Textures (v2.8 Target) ===
'282c7753': [
        (log,                           ('2.8: AriaAgentDiscordantNote Body, Decoration Diffuse Hash',)),
        (add_section_if_missing,        ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],
'263f8811': [
        (log,                           ('2.8: AriaAgentDiscordantNote Body, Decoration LightMap Hash',)),
        (add_section_if_missing,        ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],
'f5b45cc2': [
        (log,                           ('2.8: AriaAgentDiscordantNote Body, Decoration MaterialMap Hash',)),
        (add_section_if_missing,        ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],

# === Weapon Skin Textures (v2.8 Target) ===
'adbfa4c4': [
        (log,                           ('2.8: AriaAgentDiscordantNote WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'71966d3f': [
        (log,                           ('2.8: AriaAgentDiscordantNote WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'328592b5': [
        (log,                           ('2.8: AriaAgentDiscordantNote WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: AriaAgentDiscordantNote Shared NormalMap Hash',)),
        (add_section_if_missing,        ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AriaAgentDiscordantNote',
    'game_versions': ['2.8', '3.0'],
}