"""
Ellen Character Hash Commands
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
    Returns Ellen's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'd44a8015': [(log, ('2.8: Ellen Hair IB Hash',)),                       (add_ib_check_if_missing,)],
'e30fae03': [(log, ('2.8: Ellen Body IB Hash',)),                       (add_ib_check_if_missing,)],
'f6ef8f3a': [(log, ('2.8: Ellen Head IB Hash',)),                       (add_ib_check_if_missing,)],
'7b54b96f': [(log, ('2.8: Ellen Hair Shadow IB Hash',)),                (add_ib_check_if_missing,)],
'569f47ac': [(log, ('2.8: Ellen Weapon Scythe IB Hash',)),               (add_ib_check_if_missing,)],
'2747bdd1': [(log, ('2.8: Ellen Weapon Spring IB Hash',)),               (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'77ac5f85': [(log, ('2.8: Ellen Hair draw_vb',)),                       (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n'))],
'ba0fe600': [(log, ('2.8: Ellen Hair position_vb',)),                   (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n'))],
'a27a8e1a': [(log, ('2.8: Ellen Hair texcoord_vb',)),                   (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n'))],
'e91c93e0': [(log, ('2.8: Ellen Hair blend_vb',)),                      (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'3d83f929': [(log, ('2.8: Ellen Hair Shadow draw_vb',)),                (add_section_if_missing, ('7b54b96f', 'Ellen.HairShadow.IB', 'match_priority = 0\n'))],
'58dacb05': [(log, ('2.8: Ellen Hair Shadow position_vb',)),            (add_section_if_missing, ('7b54b96f', 'Ellen.HairShadow.IB', 'match_priority = 0\n'))],
'fcfafc18': [(log, ('2.8: Ellen Hair Shadow texcoord_vb',)),            (add_section_if_missing, ('7b54b96f', 'Ellen.HairShadow.IB', 'match_priority = 0\n'))],
'01033838': [(log, ('2.8: Ellen Hair Shadow blend_vb',)),               (add_section_if_missing, ('7b54b96f', 'Ellen.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'cdce1fc2': [(log, ('2.8: Ellen Body draw_vb',)),                       (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n'))],
'b78f3616': [(log, ('2.8: Ellen Body position_vb',)),                   (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n'))],
'5ac6d5ee': [(log, ('2.8: Ellen Body texcoord_vb',)),                   (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n'))],
'ed9cb852': [(log, ('2.8: Ellen Body blend_vb',)),                      (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n'))],

# Face
'96baf0ee': [(log, ('2.8: Ellen Face VertexLimit Hash',)),               (add_section_if_missing, ('f6ef8f3a', 'Ellen.Head.IB', 'match_priority = 0\n'))],
'aca863a9': [(log, ('2.8: Ellen Face position_vb Hash',)),               (add_section_if_missing, ('f6ef8f3a', 'Ellen.Head.IB', 'match_priority = 0\n'))],
'158fa3f3': [(log, ('2.8: Ellen Face texcoord_vb Hash',)),               (add_section_if_missing, ('f6ef8f3a', 'Ellen.Head.IB', 'match_priority = 0\n'))],
'e015297d': [(log, ('2.8: Ellen Face blend_vb Hash',)),                  (add_section_if_missing, ('f6ef8f3a', 'Ellen.Head.IB', 'match_priority = 0\n'))],

# Weapon - Scythe
'14ee18a1': [(log, ('2.8: Ellen Scythe Weapon VertexLimit Hash',)),     (add_section_if_missing, ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n'))],
'0e6ed776': [(log, ('2.8: Ellen Scythe Weapon position_vb Hash',)),     (add_section_if_missing, ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n'))],
'ad548430': [(log, ('2.8: Ellen Scythe Weapon texcoord_vb Hash',)),     (add_section_if_missing, ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n'))],
'6500eb53': [(log, ('2.8: Ellen Scythe Weapon blend_vb Hash',)),        (add_section_if_missing, ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n'))],

# Weapon - Spring
'a063d963': [(log, ('2.8: Ellen Spring Weapon VertexLimit Hash',)),     (add_section_if_missing, ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n'))],
'4b5ecba8': [(log, ('2.8: Ellen Spring Weapon position_vb Hash',)),     (add_section_if_missing, ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n'))],
'c75b2bfe': [(log, ('2.8: Ellen Spring Weapon texcoord_vb Hash',)),     (add_section_if_missing, ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n'))],
'4afdcca5': [(log, ('2.8: Ellen Spring Weapon blend_vb Hash',)),        (add_section_if_missing, ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'9c7fac5a': [(log, ('1.0 -> 1.1: Ellen Head IB Hash',)),       (update_hash, ('f6ef8f3a',))],
'7f89a2b3': [(log, ('1.0 -> 1.1: Ellen Hair IB Hash',)),       (update_hash, ('d44a8015',))],
'a72cfb34': [(log, ('1.0 -> 1.1: Ellen Body IB Hash',)),       (update_hash, ('e30fae03',))],
'4f4a54f0': [(log, ('1.0 -> 1.1: Ellen Body Blend Hash',)),    (update_hash, ('89589539',))],
'83dfd744': [(log, ('1.0 -> 1.1: Ellen Head Texcoord Hash',)), (update_hash, ('8744badf',))],
'd59a5fec': [(log, ('1.0 -> 1.1: Ellen Hair Draw Hash',)),     (update_hash, ('77ac5f85',))],
'a5448398': [(log, ('1.0 -> 1.1: Ellen Hair Position Hash',)), (update_hash, ('ba0fe600',))],
'9cddb082': [
        (log, ('1.0 -> 1.1: Ellen Hair Texcoord Hash',)),
        (update_hash, ('5c33833e',)),
        (log, ('+ Remapping texcoord buffer from stride 24 to 36',)),
        (zzz_13_remap_texcoord, ('11_Ellen_Hair', ('4B', '2e', '2f', '2e', '2e'), ('4f', '2e', '2f', '2e', '2e'))), # attention
    ],
'5c33833e': [
        (log, ('1.1 -> 1.2: Ellen Hair Texcoord Hash',)),
        (update_hash, ('a27a8e1a',)),
        (log, ('+ Remapping texcoord buffer from stride 36 to 24',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'2f9df031': [(log, ('1.2 -> 1.3: Ellen Hair Blend Hash',)),    (update_hash, ('52188576',))],
'52188576': [
        (log,                         ('1.3 -> 1.4: Ellen Hair Blend Remap',)),
        (update_buffer_blend_indices, (
            '52188576',
            (34, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50),
            (39, 34, 40, 35, 38, 42, 43, 44, 45, 46, 47, 41, 50, 49),
        )),
        (update_hash,                 ('e91c93e0',)),
    ],
'7bd3f8c2': [(log, ('1.0 -> 1.1: Ellen Body Draw Hash',)),     (update_hash, ('cdce1fc2',))],
'89d5fba4': [(log, ('1.0 -> 1.1: Ellen Body Position Hash',)), (update_hash, ('b78f3616',))],
'26966844': [(log, ('1.0 -> 1.1: Ellen Body Texcoord Hash',)), (update_hash, ('5ac6d5ee',))],
'89589539': [(log, ('1.5 -> 1.6: Ellen Body Blend Hash',)),    (update_hash, ('ed9cb852',))],
'09d55bce': [(log, ('1.0 -> 1.1: Ellen HeadA Diffuse 2048p Hash',)), (update_hash, ('465a66eb',))],
'465a66eb': [
        (log,                           ('1.1: Ellen HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('f6ef8f3a', '9c7fac5a'), 'Ellen.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4808d050', 'e6b27e31'), 'Ellen.HeadA.Diffuse.1024')),
    ],
'e6b27e31': [(log, ('1.0 -> 1.1: Ellen HeadA Diffuse 1024p Hash',)), (update_hash, ('4808d050',))],

# === Pembaruan Sinkronisasi Senjata v2.8 (Scythe) ===
'b06f7cb9': [(log, ('2.0 -> 2.8: Ellen Weapon Diffuse [Legacy]',)), (update_hash, ('e9e610cd',))],
'0567bc4e': [(log, ('2.0 -> 2.8: Ellen Weapon LightMap [Legacy]',)), (update_hash, ('1721ed1a',))],
'd4c2adaa': [(log, ('2.0 -> 2.8: Ellen Weapon MaterialMap [Legacy]',)), (update_hash, ('9aaa6b4b',))],

# === Face Textures ===
'4808d050': [
        (log,                           ('2.8: Ellen HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('f6ef8f3a', '9c7fac5a'), 'Ellen.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('465a66eb', '09d55bce'), 'Ellen.HeadA.Diffuse.2048')),
    ],

# === Hair Textures ===
'81ccd2e2': [
        (log,                           ('2.8: Ellen HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1440e534', 'Ellen.HairA.Diffuse.1024')),
    ],
'1440e534': [
        (log,                           ('2.8: Ellen HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('81ccd2e2', 'Ellen.HairA.Diffuse.2048')),
    ],
'dc9d8b6e': [
        (log,                           ('2.8: Ellen HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8c835faa', 'Ellen.HairA.LightMap.1024')),
    ],
'8c835faa': [
        (log,                           ('2.8: Ellen HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc9d8b6e', 'Ellen.HairA.LightMap.2048')),
    ],
'01bb8189': [
        (log,                           ('2.8: Ellen HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b21b8370', 'Ellen.HairA.MaterialMap.1024')),
    ],
'b21b8370': [
        (log,                           ('2.8: Ellen HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('01bb8189', 'Ellen.HairA.MaterialMap.2048')),
    ],
'aaadca31': [
        (log,                           ('2.8: Ellen HairA NormalMap 2048p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'd6715e09': [
        (log,                           ('2.8: Ellen HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', 'aaadca31'), 'Ellen.HairA.NormalMap.2048')),
    ],

# === Body Textures ===
'cf5f5fed': [
        (log,                           ('2.8: Ellen BodyA Diffuse 2048p Hash (Old)',)),
        (update_hash,                   ('163e2559',)),
    ],
'163e2559': [
        (log,                           ('2.8: Ellen BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('22fa0cd6', '94c15986'), 'Ellen.BodyA.Diffuse.1024')),
    ],
'94c15986': [
        (log,                           ('2.8: Ellen BodyA Diffuse 1024p Hash (Old)',)),
        (update_hash,                   ('22fa0cd6',)),
    ],
'22fa0cd6': [
        (log,                           ('2.8: Ellen BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('163e2559', 'cf5f5fed'), 'Ellen.BodyA.Diffuse.2048')),
    ],
'ff26fb83': [
        (log,                           ('2.8: Ellen BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cea7516a', 'Ellen.BodyA.LightMap.1024')),
    ],
'cea7516a': [
        (log,                           ('2.8: Ellen BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ff26fb83', 'Ellen.BodyA.LightMap.2048')),
    ],
'f4487235': [
        (log,                           ('2.8: Ellen BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('30dc14d7', 'Ellen.BodyA.MaterialMap.1024')),
    ],
'30dc14d7': [
        (log,                           ('2.8: Ellen BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f4487235', 'Ellen.BodyA.MaterialMap.2048')),
    ],
'798c3a51': [
        (log,                           ('2.8: Ellen BodyA NormalMap 2048p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'590880e5': [
        (log,                           ('2.8: Ellen BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '798c3a51'), 'Ellen.BodyA.NormalMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'e9e610cd': [
        (log,                           ('2.8: Ellen Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n')),
    ],
'1721ed1a': [
        (log,                           ('2.8: Ellen Weapon LightMap Hash',)),
        (add_section_if_missing,        ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n')),
    ],
'9aaa6b4b': [
        (log,                           ('2.8: Ellen Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Ellen Shared NormalMap Hash',)),
        (add_section_if_missing,        ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('569f47ac', 'Ellen.WeaponScythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2747bdd1', 'Ellen.WeaponSpring.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7b54b96f', 'Ellen.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Ellen HairA and BodyA NormalMap 2048p Hash (shared)',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d6715e09', 'Ellen.HairA.NormalMap.1024')),
        (multiply_section_if_missing,   ('590880e5', 'Ellen.BodyA.NormalMap.1024')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ellen',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}