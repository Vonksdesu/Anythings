"""
Miyabi Character Hash Commands
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
    Returns Miyabi's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'4faabaac': [(log, ('2.8: Miyabi Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'981c1a1e': [(log, ('2.8: Miyabi Body IB Hash',)),                        (add_ib_check_if_missing,)],
'd8003df3': [(log, ('2.8: Miyabi Legs IB Hash',)),                        (add_ib_check_if_missing,)],
'dbd59d30': [(log, ('2.8: Miyabi Face IB Hash',)),                        (add_ib_check_if_missing,)],
'acff032e': [(log, ('2.8: Miyabi Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'02e62d7e': [(log, ('2.8: Miyabi Hairpin IB Hash',)),                     (add_ib_check_if_missing,)],
'0c26a38b': [(log, ('2.8: Miyabi Hairpin Ribbon IB Hash',)),              (add_ib_check_if_missing,)],
'0275d39f': [(log, ('2.8: Miyabi Weapon Sword IB Hash',)),                (add_ib_check_if_missing,)],
'562b2030': [(log, ('2.8: Miyabi Weapon SwordSheath IB Hash',)),          (add_ib_check_if_missing,)],
'1a82a439': [(log, ('2.8: Miyabi Weapon SwordHandle IB Hash',)),          (add_ib_check_if_missing,)],
'12739125': [(log, ('2.8: Miyabi Weapon SwordSoul IB Hash',)),            (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'5a8d28f4': [(log, ('2.8: Miyabi Hair draw_vb Hash',)),                  (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n'))],
'f9b9b064': [(log, ('2.8: Miyabi Hair position_vb Hash',)),              (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n'))],
'b6530b86': [(log, ('2.8: Miyabi Hair texcoord_vb Hash',)),              (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n'))],
'8b2eeb77': [(log, ('2.8: Miyabi Hair blend_vb Hash',)),                 (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'e8082f3c': [(log, ('2.8: Miyabi Hair Shadow draw_vb Hash',)),           (add_section_if_missing, ('acff032e', 'Miyabi.HairShadow.IB', 'match_priority = 0\n'))],
'a10b08d2': [(log, ('2.8: Miyabi Hair Shadow position_vb Hash',)),       (add_section_if_missing, ('acff032e', 'Miyabi.HairShadow.IB', 'match_priority = 0\n'))],
'70717c93': [(log, ('2.8: Miyabi Hair Shadow texcoord_vb Hash',)),       (add_section_if_missing, ('acff032e', 'Miyabi.HairShadow.IB', 'match_priority = 0\n'))],
'9c3d5e1f': [(log, ('2.8: Miyabi Hair Shadow blend_vb Hash',)),          (add_section_if_missing, ('acff032e', 'Miyabi.HairShadow.IB', 'match_priority = 0\n'))],

# Hairpin
'bbce89b9': [(log, ('2.8: Miyabi Hairpin draw_vb Hash',)),               (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n'))],
'e7041a99': [(log, ('2.8: Miyabi Hairpin position_vb Hash',)),           (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n'))],
'750d2a46': [(log, ('2.8: Miyabi Hairpin texcoord_vb Hash',)),           (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n'))],
'7ed40a2f': [(log, ('2.8: Miyabi Hairpin blend_vb Hash',)),              (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n'))],

# Hairpin Ribbon
'3421e96d': [(log, ('2.8: Miyabi Hairpin Ribbon draw_vb Hash',)),        (add_section_if_missing, ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n'))],
'be288799': [(log, ('2.8: Miyabi Hairpin Ribbon position_vb Hash',)),    (add_section_if_missing, ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n'))],
'fcc57f25': [(log, ('2.8: Miyabi Hairpin Ribbon texcoord_vb Hash',)),    (add_section_if_missing, ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n'))],
'827f5947': [(log, ('2.8: Miyabi Hairpin Ribbon blend_vb Hash',)),       (add_section_if_missing, ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n'))],

# Body
'6201dd9e': [(log, ('2.8: Miyabi Body draw_vb Hash',)),                  (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n'))],
'8ecb10b3': [(log, ('2.8: Miyabi Body position_vb Hash',)),              (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n'))],
'303fb1b6': [(log, ('2.8: Miyabi Body texcoord_vb Hash',)),              (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n'))],
'a4aeb1d5': [(log, ('2.8: Miyabi Body IB Hash [Legacy]',)),              (update_hash, ('981c1a1e',))],
'5e942526': [(log, ('2.8: Miyabi Body Blend Hash [Legacy]',)),           (update_hash, ('9a4227c8',))],
'f3569f8d': [(log, ('2.8: Miyabi Body Position Hash [Legacy]',)),        (update_hash, ('8ecb10b3',))],
'160872c0': [(log, ('2.8: Miyabi Body Texcoord Hash [Legacy]',)),        (update_hash, ('303fb1b6',))],
'9a4227c8': [(log, ('2.8: Miyabi Body blend_vb Hash',)),                 (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n'))],

# Legs
'8336ded4': [(log, ('2.8: Miyabi Legs draw_vb Hash',)),                  (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n'))],
'e71bbd08': [(log, ('2.8: Miyabi Legs position_vb Hash',)),              (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n'))],
'fb94d66c': [(log, ('2.8: Miyabi Legs texcoord_vb Hash',)),              (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n'))],
'bc586fd9': [(log, ('2.8: Miyabi Legs blend_vb Hash',)),                 (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n'))],

# Face
'0dbd45ea': [(log, ('2.8: Miyabi Face draw_vb Hash',)),                  (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n'))],
'37afd6ad': [(log, ('2.8: Miyabi Face position_vb Hash',)),              (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n'))],
'7a476f86': [(log, ('2.8: Miyabi Face texcoord_vb Hash',)),              (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n'))],
'd7781c46': [(log, ('2.8: Miyabi Face blend_vb Hash',)),                 (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n'))],

# Weapon - Sword
'9d6f441f': [(log, ('2.8: Miyabi Weapon Sword draw_vb Hash',)),          (add_section_if_missing, ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n'))],
'81a99d68': [(log, ('2.8: Miyabi Weapon Sword position_vb Hash',)),      (add_section_if_missing, ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n'))],
'aeb95d61': [(log, ('2.8: Miyabi Weapon Sword texcoord_vb Hash',)),      (add_section_if_missing, ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n'))],
'8bc72b94': [(log, ('2.8: Miyabi Weapon Sword blend_vb Hash',)),         (add_section_if_missing, ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n'))],

# Weapon - SwordSheath
'e3590e91': [(log, ('2.8: Miyabi Weapon SwordSheath draw_vb Hash',)),    (add_section_if_missing, ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n'))],
'fc93f762': [(log, ('2.8: Miyabi Weapon SwordSheath position_vb Hash',)),(add_section_if_missing, ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n'))],
'a9ac3439': [(log, ('2.8: Miyabi Weapon SwordSheath texcoord_vb Hash',)),(add_section_if_missing, ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n'))],
'38c91cb1': [(log, ('2.8: Miyabi Weapon SwordSheath blend_vb Hash',)),   (add_section_if_missing, ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n'))],

# Weapon - SwordHandle
'5e1e12aa': [(log, ('2.8: Miyabi Weapon SwordHandle draw_vb Hash',)),    (add_section_if_missing, ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n'))],
'10545b04': [(log, ('2.8: Miyabi Weapon SwordHandle position_vb',)),    (add_section_if_missing, ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n'))],
'51af1803': [(log, ('2.8: Miyabi Weapon SwordHandle texcoord_vb',)),    (add_section_if_missing, ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n'))],
'c55927b0': [(log, ('2.8: Miyabi Weapon SwordHandle blend_vb Hash',)),   (add_section_if_missing, ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n'))],

# Weapon - SwordSoul (剑灵)
'79bd2f22': [(log, ('2.8: Miyabi Weapon SwordSoul draw_vb Hash',)),      (add_section_if_missing, ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n'))],
'e106fdc0': [(log, ('2.8: Miyabi Weapon SwordSoul position_vb Hash',)),  (add_section_if_missing, ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n'))],
'd6ea3283': [(log, ('2.8: Miyabi Weapon SwordSoul texcoord_vb Hash',)),  (add_section_if_missing, ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n'))],
'51a4604d': [(log, ('2.8: Miyabi Weapon SwordSoul blend_vb Hash',)),     (add_section_if_missing, ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'1d487fd5': [
        (log,                           ('2.8: Miyabi FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('92599e94', 'Miyabi.FaceA.Diffuse.1024')),
    ],
'92599e94': [
        (log,                           ('2.8: Miyabi FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1d487fd5', 'Miyabi.FaceA.Diffuse.2048')),
    ],

# === Hair & Legs Textures ===
'012e84e9': [
        (log,                           ('2.8: Miyabi HairA, LegsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('ed6b94f7', 'Miyabi.HairA.Diffuse.1024')),
    ],
'ed6b94f7': [
        (log,                           ('2.8: Miyabi HairA, LegsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('012e84e9', 'Miyabi.HairA.Diffuse.2048')),
    ],
'a6ea6d83': [
        (log,                           ('2.8: Miyabi HairA, LegsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8b5708f4', 'Miyabi.HairA.LightMap.1024')),
    ],
'8b5708f4': [
        (log,                           ('2.8: Miyabi HairA, LegsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('a6ea6d83', 'Miyabi.HairA.LightMap.2048')),
    ],
'd5462e37': [
        (log,                           ('2.8: Miyabi HairA, LegsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a84d9003', 'Miyabi.HairA.MaterialMap.1024')),
    ],
'a84d9003': [
        (log,                           ('2.8: Miyabi HairA, LegsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d5462e37', 'Miyabi.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'09a2bbd1': [
        (log,                           ('2.8: Miyabi BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('1a3644e7', 'Miyabi.BodyA.Diffuse.1024')),
    ],
'1a3644e7': [
        (log,                           ('2.8: Miyabi BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('09a2bbd1', 'Miyabi.BodyA.Diffuse.2048')),
    ],
'fd289380': [
        (log,                           ('2.8: Miyabi BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('0492f64a', 'Miyabi.BodyA.LightMap.1024')),
    ],
'0492f64a': [
        (log,                           ('2.8: Miyabi BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('fd289380', 'Miyabi.BodyA.LightMap.2048')),
    ],
'450770fd': [
        (log,                           ('2.8: Miyabi BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('168b1df9', 'Miyabi.BodyA.MaterialMap.1024')),
    ],
'168b1df9': [
        (log,                           ('2.8: Miyabi BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('450770fd', 'Miyabi.BodyA.MaterialMap.2048')),
    ],

# === Hairpin Textures ===
'e24bfe0e': [
        (log,                           ('2.8: Miyabi Hairpin Diffuse Hash',)),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],
'4e752f58': [
        (log,                           ('2.8: Miyabi Hairpin Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],
'9e1067e9': [
        (log,                           ('2.8: Miyabi Hairpin LightMap Hash',)),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],
'e10040c7': [
        (log,                           ('2.8: Miyabi Hairpin LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],
'f4d343b2': [
        (log,                           ('2.8: Miyabi Hairpin MaterialMap Hash',)),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],
'3af946eb': [
        (log,                           ('2.8: Miyabi Hairpin MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures ===
'718d7915': [
        (log,                           ('2.8: Miyabi Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],
'ac7673da': [
        (log,                           ('2.8: Miyabi Weapon Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],
'b73ed7e7': [
        (log,                           ('2.8: Miyabi Weapon LightMap Hash',)),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],
'f33cdee7': [
        (log,                           ('2.8: Miyabi Weapon LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],
'e1603ca5': [
        (log,                           ('2.8: Miyabi Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],
'8931b1ec': [
        (log,                           ('2.8: Miyabi Weapon MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Miyabi Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('acff032e', 'Miyabi.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0275d39f', 'Miyabi.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('562b2030', 'Miyabi.WeaponSwordSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1a82a439', 'Miyabi.WeaponSwordHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12739125', 'Miyabi.WeaponSwordSoul.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Miyabi Shared NormalMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        (('4faabaac', '981c1a1e', 'd8003df3'), 'Miyabi.Shared.NormalMap.2048', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log,                           ('2.8: Miyabi Hair Shared NormalMap Hash',)),
        (add_section_if_missing,        ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0c26a38b', 'Miyabi.HairpinRibbon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Miyabi',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}