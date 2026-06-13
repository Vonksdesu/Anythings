"""
YeShunguangUlt Character Hash Commands
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
    Returns YeShunguangUlt's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.8: YeShunguangUlt Ears IB Hash',)),         (add_ib_check_if_missing,)],
'4df52aae': [(log, ('2.8: YeShunguangUlt Legs IB Hash',)),         (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.8: YeShunguangUlt Brows IB Hash',)),        (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.8: YeShunguangUlt Tail IB Hash',)),         (add_ib_check_if_missing,)],
'8e7f72d5': [(log, ('2.8: YeShunguangUlt Torso IB Hash',)),        (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.8: YeShunguangUlt HairTassels IB Hash',)),  (add_ib_check_if_missing,)],
'bafd232d': [(log, ('2.8: YeShunguangUlt Dress IB Hash',)),        (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.8: YeShunguangUlt Face IB Hash',)),         (add_ib_check_if_missing,)],
'f383537b': [(log, ('2.8: YeShunguangUlt Bow IB Hash',)),          (add_ib_check_if_missing,)],
'85d52cb7': [(log, ('2.8: YeShunguangUlt RibbonFlower IB Hash',)), (add_ib_check_if_missing,)],
'be28e18b': [(log, ('2.8: YeShunguangUlt Hair IB Hash',)),         (add_ib_check_if_missing,)],
'a9c76fcf': [(log, ('2.8: YeShunguangUlt HairShadow IB Hash',)),   (add_ib_check_if_missing,)],
'2d72a119': [(log, ('2.8: YeShunguangUlt ArmsRibbons IB Hash',)),  (add_ib_check_if_missing,)],
'dd46b065': [(log, ('2.8: YeShunguangUlt Sword IB Hash',)),         (add_ib_check_if_missing,)],

# === VB Hashes (v2.8 Target) ===
# Hair Shadow
'53b4c9f3': [(log, ('2.8: YeShunguangUlt HairShadow draw_vb',)),         (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n'))],
'ac4f1cc8': [(log, ('2.8: YeShunguangUlt HairShadow position_vb',)),     (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n'))],
'0818885d': [(log, ('2.8: YeShunguangUlt HairShadow texcoord_vb',)),     (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n'))],
'4654a675': [(log, ('2.8: YeShunguangUlt HairShadow blend_vb',)),        (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n'))],

# FrontHair
'5234bbcb': [(log, ('2.8: YeShunguangUlt FrontHair draw_vb',)),         (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n'))],
'2f030baf': [(log, ('2.8: YeShunguangUlt FrontHair position_vb',)),     (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n'))],
'13343914': [(log, ('2.8: YeShunguangUlt FrontHair texcoord_vb',)),     (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n'))],
'0041e5e3': [(log, ('2.8: YeShunguangUlt FrontHair blend_vb',)),        (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n'))],

# ArmsRibbons
'ebdbb8db': [(log, ('2.8: YeShunguangUlt ArmsRibbons draw_vb',)),        (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n'))],
'4c1e777e': [(log, ('2.8: YeShunguangUlt ArmsRibbons position_vb',)),    (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n'))],
'49a95c22': [(log, ('2.8: YeShunguangUlt ArmsRibbons texcoord_vb',)),    (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n'))],
'649a0ed6': [(log, ('2.8: YeShunguangUlt ArmsRibbons blend_vb',)),       (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n'))],

# Braid
'e05bf3a8': [(log, ('2.8: YeShunguangUlt Braid draw_vb',)),             (add_section_if_missing, ('38b3bd13', 'YeShunguangUlt.BraidRibbons.IB', 'match_priority = 0\n'))],
'b871ef41': [(log, ('2.8: YeShunguangUlt Braid position_vb',)),         (add_section_if_missing, ('38b3bd13', 'YeShunguangUlt.BraidRibbons.IB', 'match_priority = 0\n'))],
'd7d41552': [(log, ('2.8: YeShunguangUlt Braid texcoord_vb',)),         (add_section_if_missing, ('38b3bd13', 'YeShunguangUlt.BraidRibbons.IB', 'match_priority = 0\n'))],
'06e29dd2': [(log, ('2.8: YeShunguangUlt Braid blend_vb',)),            (add_section_if_missing, ('38b3bd13', 'YeShunguangUlt.BraidRibbons.IB', 'match_priority = 0\n'))],

# Body
'f201bd10': [(log, ('2.8: YeShunguangUlt Body draw_vb',)),               (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n'))],
'3239124c': [(log, ('2.8: YeShunguangUlt Body position_vb',)),           (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n'))],
'dbb027eb': [(log, ('2.8: YeShunguangUlt Body texcoord_vb',)),           (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n'))],
'79c7949c': [(log, ('2.8: YeShunguangUlt Body blend_vb',)),              (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n'))],

# Legs
'25033e92': [(log, ('2.8: YeShunguangUlt Legs draw_vb',)),               (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n'))],
'514dc7f3': [(log, ('2.8: YeShunguangUlt Legs position_vb',)),           (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n'))],
'5d7f073e': [(log, ('2.8: YeShunguangUlt Legs texcoord_vb',)),           (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n'))],
'fb37e9f8': [(log, ('2.8: YeShunguangUlt Legs blend_vb',)),              (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n'))],

# Tail
'3fe83226': [(log, ('2.8: YeShunguangUlt Tail draw_vb',)),               (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n'))],
'9a2dfc61': [(log, ('2.8: YeShunguangUlt Tail position_vb',)),           (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n'))],
'cb4b7cc7': [(log, ('2.8: YeShunguangUlt Tail texcoord_vb',)),           (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n'))],
'690ba2b1': [(log, ('2.8: YeShunguangUlt Tail blend_vb',)),              (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n'))],

# Headwear flower/Clips
'3a1f0236': [(log, ('2.8: YeShunguangUlt HeadwearFlower draw_vb',)),     (add_section_if_missing, ('8c8de427', 'YeShunguangUlt.Clips.IB', 'match_priority = 0\n'))],
'd89bbbfa': [(log, ('2.8: YeShunguangUlt HeadwearFlower position_vb',)), (add_section_if_missing, ('8c8de427', 'YeShunguangUlt.Clips.IB', 'match_priority = 0\n'))],
'a4a4ad17': [(log, ('2.8: YeShunguangUlt HeadwearFlower texcoord_vb',)), (add_section_if_missing, ('8c8de427', 'YeShunguangUlt.Clips.IB', 'match_priority = 0\n'))],
'd60923e0': [(log, ('2.8: YeShunguangUlt HeadwearFlower blend_vb',)),    (add_section_if_missing, ('8c8de427', 'YeShunguangUlt.Clips.IB', 'match_priority = 0\n'))],

# Headwear LongRibbon/Bow
'7ccb6725': [(log, ('2.8: YeShunguangUlt HeadwearLongRibbon draw_vb',)), (add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Bow.IB', 'match_priority = 0\n'))],
'682c1e3c': [(log, ('2.8: YeShunguangUlt HeadwearLongRibbon position_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Bow.IB', 'match_priority = 0\n'))],
'1e3923d1': [(log, ('2.8: YeShunguangUlt HeadwearLongRibbon texcoord_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Bow.IB', 'match_priority = 0\n'))],
'093ff56e': [(log, ('2.8: YeShunguangUlt HeadwearLongRibbon blend_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Bow.IB', 'match_priority = 0\n'))],

# Headwear ShortRibbon/Antenna
'a6f3e58f': [(log, ('2.8: YeShunguangUlt HeadwearShortRibbon draw_vb',)), (add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Antenna.IB', 'match_priority = 0\n'))],
'47e62e43': [(log, ('2.8: YeShunguangUlt HeadwearShortRibbon position_vb',)),(add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Antenna.IB', 'match_priority = 0\n'))],
'504a82ea': [(log, ('2.8: YeShunguangUlt HeadwearShortRibbon texcoord_vb',)),(add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Antenna.IB', 'match_priority = 0\n'))],
'852eedf5': [(log, ('2.8: YeShunguangUlt HeadwearShortRibbon blend_vb',)),(add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Antenna.IB', 'match_priority = 0\n'))],

# BackTassel
'a93cc204': [(log, ('2.8: YeShunguangUlt BackTassel draw_vb',)),         (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackTassel.IB', 'match_priority = 0\n'))],
'cad13a53': [(log, ('2.8: YeShunguangUlt BackTassel position_vb',)),     (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackTassel.IB', 'match_priority = 0\n'))],
'7e5fb476': [(log, ('2.8: YeShunguangUlt BackTassel texcoord_vb',)),     (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackTassel.IB', 'match_priority = 0\n'))],
'f9b50292': [(log, ('2.8: YeShunguangUlt BackTassel blend_vb',)),        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackTassel.IB', 'match_priority = 0\n'))],

# Eyebrow
'9f0ab8cd': [(log, ('2.8: YeShunguangUlt Eyebrow draw_vb',)),            (add_section_if_missing, ('611df76d', 'YeShunguangUlt.Brows.IB', 'match_priority = 0\n'))],
'287c161c': [(log, ('2.8: YeShunguangUlt Eyebrow Position Hash',)),      (add_section_if_missing, ('611df76d', 'YeShunguangUlt.Brows.IB', 'match_priority = 0\n'))],
'f5daa764': [(log, ('2.8: YeShunguangUlt Eyebrow blend_vb',)),            (add_section_if_missing, ('611df76d', 'YeShunguangUlt.Brows.IB', 'match_priority = 0\n'))],

# Face
'2f2f9780': [(log, ('2.8: YeShunguangUlt Face draw_vb',)),               (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n'))],
'153d04c7': [(log, ('2.8: YeShunguangUlt Face position_vb',)),           (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n'))],
'a1353cc8': [(log, ('2.8: YeShunguangUlt Face texcoord_vb',)),           (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n'))],
'fa261a46': [(log, ('2.8: YeShunguangUlt Face blend_vb',)),              (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n'))],

# Weapon - Sword
'3a44ca69': [(log, ('2.8: YeShunguangUlt Sword draw_vb',)),              (add_section_if_missing, ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n'))],
'724d29ad': [(log, ('2.8: YeShunguangUlt Sword position_vb',)),          (add_section_if_missing, ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n'))],
'2c36b1a8': [(log, ('2.8: YeShunguangUlt Sword texcoord_vb',)),          (add_section_if_missing, ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n'))],
'2e3a5c01': [(log, ('2.8: YeShunguangUlt Sword blend_vb',)),             (add_section_if_missing, ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'c28b9829': [(log, ('2.0 -> 2.8: YeShunguangUlt Legs, Tail Diffuse Hash [Legacy]',)),      (update_hash, ('0b7c1487',))],
'5ca93726': [(log, ('2.0 -> 2.8: YeShunguangUlt Bow LightMap Hash [Legacy]',)),             (update_hash, ('0d70f7cd',))],
'4700e4bd': [(log, ('2.0 -> 2.8: YeShunguangUlt Legs, Tail MaterialMap Hash [Legacy]',)),  (update_hash, ('263992f5',))],
'87d4dd37': [(log, ('2.0 -> 2.8: YeShunguangUlt Legs, Tail LightMap Hash [Legacy]',)),     (update_hash, ('afbdd8a1',))],
'1ba6bebf': [(log, ('2.0 -> 2.8: YeShunguangUlt TasselSet MaterialMap Hash [Legacy]',)),   (update_hash, ('7bf83964',))],
'b4a2abbc': [(log, ('2.0 -> 2.8: YeShunguangUlt Strip MaterialMap Hash [Legacy]',)),       (update_hash, ('dd1adbe8',))],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.8: YeShunguangUlt Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('01ef4403', '4df52aae', '869976a3', '8e7f72d5', '9258d5f8', 'bafd232d', 'f383537b', '85d52cb7', 'be28e18b', 'a9c76fcf', '2d72a119', '3b1b73fe', '0534b536'), 'YeShunguangUlt.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'6ed0c951': [
        (log,                           ('2.8: YeShunguangUlt FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
    ],

# === Brows Textures ===
'ac8c7ca2': [
        (log,                           ('2.8: YeShunguangUlt BrowsA Diffuse Hash',)),
        (add_section_if_missing,        ('611df76d', 'YeShunguangUlt.Brows.IB', 'match_priority = 0\n')),
    ],

# === Ears Textures ===
'e8a8ac0b': [
        (log,                           ('2.8: YeShunguangUlt EarsA Diffuse Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],
'652e15a3': [
        (log,                           ('2.8: YeShunguangUlt EarsB Diffuse Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],
'9f7defbc': [
        (log,                           ('2.8: YeShunguangUlt Ears LightMap Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],
'c74f9710': [
        (log,                           ('2.8: YeShunguangUlt Ears MaterialMap Hash',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangUlt.Ears.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'9b7da949': [
        (log,                           ('2.8: YeShunguangUlt Hair DiffuseA Hash',)),
        (add_section_if_missing,        (('01ef4403', 'be28e18b', 'ae840e72'), 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'22ad0434': [
        (log,                           ('2.8: YeShunguangUlt Hair DiffuseB Hash',)),
        (add_section_if_missing,        (('01ef4403', 'be28e18b', 'ae840e72'), 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'd8ce86a1': [
        (log,                           ('2.8: YeShunguangUlt Hair LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', 'be28e18b', 'ae840e72'), 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'd864cc64': [
        (log,                           ('2.8: YeShunguangUlt Hair MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', 'be28e18b', 'ae840e72'), 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'34097193': [
        (log,                           ('2.8: YeShunguangUlt Body Diffuse Hash',)),
        (add_section_if_missing,        ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n')),
    ],
'0e921a23': [
        (log,                           ('2.8: YeShunguangUlt Body MaterialMap Hash',)),
        (add_section_if_missing,        ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n')),
    ],

# === Legs, Tail Textures (v2.8 Target) ===
'0b7c1487': [
        (log,                           ('2.8: YeShunguangUlt Legs, Tail Diffuse Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangUlt.LegsTail.IB', 'match_priority = 0\n')),
    ],
'afbdd8a1': [
        (log,                           ('2.8: YeShunguangUlt Legs, Tail LightMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangUlt.LegsTail.IB', 'match_priority = 0\n')),
    ],
'263992f5': [
        (log,                           ('2.8: YeShunguangUlt Legs, Tail MaterialMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangUlt.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === Tassels / LongRibbon Textures (v2.8 Target) ===
'0d70f7cd': [
        (log,                           ('2.8: YeShunguangUlt HeadwearLongRibbon LightMap Hash',)),
        (add_section_if_missing,        ('9258d5f8', 'YeShunguangUlt.Bow.IB', 'match_priority = 0\n')),
    ],
'7bf83964': [
        (log,                           ('2.8: YeShunguangUlt HeadwearLongRibbon MaterialMap Hash',)),
        (add_section_if_missing,        ('9258d5f8', 'YeShunguangUlt.Bow.IB', 'match_priority = 0\n')),
    ],
'fc76ef5b': [
        (log,                           ('2.8: YeShunguangUlt Tassels LightMap Hash [Legacy]',)),
        (add_section_if_missing,        (('9258d5f8', '0534b536'), 'YeShunguangUlt.HairTasselsRibbon.IB', 'match_priority = 0\n')),
    ],
'0afd6ddf': [
        (log,                           ('2.8: YeShunguangUlt Tassels MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        (('9258d5f8', '0534b536'), 'YeShunguangUlt.HairTasselsRibbon.IB', 'match_priority = 0\n')),
    ],

# === Body & TransparentCloth Textures (v2.8 Target) ===
'43ca3d50': [
        (log,                           ('2.8: YeShunguangUlt Body Diffuse Hash',)),
        (add_section_if_missing,        ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n')),
    ],
'e41b12be': [
        (log,                           ('2.8: YeShunguangUlt Body MaterialMap / TransparentCloth Diffuse Hash',)),
        (add_section_if_missing,        ('c209c22b', 'YeShunguangUlt.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3b1b73fe', 'YeShunguangUlt.Strip.IB', 'match_priority = 0\n')),
    ],
'dd1adbe8': [
        (log,                           ('2.8: YeShunguangUlt TransparentCloth MaterialMap Hash',)),
        (add_section_if_missing,        ('3b1b73fe', 'YeShunguangUlt.Strip.IB', 'match_priority = 0\n')),
    ],

# === Sword Textures (v2.8 Target) ===
'512d9f71': [
        (log,                           ('2.8: YeShunguangUlt Sword Diffuse Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'd87a1e13': [
        (log,                           ('2.8: YeShunguangUlt Sword LightMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'ce96ea2f': [
        (log,                           ('2.8: YeShunguangUlt Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'8842671b': [
        (log,                           ('2.8: YeShunguangUlt Sword NormalMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangUlt',
    'game_versions': ['2.8'],
}