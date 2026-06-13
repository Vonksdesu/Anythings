"""
Seed Character Hash Commands
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
    Returns Seed's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'6cb35165': [(log, ('2.8: Seed Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'634ac589': [(log, ('2.8: Seed Body IB Hash',)),                        (add_ib_check_if_missing,)],
'1d81bcc7': [(log, ('2.8: Seed Bib IB Hash',)),                         (add_ib_check_if_missing,)],
'914e39c6': [(log, ('2.8: Seed Accessories IB Hash',)),                 (add_ib_check_if_missing,)],
'09d9dca7': [(log, ('2.8: Seed Face IB Hash',)),                        (add_ib_check_if_missing,)],
'468e0f21': [(log, ('2.8: Seed Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'651f4fd5': [(log, ('2.8: Seed Scooter IB Hash',)),                     (add_ib_check_if_missing,)],
'c7f4f4ec': [(log, ('2.8: Seed Weapon Normal State IB Hash',)),          (add_ib_check_if_missing,)],
'75e1ae0a': [(log, ('2.8: Seed Weapon Cockpit IB Hash',)),                (add_ib_check_if_missing,)],
'b3f47664': [(log, ('2.8: Seed Weapon Torso IB Hash',)),                  (add_ib_check_if_missing,)],
'126bd0a1': [(log, ('2.8: Seed Weapon Limbs IB Hash',)),                  (add_ib_check_if_missing,)],
'71e8d07a': [(log, ('2.8: Seed Weapon Hand Device IB Hash',)),            (add_ib_check_if_missing,)],
'8a995990': [(log, ('2.8: Seed Weapon Back Device IB Hash',)),            (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'12bd16f4': [(log, ('2.8: Seed Hair draw_vb Hash',)),                    (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n'))],
'25a8bde2': [(log, ('2.8: Seed Hair position_vb Hash',)),                (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n'))],
'9e25742c': [(log, ('2.8: Seed Hair texcoord_vb Hash',)),                (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n'))],
'afe31e96': [(log, ('2.8: Seed Hair blend_vb Hash',)),                   (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'4d61e6f3': [(log, ('2.8: Seed Hair Shadow draw_vb Hash',)),             (add_section_if_missing, ('468e0f21', 'Seed.HairShadow.IB', 'match_priority = 0\n'))],
'3a097353': [(log, ('2.8: Seed Hair Shadow position_vb Hash',)),         (add_section_if_missing, ('468e0f21', 'Seed.HairShadow.IB', 'match_priority = 0\n'))],
'9f4d4106': [(log, ('2.8: Seed Hair Shadow texcoord_vb Hash',)),         (add_section_if_missing, ('468e0f21', 'Seed.HairShadow.IB', 'match_priority = 0\n'))],
'1abfa087': [(log, ('2.8: Seed Hair Shadow blend_vb Hash',)),             (add_section_if_missing, ('468e0f21', 'Seed.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'43185be9': [(log, ('2.8: Seed Body draw_vb Hash',)),                    (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n'))],
'5e2f1e06': [(log, ('2.8: Seed Body position_vb Hash',)),                (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n'))],
'f4cf83ff': [(log, ('2.8: Seed Body texcoord_vb Hash',)),                (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n'))],
'5b3d022f': [(log, ('2.8: Seed Body blend_vb Hash',)),                   (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n'))],

# Accessories
'c24ebf3b': [(log, ('2.8: Seed Accessories draw_vb Hash',)),             (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n'))],
'12d6c223': [(log, ('2.8: Seed Accessories position_vb Hash',)),         (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n'))],
'99be167f': [(log, ('2.8: Seed Accessories texcoord_vb Hash',)),         (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n'))],
'746e7bf8': [(log, ('2.8: Seed Accessories blend_vb Hash',)),            (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n'))],

# Bib / ChestClothing
'72fbbba3': [(log, ('2.8: Seed Bib draw_vb Hash',)),                     (add_section_if_missing, ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n'))],
'b2690ac8': [(log, ('2.8: Seed Bib position_vb Hash',)),                 (add_section_if_missing, ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n'))],
'2f706a18': [(log, ('2.8: Seed Bib texcoord_vb Hash',)),                 (add_section_if_missing, ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n'))],
'319ba025': [(log, ('2.8: Seed Bib blend_vb Hash',)),                    (add_section_if_missing, ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n'))],

# SelfBalancingScooter
'2d77a8c9': [(log, ('2.8: Seed Scooter draw_vb Hash',)),                 (add_section_if_missing, ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n'))],
'95941dba': [(log, ('2.8: Seed Scooter position_vb Hash',)),             (add_section_if_missing, ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n'))],
'4635f4f0': [(log, ('2.8: Seed Scooter texcoord_vb Hash',)),             (add_section_if_missing, ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n'))],
'547acb7e': [(log, ('2.8: Seed Scooter blend_vb Hash',)),                (add_section_if_missing, ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n'))],

# Face
'064aa73b': [(log, ('2.8: Seed Face draw_vb Hash',)),                    (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n'))],
'3c58347c': [(log, ('2.8: Seed Face position_vb Hash',)),                (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n'))],
'a0dfaf80': [(log, ('2.8: Seed Face texcoord_vb Hash',)),                (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n'))],
'7625e6d6': [(log, ('2.8: Seed Face blend_vb Hash',)),                   (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n'))],

# Weapon - Constant State (weapon-常驻状态)
'0238f9fc': [(log, ('2.8: Seed Weapon Constant draw_vb Hash',)),         (add_section_if_missing, ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n'))],
'8bb86a2d': [(log, ('2.8: Seed Weapon Constant position_vb Hash',)),     (add_section_if_missing, ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n'))],
'5abfc179': [(log, ('2.8: Seed Weapon Constant texcoord_vb Hash',)),     (add_section_if_missing, ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n'))],
'b6b679de': [(log, ('2.8: Seed Weapon Constant blend_vb Hash',)),        (add_section_if_missing, ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n'))],

# Weapon - Cockpit (weapon-驾驶舱)
'5bca6676': [(log, ('2.8: Seed Weapon Cockpit draw_vb Hash',)),          (add_section_if_missing, ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n'))],
'567f9bcd': [(log, ('2.8: Seed Weapon Cockpit position_vb Hash',)),      (add_section_if_missing, ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n'))],
'030e0aca': [(log, ('2.8: Seed Weapon Cockpit texcoord_vb Hash',)),      (add_section_if_missing, ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n'))],
'10c13253': [(log, ('2.8: Seed Weapon Cockpit blend_vb Hash',)),         (add_section_if_missing, ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n'))],

# Weapon - Torso (weapon-躯干)
'b7c36a17': [(log, ('2.8: Seed Weapon Torso draw_vb Hash',)),            (add_section_if_missing, ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n'))],
'e2694177': [(log, ('2.8: Seed Weapon Torso position_vb Hash',)),        (add_section_if_missing, ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n'))],
'efc82ade': [(log, ('2.8: Seed Weapon Torso texcoord_vb Hash',)),        (add_section_if_missing, ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n'))],
'09c28e33': [(log, ('2.8: Seed Weapon Torso blend_vb Hash',)),           (add_section_if_missing, ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n'))],

# Weapon - Limbs (weapon-手足)
'e0736df2': [(log, ('2.8: Seed Weapon Limbs draw_vb Hash',)),            (add_section_if_missing, ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n'))],
'fdfdf144': [(log, ('2.8: Seed Weapon Limbs position_vb Hash',)),        (add_section_if_missing, ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n'))],
'255a77a9': [(log, ('2.8: Seed Weapon Limbs texcoord_vb Hash',)),        (add_section_if_missing, ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n'))],
'98f46d5b': [(log, ('2.8: Seed Weapon Limbs blend_vb Hash',)),           (add_section_if_missing, ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n'))],

# Weapon - Hand Device (weapon-手部装置)
'c6043e88': [(log, ('2.8: Seed Weapon Hand draw_vb Hash',)),             (add_section_if_missing, ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n'))],
'143481a0': [(log, ('2.8: Seed Weapon Hand position_vb Hash',)),         (add_section_if_missing, ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n'))],
'd06b00ad': [(log, ('2.8: Seed Weapon Hand texcoord_vb Hash',)),         (add_section_if_missing, ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n'))],
'd3adb384': [(log, ('2.8: Seed Weapon Hand blend_vb Hash',)),            (add_section_if_missing, ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n'))],

# Weapon - Back Device (weapon-背部装置)
'3253babd': [(log, ('2.8: Seed Weapon Back draw_vb Hash',)),             (add_section_if_missing, ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n'))],
'f66c29e6': [(log, ('2.8: Seed Weapon Back position_vb Hash',)),         (add_section_if_missing, ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n'))],
'72329a18': [(log, ('2.8: Seed Weapon Back texcoord_vb Hash',)),         (add_section_if_missing, ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n'))],
'8cb92072': [(log, ('2.8: Seed Weapon Back blend_vb Hash',)),            (add_section_if_missing, ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n'))],

# === Legacy / Version Updates ===
'b095c5cf': [(log, ('2.8: Updating Seed cockpit position_vb to 567f9bcd [Legacy]',)),(update_hash, ('567f9bcd',))],
'56979e94': [(log, ('2.8: Updating Seed cockpit texcoord_vb to 030e0aca [Legacy]',)),(update_hash, ('030e0aca',))],

# === Face Textures ===
'f02ebff3': [
        (log,                           ('2.8: Face Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],
'a7e3da19': [
        (log,                           ('2.8: Seed Face Diffuse Hash',)),
        (add_section_if_missing,        ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair, Bib & Accessories Shared Textures ===
'2fff22a7': [
        (log,                           ('2.8: Seed HairA, BibA, AccessoriesA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'9d4019f4': [
        (log,                           ('2.8: Seed Hair, Bib, Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'bf2c273a': [
        (log,                           ('2.8: Seed HairA, BibA, AccessoriesA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'e7efee45': [
        (log,                           ('2.8: Seed Hair, Bib, Accessories LightMap Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'a1658bbd': [
        (log,                           ('2.8: Seed HairA, BibA, AccessoriesA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'bfcfcdc6': [
        (log,                           ('2.8: Seed Hair, Bib, Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'7c7c2622': [
        (log,                           ('2.8: Seed BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'684d2bd5': [
        (log,                           ('2.8: Seed Body Diffuse Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'b14c9c6f': [
        (log,                           ('2.8: Seed BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'522ee460': [
        (log,                           ('2.8: Seed Body LightMap Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'da2deeaa': [
        (log,                           ('2.8: Seed BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'be9dd4c2': [
        (log,                           ('2.8: Seed Body MaterialMap Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],

# === Scooter Textures ===
'74b9c4c8': [
        (log,                           ('2.8: Seed Scooter Diffuse Hash',)),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
    ],
'bd0f0925': [
        (log,                           ('2.8: Seed Scooter LightMap Hash',)),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
    ],
'7f7b60c9': [
        (log,                           ('2.8: Seed Scooter MaterialMap Hash',)),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
    ],

# === Constant State Weapon Textures ===
'11be1be8': [
        (log,                           ('2.8: Seed Constant Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
    ],
'c7a71ca0': [
        (log,                           ('2.8: Seed Constant Weapon LightMap Hash',)),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
    ],
'6cdfa1b1': [
        (log,                           ('2.8: Seed Constant Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
    ],

# === Cockpit State Weapon Textures ===
'd8e36eca': [
        (log,                           ('2.8: Seed Cockpit Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n')),
    ],
'bb3bae0e': [
        (log,                           ('2.8: Seed Cockpit Weapon LightMap Hash',)),
        (add_section_if_missing,        ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n')),
    ],
'efeed071': [
        (log,                           ('2.8: Seed Cockpit Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n')),
    ],

# === Torso State Weapon Textures ===
'a44bbeb3': [
        (log,                           ('2.8: Seed Torso Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
    ],
'3d66757d': [
        (log,                           ('2.8: Seed Torso Weapon LightMap Hash',)),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
    ],
'5fa93693': [
        (log,                           ('2.8: Seed Torso Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
    ],

# === Limbs State Weapon Textures ===
'93c858df': [
        (log,                           ('2.8: Seed Limbs Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
    ],
'494e24a6': [
        (log,                           ('2.8: Seed Limbs Weapon LightMap Hash',)),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
    ],
'7832e989': [
        (log,                           ('2.8: Seed Limbs Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
    ],

# === Devices (Hand & Back) State Weapon Textures ===
'2e2a9097': [
        (log,                           ('2.8: Seed Hand/Back Device Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n')),
    ],
'cc24383a': [
        (log,                           ('2.8: Seed Hand/Back Device Weapon LightMap Hash',)),
        (add_section_if_missing,        ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n')),
    ],
'4be2f394': [
        (log,                           ('2.8: Seed Hand/Back Device Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Seed Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('71e8d07a', 'Seed.WeaponHand.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a995990', 'Seed.WeaponBack.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Seed hashes ===
'0a4cecd8': [
        (log,                           ('2.8: Seed Weapon Torso Diffuse Hash [New]',)),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
    ],
'1962d85c': [
        (log,                           ('2.8: Seed Weapon Torso LightMap Hash [New]',)),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
    ],
'54a8ad89': [
        (log,                           ('2.8: Seed Weapon Constant MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
    ],
'64bb6cb7': [
        (log,                           ('2.8: Seed Weapon Torso MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('b3f47664', 'Seed.WeaponTorso.IB', 'match_priority = 0\n')),
    ],
'6f269065': [
        (log,                           ('2.8: Seed Weapon Cockpit LightMap Hash [New]',)),
        (add_section_if_missing,        ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n')),
    ],
'91d18cf9': [
        (log,                           ('2.8: Seed Scooter Diffuse Hash [New]',)),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
    ],
'9896a7c2': [
        (log,                           ('2.8: Seed Scooter MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
    ],
'a065222f': [
        (log,                           ('2.8: Seed Weapon Limbs Diffuse Hash [New]',)),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
    ],
'a06afdbc': [
        (log,                           ('2.8: Seed Weapon Constant Diffuse Hash [New]',)),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
    ],
'a6726612': [
        (log,                           ('2.8: Seed Scooter LightMap Hash [New]',)),
        (add_section_if_missing,        ('651f4fd5', 'Seed.Scooter.IB', 'match_priority = 0\n')),
    ],
'a9a40828': [
        (log,                           ('2.8: Seed Weapon Device Diffuse Hash [New]',)),
        (add_section_if_missing,        (('71e8d07a', '8a995990'), 'Seed.WeaponDevice.IB', 'match_priority = 0\n')),
    ],
'b2e81a28': [
        (log,                           ('2.8: Seed Weapon Cockpit Diffuse Hash [New]',)),
        (add_section_if_missing,        ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n')),
    ],
'bc0bd24c': [
        (log,                           ('2.8: Seed Weapon Device MaterialMap Hash [New]',)),
        (add_section_if_missing,        (('71e8d07a', '8a995990'), 'Seed.WeaponDevice.IB', 'match_priority = 0\n')),
    ],
'caf87ff4': [
        (log,                           ('2.8: Seed Weapon Limbs MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
    ],
'ceb90df0': [
        (log,                           ('2.8: Seed Weapon Cockpit MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('75e1ae0a', 'Seed.WeaponCockpit.IB', 'match_priority = 0\n')),
    ],
'd6e62b3f': [
        (log,                           ('2.8: Seed Weapon Device LightMap Hash [New]',)),
        (add_section_if_missing,        (('71e8d07a', '8a995990'), 'Seed.WeaponDevice.IB', 'match_priority = 0\n')),
    ],
'dd157642': [
        (log,                           ('2.8: Seed Weapon Constant LightMap Hash [New]',)),
        (add_section_if_missing,        ('c7f4f4ec', 'Seed.WeaponConstant.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Seed Shared NormalMap [Legacy] [New]',)),
        (add_section_if_missing,        (('6cb35165', '634ac589'), 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'f56f3ac1': [
        (log,                           ('2.8: Seed Weapon Limbs LightMap Hash [New]',)),
        (add_section_if_missing,        ('126bd0a1', 'Seed.WeaponLimbs.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seed',
    'game_versions': ['2.8'],
}