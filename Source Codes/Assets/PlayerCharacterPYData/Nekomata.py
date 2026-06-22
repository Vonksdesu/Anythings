"""
Nekomata Character Hash Commands
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
    Returns Nekomata's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'da11fd85': [(log, ('2.8: Nekomata Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'26a487ff': [(log, ('2.8: Nekomata Body IB Hash',)),                      (add_ib_check_if_missing,)],
'74688145': [(log, ('2.8: Nekomata Swords IB Hash',)),                    (add_ib_check_if_missing,)],
'37119851': [(log, ('2.8: Nekomata Head IB Hash',)),                      (add_ib_check_if_missing,)],
'23c162fc': [(log, ('2.8: Nekomata Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'a00df230': [(log, ('2.8: Nekomata Hair draw_vb',)),                      (add_section_if_missing, ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n'))],
'35439aa6': [(log, ('2.8: Nekomata Hair position_vb',)),                  (add_section_if_missing, ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n'))],
'9ada013d': [(log, ('2.8: Nekomata Hair texcoord_vb',)),                  (add_section_if_missing, ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n'))],
'f16498bf': [(log, ('2.8: Nekomata Hair blend_vb',)),                     (add_section_if_missing, ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'fef9750a': [(log, ('2.8: Nekomata Hair Shadow draw_vb',)),               (add_section_if_missing, ('23c162fc', 'Nekomata.HairShadow.IB', 'match_priority = 0\n'))],
'0630f676': [(log, ('2.8: Nekomata Hair Shadow position_vb',)),           (add_section_if_missing, ('23c162fc', 'Nekomata.HairShadow.IB', 'match_priority = 0\n'))],
'bef56da3': [(log, ('2.8: Nekomata Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('23c162fc', 'Nekomata.HairShadow.IB', 'match_priority = 0\n'))],
'65ae2514': [(log, ('2.8: Nekomata Hair Shadow blend_vb',)),              (add_section_if_missing, ('23c162fc', 'Nekomata.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'0c01e6a5': [(log, ('2.8: Nekomata Body draw_vb',)),                      (add_section_if_missing, ('26a487ff', 'Nekomata.Body.IB', 'match_priority = 0\n'))],
'eaad1408': [(log, ('2.8: Nekomata Body position_vb',)),                  (add_section_if_missing, ('26a487ff', 'Nekomata.Body.IB', 'match_priority = 0\n'))],
'f589a51f': [(log, ('2.8: Nekomata Body texcoord_vb',)),                  (add_section_if_missing, ('26a487ff', 'Nekomata.Body.IB', 'match_priority = 0\n'))],
'd27d0e6b': [(log, ('2.8: Nekomata Body blend_vb',)),                     (add_section_if_missing, ('26a487ff', 'Nekomata.Body.IB', 'match_priority = 0\n'))],

# Legs
'99132d05': [(log, ('2.8: Nekomata Legs draw_vb',)),                      (add_section_if_missing, ('74688145', 'Nekomata.Swords.IB', 'match_priority = 0\n'))],
'3c4015fd': [(log, ('2.8: Nekomata Legs position_vb',)),                  (add_section_if_missing, ('74688145', 'Nekomata.Swords.IB', 'match_priority = 0\n'))],
'2a4f8c9e': [(log, ('2.8: Nekomata Legs texcoord_vb',)),                  (add_section_if_missing, ('74688145', 'Nekomata.Swords.IB', 'match_priority = 0\n'))],
'f5efd8b1': [(log, ('2.8: Nekomata Legs blend_vb',)),                     (add_section_if_missing, ('74688145', 'Nekomata.Swords.IB', 'match_priority = 0\n'))],

# Face
'c719aab9': [(log, ('2.8: Nekomata Face draw_vb',)),                      (add_section_if_missing, ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n'))],
'fd0b39fe': [(log, ('2.8: Nekomata Face position_vb',)),                  (add_section_if_missing, ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n'))],
'aa036e70': [(log, ('2.8: Nekomata Face texcoord_vb',)),                  (add_section_if_missing, ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n'))],
'5cfcac2d': [(log, ('2.8: Nekomata Face blend_vb',)),                     (add_section_if_missing, ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'd9370c84': [(log, ('1.0 -> 1.1: Nekomata HeadA Diffuse 1024p Hash',)), (update_hash, ('0834f635',))],
'fed3abbe': [(log, ('1.0 -> 1.1: Nekomata HeadA Diffuse 2048p Hash',)), (update_hash, ('ba411d22',))],
'2c317dda': [(log, ('1.0 -> 1.1: Nekomata Body Position Hash',)),  (update_hash, ('eaad1408',))],
'b5a4c084': [(log, ('1.0 -> 1.1: Nekomata Body Texcoord Hash',)),  (update_hash, ('f589a51f',))],
'd73bc96f': [(log, ('1.0 -> 1.1: Nekomata Body Blend Hash',)),  (update_hash, ('d27d0e6b',))],
'6abb714e': [(log, ('1.0 -> 1.1: Nekomata Swords Position Hash',)), (update_hash, ('3c4015fd',))],
'70f4875e': [(log, ('1.0 -> 1.1: Nekomata Swords Texcoord Hash',)), (update_hash, ('2a4f8c9e',))],
'548c7f7d': [(log, ('1.0 -> 2.5: Nekomata HairA LightMap 2048p Hash',)), (update_hash, ('1c0193dc',))],
'4ca5efc6': [(log, ('1.0 -> 2.5: Nekomata HairA MaterialMap 2048p Hash',)), (update_hash, ('3f73186f',))],
'799eb07d': [(log, ('1.0 -> 2.5: Nekomata HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'd3f67c0d': [(log, ('1.0: -> 1.1: Nekomata HairB, BodyA, SwordsA Diffuse 2048p Hash',)), (update_hash, ('207b8e63',))],
'37d3154d': [(log, ('1.0: -> 1.1: Nekomata HairB, BodyA, SwordsA Diffuse 1024p Hash',)), (update_hash, ('60687646',))],
'fc53fc6f': [(log, ('1.0 -> 2.5: Nekomata HairB, BodyA, SwordsA LightMap 2048p Hash',)), (update_hash, ('25df29e7',))],
'f26828bd': [(log, ('1.0: Nekomata HairB, BodyA, SwordsA MaterialMap 2048p Hash',)), (update_hash, ('b3286755',))],
'424da647': [(log, ('1.0 -> 1.1: Nekomata HairB, BodyA, SwordsA MaterialMap 1024p Hash',)), (update_hash, ('a5529690',))],
'ecaef71c': [(log, ('1.0 -> 2.5: Nekomata HairB, BodyA, SwordsA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],

# === Face Textures ===
'0834f635': [
        (log,                           ('2.8: Nekomata HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ba411d22', 'fed3abbe'), 'Nekomata.HeadA.Diffuse.2048')),
    ],
'ba411d22': [
        (log,                           ('2.8: Nekomata HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('37119851', 'Nekomata.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('0834f635', 'd9370c84'), 'Nekomata.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'25f3ae9b': [
        (log,                           ('2.8: Nekomata HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('aed3d8bd', 'Nekomata.HairA.Diffuse.1024')),
    ],
'aed3d8bd': [
        (log,                           ('2.8: Nekomata HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('25f3ae9b', 'Nekomata.HairA.Diffuse.2048')),
    ],
'362c205e': [
        (log,                           ('2.8: Nekomata Hair LightMap Hash',)),
        (add_section_if_missing,        ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n')),
    ],
'1c0193dc': [
        (log,                           ('2.8: Nekomata HairA LightMap 2048p Hash [Legacy]',)),
        (multiply_section_if_missing,   ('f8accad8', 'Nekomata.HairA.LightMap.1024')),
    ],
'f8accad8': [
        (log,                           ('2.8: Nekomata HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('1c0193dc', 'Nekomata.HairA.LightMap.2048')),
    ],
'378b282c': [
        (log,                           ('2.8: Nekomata Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n')),
    ],
'3f73186f': [
        (log,                           ('2.8: Nekomata HairA MaterialMap 2048p Hash [Legacy]',)),
        (multiply_section_if_missing,   ('0c22352c', 'Nekomata.HairA.MaterialMap.1024')),
    ],
'0c22352c': [
        (log,                           ('2.8: Nekomata HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('3f73186f', 'Nekomata.HairA.MaterialMap.2048')),
    ],

# === Body & Swords Shared Textures ===
'207b8e63': [
        (log,                           ('2.8: Nekomata HairB, BodyA, SwordsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('60687646', '37d3154d'), 'Nekomata.HairB.Diffuse.1024')),
    ],
'60687646': [
        (log,                           ('2.8: Nekomata HairB, BodyA, SwordsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('207b8e63', 'd3f67c0d'), 'Nekomata.HairB.Diffuse.2048')),
    ],
'25df29e7': [
        (log,                           ('2.8: Nekomata HairB, BodyA, SwordsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('4f3f7df0', 'Nekomata.HairB.LightMap.1024')),
    ],
'4f3f7df0': [
        (log,                           ('2.8: Nekomata HairB, BodyA, SwordsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('25df29e7', 'Nekomata.HairB.LightMap.2048')),
    ],
'4c09361d': [
        (log,                           ('2.8: Nekomata Body & Swords LightMap Hash',)),
        (add_section_if_missing,        ('26a487ff', 'Nekomata.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('74688145', 'Nekomata.Swords.IB', 'match_priority = 0\n')),
    ],
'b3286755': [
        (log,                           ('2.8: Nekomata HairB, BodyA, SwordsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   (('a5529690', '424da647'), 'Nekomata.HairB.MaterialMap.1024')),
    ],
'a5529690': [
        (log,                           ('2.8: Nekomata HairB, BodyA, SwordsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   (('b3286755', 'f26828bd'), 'Nekomata.HairB.MaterialMap.2048')),
    ],

# === Normal Map ===
'798adba3': [
        (log,                           ('2.8: Nekomata Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('da11fd85', 'Nekomata.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('26a487ff', 'Nekomata.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('74688145', 'Nekomata.Swords.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('23c162fc', 'Nekomata.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Nekomata Shared NormalMap 2048p Hash',)),
        (multiply_section_if_missing,   (('c936ea68', 'c1933b38'), 'Nekomata.Shared.NormalMap.1024')),
    ],
'c936ea68': [(log, ('2.8: Nekomata HairA NormalMap 1024p Hash',)), (multiply_section_if_missing, ('ebac056e', 'Nekomata.HairA.NormalMap.2048'))],
'c1933b38': [(log, ('2.8: Nekomata HairB, BodyA, SwordsA NormalMap 1024p Hash',)), (multiply_section_if_missing, ('ebac056e', 'Nekomata.HairB.NormalMap.2048'))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Nekomata',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}