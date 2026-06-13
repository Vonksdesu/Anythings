"""
StarlightBilly Character Hash Commands
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
    Returns StarlightBilly's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'b126d40d': [(log, ('2.8: StarlightBilly Hair IB Hash',)),          (add_ib_check_if_missing,)],
'099cc55b': [(log, ('2.8: StarlightBilly Body IB Hash',)),          (add_ib_check_if_missing,)],
'b602e4de': [(log, ('2.8: StarlightBilly Torso IB Hash',)),         (add_ib_check_if_missing,)],
'85ec4f39': [(log, ('2.8: StarlightBilly LeftArm IB Hash',)),       (add_ib_check_if_missing,)],
'fed4432c': [(log, ('2.8: StarlightBilly Collar IB Hash',)),        (add_ib_check_if_missing,)],
'169e16c1': [(log, ('2.8: StarlightBilly BackDeco1 IB Hash',)),     (add_ib_check_if_missing,)],
'11727cec': [(log, ('2.8: StarlightBilly BackDeco2 IB Hash',)),     (add_ib_check_if_missing,)],
'26d71d07': [(log, ('2.8: StarlightBilly Motorcycle IB Hash',)),    (add_ib_check_if_missing,)],
'47be3135': [(log, ('2.8: StarlightBilly Face IB Hash',)),          (add_ib_check_if_missing,)],
'9f671d6b': [(log, ('2.8: StarlightBilly Gun IB Hash',)),           (add_ib_check_if_missing,)],
'75f90347': [(log, ('2.8: StarlightBilly Weapon IB Hash',)),        (add_ib_check_if_missing,)],
'1ee52291': [(log, ('2.8: StarlightBilly WeaponAcc1 IB Hash',)),    (add_ib_check_if_missing,)],
'8f4285cd': [(log, ('2.8: StarlightBilly WeaponAcc2 IB Hash',)),    (add_ib_check_if_missing,)],
'15ae37ae': [(log, ('2.8: StarlightBilly WeaponAcc3 IB Hash',)),    (add_ib_check_if_missing,)],
'd3e8cd51': [(log, ('2.8: StarlightBilly WeaponAcc4 IB Hash',)),    (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'0a1f876f': [(log, ('2.8: StarlightBilly Hair draw_vb',)),          (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n'))],
'2182114e': [(log, ('2.8: StarlightBilly Hair position_vb',)),      (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n'))],
'bedc10c4': [(log, ('2.8: StarlightBilly Hair texcoord_vb',)),      (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n'))],
'794d5c7b': [(log, ('2.8: StarlightBilly Hair blend_vb',)),         (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n'))],

# Body
'c0d45183': [(log, ('2.8: StarlightBilly Body draw_vb',)),          (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n'))],
'b792110b': [(log, ('2.8: StarlightBilly Body position_vb',)),      (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n'))],
'203e1a47': [(log, ('2.8: StarlightBilly Body texcoord_vb',)),      (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n'))],
'ccfa3c1f': [(log, ('2.8: StarlightBilly Body blend_vb',)),         (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n'))],

# Torso
'617a4f7c': [(log, ('2.8: StarlightBilly Torso draw_vb',)),         (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n'))],
'45992c18': [(log, ('2.8: StarlightBilly Torso position_vb',)),     (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n'))],
'97c35484': [(log, ('2.8: StarlightBilly Torso texcoord_vb',)),     (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n'))],
'a829800f': [(log, ('2.8: StarlightBilly Torso blend_vb',)),        (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n'))],

# LeftArm
'5a7ee5ae': [(log, ('2.8: StarlightBilly LeftArm draw_vb',)),       (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n'))],
'0d842713': [(log, ('2.8: StarlightBilly LeftArm position_vb',)),   (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n'))],
'd4575d84': [(log, ('2.8: StarlightBilly LeftArm texcoord_vb',)),   (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n'))],
'6d19734d': [(log, ('2.8: StarlightBilly LeftArm blend_vb',)),      (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n'))],

# Collar
'b729d418': [(log, ('2.8: StarlightBilly Collar draw_vb',)),        (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n'))],
'b5ba7f2c': [(log, ('2.8: StarlightBilly Collar position_vb',)),    (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n'))],
'6cbb0e03': [(log, ('2.8: StarlightBilly Collar texcoord_vb',)),    (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n'))],
'0c780fde': [(log, ('2.8: StarlightBilly Collar blend_vb',)),       (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n'))],

# BackDeco1
'730440ae': [(log, ('2.8: StarlightBilly BackDeco1 draw_vb',)),     (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n'))],
'9eda96ca': [(log, ('2.8: StarlightBilly BackDeco1 position_vb',)), (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n'))],
'02125c63': [(log, ('2.8: StarlightBilly BackDeco1 texcoord_vb',)), (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n'))],
'14896011': [(log, ('2.8: StarlightBilly BackDeco1 blend_vb',)),    (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n'))],

# BackDeco2
'93a9492c': [(log, ('2.8: StarlightBilly BackDeco2 draw_vb',)),     (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n'))],
'c9c3436f': [(log, ('2.8: StarlightBilly BackDeco2 position_vb',)), (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n'))],
'2f2f4055': [(log, ('2.8: StarlightBilly BackDeco2 texcoord_vb',)), (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n'))],
'52225c15': [(log, ('2.8: StarlightBilly BackDeco2 blend_vb',)),    (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n'))],

# Motorcycle
'7a547ef8': [(log, ('2.8: StarlightBilly Motorcycle draw_vb',)),    (add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n'))],
'a7516e2b': [(log, ('2.8: StarlightBilly Motorcycle position_vb',)),(add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n'))],
'09439f49': [(log, ('2.8: StarlightBilly Motorcycle texcoord_vb',)),(add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n'))],
'5c3aba5b': [(log, ('2.8: StarlightBilly Motorcycle blend_vb',)),   (add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n'))],

# Face
'eabcb930': [(log, ('2.8: StarlightBilly Face draw_vb',)),          (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n'))],
'd0ae2a77': [(log, ('2.8: StarlightBilly Face position_vb',)),      (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n'))],
'7d045e09': [(log, ('2.8: StarlightBilly Face texcoord_vb',)),      (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n'))],
'be8fd496': [(log, ('2.8: StarlightBilly Face blend_vb',)),         (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n'))],

# Gun
'ccd59cb9': [(log, ('2.8: StarlightBilly Gun draw_vb',)),          (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n'))],
'e2a3e69e': [(log, ('2.8: StarlightBilly Gun position_vb',)),      (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n'))],
'dceb0608': [(log, ('2.8: StarlightBilly Gun texcoord_vb',)),      (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n'))],
'1f409c43': [(log, ('2.8: StarlightBilly Gun blend_vb',)),         (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n'))],

# Weapon
'cf21b035': [(log, ('2.8: StarlightBilly Weapon draw_vb',)),        (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n'))],
'db0321a9': [(log, ('2.8: StarlightBilly Weapon position_vb',)),    (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n'))],
'bbe34d15': [(log, ('2.8: StarlightBilly Weapon texcoord_vb',)),    (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n'))],
'6023cad8': [(log, ('2.8: StarlightBilly Weapon blend_vb',)),       (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n'))],

# WeaponAcc1
'696bd946': [(log, ('2.8: StarlightBilly WeaponAcc1 draw_vb',)),    (add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n'))],
'f293dadb': [(log, ('2.8: StarlightBilly WeaponAcc1 position_vb',)),(add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n'))],
'804cf62d': [(log, ('2.8: StarlightBilly WeaponAcc1 texcoord_vb',)),(add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n'))],
'7b217048': [(log, ('2.8: StarlightBilly WeaponAcc1 blend_vb',)),   (add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n'))],

# WeaponAcc2
'f91227b7': [(log, ('2.8: StarlightBilly WeaponAcc2 draw_vb',)),    (add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n'))],
'ce8c77da': [(log, ('2.8: StarlightBilly WeaponAcc2 position_vb',)),(add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n'))],
'8190a48a': [(log, ('2.8: StarlightBilly WeaponAcc2 texcoord_vb',)),(add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n'))],
'131e5a0a': [(log, ('2.8: StarlightBilly WeaponAcc2 blend_vb',)),   (add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n'))],

# WeaponAcc3
'84a7e817': [(log, ('2.8: StarlightBilly WeaponAcc3 draw_vb',)),    (add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n'))],
'612b519c': [(log, ('2.8: StarlightBilly WeaponAcc3 position_vb',)),(add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n'))],
'8a828eae': [(log, ('2.8: StarlightBilly WeaponAcc3 texcoord_vb',)),(add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n'))],
'fbf0b1bb': [(log, ('2.8: StarlightBilly WeaponAcc3 blend_vb',)),   (add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n'))],

# WeaponAcc4
'6ccff03a': [(log, ('2.8: StarlightBilly WeaponAcc4 draw_vb',)),    (add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n'))],
'20ccc597': [(log, ('2.8: StarlightBilly WeaponAcc4 position_vb',)),(add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n'))],
'4cfcbaf4': [(log, ('2.8: StarlightBilly WeaponAcc4 texcoord_vb',)),(add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n'))],
'82c72748': [(log, ('2.8: StarlightBilly WeaponAcc4 blend_vb',)),   (add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'e706ba29': [
        (log,                           ('2.8: StarlightBilly FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'f55b5dbb': [
        (log,                           ('2.8: StarlightBilly FaceA Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'4784f14a': [
        (log,                           ('2.8: StarlightBilly FaceA LightMap Hash',)),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'ba8a1e40': [
        (log,                           ('2.8: StarlightBilly FaceA LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'd08a92b4': [
        (log,                           ('2.8: StarlightBilly FaceA MaterialMap Hash',)),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'bdc617ad': [
        (log,                           ('2.8: StarlightBilly FaceA MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'6a6a1c79': [
        (log,                           ('2.8: StarlightBilly Hair Diffuse Hash',)),
        (add_section_if_missing,        ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'2edbc842': [
        (log,                           ('2.8: StarlightBilly Hair LightMap Hash',)),
        (add_section_if_missing,        ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'be5165ce': [
        (log,                           ('2.8: StarlightBilly BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'30b6b9c7': [
        (log,                           ('2.8: StarlightBilly BodyA Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'7ac1a66a': [
        (log,                           ('2.8: StarlightBilly BodyA LightMap Hash',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'da2181cf': [
        (log,                           ('2.8: StarlightBilly BodyA LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'150df321': [
        (log,                           ('2.8: StarlightBilly BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'd85dec5d': [
        (log,                           ('2.8: StarlightBilly BodyA MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],

# === Torso, Collar & BackDeco Shared Textures ===
'a6ef0c74': [
        (log,                           ('2.8: StarlightBilly Torso, Collar, BackDeco Diffuse Hash',)),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
    ],
'd82e8cd7': [
        (log,                           ('2.8: StarlightBilly Torso, Collar, BackDeco Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
    ],
'6effa144': [
        (log,                           ('2.8: StarlightBilly Torso, Collar, BackDeco LightMap Hash',)),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
    ],
'a28930f3': [
        (log,                           ('2.8: StarlightBilly Torso, Collar, BackDeco LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
    ],
'744b53d4': [
        (log,                           ('2.8: StarlightBilly Torso, Collar, BackDeco MaterialMap Hash',)),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
    ],
'f8f7fdbe': [
        (log,                           ('2.8: StarlightBilly Torso, Collar, BackDeco MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
    ],

# === LeftArm, Weapon & WeaponAcc Shared Textures ===
'1d5dcd0a': [
        (log,                           ('2.8: StarlightBilly LeftArm, Weapon & Acc Diffuse Hash',)),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],
'6fe50be9': [
        (log,                           ('2.8: StarlightBilly LeftArm, Weapon & Acc Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],
'16d85b96': [
        (log,                           ('2.8: StarlightBilly LeftArm, Weapon & Acc LightMap Hash',)),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],
'c0a681c1': [
        (log,                           ('2.8: StarlightBilly LeftArm, Weapon & Acc LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],
'02ac888a': [
        (log,                           ('2.8: StarlightBilly LeftArm, Weapon & Acc MaterialMap Hash',)),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],
'95454832': [
        (log,                           ('2.8: StarlightBilly LeftArm, Weapon & Acc MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],

# === Motorcycle Textures ===
'd4aabf11': [
        (log,                           ('2.8: StarlightBilly Motorcycle Diffuse Hash',)),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'ed4bde0d': [
        (log,                           ('2.8: StarlightBilly Motorcycle Diffuse Hash (Skins)',)),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'5dc62b0b': [
        (log,                           ('2.8: StarlightBilly Motorcycle LightMap Hash',)),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'573e87e3': [
        (log,                           ('2.8: StarlightBilly Motorcycle LightMap Hash (Skins)',)),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'81cd8366': [
        (log,                           ('2.8: StarlightBilly Motorcycle MaterialMap Hash',)),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'6b61b30c': [
        (log,                           ('2.8: StarlightBilly Motorcycle MaterialMap Hash (Skins)',)),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],

# === Gun Textures ===
'3541c183': [
        (log,                           ('2.8: StarlightBilly Gun Diffuse Hash',)),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'3a1ee1d7': [
        (log,                           ('2.8: StarlightBilly Gun Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'6f6aad09': [
        (log,                           ('2.8: StarlightBilly Gun LightMap Hash',)),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'4b0a8224': [
        (log,                           ('2.8: StarlightBilly Gun LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'11af0644': [
        (log,                           ('2.8: StarlightBilly Gun MaterialMap Hash',)),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'49782d36': [
        (log,                           ('2.8: StarlightBilly Gun MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: StarlightBilly Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('169e16c1', 'StarlightBilly.BackDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('11727cec', 'StarlightBilly.BackDeco2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1ee52291', 'StarlightBilly.WeaponAcc1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8f4285cd', 'StarlightBilly.WeaponAcc2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15ae37ae', 'StarlightBilly.WeaponAcc3.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3e8cd51', 'StarlightBilly.WeaponAcc4.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log,                           ('2.8: StarlightBilly Hair Shared NormalMap Hash',)),
        (add_section_if_missing,        ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'StarlightBilly',
    'game_versions': ['2.8'],
}