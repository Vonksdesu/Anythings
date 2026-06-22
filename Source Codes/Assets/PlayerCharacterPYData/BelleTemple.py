"""
BelleTemple Character Hash Commands
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
    Returns BelleTemple's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'30e40390': [(log, ('2.8: BelleTemple HeadAcc IB Hash',)),              (add_ib_check_if_missing,)],
'62ed56cc': [(log, ('2.8 -> 3.0: BelleTemple Neck IB Hash [Legacy]',)), (update_hash, ('d0627e1f',))],
'9a9780a7': [(log, ('2.8: BelleTemple Face IB Hash',)),                 (add_ib_check_if_missing,)],
'aa9ffb85': [(log, ('2.8: BelleTemple Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'bcc9e4e1': [(log, ('2.8: BelleTemple Legs IB Hash',)),                 (add_ib_check_if_missing,)],
'ce86946f': [(log, ('2.8: BelleTemple BackAcc IB Hash',)),              (add_ib_check_if_missing,)],
'd509bdd4': [(log, ('2.8: BelleTemple Body IB Hash',)),                 (add_ib_check_if_missing,)],
'db72ceab': [(log, ('2.8: BelleTemple HairWAcc IB Hash',)),              (add_ib_check_if_missing,)],
'403eace9': [(log, ('2.8: BelleTemple Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'c2189ddf': [(log, ('2.8: BelleTemple Red Knot Rope IB Hash',)),        (add_ib_check_if_missing,)],
'2ac09c8f': [(log, ('2.8: BelleTemple Orange Green Ribbon IB Hash',)),  (add_ib_check_if_missing,)],
'c0fcc53d': [(log, ('2.8: BelleTemple Earrings1 IB Hash',)),            (add_ib_check_if_missing,)],
'e6e890a7': [(log, ('2.8: BelleTemple Earrings2 IB Hash',)),            (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: BelleTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'b28a7685': [(log, ('2.8: BelleTemple Cat Ear Accessories IB Hash',)),  (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.8: BelleTemple Pink Badge IB Hash',)),           (add_ib_check_if_missing,)],
'4dcc384f': [(log, ('2.8: BelleTemple Orange Green Badge IB Hash',)),   (add_ib_check_if_missing,)],
'455bcfc7': [(log, ('2.8: BelleTemple Glasses IB Hash',)),               (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'd0627e1f': [(log, ('3.0: BelleTemple Neck IB Hash',)),                  (add_ib_check_if_missing,)],
'20d3a340': [(log, ('3.0: BelleTemple Headwear IB Hash',)),              (add_ib_check_if_missing,)],

# === VB Hashes ===
# HeadAcc
'eeea5739': [(log, ('2.8: BelleTemple HeadAcc draw_vb',)),              (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],
'17f8b9dc': [(log, ('2.8: BelleTemple HeadAcc position_vb',)),          (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],
'e5a8578f': [(log, ('2.8: BelleTemple HeadAcc blend_vb',)),             (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],
'fb8393bd': [(log, ('2.8: BelleTemple HeadAcc texcoord_vb',)),          (add_section_if_missing, ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n'))],

# TorsoAcc (Pink Badge)
'0406d75f': [(log, ('2.8: BelleTemple TorsoAcc draw_vb',)),             (add_section_if_missing, ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'a7882762': [(log, ('2.8: BelleTemple Pink Badge position_vb',)),       (add_section_if_missing, ('4e8b2454', 'BelleTemple.PinkBadge.IB', 'match_priority = 0\n'))],
'1ff12440': [(log, ('2.8: BelleTemple Pink Badge texcoord_vb',)),       (add_section_if_missing, ('4e8b2454', 'BelleTemple.PinkBadge.IB', 'match_priority = 0\n'))],
'e147258a': [(log, ('2.8: BelleTemple TorsoAcc blend_vb',)),            (add_section_if_missing, ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n'))],

# BackAcc
'83ba6b1f': [(log, ('2.8: BelleTemple BackAcc draw_vb',)),              (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],
'601e27b5': [(log, ('2.8: BelleTemple BackAcc position_vb',)),          (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],
'1a44a5ba': [(log, ('2.8: BelleTemple BackAcc blend_vb',)),             (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],
'81fd09f8': [(log, ('2.8: BelleTemple BackAcc texcoord_vb',)),          (add_section_if_missing, ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n'))],

# Hair
'992d149f': [(log, ('2.8: BelleTemple Hair draw_vb',)),                 (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'71d2bf80': [(log, ('2.8: BelleTemple Hair position_vb',)),             (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'39ac6700': [(log, ('2.8 -> 3.0: BelleTemple Hair blend_vb [Legacy]',)), (update_hash, ('8f7ae834',))],
'a5e62ece': [(log, ('2.8: BelleTemple Hair texcoord_vb',)),             (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],

# HairWAcc
'040e066c': [(log, ('2.8: BelleTemple HairWAcc draw_vb',)),             (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'682cbbe5': [(log, ('2.8: BelleTemple HairWAcc position_vb',)),         (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'd5b33c94': [(log, ('2.8: BelleTemple HairWAcc blend_vb',)),            (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],
'c6fe65c9': [(log, ('2.8: BelleTemple HairWAcc texcoord_vb',)),         (add_section_if_missing, ('db72ceab', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],

# Face
'04abceb5': [(log, ('2.8: BelleTemple Face draw_vb',)),                 (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('2.8: BelleTemple Face position_vb',)),             (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],
'0c9a075b': [(log, ('2.8 -> 3.0: BelleTemple Face blend_vb [Legacy]',)), (update_hash, ('359e4502',))],
'ccc76aea': [(log, ('2.8 -> 3.0: BelleTemple Face texcoord_vb Hash [Legacy]',)), (update_hash, ('d3000b22',))],

# Neck
'4c215c73': [(log, ('2.8 -> 3.0: BelleTemple Neck draw_vb Hash [Legacy]',)), (update_hash, ('3f594476',))],
'be75a4be': [(log, ('2.8 -> 3.0: BelleTemple Neck position_vb Hash [Legacy]',)), (update_hash, ('e2ee9309',))],
'dd2b89aa': [(log, ('2.8 -> 3.0: BelleTemple Neck texcoord_vb Hash [Legacy]',)), (update_hash, ('2f7f6398',))],
'3bd79a0b': [(log, ('2.8 -> 3.0: BelleTemple Neck blend_vb Hash [Legacy]',)), (update_hash, ('0a11b1d7',))],

# Body
'19e5f486': [(log, ('2.8: BelleTemple Body draw_vb',)),                 (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],
'8a4e97cd': [(log, ('2.8: BelleTemple Body position_vb',)),             (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],
'f3dedb50': [(log, ('2.8 -> 3.0: BelleTemple Body blend_vb Hash [Legacy]',)), (update_hash, ('4d74d5e9',))],
'd761e076': [(log, ('2.8: BelleTemple Body texcoord_vb',)),             (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],

# Legs
'720d6a16': [(log, ('2.8: BelleTemple Legs draw_vb',)),                 (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],
'42b88f48': [(log, ('2.8: BelleTemple Legs position_vb',)),             (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],
'f53b2eba': [(log, ('2.8 -> 3.0: BelleTemple Legs blend_vb Hash [Legacy]',)), (update_hash, ('922a7db6',))],
'82d0aadd': [(log, ('2.8: BelleTemple Legs texcoord_vb',)),             (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],

# Red Knot Rope VBs
'364415bf': [(log, ('2.8: BelleTemple Red Knot Rope draw_vb',)),        (add_section_if_missing, ('c2189ddf', 'BelleTemple.RedKnotRope.IB', 'match_priority = 0\n'))],
'903e5a55': [(log, ('2.8: BelleTemple Red Knot Rope position_vb',)),    (add_section_if_missing, ('c2189ddf', 'BelleTemple.RedKnotRope.IB', 'match_priority = 0\n'))],
'751107c4': [(log, ('2.8: BelleTemple Red Knot Rope texcoord_vb',)),    (add_section_if_missing, ('c2189ddf', 'BelleTemple.RedKnotRope.IB', 'match_priority = 0\n'))],
'83967fb0': [(log, ('2.8: BelleTemple Red Knot Rope blend_vb',)),       (add_section_if_missing, ('c2189ddf', 'BelleTemple.RedKnotRope.IB', 'match_priority = 0\n'))],

# Orange Green Ribbon VBs
'4fc2c5d3': [(log, ('2.8: BelleTemple Orange Green Ribbon draw_vb',)),   (add_section_if_missing, ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'bdfbdec4': [(log, ('2.8: BelleTemple Orange Green Ribbon position_vb',)),(add_section_if_missing, ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'01118441': [(log, ('2.8: BelleTemple Orange Green Ribbon texcoord_vb',)),(add_section_if_missing, ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'4e5447eb': [(log, ('2.8: BelleTemple Orange Green Ribbon blend_vb',)),   (add_section_if_missing, ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],

# Earrings1 VBs
'c0eb7af5': [(log, ('2.8: BelleTemple Earrings1 draw_vb',)),            (add_section_if_missing, ('c0fcc53d', 'BelleTemple.Earrings1.IB', 'match_priority = 0\n'))],
'fc4bea64': [(log, ('2.8: BelleTemple Earrings1 position_vb',)),        (add_section_if_missing, ('c0fcc53d', 'BelleTemple.Earrings1.IB', 'match_priority = 0\n'))],
'dde5eb66': [(log, ('2.8: BelleTemple Earrings1 texcoord_vb',)),        (add_section_if_missing, ('c0fcc53d', 'BelleTemple.Earrings1.IB', 'match_priority = 0\n'))],
'c2a072c2': [(log, ('2.8: BelleTemple Earrings1 blend_vb',)),           (add_section_if_missing, ('c0fcc53d', 'BelleTemple.Earrings1.IB', 'match_priority = 0\n'))],

# Earrings2 VBs
'8a73bd43': [(log, ('2.8: BelleTemple Earrings2 draw_vb',)),            (add_section_if_missing, ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n'))],
'c64ed62f': [(log, ('2.8: BelleTemple Earrings2 position_vb',)),        (add_section_if_missing, ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n'))],
'cd336cdb': [(log, ('2.8: BelleTemple Earrings2 texcoord_vb',)),        (add_section_if_missing, ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n'))],
'3d24a922': [(log, ('2.8: BelleTemple Earrings2 blend_vb',)),           (add_section_if_missing, ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n'))],

# Panda Headgear VBs
'e7d550d0': [(log, ('2.8: BelleTemple Panda Headgear draw_vb',)),        (add_section_if_missing, ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'910612d6': [(log, ('2.8: BelleTemple Panda Headgear position_vb',)),    (add_section_if_missing, ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'dc08776f': [(log, ('2.8: BelleTemple Panda Headgear texcoord_vb',)),    (add_section_if_missing, ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'f621226d': [(log, ('2.8: BelleTemple Panda Headgear blend_vb',)),       (add_section_if_missing, ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],

# CatEar VBs
'7c3db690': [(log, ('2.8: BelleTemple Cat Ear Accessories draw_vb',)),  (add_section_if_missing, ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n'))],
'b4341a72': [(log, ('2.8: BelleTemple Cat Ear Accessories position_vb',)),(add_section_if_missing, ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n'))],
'f98659b3': [(log, ('2.8: BelleTemple Cat Ear Accessories texcoord_vb',)),(add_section_if_missing, ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n'))],
'8650be1b': [(log, ('2.8: BelleTemple Cat Ear Accessories blend_vb',)),   (add_section_if_missing, ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n'))],

# Glasses VBs
'ba8bde72': [(log, ('2.8: BelleTemple Glasses draw_vb',)),               (add_section_if_missing, ('455bcfc7', 'BelleTemple.Glasses.IB', 'match_priority = 0\n'))],
'6018a88b': [(log, ('2.8: BelleTemple Glasses position_vb',)),           (add_section_if_missing, ('455bcfc7', 'BelleTemple.Glasses.IB', 'match_priority = 0\n'))],
'a70c787c': [(log, ('2.8: BelleTemple Glasses texcoord_vb',)),           (add_section_if_missing, ('455bcfc7', 'BelleTemple.Glasses.IB', 'match_priority = 0\n'))],
'a8620018': [(log, ('2.8: BelleTemple Glasses blend_vb',)),              (add_section_if_missing, ('455bcfc7', 'BelleTemple.Glasses.IB', 'match_priority = 0\n'))],

# Orange Green Badge VBs
'6c62e9d0': [(log, ('2.8: BelleTemple Orange Green Badge draw_vb',)),   (add_section_if_missing, ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n'))],
'e837ab1b': [(log, ('2.8: BelleTemple Orange Green Badge position_vb',)),(add_section_if_missing, ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n'))],
'632b2ed3': [(log, ('2.8: BelleTemple Orange Green Badge texcoord_vb',)),(add_section_if_missing, ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n'))],
'66797141': [(log, ('2.8: BelleTemple Orange Green Badge blend_vb',)),   (add_section_if_missing, ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n'))],

# === Headwear VBs (Reactivated for v3.0) ===
'2f828e6a': [(log, ('3.0: BelleTemple Headwear draw_vb',)),                 (add_section_if_missing, ('20d3a340', 'BelleTemple.Headwear.IB', 'match_priority = 0\n'))],
'4dec8913': [(log, ('3.0: BelleTemple Headwear position_vb',)),             (add_section_if_missing, ('20d3a340', 'BelleTemple.Headwear.IB', 'match_priority = 0\n'))],
'cdd7fc8a': [(log, ('3.0: BelleTemple Headwear texcoord_vb',)),             (add_section_if_missing, ('20d3a340', 'BelleTemple.Headwear.IB', 'match_priority = 0\n'))],

# === Body Updates ===
'01b0c8b6': [(log, ('2.8: Updating BelleTemple Body blend_vb to f3dedb50',)), (update_hash, ('f3dedb50',))],
'862dc27a': [(log, ('2.8: Updating BelleTemple Body texcoord_vb to d761e076',)), (update_hash, ('d761e076',))],
'0b3c5e7c': [(log, ('2.8: Updating BelleTemple Body position_vb to 8a4e97cd',)), (update_hash, ('8a4e97cd',))],
'02c9dc4b': [(log, ('2.8: Updating BelleTemple Body draw_vb to 19e5f486',)), (update_hash, ('19e5f486',))],
'860e1558': [(log, ('2.8: Updating BelleTemple Body IB to d509bdd4',)), (update_hash, ('d509bdd4',))],

# === Neck Updates ===
'20d3a340': [(log, ('3.0: BelleTemple Headwear IB Hash',)),                 (add_ib_check_if_missing,)],

# === Broken References Fix (v2.8) ===
'f425bd04': [(log, ('2.8: Belle Body Texcoord Hash [Legacy] 2.0',)),     (update_hash, ('91fbd2fa',))],
'84529dab': [(log, ('2.8: Belle BodyA Diffuse 2048p Hash [Legacy] Old',)), (update_hash, ('da2bfe2f',))],
'ef76b675': [(log, ('2.8: Belle BodyA Diffuse 1024p Hash [Legacy] Old',)), (update_hash, ('0a2e0f42',))],
'db7add33': [(log, ('2.8 -> 3.0: BelleTemple Neck blend_vb Hash [Legacy]',)), (update_hash, ('3bd79a0b',))],

# === 3.0 Database Updates (Strict Sync) ===
# Hair
'8f7ae834': [(log, ('3.0: BelleTemple Hair blend_vb',)),                 (add_section_if_missing, ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n'))],

# Headwear
'f18dd23f': [(log, ('3.0: BelleTemple Headwear blend_vb',)),             (add_section_if_missing, ('20d3a340', 'BelleTemple.Headwear.IB', 'match_priority = 0\n'))],

# Neck
'3f594476': [(log, ('3.0: BelleTemple Neck draw_vb',)),                  (add_section_if_missing, ('d0627e1f', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],
'e2ee9309': [(log, ('3.0: BelleTemple Neck position_vb',)),              (add_section_if_missing, ('d0627e1f', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],
'2f7f6398': [(log, ('3.0: BelleTemple Neck texcoord_vb',)),              (add_section_if_missing, ('d0627e1f', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],
'0a11b1d7': [(log, ('3.0: BelleTemple Neck blend_vb',)),                 (add_section_if_missing, ('d0627e1f', 'BelleTemple.Neck.IB', 'match_priority = 0\n'))],

# Torso / Body
'4d74d5e9': [(log, ('3.0: BelleTemple Body blend_vb',)),                 (add_section_if_missing, ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n'))],

# Leg / Legs
'922a7db6': [(log, ('3.0: BelleTemple Legs blend_vb',)),                 (add_section_if_missing, ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n'))],

# Face
'359e4502': [(log, ('3.0: BelleTemple Face blend_vb',)),                 (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],
'd3000b22': [(log, ('3.0: BelleTemple Face texcoord_vb',)),              (add_section_if_missing, ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'75ec3614': [
        (log,                           ('2.8: BelleTemple Face Diffuse 2048p Hash (Shared)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n')),
    ],
'77eef7e8': [
        (log,                           ('2.8: BelleTemple Face Diffuse Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleTemple.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'08f04d95': [
        (log,                           ('2.8: BelleTemple Hair Diffuse Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'1ce58567': [
        (log,                           ('2.8: BelleTemple HairA Diffuse Hash (Old)',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'f44f330b': [
        (log,                           ('2.8: BelleTemple Hair LightMap Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log,                           ('2.8: BelleTemple HairA LightMap Hash (Old)',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'7542ef4b': [
        (log,                           ('2.8: BelleTemple Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log,                           ('2.8: BelleTemple HairA MaterialMap Hash (Old)',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body/Neck/Legs Shared Textures ===
'fdf0b49e': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs Diffuse Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
    ],
'da2bfe2f': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0a2e0f42', 'BelleTemple.BodyNeckLegs.Diffuse.1024')),
    ],
'0a2e0f42': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da2bfe2f', 'BelleTemple.BodyNeckLegs.Diffuse.2048')),
    ],
'93d94f22': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs LightMap Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
    ],
'74f2fae3': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs LightMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f8e4e93a', 'BelleTemple.BodyNeckLegs.LightMap.1024')),
    ],
'f8e4e93a': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs LightMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('74f2fae3', 'BelleTemple.BodyNeckLegs.LightMap.2048')),
    ],
'b95c08fb': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
    ],
'657402d0': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('93c5f5ff', 'BelleTemple.BodyNeckLegs.MaterialMap.1024')),
    ],
'93c5f5ff': [
        (log,                           ('2.8: BelleTemple Body/Neck/Legs MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('657402d0', 'BelleTemple.BodyNeckLegs.MaterialMap.2048')),
    ],

# === HeadAcc Textures ===
'5e12872e': [
        (log,                           ('2.8: BelleTemple HeadAcc/BackAcc Diffuse Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],
'714e278c': [
        (log,                           ('2.8: BelleTemple HeadAcc/BackAcc NormalMap Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],
'54bd71d8': [
        (log,                           ('2.8: BelleTemple HeadAcc/BackAcc LightMap Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],
'd7de8ddf': [
        (log,                           ('2.8: BelleTemple HeadAcc/BackAcc MaterialMap Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleTemple.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleTemple.BackAcc.IB', 'match_priority = 0\n')),
    ],

# === TorsoAcc Textures ===
'5a8f8d57': [
        (log,                           ('2.8: BelleTemple TorsoAcc Diffuse Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'a7e0cba0': [
        (log,                           ('2.8: BelleTemple TorsoAcc LightMap Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'07e9e8f5': [
        (log,                           ('2.8: BelleTemple TorsoAcc MaterialMap Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleTemple.TorsoAcc.IB', 'match_priority = 0\n')),
    ],

# === Panda Headgear Textures (v2.8 Target) ===
'a2f096fc': [
        (log,                           ('2.8: BelleTemple Panda Headgear Diffuse Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n')),
    ],
'78c2d1dd': [
        (log,                           ('2.8: BelleTemple Panda Headgear LightMap Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n')),
    ],
'2a7548a9': [
        (log,                           ('2.8: BelleTemple Panda Headgear MaterialMap Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'BelleTemple.PandaHeadgear.IB', 'match_priority = 0\n')),
    ],

# === Earrings2 / CatEar Textures (v2.8 Target) ===
'ed1a5b7f': [
        (log,                           ('2.8: BelleTemple Earrings2 / CatEar Diffuse Hash',)),
        (add_section_if_missing,        ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n')),
    ],
'f5dc4198': [
        (log,                           ('2.8: BelleTemple Earrings2 / CatEar LightMap Hash',)),
        (add_section_if_missing,        ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n')),
    ],
'5346205a': [
        (log,                           ('2.8: BelleTemple Earrings2 / CatEar MaterialMap Hash',)),
        (add_section_if_missing,        ('b28a7685', 'BelleTemple.CatEar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6e890a7', 'BelleTemple.Earrings2.IB', 'match_priority = 0\n')),
    ],

# === Orange Green Ribbon / Badge Textures (v2.8 Target) ===
'96ad58d4': [
        (log,                           ('2.8: BelleTemple Orange Green Ribbon / Badge Diffuse Hash',)),
        (add_section_if_missing,        ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n')),
    ],
'8839d1fc': [
        (log,                           ('2.8: BelleTemple Orange Green Ribbon / Badge LightMap Hash',)),
        (add_section_if_missing,        ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n')),
    ],
'cd075caa': [
        (log,                           ('2.8: BelleTemple Orange Green Ribbon / Badge MaterialMap Hash',)),
        (add_section_if_missing,        ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4dcc384f', 'BelleTemple.OrangeGreenBadge.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8 -> 3.0: BelleTemple Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleTemple.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62ed56cc', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleTemple.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleTemple.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2ac09c8f', 'BelleTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d0627e1f', 'BelleTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('20d3a340', 'BelleTemple.Headwear.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: BelleTemple Shared NormalMap Hash [Legacy]',)),
        (update_hash,                   ('798adba3',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleTemple',
    'game_versions': ['2.8', '3.0'],
}