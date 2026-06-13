"""
EllenCampus Character Hash Commands
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
    Returns EllenCampus's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'f601f643': [(log, ('2.8: EllenCampus Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'4a938c0a': [(log, ('2.8: EllenCampus Body IB Hash',)),                 (add_ib_check_if_missing,)],
'fafcfe36': [(log, ('2.8: EllenCampus Tail IB Hash',)),                 (add_ib_check_if_missing,)],
'7b54b96f': [(log, ('2.8: EllenCampus Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'f6ef8f3a': [(log, ('2.8: EllenCampus Face IB Hash (Shared)',)),        (add_ib_check_if_missing,)],
'4ce3a865': [(log, ('2.8: EllenCampus Weapon Scythe IB Hash',)),        (add_ib_check_if_missing,)],
'2747bdd1': [(log, ('2.8: EllenCampus Weapon Spring IB Hash',)),        (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'a93fc9a1': [(log, ('2.8: EllenCampus Hair draw_vb',)),                 (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n'))],
'9e8e3811': [(log, ('2.8: EllenCampus Hair position_vb',)),             (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n'))],
'887a6214': [(log, ('2.8: EllenCampus Hair texcoord_vb',)),             (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n'))],
'e246fbec': [(log, ('2.8: EllenCampus Hair blend_vb',)),                (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'3d83f929': [(log, ('2.8: EllenCampus Hair Shadow draw_vb',)),          (add_section_if_missing, ('7b54b96f', 'EllenCampus.HairShadow.IB', 'match_priority = 0\n'))],
'9702c71e': [(log, ('2.8: EllenCampus Hair Shadow position_vb',)),      (add_section_if_missing, ('7b54b96f', 'EllenCampus.HairShadow.IB', 'match_priority = 0\n'))],
'fc566cba': [(log, ('2.8: EllenCampus Hair Shadow texcoord_vb',)),      (add_section_if_missing, ('7b54b96f', 'EllenCampus.HairShadow.IB', 'match_priority = 0\n'))],
'42b50496': [(log, ('2.8: EllenCampus Hair Shadow blend_vb',)),         (add_section_if_missing, ('7b54b96f', 'EllenCampus.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'a31d576e': [(log, ('2.8: EllenCampus Body draw_vb',)),                 (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n'))],
'a1566c40': [(log, ('2.8: EllenCampus Body position_vb',)),             (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n'))],
'fc0d07a3': [(log, ('2.8: EllenCampus Body texcoord_vb',)),             (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n'))],
'f6f9cc24': [(log, ('2.8: EllenCampus Body blend_vb',)),                (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n'))],

# Tail
'bfa3b361': [(log, ('2.8: EllenCampus Tail draw_vb',)),                 (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n'))],
'e053cbbd': [(log, ('2.8: EllenCampus Tail position_vb',)),             (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n'))],
'54db15a2': [(log, ('2.8: EllenCampus Tail texcoord_vb',)),             (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n'))],
'f2c0c20f': [(log, ('2.8: EllenCampus Tail blend_vb',)),                (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n'))],

# Face
'96baf0ee': [(log, ('2.8: EllenCampus Face VertexLimit Hash',)),        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n'))],
'aca863a9': [(log, ('2.8: EllenCampus Face position_vb Hash',)),        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n'))],
'f87ddcae': [(log, ('2.8: EllenCampus Face texcoord_vb Hash',)),        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n'))],
'9cc30b79': [(log, ('2.8: EllenCampus Face blend_vb Hash',)),           (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n'))],

# Weapon - Scythe
'14ee18a1': [(log, ('2.8: EllenCampus Scythe VertexLimit Hash',)),      (add_section_if_missing, ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n'))],
'4140d1e3': [(log, ('2.8: EllenCampus Scythe position_vb Hash',)),      (add_section_if_missing, ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n'))],
'64df6d71': [(log, ('2.8: EllenCampus Scythe texcoord_vb Hash',)),      (add_section_if_missing, ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n'))],
'12c97a8a': [(log, ('2.8: EllenCampus Scythe blend_vb Hash',)),         (add_section_if_missing, ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n'))],

# Weapon - Spring
'a063d963': [(log, ('2.8: EllenCampus Spring VertexLimit Hash',)),      (add_section_if_missing, ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n'))],
'4b5ecba8': [(log, ('2.8: EllenCampus Spring position_vb Hash',)),      (add_section_if_missing, ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n'))],
'21b31add': [(log, ('2.8: EllenCampus Spring texcoord_vb Hash',)),      (add_section_if_missing, ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n'))],
'4afdcca5': [(log, ('2.8: EllenCampus Spring blend_vb Hash',)),         (add_section_if_missing, ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'4808d050': [
        (log,                           ('2.8: EllenCampus FaceA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
    ],

# === Legacy Hash Updates ===
'b06f7cb9': [(log, ('2.0 -> 2.8: EllenCampus Weapon Diffuse [Legacy]',)), (update_hash, ('e9e610cd',))],
'0567bc4e': [(log, ('2.0 -> 2.8: EllenCampus Weapon LightMap [Legacy]',)), (update_hash, ('1721ed1a',))],
'd4c2adaa': [(log, ('2.0 -> 2.8: EllenCampus Weapon MaterialMap [Legacy]',)), (update_hash, ('9aaa6b4b',))],

# === Hair Textures ===
'37eefb17': [
        (log,                           ('2.8: EllenCampus Hair Diffuse Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'6e15911b': [
        (log,                           ('2.8: EllenCampus HairA Diffuse 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9a5c0d42', 'EllenCampus.HairA.Diffuse.1024')),
    ],
'9a5c0d42': [
        (log,                           ('2.8: EllenCampus HairA Diffuse 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6e15911b', 'EllenCampus.HairA.Diffuse.2048')),
    ],
'aa77b3ff': [
        (log,                           ('2.8: EllenCampus Hair LightMap Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'48fd827b': [
        (log,                           ('2.8: EllenCampus HairA LightMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('72e65ade', 'EllenCampus.HairA.LightMap.1024')),
    ],
'72e65ade': [
        (log,                           ('2.8: EllenCampus HairA LightMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('48fd827b', 'EllenCampus.HairA.LightMap.2048')),
    ],
'0ab940d8': [
        (log,                           ('2.8: EllenCampus Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'8740602f': [
        (log,                           ('2.8: EllenCampus HairA MaterialMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d69b5a86', 'EllenCampus.HairA.MaterialMap.1024')),
    ],
'd69b5a86': [
        (log,                           ('2.8: EllenCampus HairA MaterialMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8740602f', 'EllenCampus.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'61beec5c': [
        (log,                           ('2.8: EllenCampus Body Diffuse Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
'76f42184': [
        (log,                           ('2.8: EllenCampus BodyA Diffuse 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fec9bbf8', 'EllenCampus.BodyA.Diffuse.1024')),
    ],
'fec9bbf8': [
        (log,                           ('2.8: EllenCampus BodyA Diffuse 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('76f42184', 'EllenCampus.BodyA.Diffuse.2048')),
    ],
'd13c6700': [
        (log,                           ('2.8: EllenCampus Body LightMap Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
'e6c9a6e1': [
        (log,                           ('2.8: EllenCampus BodyA LightMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('82a31ce3', 'EllenCampus.BodyA.LightMap.1024')),
    ],
'82a31ce3': [
        (log,                           ('2.8: EllenCampus BodyA LightMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e6c9a6e1', 'EllenCampus.BodyA.LightMap.2048')),
    ],
'ae919d9f': [
        (log,                           ('2.8: EllenCampus Body MaterialMap Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
'1d7b458d': [
        (log,                           ('2.8: EllenCampus BodyA MaterialMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('30427c9e', 'EllenCampus.BodyA.MaterialMap.1024')),
    ],
'30427c9e': [
        (log,                           ('2.8: EllenCampus BodyA MaterialMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1d7b458d', 'EllenCampus.BodyA.MaterialMap.2048')),
    ],

# === Tail Textures ===
'8df52d2a': [
        (log,                           ('2.8: EllenCampus Tail Diffuse Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'0e474202': [
        (log,                           ('2.8: EllenCampus TailA Diffuse 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e0c36e7e', 'EllenCampus.TailA.Diffuse.1024')),
    ],
'e0c36e7e': [
        (log,                           ('2.8: EllenCampus TailA Diffuse 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0e474202', 'EllenCampus.TailA.Diffuse.2048')),
    ],
'a2f7a7db': [
        (log,                           ('2.8: EllenCampus Tail LightMap Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'8f2cb44d': [
        (log,                           ('2.8: EllenCampus TailA LightMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f21e3fa3', 'EllenCampus.TailA.LightMap.1024')),
    ],
'f21e3fa3': [
        (log,                           ('2.8: EllenCampus TailA LightMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8f2cb44d', 'EllenCampus.TailA.LightMap.2048')),
    ],
'cf37068c': [
        (log,                           ('2.8: EllenCampus Tail MaterialMap Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'51cc39d5': [
        (log,                           ('2.8: EllenCampus TailA MaterialMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('78e70ba9', 'EllenCampus.TailA.MaterialMap.1024')),
    ],
'78e70ba9': [
        (log,                           ('2.8: EllenCampus TailA MaterialMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('51cc39d5', 'EllenCampus.TailA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'e9e610cd': [
        (log,                           ('2.8: EllenCampus Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n')),
    ],
'1721ed1a': [
        (log,                           ('2.8: EllenCampus Weapon LightMap Hash',)),
        (add_section_if_missing,        ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n')),
    ],
'9aaa6b4b': [
        (log,                           ('2.8: EllenCampus Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: EllenCampus Shared NormalMap Hash (Hair, Body, Tail & Scythe)',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4ce3a865', 'EllenCampus.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'EllenCampus.WeaponSpring.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: EllenCampus Shared NormalMap 2048p Hash (Hair/Body/Tail) [Legacy]',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d6715e09', 'EllenCampus.Shared.NormalMap.1024')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'EllenCampus',
    'game_versions': ['2.8'],
}