"""
WiseTemple Character Hash Commands
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
    Returns WiseTemple's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'01c42a1d': [(log, ('2.8: WiseTemple Neck IB Hash',)),                  (add_ib_check_if_missing,)],
'1eca2097': [(log, ('2.8: WiseTemple Body IB Hash',)),                  (add_ib_check_if_missing,)],
'1fdaf388': [(log, ('2.8: WiseTemple Face IB Hash',)),                  (add_ib_check_if_missing,)],
'd5ca0411': [(log, ('2.8: WiseTemple Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'e7f527ea': [(log, ('2.8: WiseTemple DiskPlayer IB Hash',)),             (add_ib_check_if_missing,)],
'8d08b190': [(log, ('2.8: WiseTemple HairShadow IB Hash',)),            (add_ib_check_if_missing,)],
'eeabff55': [(log, ('2.8: WiseTemple Torso Ribbon IB Hash',)),          (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: WiseTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'e5f8b021': [(log, ('2.8: WiseTemple Black Orange Ribbon IB Hash',)),   (add_ib_check_if_missing,)],
'e5f269f4': [(log, ('2.8: WiseTemple Orange Green Ribbon IB Hash',)),   (add_ib_check_if_missing,)],
'bfce3c18': [(log, ('2.8: WiseTemple Glasses IB Hash',)),               (add_ib_check_if_missing,)],
'b856d397': [(log, ('2.8: WiseTemple Earrings IB Hash',)),               (add_ib_check_if_missing,)],
'd0e278fc': [(log, ('2.8: WiseTemple CatEar IB Hash',)),                 (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.8: WiseTemple TorsoAcc IB Hash',)),               (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'ef9c0510': [(log, ('2.8: WiseTemple Hair draw_vb',)),                  (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],
'e8df7ff3': [(log, ('2.8: WiseTemple Hair position_vb',)),              (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],
'774071dd': [(log, ('2.8: WiseTemple Hair texcoord_vb',)),              (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],
'edfd1666': [(log, ('2.8 -> 3.0: WiseTemple Hair blend_vb Hash [Legacy]',)), (update_hash, ('68e4f572',))],

# Hair Shadow
'681651f9': [(log, ('2.8: WiseTemple HairShadow draw_vb',)),            (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],
'4af493e5': [(log, ('2.8: WiseTemple HairShadow position_vb',)),        (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],
'ad7d7eca': [(log, ('2.8: WiseTemple HairShadow texcoord_vb',)),        (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],
'795e9a7c': [(log, ('2.8: WiseTemple HairShadow blend_vb',)),           (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],

# Neck
'276e1373': [(log, ('2.8: WiseTemple Neck draw_vb',)),                  (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],
'd8ad824b': [(log, ('2.8: WiseTemple Neck position_vb',)),              (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],
'39a1dfe3': [(log, ('2.8: WiseTemple Neck texcoord_vb',)),              (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],
'458bbde3': [(log, ('2.8 -> 3.0: WiseTemple Neck blend_vb Hash [Legacy]',)), (update_hash, ('e0b1e734',))],

# Body (WiseTemple Outfit)
'ca02f614': [(log, ('2.8: WiseTemple Body draw_vb',)),                  (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],
'a388eb6b': [(log, ('2.8: WiseTemple Body position_vb',)),              (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],
'b39870e1': [(log, ('2.8: WiseTemple Body texcoord_vb',)),              (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],
'8612559a': [(log, ('2.8 -> 3.0: WiseTemple Body blend_vb Hash [Legacy]',)), (update_hash, ('f28a6363',))],

# WaistAccessories (DiskPlayer Acc)
'0c1c9bf3': [(log, ('2.8: WiseTemple WaistAccessories draw_vb',)),       (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],
'1e5cafee': [(log, ('2.8: WiseTemple WaistAccessories position_vb',)),   (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],
'06f42a6f': [(log, ('2.8: WiseTemple WaistAccessories texcoord_vb',)),   (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],
'0a0aa1a8': [(log, ('2.8: WiseTemple WaistAccessories blend_vb',)),      (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],

# Face VBs & Limits
'6c4552bb': [(log, ('2.8: WiseTemple Face VertexLimit',)),              (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],
'5657c1fc': [(log, ('2.8: WiseTemple Face Position',)),                 (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],
'c83b6cbf': [(log, ('2.8: WiseTemple Face Texcoord',)),                 (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],
'757bc7cc': [(log, ('2.8: WiseTemple Face Blend',)),                    (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],

# Torso Ribbon VBs
'e0931b87': [(log, ('2.8: WiseTemple Torso Ribbon draw_vb',)),          (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],
'fe8e2ff8': [(log, ('2.8: WiseTemple Torso Ribbon position_vb',)),      (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],
'b6108302': [(log, ('2.8: WiseTemple Torso Ribbon texcoord_vb',)),      (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],
'd9691e6b': [(log, ('2.8: WiseTemple Torso Ribbon blend_vb',)),          (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],

# Panda Headgear VBs
'e7d550d0': [(log, ('2.8: WiseTemple Panda Headgear draw_vb',)),        (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'c8a749b1': [(log, ('2.8: WiseTemple Panda Headgear position_vb',)),    (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'e938a289': [(log, ('2.8: WiseTemple Panda Headgear texcoord_vb',)),    (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'ece854ad': [(log, ('2.8: WiseTemple Panda Headgear blend_vb',)),       (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],

# Black Orange Ribbon VBs
'aad48132': [(log, ('2.8: WiseTemple Black Orange Ribbon draw_vb',)),   (add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],
'139c0e20': [(log, ('2.8: WiseTemple Black Orange Ribbon position_vb',)),(add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],
'0f705b4a': [(log, ('2.8: WiseTemple Black Orange Ribbon texcoord_vb',)),(add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],
'a60b2098': [(log, ('2.8: WiseTemple Black Orange Ribbon blend_vb',)),   (add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],

# Orange Green Ribbon VBs
'2efc0d70': [(log, ('2.8: WiseTemple Orange Green Ribbon draw_vb',)),   (add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'e801def3': [(log, ('2.8: WiseTemple Orange Green Ribbon position_vb',)),(add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'bc87900c': [(log, ('2.8: WiseTemple Orange Green Ribbon texcoord_vb',)),(add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'4851307e': [(log, ('2.8: WiseTemple Orange Green Ribbon blend_vb',)),   (add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],

# Glasses VBs
'ba8bde72': [(log, ('2.8: WiseTemple Glasses draw_vb',)),               (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],
'66cabdf9': [(log, ('2.8: WiseTemple Glasses position_vb',)),           (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],
'ac329cd7': [(log, ('2.8: WiseTemple Glasses texcoord_vb',)),           (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],
'a8620018': [(log, ('2.8: WiseTemple Glasses blend_vb',)),              (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],

# Earrings VBs
'5a617015': [(log, ('2.8: WiseTemple Earrings draw_vb',)),               (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],
'49a9bab4': [(log, ('2.8: WiseTemple Earrings position_vb',)),           (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],
'a9b9bf40': [(log, ('2.8: WiseTemple Earrings texcoord_vb',)),           (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],
'686847cc': [(log, ('2.8: WiseTemple Earrings blend_vb',)),              (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],

# CatEar VBs
'ad73aefc': [(log, ('2.8: WiseTemple CatEar draw_vb',)),                 (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],
'53b4170f': [(log, ('2.8: WiseTemple CatEar position_vb',)),             (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],
'3280491f': [(log, ('2.8: WiseTemple CatEar texcoord_vb',)),             (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],
'603fdb26': [(log, ('2.8: WiseTemple CatEar blend_vb',)),                (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],

# TorsoAcc VBs
'0406d75f': [(log, ('2.8: WiseTemple TorsoAcc draw_vb',)),             (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'13e791fa': [(log, ('2.8: WiseTemple TorsoAcc position_vb',)),         (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'fd95b568': [(log, ('2.8: WiseTemple TorsoAcc texcoord_vb',)),         (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'e147258a': [(log, ('2.8: WiseTemple TorsoAcc blend_vb',)),            (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],

# === Legacy / Version Updates ===
'6acc1eb8': [(log, ('2.5 -> 2.8: WiseTemple Body IB [Legacy]',)),       (update_hash, ('1eca2097',))],
'ae59eabb': [(log, ('2.5 -> 2.8: WiseTemple Body Position [Legacy]',)), (update_hash, ('a388eb6b',))],
'a83ada4e': [(log, ('2.5 -> 2.8: WiseTemple Body Texcoord [Legacy]',)), (update_hash, ('b39870e1',))],
'177ad7e8': [(log, ('2.5 -> 2.8: WiseTemple Body Blend [Legacy]',)),    (update_hash, ('8612559a',))],
'4fa228f9': [(log, ('2.5 -> 2.8: WiseTemple Body Draw [Legacy]',)),     (update_hash, ('ca02f614',))],

# === Broken References Fix (v2.8) ===
'f425bd04': [(log, ('2.8: Wise Body Texcoord Hash [Legacy] 2.0',)),     (update_hash, ('91fbd2fa',))],
'84529dab': [(log, ('2.8: Wise BodyA Diffuse 2048p Hash [Legacy] Old',)), (update_hash, ('f2fb7a37',))],
'ef76b675': [(log, ('2.8: Wise BodyA Diffuse 1024p Hash [Legacy] Old',)), (update_hash, ('3d7a53b0',))],

# === 2.8 Sync Updates ===
'868709f2': [(log, ('2.7 -> 2.8: Wise BodyA Diffuse [Legacy]',)), (update_hash, ('f2fb7a37',))],

# === 3.0 Database Updates (Strict Sync) ===
# Hair VBs
'68e4f572': [(log, ('3.0: WiseTemple Hair blend_vb Hash',)),            (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],

# Neck VBs
'e0b1e734': [(log, ('3.0: WiseTemple Neck blend_vb Hash',)),            (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],

# Body VBs
'f28a6363': [(log, ('3.0: WiseTemple Body blend_vb Hash',)),            (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'5d75fddc': [
        (log,                           ('2.8: WiseTemple Face Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
    ],
'588d7d2d': [
        (log,                           ('2.8: WiseTemple FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
    ],
'8f9d78c1': [
        (log,                           ('2.8: WiseTemple HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('1fdaf388', '4894246e'), 'WiseTemple.Head.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'cb0d0c22': [
        (log,                           ('2.8: WiseTemple HairA Diffuse Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'28005a5b': [
        (log,                           ('2.8: WiseTemple Hair Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'33368e12': [
        (log,                           ('2.8: WiseTemple HairA LightMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('2.8: WiseTemple Hair LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'd9383a15': [
        (log,                           ('2.8: WiseTemple HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('2.8: WiseTemple Hair MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],

# === Neck & Body Textures ===
'669191ec': [
        (log,                           ('3.0: WiseTemple Neck, Body Diffuse Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'9fc3646e': [
        (log,                           ('2.8 -> 3.0: WiseTemple Neck, Body Diffuse Hash [Legacy]',)),
        (update_hash,                   ('669191ec',)),
    ],
'81406abe': [
        (log,                           ('2.8 -> 3.0: WiseTemple Body/Neck Diffuse Hash [Legacy]',)),
        (update_hash,                   ('669191ec',)),
    ],
'dd79b44b': [
        (log,                           ('2.8: WiseTemple Neck, Body LightMap Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'05b25d35': [
        (log,                           ('2.8: WiseTemple Body/Neck LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'aa712fb9': [
        (log,                           ('2.8: WiseTemple Neck, Body MaterialMap Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'24af1f48': [
        (log,                           ('2.8: WiseTemple Body/Neck MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],

# === DiskPlayer / WaistAccessories Textures ===
'e590e6be': [
        (log,                           ('2.8: WiseTemple WaistAccessories Diffuse Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'3fef0e14': [
        (log,                           ('2.8: WiseTemple DiskPlayer Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'a78880dc': [
        (log,                           ('2.8: WiseTemple WaistAccessories LightMap Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'08b27f4a': [
        (log,                           ('2.8: WiseTemple DiskPlayer LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'4a0b4014': [
        (log,                           ('2.8: WiseTemple WaistAccessories MaterialMap Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'a15aa6b3': [
        (log,                           ('2.8: WiseTemple Face/DiskPlayer MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

# === Panda Headgear Textures (v2.8 Target) ===
'a2f096fc': [
        (log,                           ('2.8: WiseTemple Panda Headgear Diffuse Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n')),
    ],
'78c2d1dd': [
        (log,                           ('2.8: WiseTemple Panda Headgear LightMap Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n')),
    ],
'2a7548a9': [
        (log,                           ('2.8: WiseTemple Panda Headgear MaterialMap Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n')),
    ],

# === Earrings2 / CatEar Textures (v2.8 Target) ===
'ed1a5b7f': [
        (log,                           ('2.8: WiseTemple Earrings2 / CatEar Diffuse Hash',)),
        (add_section_if_missing,        ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n')),
    ],
'f5dc4198': [
        (log,                           ('2.8: WiseTemple Earrings2 / CatEar LightMap Hash',)),
        (add_section_if_missing,        ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n')),
    ],
'5346205a': [
        (log,                           ('2.8: WiseTemple Earrings2 / CatEar MaterialMap Hash',)),
        (add_section_if_missing,        ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n')),
    ],

# === Orange Green Ribbon / Badge Textures (v2.8 Target) ===
'96ad58d4': [
        (log,                           ('2.8: WiseTemple Orange Green Ribbon / Badge Diffuse Hash',)),
        (add_section_if_missing,        ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n')),
    ],
'8839d1fc': [
        (log,                           ('2.8: WiseTemple Orange Green Ribbon / Badge LightMap Hash',)),
        (add_section_if_missing,        ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n')),
    ],
'cd075caa': [
        (log,                           ('2.8: WiseTemple Orange Green Ribbon / Badge MaterialMap Hash',)),
        (add_section_if_missing,        ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: WiseTemple Shared NormalMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseTemple',
    'game_versions': ['2.8', '3.0'],
}