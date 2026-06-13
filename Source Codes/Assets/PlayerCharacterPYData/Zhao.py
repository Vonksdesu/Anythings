"""
Zhao Character Hash Commands
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
    Returns Zhao's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'2d519056': [(log, ('2.8: Zhao Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'43c3c5a0': [(log, ('2.8: Zhao Face IB Hash',)),                        (add_ib_check_if_missing,)],
'6a57d06b': [(log, ('2.8: Zhao Body IB Hash',)),                        (add_ib_check_if_missing,)],
'75cf4c8a': [(log, ('2.8: Zhao Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'4141c5ee': [(log, ('2.8: Zhao Weapon Knife IB Hash',)),                 (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'9bfc82f2': [(log, ('2.8: Zhao Hair Draw Hash',)),                      (add_section_if_missing, ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n'))],
'f86dba12': [(log, ('2.8: Zhao Hair Position Hash',)),                  (add_section_if_missing, ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n'))],
'e1fe5e10': [(log, ('2.8: Zhao Hair Texcoord Hash',)),                  (add_section_if_missing, ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n'))],
'4b9ea40c': [(log, ('2.8: Zhao Hair Blend Hash',)),                     (add_section_if_missing, ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'302715ad': [(log, ('2.8: Zhao Hair shadow draw_vb',)),                 (add_section_if_missing, ('75cf4c8a', 'Zhao.HairShadow.IB', 'match_priority = 0\n'))],
'9d33a619': [(log, ('2.8: Zhao Hair shadow position_vb',)),             (add_section_if_missing, ('75cf4c8a', 'Zhao.HairShadow.IB', 'match_priority = 0\n'))],
'f4afa896': [(log, ('2.8: Zhao Hair shadow texcoord_vb',)),             (add_section_if_missing, ('75cf4c8a', 'Zhao.HairShadow.IB', 'match_priority = 0\n'))],
'f1c99dcc': [(log, ('2.8: Zhao Hair shadow blend_vb',)),                (add_section_if_missing, ('75cf4c8a', 'Zhao.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'a08c7b83': [(log, ('2.8: Zhao Body Draw Hash',)),                      (add_section_if_missing, ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n'))],
'ac4490da': [(log, ('2.8: Zhao Body Position Hash',)),                  (add_section_if_missing, ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n'))],
'834b607a': [(log, ('2.8: Zhao Body Texcoord Hash',)),                  (add_section_if_missing, ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n'))],
'06ce2ca1': [(log, ('2.8: Zhao Body Blend Hash',)),                     (add_section_if_missing, ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n'))],

# Face
'b26f9258': [(log, ('2.8: Zhao Face Draw Hash',)),                      (add_section_if_missing, ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n'))],
'887d011f': [(log, ('2.8: Zhao Face Position Hash',)),                  (add_section_if_missing, ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n'))],
'76c4a041': [(log, ('2.8: Zhao Face Texcoord Hash',)),                  (add_section_if_missing, ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n'))],
'd3c0fe17': [(log, ('2.8: Zhao Face Blend Hash',)),                     (add_section_if_missing, ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n'))],

# Weapon - Knife
'1acc9c40': [(log, ('2.8: Zhao Weapon draw_vb Hash',)),                 (add_section_if_missing, ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n'))],
'6caf1e01': [(log, ('2.8: Zhao Weapon position_vb Hash',)),             (add_section_if_missing, ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n'))],
'b61f8d2c': [(log, ('2.8: Zhao Weapon texcoord_vb Hash',)),             (add_section_if_missing, ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n'))],
'0a4341f5': [(log, ('2.8: Zhao Weapon blend_vb Hash',)),                (add_section_if_missing, ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'61730662': [(log, ('2.0 -> 2.8: Zhao Weapon Knife Diffuse [Legacy]',)), (update_hash, ('fa03bb15',))],
'c3cad120': [(log, ('2.0 -> 2.8: Zhao Weapon Knife LightMap [Legacy]',)), (update_hash, ('c8892598',))],
'b900c202': [(log, ('2.0 -> 2.8: Zhao Weapon Knife MaterialMap [Legacy]',)), (update_hash, ('36b0a2b1',))],

# === Hair Textures ===
'738b6ad0': [
        (log,                           ('2.8: Zhao Hair Diffuse Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'3400d1fc': [
        (log,                           ('2.8: Zhao HairA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'39dab7f4': [
        (log,                           ('2.8: Zhao Hair LightMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'4c988418': [
        (log,                           ('2.8: Zhao HairA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'06b8c2ae': [
        (log,                           ('2.8: Zhao Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'bdc3666d': [
        (log,                           ('2.8: Zhao HairA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'b9f4efa3': [
        (log,                           ('2.8: Zhao Face Diffuse Hash',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
    ],
'6f06cdfa': [
        (log,                           ('2.8: Zhao FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'bebe4176': [
        (log,                           ('2.8: Zhao Body Diffuse Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'77dc1746': [
        (log,                           ('2.8: Zhao BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'dd6cfe48': [
        (log,                           ('2.8: Zhao Body LightMap Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'5ed57658': [
        (log,                           ('2.8: Zhao BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'04383cb9': [
        (log,                           ('2.8: Zhao Body MaterialMap Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'e98b7e9e': [
        (log,                           ('2.8: Zhao Shared MaterialMap Hash (Face/Body) [Legacy]',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'fa03bb15': [
        (log,                           ('2.8: Zhao Weapon Knife Diffuse Hash',)),
        (add_section_if_missing,        ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n')),
    ],
'c8892598': [
        (log,                           ('2.8: Zhao Weapon Knife LightMap Hash',)),
        (add_section_if_missing,        ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n')),
    ],
'36b0a2b1': [
        (log,                           ('2.8: Zhao Weapon Knife MaterialMap Hash',)),
        (add_section_if_missing,        ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Zhao Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4141c5ee', 'Zhao.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75cf4c8a', 'Zhao.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Zhao Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Zhao',
    'game_versions': ['2.8'],
}