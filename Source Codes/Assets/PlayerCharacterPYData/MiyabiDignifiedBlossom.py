"""
MiyabiDignifiedBlossom Character Hash Commands
ZZZ Mod Fixer v3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns MiyabiDignifiedBlossom's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'ecaf558f': [(log, ('2.8: MiyabiDignifiedBlossom Hair IB Hash',)),        (add_ib_check_if_missing,)],
'244eb75a': [(log, ('2.8: MiyabiDignifiedBlossom HairShadow IB Hash',)),  (add_ib_check_if_missing,)],
'a913e9a9': [(log, ('2.8: MiyabiDignifiedBlossom Body IB Hash',)),        (add_ib_check_if_missing,)],
'fbb18630': [(log, ('2.8: MiyabiDignifiedBlossom Clothes IB Hash',)),     (add_ib_check_if_missing,)],
'dbd59d30': [(log, ('2.8: MiyabiDignifiedBlossom Face IB Hash',)),        (add_ib_check_if_missing,)],
'0275d39f': [(log, ('2.8: MiyabiDignifiedBlossom Sword IB Hash',)),       (add_ib_check_if_missing,)],
'562b2030': [(log, ('2.8: MiyabiDignifiedBlossom SwordSheath IB Hash',)), (add_ib_check_if_missing,)],
'1a82a439': [(log, ('2.8: MiyabiDignifiedBlossom SwordHandle IB Hash',)), (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd011ed6c': [(log, ('2.8: MiyabiDignifiedBlossom Hair draw_vb Hash',)),              (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n'))],
'e49def56': [(log, ('2.8: MiyabiDignifiedBlossom Hair position_vb Hash',)),          (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n'))],
'b8cb383f': [(log, ('2.8: MiyabiDignifiedBlossom Hair texcoord_vb Hash',)),          (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n'))],
'28a01b2c': [(log, ('2.8: MiyabiDignifiedBlossom Hair blend_vb Hash',)),             (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n'))],

# Body
'a4a705f6': [(log, ('2.8: MiyabiDignifiedBlossom Body draw_vb Hash',)),              (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n'))],
'6567066b': [(log, ('2.8: MiyabiDignifiedBlossom Body position_vb Hash',)),          (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n'))],
'01c36f40': [(log, ('2.8: MiyabiDignifiedBlossom Body texcoord_vb Hash',)),          (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n'))],
'5121459b': [(log, ('2.8: MiyabiDignifiedBlossom Body blend_vb Hash',)),             (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n'))],

# Clothes
'467f402c': [(log, ('2.8: MiyabiDignifiedBlossom Clothes draw_vb Hash',)),           (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n'))],
'c2b0eca3': [(log, ('2.8: MiyabiDignifiedBlossom Clothes position_vb Hash',)),       (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n'))],
'6eb82b02': [(log, ('2.8: MiyabiDignifiedBlossom Clothes texcoord_vb Hash',)),       (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n'))],
'958db681': [(log, ('2.8: MiyabiDignifiedBlossom Clothes blend_vb Hash',)),          (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n'))],

# Face
'0dbd45ea': [(log, ('2.8: MiyabiDignifiedBlossom Face draw_vb Hash',)),              (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n'))],
'37afd6ad': [(log, ('2.8: MiyabiDignifiedBlossom Face position_vb Hash',)),          (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n'))],
'7a476f86': [(log, ('2.8: MiyabiDignifiedBlossom Face texcoord_vb Hash',)),          (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n'))],
'd7781c46': [(log, ('2.8: MiyabiDignifiedBlossom Face blend_vb Hash',)),             (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n'))],

# Sword
'9d6f441f': [(log, ('2.8: MiyabiDignifiedBlossom Sword draw_vb Hash',)),             (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n'))],
'81a99d68': [(log, ('2.8: MiyabiDignifiedBlossom Sword position_vb Hash',)),         (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n'))],
'aeb95d61': [(log, ('2.8: MiyabiDignifiedBlossom Sword texcoord_vb Hash',)),         (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n'))],
'8bc72b94': [(log, ('2.8: MiyabiDignifiedBlossom Sword blend_vb Hash',)),            (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n'))],

# Sword Sheath
'e3590e91': [(log, ('2.8: MiyabiDignifiedBlossom SwordSheath draw_vb Hash',)),       (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n'))],
'fc93f762': [(log, ('2.8: MiyabiDignifiedBlossom SwordSheath position_vb Hash',)),   (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n'))],
'a9ac3439': [(log, ('2.8: MiyabiDignifiedBlossom SwordSheath texcoord_vb Hash',)),   (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n'))],
'38c91cb1': [(log, ('2.8: MiyabiDignifiedBlossom SwordSheath blend_vb Hash',)),      (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n'))],

# Sword Handle
'5e1e12aa': [(log, ('2.8: MiyabiDignifiedBlossom SwordHandle draw_vb Hash',)),       (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n'))],
'10545b04': [(log, ('2.8: MiyabiDignifiedBlossom SwordHandle position_vb Hash',)),   (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n'))],
'51af1803': [(log, ('2.8: MiyabiDignifiedBlossom SwordHandle texcoord_vb Hash',)),   (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n'))],
'c55927b0': [(log, ('2.8: MiyabiDignifiedBlossom SwordHandle blend_vb Hash',)),      (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'1d487fd5': [
        (log,                           ('3.0: MiyabiDignifiedBlossom Face Diffuse Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'92599e94': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom Face Diffuse Hash [Legacy]',)),
        (update_hash,                   ('1d487fd5',)),
    ],

# === Hair Textures ===
'012e84e9': [
        (log,                           ('3.0: MiyabiDignifiedBlossom Hair Diffuse Hash',)),
        (add_section_if_missing,        ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'ed6b94f7': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom Hair Diffuse Hash [Legacy]',)),
        (update_hash,                   ('012e84e9',)),
    ],
'a6ea6d83': [
        (log,                           ('3.0: MiyabiDignifiedBlossom Hair LightMap Hash',)),
        (add_section_if_missing,        ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'8b5708f4': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom Hair LightMap Hash [Legacy]',)),
        (update_hash,                   ('a6ea6d83',)),
    ],
'd5462e37': [
        (log,                           ('3.0: MiyabiDignifiedBlossom Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'a84d9003': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom Hair MaterialMap Hash [Legacy]',)),
        (update_hash,                   ('d5462e37',)),
    ],

# === Body Textures ===
'18299e4d': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'7d420160': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'6b59bc2d': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'd8ad1898': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'93d7173c': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'417337f2': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],

# === Clothes Textures ===
'4e6c90bd': [
        (log,                           ('3.0: MiyabiDignifiedBlossom Clothes Diffuse Hash',)),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'66724f5a': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom Clothes Diffuse Hash [Legacy]',)),
        (update_hash,                   ('4e6c90bd',)),
    ],
'88e357af': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'7b8eb437': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'93b264d9': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'30590865': [
        (log,                           ('3.0: MiyabiDignifiedBlossom Clothes MaterialMap Hash',)),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'1e1485e7': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom Clothes MaterialMap Hash [Legacy]',)),
        (update_hash,                   ('30590865',)),
    ],
'85aad660': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],

# === Sword, SwordSheath & SwordHandle Shared Textures ===
'e1215530': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Sword, SwordSheath, SwordHandle Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'f9ec3ac8': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Sword, SwordSheath, SwordHandle Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'9d2adcc5': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Sword, SwordSheath, SwordHandle LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'0f21a6c9': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Sword, SwordSheath, SwordHandle LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'4659445f': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Sword, SwordSheath, SwordHandle MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'e6eab72f': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Sword, SwordSheath, SwordHandle MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Shared NormalMap Hash',)),
        (add_section_if_missing,        ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('ecaf558f', 'a913e9a9', 'fbb18630', '0275d39f', '562b2030', '1a82a439'), 'MiyabiDignifiedBlossom.Shared.NormalMap.2048', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'MiyabiDignifiedBlossom',
    'game_versions': ['2.8', '3.0'],
}