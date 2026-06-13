"""
YeShunguang Character Hash Commands
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
    Returns YeShunguang's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.8: YeShunguang Ears IB Hash',)),         (add_ib_check_if_missing,)],
'3b1b73fe': [(log, ('2.8: YeShunguang Strip IB Hash',)),        (add_ib_check_if_missing,)],
'4a178546': [(log, ('2.8: YeShunguang Legs IB Hash',)),         (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.8: YeShunguang Tail IB Hash',)),         (add_ib_check_if_missing,)],
'8c8de427': [(log, ('2.8: YeShunguang Clips IB Hash',)),        (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.8: YeShunguang Hair IB Hash',)),         (add_ib_check_if_missing,)],
'ae840e72': [(log, ('2.8: YeShunguang Antenna IB Hash',)),      (add_ib_check_if_missing,)],
'c209c22b': [(log, ('2.8: YeShunguang Torso IB Hash',)),        (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.8: YeShunguang Face IB Hash',)),         (add_ib_check_if_missing,)],
'f9ce7b07': [(log, ('2.8: YeShunguang ArmTassels IB Hash',)),   (add_ib_check_if_missing,)],
'0534b536': [(log, ('2.8: YeShunguang BackTassel IB Hash',)),   (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.8: YeShunguang BraidStrips IB Hash',)),  (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.8: YeShunguang Bow IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.8: YeShunguang Brows IB Hash',)),        (add_ib_check_if_missing,)],
'bdf6d0eb': [(log, ('2.8: YeShunguang HairShadow IB Hash',)),   (add_ib_check_if_missing,)],
'd15c8cd9': [(log, ('2.8: YeShunguang SwordBox IB Hash',)),     (add_ib_check_if_missing,)],
'5d842a9d': [(log, ('2.8: YeShunguang SwordBoxBall IB Hash',)), (add_ib_check_if_missing,)],

# === VB Hashes (v2.8 Target) ===
# Hair
'bd9b6102': [(log, ('2.8: YeShunguang Hair draw_vb',)),                 (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],
'f84ce9bf': [(log, ('2.8: YeShunguang Hair position_vb',)),             (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],
'afe311e8': [(log, ('2.8: YeShunguang Hair texcoord_vb',)),             (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],
'e841684d': [(log, ('2.8: YeShunguang Hair blend_vb',)),                (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'9e743bd7': [(log, ('2.8: YeShunguang HairShadow draw_vb',)),           (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n'))],
'520b7f22': [(log, ('2.8: YeShunguang HairShadow position_vb',)),       (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n'))],
'af0e2b6e': [(log, ('2.8: YeShunguang HairShadow texcoord_vb',)),       (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n'))],
'1e57173e': [(log, ('2.8: YeShunguang HairShadow blend_vb',)),          (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n'))],

# FrontHair
'01d5a625': [(log, ('2.8: YeShunguang FrontHair draw_vb',)),            (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],
'bba40575': [(log, ('2.8: YeShunguang FrontHair position_vb',)),        (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],
'bea60077': [(log, ('2.8: YeShunguang FrontHair texcoord_vb',)),        (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],
'4ca25eef': [(log, ('2.8: YeShunguang FrontHair blend_vb',)),           (add_section_if_missing, ('999bff94', 'YeShunguang.Hair.IB', 'match_priority = 0\n'))],

# Braid
'e05bf3a8': [(log, ('2.8: YeShunguang Braid draw_vb',)),                (add_section_if_missing, ('38b3bd13', 'YeShunguang.BraidStrips.IB', 'match_priority = 0\n'))],
'b871ef41': [(log, ('2.8: YeShunguang Braid position_vb',)),            (add_section_if_missing, ('38b3bd13', 'YeShunguang.BraidStrips.IB', 'match_priority = 0\n'))],
'd7d41552': [(log, ('2.8: YeShunguang Braid texcoord_vb',)),            (add_section_if_missing, ('38b3bd13', 'YeShunguang.BraidStrips.IB', 'match_priority = 0\n'))],
'06e29dd2': [(log, ('2.8: YeShunguang Braid blend_vb',)),               (add_section_if_missing, ('38b3bd13', 'YeShunguang.BraidStrips.IB', 'match_priority = 0\n'))],

# Body / Torso
'f201bd10': [(log, ('2.8: YeShunguang Torso draw_vb',)),                (add_section_if_missing, ('c209c22b', 'YeShunguang.Torso.IB', 'match_priority = 0\n'))],
'3239124c': [(log, ('2.8: YeShunguang Torso position_vb',)),            (add_section_if_missing, ('c209c22b', 'YeShunguang.Torso.IB', 'match_priority = 0\n'))],
'dbb027eb': [(log, ('2.8: YeShunguang Torso texcoord_vb',)),            (add_section_if_missing, ('c209c22b', 'YeShunguang.Torso.IB', 'match_priority = 0\n'))],
'79c7949c': [(log, ('2.8: YeShunguang Torso blend_vb',)),               (add_section_if_missing, ('c209c22b', 'YeShunguang.Torso.IB', 'match_priority = 0\n'))],

# Legs
'25033e92': [(log, ('2.8: YeShunguang Legs draw_vb',)),                 (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n'))],
'514dc7f3': [(log, ('2.8: YeShunguang Legs position_vb',)),             (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n'))],
'5d7f073e': [(log, ('2.8: YeShunguang Legs texcoord_vb',)),             (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n'))],
'fb37e9f8': [(log, ('2.8: YeShunguang Legs blend_vb',)),                (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n'))],

# Tail
'3fe83226': [(log, ('2.8: YeShunguang Tail draw_vb',)),                 (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n'))],
'9a2dfc61': [(log, ('2.8: YeShunguang Tail position_vb',)),             (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n'))],
'cb4b7cc7': [(log, ('2.8: YeShunguang Tail texcoord_vb',)),             (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n'))],
'690ba2b1': [(log, ('2.8: YeShunguang Tail blend_vb',)),                (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n'))],

# Headwear Flower
'3a1f0236': [(log, ('2.8: YeShunguang HeadwearFlower draw_vb',)),       (add_section_if_missing, ('8c8de427', 'YeShunguang.Clips.IB', 'match_priority = 0\n'))],
'd89bbbfa': [(log, ('2.8: YeShunguang HeadwearFlower position_vb',)),   (add_section_if_missing, ('8c8de427', 'YeShunguang.Clips.IB', 'match_priority = 0\n'))],
'a4a4ad17': [(log, ('2.8: YeShunguang HeadwearFlower texcoord_vb',)),   (add_section_if_missing, ('8c8de427', 'YeShunguang.Clips.IB', 'match_priority = 0\n'))],
'd60923e0': [(log, ('2.8: YeShunguang HeadwearFlower blend_vb',)),      (add_section_if_missing, ('8c8de427', 'YeShunguang.Clips.IB', 'match_priority = 0\n'))],

# Headwear LongRibbon
'7ccb6725': [(log, ('2.8: YeShunguang HeadwearLongRibbon draw_vb',)),   (add_section_if_missing, ('9258d5f8', 'YeShunguang.Bow.IB', 'match_priority = 0\n'))],
'682c1e3c': [(log, ('2.8: YeShunguang HeadwearLongRibbon position_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguang.Bow.IB', 'match_priority = 0\n'))],
'1e3923d1': [(log, ('2.8: YeShunguang HeadwearLongRibbon texcoord_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguang.Bow.IB', 'match_priority = 0\n'))],
'093ff56e': [(log, ('2.8: YeShunguang HeadwearLongRibbon blend_vb',)),   (add_section_if_missing, ('9258d5f8', 'YeShunguang.Bow.IB', 'match_priority = 0\n'))],

# Headwear ShortRibbon
'a6f3e58f': [(log, ('2.8: YeShunguang HeadwearShortRibbon draw_vb',)),   (add_section_if_missing, ('ae840e72', 'YeShunguang.Antenna.IB', 'match_priority = 0\n'))],
'47e62e43': [(log, ('2.8: YeShunguang HeadwearShortRibbon position_vb',)),(add_section_if_missing, ('ae840e72', 'YeShunguang.Antenna.IB', 'match_priority = 0\n'))],
'504a82ea': [(log, ('2.8: YeShunguang HeadwearShortRibbon texcoord_vb',)),(add_section_if_missing, ('ae840e72', 'YeShunguang.Antenna.IB', 'match_priority = 0\n'))],
'852eedf5': [(log, ('2.8: YeShunguang HeadwearShortRibbon blend_vb',)),   (add_section_if_missing, ('ae840e72', 'YeShunguang.Antenna.IB', 'match_priority = 0\n'))],

# ArmsRibbons
'19c6b04a': [(log, ('2.8: YeShunguang ArmsRibbons draw_vb',)),          (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmTassels.IB', 'match_priority = 0\n'))],
'0a74e427': [(log, ('2.8: YeShunguang ArmsRibbons position_vb',)),      (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmTassels.IB', 'match_priority = 0\n'))],
'fc246482': [(log, ('2.8: YeShunguang ArmsRibbons texcoord_vb',)),      (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmTassels.IB', 'match_priority = 0\n'))],
'd7558cdf': [(log, ('2.8: YeShunguang ArmsRibbons blend_vb',)),          (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmTassels.IB', 'match_priority = 0\n'))],

# TransparentCloth
'67a50546': [(log, ('2.8: YeShunguang TransparentCloth draw_vb',)),     (add_section_if_missing, ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n'))],
'5bc3d9ca': [(log, ('2.8: YeShunguang TransparentCloth position_vb',)), (add_section_if_missing, ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n'))],
'441f1cf2': [(log, ('2.8: YeShunguang TransparentCloth texcoord_vb',)), (add_section_if_missing, ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n'))],
'ae7d7235': [(log, ('2.8: YeShunguang TransparentCloth blend_vb',)),     (add_section_if_missing, ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n'))],

# BackTassel
'a93cc204': [(log, ('2.8: YeShunguang BackTassel draw_vb',)),           (add_section_if_missing, ('0534b536', 'YeShunguang.BackTassel.IB', 'match_priority = 0\n'))],
'cad13a53': [(log, ('2.8: YeShunguang BackTassel position_vb',)),       (add_section_if_missing, ('0534b536', 'YeShunguang.BackTassel.IB', 'match_priority = 0\n'))],
'7e5fb476': [(log, ('2.8: YeShunguang BackTassel texcoord_vb',)),       (add_section_if_missing, ('0534b536', 'YeShunguang.BackTassel.IB', 'match_priority = 0\n'))],
'f9b50292': [(log, ('2.8: YeShunguang BackTassel blend_vb',)),          (add_section_if_missing, ('0534b536', 'YeShunguang.BackTassel.IB', 'match_priority = 0\n'))],

# Eyebrow
'9f0ab8cd': [(log, ('2.8: YeShunguang Eyebrow draw_vb',)),              (add_section_if_missing, ('611df76d', 'YeShunguang.Brows.IB', 'match_priority = 0\n'))],
'287c161c': [(log, ('2.8: YeShunguang Eyebrow position_vb',)),          (add_section_if_missing, ('611df76d', 'YeShunguang.Brows.IB', 'match_priority = 0\n'))],
'f5daa764': [(log, ('2.8: YeShunguang Eyebrow blend_vb',)),              (add_section_if_missing, ('611df76d', 'YeShunguang.Brows.IB', 'match_priority = 0\n'))],

# Face
'2f2f9780': [(log, ('2.8: YeShunguang Face draw_vb',)),                 (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n'))],
'153d04c7': [(log, ('2.8: YeShunguang Face position_vb',)),             (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n'))],
'a1353cc8': [(log, ('2.8: YeShunguang Face texcoord_vb',)),             (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n'))],
'fa261a46': [(log, ('2.8: YeShunguang Face blend_vb',)),                (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n'))],

# === SwordBox Components (v2.8 Target) ===
'd15c8cd9': [(log, ('2.8: YeShunguang SwordBox IB Hash',)),              (add_ib_check_if_missing,)],
'5d842a9d': [(log, ('2.8: YeShunguang SwordBoxBall IB Hash',)),          (add_ib_check_if_missing,)],

'd0bc0522': [(log, ('2.8: YeShunguang SwordBox draw_vb',)),             (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n'))],
'b7b9a03a': [(log, ('2.8: YeShunguang SwordBox position_vb',)),         (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n'))],
'5b63465a': [(log, ('2.8: YeShunguang SwordBox texcoord_vb',)),         (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n'))],
'aff24453': [(log, ('2.8: YeShunguang SwordBox blend_vb',)),            (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n'))],

'0da4c71b': [(log, ('2.8: YeShunguang SwordBoxBall draw_vb',)),         (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBoxBall.IB', 'match_priority = 0\n'))],
'eaf14596': [(log, ('2.8: YeShunguang SwordBoxBall position_vb',)),     (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBoxBall.IB', 'match_priority = 0\n'))],
'eaa601b5': [(log, ('2.8: YeShunguang SwordBoxBall texcoord_vb',)),     (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBoxBall.IB', 'match_priority = 0\n'))],
'c1713762': [(log, ('2.8: YeShunguang SwordBoxBall blend_vb',)),        (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBoxBall.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'd1ffd339': [(log, ('2.5: YeShunguang TexCoord VB Hash [Legacy]',)),    (update_hash, ('dbb027eb',))],
'c7f8046f': [(log, ('2.0 -> 2.8: YeShunguang SwordBox Diffuse [Legacy]',)), (update_hash, ('f65635ed',))],
'4ba72780': [(log, ('2.0 -> 2.8: YeShunguang SwordBox LightMap [Legacy]',)), (update_hash, ('426d4871',))],
'745fb007': [(log, ('2.0 -> 2.8: YeShunguang SwordBox MaterialMap [Legacy]',)), (update_hash, ('ae41d045',))],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.8: YeShunguang Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('01ef4403', '3b1b73fe', '4a178546', '869976a3', '8c8de427', '999bff94', 'ae840e72', 'c209c22b', 'f9ce7b07', '0534b536', '38b3bd13', '9258d5f8', 'd15c8cd9', '5d842a9d'), 'YeShunguang.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'6ed0c951': [
        (log,                           ('2.8: YeShunguang FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguang.Face.IB', 'match_priority = 0\n')),
    ],

# === Ears, Clips, Hair, Antenna Textures (Shared Set 1) ===
'79f6acd7': [
        (log,                           ('2.8: YeShunguang EarsA, ClipsA, HairA, AntennaA Diffuse Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
    ],
'88269532': [
        (log,                           ('2.8: YeShunguang EarsA, ClipsA, HairA, AntennaA LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
    ],
'825fbf26': [
        (log,                           ('2.8: YeShunguang EarsA, ClipsA, HairA, AntennaA MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
    ],

# === Strip, Torso, ArmTassels Textures (Shared Set 2) ===
'5bd7d31b': [
        (log,                           ('2.8: YeShunguang StripA, TorsoA, ArmTasselsA Diffuse Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
    ],
'369a2106': [
        (log,                           ('2.8: YeShunguang StripA LightMap Hash',)),
        (add_section_if_missing,        ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n')),
    ],
'72c1cf72': [
        (log,                           ('2.8: YeShunguang TorsoA, ArmTasselsA LightMap Hash',)),
        (add_section_if_missing,        (('c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoArmSet.IB', 'match_priority = 0\n')),
    ],
'a5872c6e': [
        (log,                           ('2.8: YeShunguang StripA, TorsoA, ArmTasselsA MaterialMap Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
    ],

# === Legs, Tail Textures (Shared Set 3) ===
'727d3454': [
        (log,                           ('2.8: YeShunguang LegsA, TailA Diffuse Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
    ],
'4eb5aae2': [
        (log,                           ('2.8: YeShunguang LegsA, TailA LightMap Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
    ],
'7f5f0193': [
        (log,                           ('2.8: YeShunguang LegsA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === BackTassel, BraidStrips, Bow Textures (Shared Set 4) ===
'804099eb': [
        (log,                           ('2.8: YeShunguang BackTasselA, BraidStripsA, BowA Diffuse Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'5ca93726': [
        (log,                           ('2.8: YeShunguang BackTasselA, BraidStripsA, BowA LightMap Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'1ba6bebf': [
        (log,                           ('2.8: YeShunguang BackTasselA, BraidStripsA, BowA MaterialMap Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],

# === SwordBox Textures (v2.8 Target) ===
'f65635ed': [
        (log,                           ('2.8: YeShunguang SwordBox Diffuse Hash',)),
        (add_section_if_missing,        ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'426d4871': [
        (log,                           ('2.8: YeShunguang SwordBox LightMap Hash',)),
        (add_section_if_missing,        ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'ae41d045': [
        (log,                           ('2.8: YeShunguang SwordBox MaterialMap Hash',)),
        (add_section_if_missing,        ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguang',
    'game_versions': ['2.8'],
}