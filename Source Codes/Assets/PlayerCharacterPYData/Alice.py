"""
Alice Character Hash Commands
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
    Returns Alice's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'd131acb1': [(log, ('2.8: Alice Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'8a512b21': [(log, ('2.8: Alice Body IB Hash',)),                        (add_ib_check_if_missing,)],
'625c2692': [(log, ('2.8: Alice Legs IB Hash',)),                        (add_ib_check_if_missing,)],
'993d2ddd': [(log, ('2.8: Alice Sensor IB Hash',)),                      (add_ib_check_if_missing,)],
'bd2277ef': [(log, ('2.8: Alice Backpack IB Hash',)),                    (add_ib_check_if_missing,)],
'b078ff22': [(log, ('2.8: Alice Face IB Hash',)),                        (add_ib_check_if_missing,)],
'ebbe2894': [(log, ('2.8: Alice Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'30205a68': [(log, ('2.8: Alice Weapon Sword IB Hash',)),                (add_ib_check_if_missing,)],
'323b1a95': [(log, ('2.8: Alice Weapon Handguard IB Hash',)),            (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd515e182': [(log, ('2.8: Alice Hair draw_vb',)),                        (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n'))],
'ad686c31': [(log, ('2.8: Alice Hair position_vb',)),                    (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n'))],
'b86d14b0': [(log, ('2.8: Alice Hair texcoord_vb',)),                    (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n'))],
'cf1202fd': [(log, ('2.8: Alice Hair blend_vb',)),                       (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'd482d732': [(log, ('2.8: Alice Hair shadow draw_vb',)),                 (add_section_if_missing, ('ebbe2894', 'Alice.HairShadow.IB', 'match_priority = 0\n'))],
'a3fb836a': [(log, ('2.8: Alice Hair shadow position_vb',)),             (add_section_if_missing, ('ebbe2894', 'Alice.HairShadow.IB', 'match_priority = 0\n'))],
'85fb0c65': [(log, ('2.8: Alice Hair shadow texcoord_vb',)),             (add_section_if_missing, ('ebbe2894', 'Alice.HairShadow.IB', 'match_priority = 0\n'))],
'14c96dd0': [(log, ('2.8: Alice Hair shadow blend_vb',)),                (add_section_if_missing, ('ebbe2894', 'Alice.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'7a318f3d': [(log, ('2.8: Alice Body draw_vb',)),                        (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n'))],
'37a05757': [(log, ('2.8: Alice Body position_vb',)),                    (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n'))],
'9ad7d70c': [(log, ('2.8: Alice Body texcoord_vb',)),                    (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n'))],
'15935e48': [(log, ('2.8: Alice Body blend_vb',)),                       (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n'))],

# Legs
'3e4c0174': [(log, ('2.8: Alice Legs draw_vb',)),                        (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n'))],
'c1aaa893': [(log, ('2.8: Alice Legs position_vb',)),                    (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n'))],
'2821afc9': [(log, ('2.8: Alice Legs texcoord_vb',)),                    (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n'))],
'a1b46da2': [(log, ('2.8: Alice Legs blend_vb',)),                       (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n'))],

# Sensor
'c2b0bfbd': [(log, ('2.8: Alice Sensor draw_vb',)),                      (add_section_if_missing, ('993d2ddd', 'Alice.Sensor.IB', 'match_priority = 0\n'))],
'd0867379': [(log, ('2.8: Alice Sensor position_vb',)),                  (add_section_if_missing, ('993d2ddd', 'Alice.Sensor.IB', 'match_priority = 0\n'))],
'd72a4315': [(log, ('2.8: Alice Sensor texcoord_vb',)),                  (add_section_if_missing, ('993d2ddd', 'Alice.Sensor.IB', 'match_priority = 0\n'))],
'73b54620': [(log, ('2.8: Alice Sensor blend_vb',)),                     (add_section_if_missing, ('993d2ddd', 'Alice.Sensor.IB', 'match_priority = 0\n'))],

# Backpack
'03090c30': [(log, ('2.8: Alice Backpack draw_vb',)),                    (add_section_if_missing, ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n'))],
'23712d3d': [(log, ('2.8: Alice Backpack position_vb',)),                (add_section_if_missing, ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n'))],
'1c272241': [(log, ('2.8: Alice Backpack texcoord_vb',)),                (add_section_if_missing, ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n'))],
'37717c75': [(log, ('2.8: Alice Backpack blend_vb',)),                   (add_section_if_missing, ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n'))],

# Face
'70088a4a': [(log, ('2.8: Alice Face draw_vb',)),                        (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n'))],
'4a1a190d': [(log, ('2.8: Alice Face position_vb',)),                    (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n'))],
'7c9dbd4a': [(log, ('2.8: Alice Face texcoord_vb',)),                    (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n'))],
'2326355e': [(log, ('2.8: Alice Face blend_vb',)),                       (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n'))],

# Weapon - Sword
'f26a8aac': [(log, ('2.8: Alice Weapon Sword draw_vb',)),                 (add_section_if_missing, ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n'))],
'47a48c42': [(log, ('2.8: Alice Weapon Sword position_vb',)),             (add_section_if_missing, ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n'))],
'7b3126b6': [(log, ('2.8: Alice Weapon Sword texcoord_vb',)),             (add_section_if_missing, ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n'))],
'bb487b00': [(log, ('2.8: Alice Weapon Sword blend_vb',)),                (add_section_if_missing, ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n'))],

# Weapon - Handguard
'0a06059e': [(log, ('2.8: Alice Weapon Handguard draw_vb',)),             (add_section_if_missing, ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n'))],
'bd544be3': [(log, ('2.8: Alice Weapon Handguard position_vb',)),         (add_section_if_missing, ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n'))],
'9a136061': [(log, ('2.8: Alice Weapon Handguard texcoord_vb',)),         (add_section_if_missing, ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n'))],
'aac53ae5': [(log, ('2.8: Alice Weapon Handguard blend_vb',)),            (add_section_if_missing, ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'33fdeb6d': [
        (log,                           ('2.8: Alice Face Diffuse Hash',)),
        (add_section_if_missing,        ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],
'9f3e582c': [
        (log,                           ('2.8: Alice FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair & Legs Shared Textures ===
'91d2f9fd': [
        (log,                           ('2.8: Alice Hair, Legs Diffuse Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'705caac9': [
        (log,                           ('2.8: Alice HairA, LegsA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'6c957d8f': [
        (log,                           ('2.8: Alice Hair, Legs LightMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'03543db2': [
        (log,                           ('2.8: Alice HairA, LegsA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'bc4c87fd': [
        (log,                           ('2.8: Alice Hair, Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'508530fe': [
        (log,                           ('2.8: Alice HairA, LegsA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'9201609a': [
        (log,                           ('2.8: Alice Body Diffuse Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'269185ed': [
        (log,                           ('2.8: Alice BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'548623cd': [
        (log,                           ('2.8: Alice Body LightMap Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'0d72cb85': [
        (log,                           ('2.8: Alice BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'e05e4c54': [
        (log,                           ('2.8: Alice Body MaterialMap Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'95967afb': [
        (log,                           ('2.8: Alice BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],

# === Sensor Textures ===
'bf0e4dab': [
        (log,                           ('2.8: Alice Sensor Diffuse Hash',)),
        (add_section_if_missing,        ('993d2ddd', 'Alice.Sensor.IB', 'match_priority = 0\n')),
    ],

# === Backpack & Sword Textures ===
'228bdc7c': [
        (log,                           ('2.8: Alice Backpack & Sword Diffuse Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n')),
    ],
'79cbbcc4': [
        (log,                           ('2.8: Alice BackpackA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'980c7ed0': [
        (log,                           ('2.8: Alice Backpack & Sword LightMap Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n')),
    ],
'a226ce08': [
        (log,                           ('2.8: Alice BackpackA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'072eabe7': [
        (log,                           ('2.8: Alice Backpack & Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n')),
    ],
'9ada942b': [
        (log,                           ('2.8: Alice BackpackA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],

# === Normal Map ===
'798adba3': [
        (log,                           ('2.8: Alice Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30205a68', 'Alice.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('323b1a95', 'Alice.WeaponHandguard.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Alice HairA, LegsA, BodyA, BackpackA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Alice',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}