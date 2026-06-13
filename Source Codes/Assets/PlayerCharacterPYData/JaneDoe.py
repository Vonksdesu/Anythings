"""
JaneDoe Character Hash Commands
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
    Returns JaneDoe's hash commands dictionary.
    """
    return {
# === IB Hashes (v2.8) ===
'3275b812': [(log, ('2.8: Jane Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'ba4255a5': [(log, ('2.8: Jane Body IB Hash',)),                        (add_ib_check_if_missing,)],
'ef86fc9f': [(log, ('2.8: Jane Head/Face IB Hash',)),                   (add_ib_check_if_missing,)],
'27805144': [(log, ('2.8: Jane Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'602c545a': [(log, ('2.8: Jane Weapon Hand Blade IB Hash',)),            (add_ib_check_if_missing,)],
'f7a304e8': [(log, ('2.8: Jane Weapon Leg Blade IB Hash',)),             (add_ib_check_if_missing,)],
'294a319a': [(log, ('2.8: Jane Hands & Accessories IB Hash',)),         (add_ib_check_if_missing,)],
'ac900322': [(log, ('2.8: JaneSkin Body IB Hash',)),                      (add_ib_check_if_missing,)],
'ca887a07': [(log, ('2.8: JaneSkin LegRingGemstone IB Hash',)),           (add_ib_check_if_missing,)],

# === VB Hashes (v2.8) ===
# Hair
'74bc0b7f': [(log, ('2.8: Jane Hair Draw Hash',)),                      (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],
'33a09cfe': [(log, ('2.8: Jane Hair Position Hash',)),                  (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],
'fa617c9a': [(log, ('2.8: Jane Hair Texcoord Hash',)),                  (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],
'e42171df': [(log, ('2.8: Jane Hair Blend Hash',)),                     (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],

# Body
'0e1c6740': [(log, ('2.8: Jane Body Draw Hash',)),                      (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],
'10050266': [(log, ('2.8: Jane Body Position Hash',)),                  (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],
'949549de': [(log, ('2.8: Jane Body Texcoord Hash',)),                  (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],
'e27f398e': [(log, ('2.8: Jane Body Blend Hash',)),                     (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],

# Face
'5661afc3': [(log, ('2.8: Jane Face VertexLimit Hash',)),                (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],
'6c733c84': [(log, ('2.8: Jane Face position_vb Hash',)),                (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],
'1fa404c1': [(log, ('2.8: Jane Face texcoord_vb Hash',)),                (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],
'91846a84': [(log, ('2.8: Jane Face blend_vb Hash',)),                   (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],

# Weapon - Hand Blade
'be378e74': [(log, ('2.8: Jane Hand Blade draw_vb Hash',)),              (add_section_if_missing, ('602c545a', 'Jane.HandBlade.IB', 'match_priority = 0\n'))],

# Weapon - Leg Blade
'29a81e40': [(log, ('2.8: Jane Leg Blade draw_vb Hash',)),               (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],
'566bb5f4': [(log, ('2.8: Jane Leg Blade position_vb Hash',)),           (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],
'aa4168d9': [(log, ('2.8: Jane Leg Blade texcoord_vb Hash',)),           (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],
'f038d9a5': [(log, ('2.8: Jane Leg Blade blend_vb Hash',)),              (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],

# Hands & Accessories (v2.5+ New Component)
'2b5dc947': [(log, ('2.8: Jane Hands & Accessories draw_vb Hash',)),      (add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],
'82e7c056': [(log, ('2.8: Jane Hands & Accessories position_vb Hash',)),  (add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],
'6d482e21': [(log, ('2.8: Jane Hands & Accessories texcoord_vb Hash',)),  (add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],
'd06a9206': [(log, ('2.8: Jane Hands & Accessories blend_vb Hash',)),     (add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],

# Skin: Body VBs
'3f009560': [(log, ('2.8: JaneSkin Body draw_vb Hash',)),                (add_section_if_missing, ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n'))],
'4544dca7': [(log, ('2.8: JaneSkin Body position_vb Hash',)),            (add_section_if_missing, ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n'))],
'6845e991': [(log, ('2.8: JaneSkin Body texcoord_vb Hash',)),            (add_section_if_missing, ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n'))],
'44071a5e': [(log, ('2.8: JaneSkin Body blend_vb Hash',)),               (add_section_if_missing, ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n'))],

# Skin: LegRingGemstone VBs
'65c0f994': [(log, ('2.8: JaneSkin LegRingGemstone draw_vb Hash',)),      (add_section_if_missing, ('ca887a07', 'JaneSkin.LegRingGemstone.IB', 'match_priority = 0\n'))],
'ad125746': [(log, ('2.8: JaneSkin LegRingGemstone position_vb Hash',)),  (add_section_if_missing, ('ca887a07', 'JaneSkin.LegRingGemstone.IB', 'match_priority = 0\n'))],
'7c6a8591': [(log, ('2.8: JaneSkin LegRingGemstone texcoord_vb Hash',)),  (add_section_if_missing, ('ca887a07', 'JaneSkin.LegRingGemstone.IB', 'match_priority = 0\n'))],
'370c397a': [(log, ('2.8: JaneSkin LegRingGemstone blend_vb Hash',)),     (add_section_if_missing, ('ca887a07', 'JaneSkin.LegRingGemstone.IB', 'match_priority = 0\n'))],

# Skin: HairShadow VBs
'759a4b9f': [(log, ('2.8: JaneSkin HairShadow draw_vb Hash',)),          (add_section_if_missing, ('27805144', 'JaneSkin.HairShadow.IB', 'match_priority = 0\n'))],
'7c08cd53': [(log, ('2.8: JaneSkin HairShadow position_vb Hash',)),      (add_section_if_missing, ('27805144', 'JaneSkin.HairShadow.IB', 'match_priority = 0\n'))],
'93c5b49a': [(log, ('2.8: JaneSkin HairShadow texcoord_vb Hash',)),      (add_section_if_missing, ('27805144', 'JaneSkin.HairShadow.IB', 'match_priority = 0\n'))],
'6af472f5': [(log, ('2.8: JaneSkin HairShadow blend_vb Hash',)),         (add_section_if_missing, ('27805144', 'JaneSkin.HairShadow.IB', 'match_priority = 0\n'))],

# === Version Update Paths ===
'c8ad344e': [
        (log, ('1.1 -> 1.2: Jane Hair Texcoord Hash',)),
        (update_hash, ('257a90d6',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'5721e4e7': [(log, ('1.3 -> 1.4: Jane Hair Draw Hash',)),     (update_hash, ('2d06e785',)),],
'24323bf9': [(log, ('1.3 -> 1.4: Jane Hair Position Hash',)), (update_hash, ('e7a3b7dc',)),],
'0a10c747': [(log, ('1.3 -> 1.4: Jane Hair Blend Hash',)),    (update_hash, ('8721477f',)),],
'257a90d6': [(log, ('1.3 -> 1.4: Jane Hair Texcoord Hash',)), (update_hash, ('acec29f8',)),],
'7b16a708': [(log, ('1.3 -> 1.4: Jane Hair IB Hash',)),       (update_hash, ('9268a5af',)),],
'9268a5af': [(log, ('1.4 -> 2.5: Jane Hair IB Hash',)),       (update_hash, ('3275b812',)),],
'8721477f': [(log, ('1.4 -> 2.5: Jane Hair Blend Hash',)),    (update_hash, ('e42171df',)),],
'e7a3b7dc': [(log, ('1.4 -> 2.5: Jane Hair Position Hash',)), (update_hash, ('33a09cfe',)),],
'acec29f8': [(log, ('1.4 -> 2.5: Jane Hair Texcoord Hash',)), (update_hash, ('fa617c9a',)),],
'2d06e785': [(log, ('1.4 -> 2.5: Jane Hair Draw Hash',)),     (update_hash, ('74bc0b7f',)),],
'd1aa4b85': [(log, ('1.3 -> 1.4: Jane Body Draw Hash',)),     (update_hash, ('0e1c6740',)),],
'06f9bc49': [(log, ('1.3 -> 1.4: Jane Body Position Hash',)), (update_hash, ('10050266',)),],
'9727a184': [(log, ('1.3 -> 1.4: Jane Body Blend Hash',)),    (update_hash, ('e27f398e',)),],
'8b85c03e': [(log, ('1.3 -> 1.4: Jane Body Texcoord Hash',)), (update_hash, ('949549de',)),],
'e2c0144e': [(log, ('1.3 -> 1.4: Jane Body IB Hash',)),       (update_hash, ('ba4255a5',)),],
'689639a5': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 1024p Hash',)), (update_hash, ('d823ac80',)),],
'8974fb74': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 2048p Hash',)), (update_hash, ('3b75aa2c',)),],

# === Face Textures ===
'3b75aa2c': [
        (log,                           ('2.8: Jane HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d823ac80', '689639a5'), 'Jane.HeadA.Diffuse.1024')),
    ],
'd823ac80': [
        (log,                           ('2.8: Jane HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3b75aa2c', '8974fb74'), 'Jane.HeadA.Diffuse.2048')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Jane Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('602c545a', 'Jane.HandBlade.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Jane Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('3275b812', '9268a5af'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'f7ef1a53': [
        (log,                           ('2.8: Jane HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b33a9770', 'Jane.HairA.Diffuse.1024')),
    ],
'b33a9770': [
        (log,                           ('2.8: Jane HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f7ef1a53', 'Jane.HairA.Diffuse.2048')),
    ],
'9ec4cd4f': [
        (log,                           ('2.8: Jane HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5e12acc1', 'Jane.HairA.LightMap.1024')),
    ],
'5e12acc1': [
        (log,                           ('2.8: Jane HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9ec4cd4f', 'Jane.HairA.LightMap.2048')),
    ],
'5e34e275': [
        (log,                           ('2.8: Jane HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('40fca454', 'Jane.HairA.MaterialMap.1024')),
    ],
'40fca454': [
        (log,                           ('2.8: Jane HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5e34e275', 'Jane.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'd1f56c7d': [
        (log,                           ('2.8: Jane BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e62ae3b5', 'Jane.BodyA.Diffuse.1024')),
    ],
'e62ae3b5': [
        (log,                           ('2.8: Jane BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d1f56c7d', 'Jane.BodyA.Diffuse.2048')),
    ],
'3087f82a': [
        (log,                           ('2.8: Jane BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('52fa9861', 'Jane.BodyA.LightMap.1024')),
    ],
'52fa9861': [
        (log,                           ('2.8: Jane BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3087f82a', 'Jane.BodyA.LightMap.2048')),
    ],
'99eae42e': [
        (log,                           ('2.8: Jane BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5dce2408', 'Jane.BodyA.MaterialMap.1024')),
    ],
'5dce2408': [
        (log,                           ('2.8: Jane BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('99eae42e', 'Jane.BodyA.MaterialMap.2048')),
    ],

# === Weapon Hand Blade Textures (v2.8 Target) ===
'59c18114': [
        (log,                           ('2.8: Jane Weapon Hand Blade Diffuse Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandBlade.IB', 'match_priority = 0\n')),
    ],
'76cda993': [
        (log,                           ('2.8: Jane Weapon Hand Blade LightMap Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandBlade.IB', 'match_priority = 0\n')),
    ],
'd83ad325': [
        (log,                           ('2.8: Jane Weapon Hand Blade MaterialMap Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandBlade.IB', 'match_priority = 0\n')),
    ],

# === Skin: Body Textures (v2.8 Target) ===
'a47bf989': [
        (log,                           ('2.8: JaneSkin Body Diffuse Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n')),
    ],
'dd1b5520': [
        (log,                           ('2.8: JaneSkin Body LightMap Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n')),
    ],
'389d9c67': [
        (log,                           ('2.8: JaneSkin Body MaterialMap Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneSkin.Body.IB', 'match_priority = 0\n')),
    ],

# === Skin: LegRingGemstone Textures (v2.8 Target) ===
'e108fa5b': [
        (log,                           ('2.8: JaneSkin LegRingGemstone Diffuse Hash',)),
        (add_section_if_missing,        ('ca887a07', 'JaneSkin.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoe',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}