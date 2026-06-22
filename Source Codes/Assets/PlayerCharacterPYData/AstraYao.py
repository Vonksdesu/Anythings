"""
AstraYao Character Hash Commands
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
    Returns AstraYao's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'53cdac6c': [(log, ('2.8: AstraYao Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'7a110804': [(log, ('2.8: AstraYao Body IB Hash',)),                      (add_ib_check_if_missing,)],
'92f33156': [(log, ('2.8: AstraYao Legs IB Hash',)),                      (add_ib_check_if_missing,)],
'51831437': [(log, ('2.8: AstraYao Face IB Hash',)),                      (add_ib_check_if_missing,)],
'93d55a49': [(log, ('2.8: AstraYao Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'702b018e': [(log, ('2.8: AstraYao Weapon Body IB Hash',)),               (add_ib_check_if_missing,)],
'f4f5348d': [(log, ('2.8: AstraYao Weapon Disc IB Hash',)),               (add_ib_check_if_missing,)],
'9bb42122': [(log, ('2.8: AstraYao Weapon Singing IB Hash',)),            (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd3c951b9': [(log, ('2.8: AstraYao Hair draw_vb',)),                      (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n'))],
'ee3c305a': [(log, ('2.8: AstraYao Hair position_vb',)),                  (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n'))],
'8ba0b335': [(log, ('2.8: AstraYao Hair texcoord_vb',)),                  (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n'))],
'c3c08f85': [(log, ('2.8: AstraYao Hair blend_vb',)),                     (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'5e1e12aa': [(log, ('2.8: AstraYao Hair Shadow draw_vb',)),               (add_section_if_missing, ('93d55a49', 'AstraYao.HairShadow.IB', 'match_priority = 0\n'))],
'a378328a': [(log, ('2.8: AstraYao Hair Shadow position_vb',)),           (add_section_if_missing, ('93d55a49', 'AstraYao.HairShadow.IB', 'match_priority = 0\n'))],
'c4456161': [(log, ('2.8: AstraYao Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('93d55a49', 'AstraYao.HairShadow.IB', 'match_priority = 0\n'))],
'81ef699b': [(log, ('2.8: AstraYao Hair Shadow blend_vb',)),              (add_section_if_missing, ('93d55a49', 'AstraYao.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'13a07361': [(log, ('2.8: AstraYao Body draw_vb',)),                      (add_section_if_missing, ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n'))],
'9b17301d': [(log, ('2.8: AstraYao Body position_vb',)),                  (add_section_if_missing, ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n'))],
'240d8c83': [(log, ('2.8: AstraYao Body texcoord_vb',)),                  (add_section_if_missing, ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n'))],
'9d35c352': [(log, ('2.8: AstraYao Body blend_vb',)),                     (add_section_if_missing, ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n'))],

# Legs
'8a8dbdc5': [(log, ('2.8: AstraYao Legs draw_vb',)),                      (add_section_if_missing, ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n'))],
'97cef448': [(log, ('2.8: AstraYao Legs position_vb',)),                  (add_section_if_missing, ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n'))],
'1433ee78': [(log, ('2.8: AstraYao Legs texcoord_vb',)),                  (add_section_if_missing, ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n'))],
'bc4d6455': [(log, ('2.8: AstraYao Legs blend_vb',)),                     (add_section_if_missing, ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n'))],

# Face
'5c578f85': [(log, ('2.8: AstraYao Face draw_vb',)),                      (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n'))],
'66451cc2': [(log, ('2.8: AstraYao Face position_vb',)),                  (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n'))],
'ffac76ac': [(log, ('2.8: AstraYao Face texcoord_vb',)),                  (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n'))],
'7e05c11a': [(log, ('2.8: AstraYao Face blend_vb',)),                     (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n'))],

# Weapon - Body
'ca16b939': [(log, ('2.8: AstraYao Weapon Body draw_vb',)),               (add_section_if_missing, ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n'))],
'9879faf3': [(log, ('2.8: AstraYao Weapon Body position_vb',)),           (add_section_if_missing, ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n'))],
'b3e27d5f': [(log, ('2.8: AstraYao Weapon Body texcoord_vb',)),           (add_section_if_missing, ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n'))],
'4a4fb44e': [(log, ('2.8: AstraYao Weapon Body blend_vb',)),              (add_section_if_missing, ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n'))],

# Weapon - Disc
'7ed93255': [(log, ('2.8: AstraYao Weapon Disc draw_vb',)),               (add_section_if_missing, ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n'))],
'b8a9ba2e': [(log, ('2.8: AstraYao Weapon Disc position_vb',)),           (add_section_if_missing, ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n'))],
'd6d5743e': [(log, ('2.8: AstraYao Weapon Disc texcoord_vb',)),           (add_section_if_missing, ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n'))],
'cb9405e1': [(log, ('2.8: AstraYao Weapon Disc blend_vb',)),              (add_section_if_missing, ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n'))],

# Weapon - Singing Component
'6c67049b': [(log, ('2.8: AstraYao Weapon Singing draw_vb',)),           (add_section_if_missing, ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n'))],
'ced4a85d': [(log, ('2.8: AstraYao Weapon Singing position_vb',)),       (add_section_if_missing, ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n'))],
'401e9639': [(log, ('2.8: AstraYao Weapon Singing texcoord_vb',)),       (add_section_if_missing, ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n'))],
'8a2319f4': [(log, ('2.8: AstraYao Weapon Singing blend_vb',)),          (add_section_if_missing, ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'f8b92870': [(log, ('1.5 -> 1.6: AstraYao Hair Texcoord Hash',)), (update_hash, ('8ba0b335',)),],
'3cd13d03': [(log, ('1.5 -> 1.6: AstraYao Body Blend Hash',)),    (update_hash, ('9d35c352',)),],
'da86a32e': [(log, ('1.5 -> 1.6: AstraYao Legs Texcoord Hash',)), (update_hash, ('1433ee78',)),],
'77670042': [(log, ('1.5 -> 1.6: AstraYao Face Diffuse 1024p Hash',)), (update_hash, ('3283b8be',))],
'3a8d0dfc': [(log, ('1.5 -> 1.6: AstraYao Face Diffuse 2048p Hash',)), (update_hash, ('c41341b2',))],
'da673df0': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA Diffuse 2048p Hash',)), (update_hash, ('2daa2443',))],
'2daa2443': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA Diffuse 2048p Hash',)),   (update_hash, ('e634238a',))],
'34aad3b4': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA LightMap 2048p Hash',)), (update_hash, ('b085765e',))],
'b085765e': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA LightMap 2048p Hash',)),   (update_hash, ('34f0706c',))],
'b53b2e12': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA MaterialMap 2048p Hash',)), (update_hash, ('883a578f',))],
'7a507e4a': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA Diffuse 1024p Hash',)), (update_hash, ('4b1c1b47',))],
'4b1c1b47': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA Diffuse 1024p Hash',)),   (update_hash, ('56c71ea2',))],
'e4a4f975': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA LightMap 1024p Hash',)), (update_hash, ('c47a524a',))],
'c47a524a': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA LightMap 1024p Hash',)),   (update_hash, ('fd3ca2a6',))],
'0be99d44': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA MaterialMap 1024p Hash',)), (update_hash, ('759c15e0',))],

# === Weapon Sync Updates (v2.8) ===
'd652aa31': [(log, ('2.0 -> 2.8: AstraYao Weapon Diffuse [Legacy]',)), (update_hash, ('b5a20274',))],
'91c63955': [(log, ('2.0 -> 2.8: AstraYao Weapon LightMap [Legacy]',)), (update_hash, ('57c44e60',))],
'98e011bc': [(log, ('2.0 -> 2.8: AstraYao Weapon MaterialMap [Legacy]',)), (update_hash, ('fdb82c44',))],
'9a9e8842': [(log, ('2.0 -> 2.8: AstraYao Weapon Singing Diffuse [Legacy]',)), (update_hash, ('7503323d',))],
'364023c4': [(log, ('2.0 -> 2.8: AstraYao Weapon Singing LightMap [Legacy]',)), (update_hash, ('7e5fe2c6',))],
'fc68cf7d': [(log, ('2.0 -> 2.8: AstraYao Weapon Singing MaterialMap [Legacy]',)), (update_hash, ('87687182',))],

# === Face Textures ===
'3283b8be': [
        (log,                           ('2.8: AstraYao FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c41341b2', 'AstraYao.FaceA.Diffuse.2048')),
    ],
'c41341b2': [
        (log,                           ('2.8: AstraYao FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3283b8be', 'AstraYao.FaceA.Diffuse.1024')),
    ],

# === Hair & Legs Shared Textures ===
'e634238a': [
        (log,                           ('2.8: AstraYao HairA, LegsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('56c71ea2', '4b1c1b47', '7a507e4a'), 'AstraYao.HairA.Diffuse.1024')),
    ],
'34f0706c': [
        (log,                           ('2.8: AstraYao HairA, LegsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   (('fd3ca2a6', 'c47a524a', 'e4a4f975'), 'AstraYao.HairA.LightMap.1024')),
    ],
'883a578f': [
        (log,                           ('2.8: AstraYao HairA, LegsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   (('759c15e0', '0be99d44'), 'AstraYao.HairA.MaterialMap.1024')),
    ],
'56c71ea2': [
        (log,                           ('2.8: AstraYao HairA, LegsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('e634238a', '2daa2443', 'da673df0'), 'AstraYao.HairA.Diffuse.2048')),
    ],
'fd3ca2a6': [
        (log,                           ('2.8: AstraYao HairA, LegsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   (('34f0706c', 'b085765e', '34aad3b4'), 'AstraYao.HairA.LightMap.2048')),
    ],
'759c15e0': [
        (log,                           ('2.8: AstraYao HairA, LegsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   (('883a578f', 'b53b2e12'), 'AstraYao.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'd7f1c157': [
        (log,                           ('2.8: AstraYao BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e523eb0f', 'AstraYao.BodyA.Diffuse.1024')),
    ],
'dba7d767': [
        (log,                           ('2.8: AstraYao BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3f9f0d8a', 'AstraYao.BodyA.LightMap.1024')),
    ],
'21d5f5e3': [
        (log,                           ('2.8: AstraYao BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c4248e2d', 'AstraYao.BodyA.MaterialMap.1024')),
    ],
'e523eb0f': [
        (log,                           ('2.8: AstraYao BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d7f1c157', 'AstraYao.BodyA.Diffuse.2048')),
    ],
'3f9f0d8a': [
        (log,                           ('2.8: AstraYao BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dba7d767', 'AstraYao.BodyA.LightMap.2048')),
    ],
'c4248e2d': [
        (log,                           ('2.8: AstraYao BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('21d5f5e3', 'AstraYao.BodyA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'b5a20274': [
        (log,                           ('2.8: AstraYao Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n')),
    ],
'57c44e60': [
        (log,                           ('2.8: AstraYao Weapon LightMap Hash',)),
        (add_section_if_missing,        ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n')),
    ],
'fdb82c44': [
        (log,                           ('2.8: AstraYao Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n')),
    ],

# === Weapon Singing Textures (v2.8 Target) ===
'7503323d': [
        (log,                           ('2.8: AstraYao Weapon Singing Diffuse Hash',)),
        (add_section_if_missing,        ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n')),
    ],
'7e5fe2c6': [
        (log,                           ('2.8: AstraYao Weapon Singing LightMap Hash',)),
        (add_section_if_missing,        ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n')),
    ],
'87687182': [
        (log,                           ('2.8: AstraYao Weapon Singing MaterialMap Hash',)),
        (add_section_if_missing,        ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: AstraYao Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93d55a49', 'AstraYao.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('702b018e', 'AstraYao.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraYao.WeaponDisc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9bb42122', 'AstraYao.WeaponSinging.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: AstraYao Shared NormalMap Hash [Legacy]',)),
        (update_hash,                   ('798adba3',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AstraYao',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}