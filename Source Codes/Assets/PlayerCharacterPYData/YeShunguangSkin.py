"""
YeShunguangSkin Character Hash Commands
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
    Returns YeShunguangSkin's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.8: YeShunguangSkin Ears IB Hash',)),          (add_ib_check_if_missing,)],
'4df52aae': [(log, ('2.8: YeShunguangSkin Legs IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.8: YeShunguangSkin Brows IB Hash',)),         (add_ib_check_if_missing,)],
'6dc6c880': [(log, ('2.8: YeShunguangSkin HairClips IB Hash',)),     (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.8: YeShunguangSkin Tail IB Hash',)),          (add_ib_check_if_missing,)],
'8e7f72d5': [(log, ('2.8: YeShunguangSkin Torso IB Hash',)),         (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.8: YeShunguangSkin HairTassels IB Hash',)),   (add_ib_check_if_missing,)],
'bafd232d': [(log, ('2.8: YeShunguangSkin Dress IB Hash',)),         (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.8: YeShunguangSkin Face IB Hash',)),          (add_ib_check_if_missing,)],
'f383537b': [(log, ('2.8: YeShunguangSkin HairBow IB Hash',)),       (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.8: YeShunguangSkin BraidRibbons IB Hash',)),  (add_ib_check_if_missing,)],
'85d52cb7': [(log, ('2.8: YeShunguangSkin RibbonFlower IB Hash',)),  (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.8: YeShunguangSkin Bangs IB Hash',)),         (add_ib_check_if_missing,)],
'bdf6d0eb': [(log, ('2.8: YeShunguangSkin HairShadow IB Hash',)),   (add_ib_check_if_missing,)],
'ba7164f5': [(log, ('2.8: YeShunguangSkin TransparentCloth IB Hash',)),(add_ib_check_if_missing,)],

# === VB Hashes (v2.8 Target) ===
# Hair
'bd9b6102': [(log, ('2.8: YeShunguangSkin Hair draw_vb',)),             (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],
'f84ce9bf': [(log, ('2.8: YeShunguangSkin Hair position_vb',)),         (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],
'afe311e8': [(log, ('2.8: YeShunguangSkin Hair texcoord_vb',)),         (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],
'e841684d': [(log, ('2.8: YeShunguangSkin Hair blend_vb',)),            (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],

# Hair Shadow
'9e743bd7': [(log, ('2.8: YeShunguangSkin HairShadow draw_vb',)),       (add_section_if_missing, ('bdf6d0eb', 'YeShunguangSkin.HairShadow.IB', 'match_priority = 0\n'))],
'520b7f22': [(log, ('2.8: YeShunguangSkin HairShadow position_vb',)),   (add_section_if_missing, ('bdf6d0eb', 'YeShunguangSkin.HairShadow.IB', 'match_priority = 0\n'))],
'af0e2b6e': [(log, ('2.8: YeShunguangSkin HairShadow texcoord_vb',)),   (add_section_if_missing, ('bdf6d0eb', 'YeShunguangSkin.HairShadow.IB', 'match_priority = 0\n'))],
'1e57173e': [(log, ('2.8: YeShunguangSkin HairShadow blend_vb',)),      (add_section_if_missing, ('bdf6d0eb', 'YeShunguangSkin.HairShadow.IB', 'match_priority = 0\n'))],

# FrontHair
'01d5a625': [(log, ('2.8: YeShunguangSkin FrontHair draw_vb',)),        (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],
'bba40575': [(log, ('2.8: YeShunguangSkin FrontHair position_vb',)),    (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],
'bea60077': [(log, ('2.8: YeShunguangSkin FrontHair texcoord_vb',)),    (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],
'4ca25eef': [(log, ('2.8: YeShunguangSkin FrontHair blend_vb',)),       (add_section_if_missing, ('999bff94', 'YeShunguangSkin.Bangs.IB', 'match_priority = 0\n'))],

# Braid
'e05bf3a8': [(log, ('2.8: YeShunguangSkin Braid draw_vb',)),            (add_section_if_missing, ('38b3bd13', 'YeShunguangSkin.BraidRibbons.IB', 'match_priority = 0\n'))],
'b871ef41': [(log, ('2.8: YeShunguangSkin Braid position_vb',)),        (add_section_if_missing, ('38b3bd13', 'YeShunguangSkin.BraidRibbons.IB', 'match_priority = 0\n'))],
'd7d41552': [(log, ('2.8: YeShunguangSkin Braid texcoord_vb',)),        (add_section_if_missing, ('38b3bd13', 'YeShunguangSkin.BraidRibbons.IB', 'match_priority = 0\n'))],
'06e29dd2': [(log, ('2.8: YeShunguangSkin Braid blend_vb',)),           (add_section_if_missing, ('38b3bd13', 'YeShunguangSkin.BraidRibbons.IB', 'match_priority = 0\n'))],

# Body / Torso
'506b7080': [(log, ('2.8: YeShunguangSkin Body draw_vb',)),             (add_section_if_missing, ('8e7f72d5', 'YeShunguangSkin.Torso.IB', 'match_priority = 0\n'))],
'22213b25': [(log, ('2.8: YeShunguangSkin Body position_vb',)),         (add_section_if_missing, ('8e7f72d5', 'YeShunguangSkin.Torso.IB', 'match_priority = 0\n'))],
'2a98d810': [(log, ('2.8: YeShunguangSkin Body texcoord_vb',)),         (add_section_if_missing, ('8e7f72d5', 'YeShunguangSkin.Torso.IB', 'match_priority = 0\n'))],
'b827643b': [(log, ('2.8: YeShunguangSkin Body blend_vb',)),            (add_section_if_missing, ('8e7f72d5', 'YeShunguangSkin.Torso.IB', 'match_priority = 0\n'))],

# Legs
'b117fabb': [(log, ('2.8: YeShunguangSkin Leg draw_vb',)),              (add_section_if_missing, ('4df52aae', 'YeShunguangSkin.Legs.IB', 'match_priority = 0\n'))],
'38b4c4e8': [(log, ('2.8: YeShunguangSkin Leg position_vb',)),          (add_section_if_missing, ('4df52aae', 'YeShunguangSkin.Legs.IB', 'match_priority = 0\n'))],
'ea5a39d1': [(log, ('2.8: YeShunguangSkin Leg texcoord_vb',)),          (add_section_if_missing, ('4df52aae', 'YeShunguangSkin.Legs.IB', 'match_priority = 0\n'))],
'352c95b2': [(log, ('2.8: YeShunguangSkin Leg blend_vb',)),             (add_section_if_missing, ('4df52aae', 'YeShunguangSkin.Legs.IB', 'match_priority = 0\n'))],

# Skirt
'ff96a5d2': [(log, ('2.8: YeShunguangSkin Skirt draw_vb',)),            (add_section_if_missing, ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n'))],
'43eb20a0': [(log, ('2.8: YeShunguangSkin Skirt position_vb',)),        (add_section_if_missing, ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n'))],
'1f27ab54': [(log, ('2.8: YeShunguangSkin Skirt texcoord_vb',)),        (add_section_if_missing, ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n'))],
'6468f592': [(log, ('2.8: YeShunguangSkin Skirt blend_vb',)),           (add_section_if_missing, ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n'))],

# Tail
'3fe83226': [(log, ('2.8: YeShunguangSkin Tail draw_vb',)),             (add_section_if_missing, ('869976a3', 'YeShunguangSkin.Tail.IB', 'match_priority = 0\n'))],
'9a2dfc61': [(log, ('2.8: YeShunguangSkin Tail position_vb',)),         (add_section_if_missing, ('869976a3', 'YeShunguangSkin.Tail.IB', 'match_priority = 0\n'))],
'cb4b7cc7': [(log, ('2.8: YeShunguangSkin Tail texcoord_vb',)),         (add_section_if_missing, ('869976a3', 'YeShunguangSkin.Tail.IB', 'match_priority = 0\n'))],
'690ba2b1': [(log, ('2.8: YeShunguangSkin Tail blend_vb',)),            (add_section_if_missing, ('869976a3', 'YeShunguangSkin.Tail.IB', 'match_priority = 0\n'))],

# Headwear Flower
'0e30f719': [(log, ('2.8: YeShunguangSkin HeadwearFlower draw_vb',)),   (add_section_if_missing, ('6dc6c880', 'YeShunguangSkin.HairClips.IB', 'match_priority = 0\n'))],
'7fd64a5b': [(log, ('2.8: YeShunguangSkin HeadwearFlower position_vb',)),(add_section_if_missing, ('6dc6c880', 'YeShunguangSkin.HairClips.IB', 'match_priority = 0\n'))],
'7105bdbb': [(log, ('2.8: YeShunguangSkin HeadwearFlower texcoord_vb',)),(add_section_if_missing, ('6dc6c880', 'YeShunguangSkin.HairClips.IB', 'match_priority = 0\n'))],
'16a21c01': [(log, ('2.8: YeShunguangSkin HeadwearFlower blend_vb',)),  (add_section_if_missing, ('6dc6c880', 'YeShunguangSkin.HairClips.IB', 'match_priority = 0\n'))],

# Headwear LongRibbon
'7ccb6725': [(log, ('2.8: YeShunguangSkin HeadwearLongRibbon draw_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangSkin.HairTassels.IB', 'match_priority = 0\n'))],
'682c1e3c': [(log, ('2.8: YeShunguangSkin HeadwearLongRibbon position_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangSkin.HairTassels.IB', 'match_priority = 0\n'))],
'1e3923d1': [(log, ('2.8: YeShunguangSkin HeadwearLongRibbon texcoord_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangSkin.HairTassels.IB', 'match_priority = 0\n'))],
'093ff56e': [(log, ('2.8: YeShunguangSkin HeadwearLongRibbon blend_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangSkin.HairTassels.IB', 'match_priority = 0\n'))],

# Headwear ShortRibbon
'3874c939': [(log, ('2.8: YeShunguangSkin HeadwearShortRibbon draw_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangSkin.HairBow.IB', 'match_priority = 0\n'))],
'1b410367': [(log, ('2.8: YeShunguangSkin HeadwearShortRibbon position_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangSkin.HairBow.IB', 'match_priority = 0\n'))],
'e71ea768': [(log, ('2.8: YeShunguangSkin HeadwearShortRibbon texcoord_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangSkin.HairBow.IB', 'match_priority = 0\n'))],
'ae7cced6': [(log, ('2.8: YeShunguangSkin HeadwearShortRibbon blend_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangSkin.HairBow.IB', 'match_priority = 0\n'))],

# RibbonFlower
'a203c8fa': [(log, ('2.8: YeShunguangSkin RibbonFlower draw_vb',)),      (add_section_if_missing, ('85d52cb7', 'YeShunguangSkin.RibbonFlower.IB', 'match_priority = 0\n'))],
'4c1d8708': [(log, ('2.8: YeShunguangSkin RibbonFlower position_vb',)),  (add_section_if_missing, ('85d52cb7', 'YeShunguangSkin.RibbonFlower.IB', 'match_priority = 0\n'))],
'b8e7470f': [(log, ('2.8: YeShunguangSkin RibbonFlower texcoord_vb',)),  (add_section_if_missing, ('85d52cb7', 'YeShunguangSkin.RibbonFlower.IB', 'match_priority = 0\n'))],
'917a4c3e': [(log, ('2.8: YeShunguangSkin RibbonFlower blend_vb',)),     (add_section_if_missing, ('85d52cb7', 'YeShunguangSkin.RibbonFlower.IB', 'match_priority = 0\n'))],

# TransparentCloth
'b040f517': [(log, ('2.8: YeShunguangSkin TransparentCloth draw_vb',)),  (add_section_if_missing, ('ba7164f5', 'YeShunguangSkin.TransparentCloth.IB', 'match_priority = 0\n'))],
'd98395a9': [(log, ('2.8: YeShunguangSkin TransparentCloth position_vb',)),(add_section_if_missing, ('ba7164f5', 'YeShunguangSkin.TransparentCloth.IB', 'match_priority = 0\n'))],
'0925ae65': [(log, ('2.8: YeShunguangSkin TransparentCloth texcoord_vb',)),(add_section_if_missing, ('ba7164f5', 'YeShunguangSkin.TransparentCloth.IB', 'match_priority = 0\n'))],
'651d14a2': [(log, ('2.8: YeShunguangSkin TransparentCloth blend_vb',)), (add_section_if_missing, ('ba7164f5', 'YeShunguangSkin.TransparentCloth.IB', 'match_priority = 0\n'))],

# Eyebrow
'9f0ab8cd': [(log, ('2.8: YeShunguangSkin Eyebrow draw_vb',)),          (add_section_if_missing, ('611df76d', 'YeShunguangSkin.Brows.IB', 'match_priority = 0\n'))],
'a5182b8a': [(log, ('2.8: YeShunguangSkin Eyebrow position_vb',)),      (add_section_if_missing, ('611df76d', 'YeShunguangSkin.Brows.IB', 'match_priority = 0\n'))],
'287c161c': [(log, ('2.8: YeShunguangSkin Eyebrow Position Hash',)),    (update_hash, ('a5182b8a',))],
'f5daa764': [(log, ('2.8: YeShunguangSkin Eyebrow blend_vb',)),          (add_section_if_missing, ('611df76d', 'YeShunguangSkin.Brows.IB', 'match_priority = 0\n'))],

# Face
'2f2f9780': [(log, ('2.8: YeShunguangSkin Face draw_vb',)),             (add_section_if_missing, ('c28e6303', 'YeShunguangSkin.Face.IB', 'match_priority = 0\n'))],
'153d04c7': [(log, ('2.8: YeShunguangSkin Face position_vb',)),         (add_section_if_missing, ('c28e6303', 'YeShunguangSkin.Face.IB', 'match_priority = 0\n'))],
'a1353cc8': [(log, ('2.8: YeShunguangSkin Face texcoord_vb',)),         (add_section_if_missing, ('c28e6303', 'YeShunguangSkin.Face.IB', 'match_priority = 0\n'))],
'fa261a46': [(log, ('2.8: YeShunguangSkin Face blend_vb',)),            (add_section_if_missing, ('c28e6303', 'YeShunguangSkin.Face.IB', 'match_priority = 0\n'))],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.8: YeShunguangSkin Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('01ef4403', '4df52aae', '6dc6c880', '869976a3', '8e7f72d5', '9258d5f8', 'bafd232d', 'f383537b', '38b3bd13', '85d52cb7', '999bff94'), 'YeShunguangSkin.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face and Brows Textures ===
'6ed0c951': [
        (log,                           ('2.8: YeShunguangSkin FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguangSkin.Face.IB', 'match_priority = 0\n')),
    ],

# === Ears and Bangs Textures ===
'79f6acd7': [
        (log,                           ('2.8: YeShunguangSkin EarsA, BangsA Diffuse Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangSkin.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'88269532': [
        (log,                           ('2.8: YeShunguangSkin EarsA, BangsA LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangSkin.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'825fbf26': [
        (log,                           ('2.8: YeShunguangSkin EarsA, BangsA MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangSkin.EarsBangs.IB', 'match_priority = 0\n')),
    ],

# === Legs and Tail Textures ===
'37c5aae5': [
        (log,                           ('2.8: YeShunguangSkin LegsA, TailA Diffuse Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangSkin.LegsTail.IB', 'match_priority = 0\n')),
    ],
'01e54e40': [
        (log,                           ('2.8: YeShunguangSkin LegsA, TailA LightMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangSkin.LegsTail.IB', 'match_priority = 0\n')),
    ],
'18370cad': [
        (log,                           ('2.8: YeShunguangSkin LegsA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangSkin.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === HairClips, Torso, and HairBow Textures ===
'956bcfbd': [
        (log,                           ('2.8: YeShunguangSkin HairClipsA, TorsoA, HairBowA Diffuse Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangSkin.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],
'8e815da2': [
        (log,                           ('2.8: YeShunguangSkin HairClipsA, TorsoA, HairBowA LightMap Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangSkin.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],
'2f2c27b5': [
        (log,                           ('2.8: YeShunguangSkin HairClipsA, TorsoA, HairBowA MaterialMap Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangSkin.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],

# === HairTassels, BraidRibbons, and RibbonFlower Textures ===
'8d400443': [
        (log,                           ('2.8: YeShunguangSkin HairTasselsA, BraidRibbonsA, RibbonFlowerA Diffuse Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangSkin.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'68e162a7': [
        (log,                           ('2.8: YeShunguangSkin HairTasselsA, BraidRibbonsA, RibbonFlowerA LightMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangSkin.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'fdd44e2a': [
        (log,                           ('2.8: YeShunguangSkin HairTasselsA, BraidRibbonsA, RibbonFlowerA MaterialMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangSkin.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],

# === Dress Textures ===
'f6d35967': [
        (log,                           ('2.8: YeShunguangSkin DressA Diffuse Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n')),
    ],
'405fa4b6': [
        (log,                           ('2.8: YeShunguangSkin DressA LightMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n')),
    ],
'e67e5577': [
        (log,                           ('2.8: YeShunguangSkin DressA MaterialMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangSkin.Dress.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangSkin',
    'game_versions': ['2.8'],
}