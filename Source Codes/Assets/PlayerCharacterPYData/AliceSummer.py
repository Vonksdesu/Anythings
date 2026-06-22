"""
AliceSummer Character Hash Commands
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
    Returns AliceSummer's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'd131acb1': [(log, ('2.8: AliceSummer Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'cf8612e6': [(log, ('2.8: AliceSummer Body IB Hash',)),                  (add_ib_check_if_missing,)],
'2fcd160b': [(log, ('2.8: AliceSummer Backpack IB Hash',)),              (add_ib_check_if_missing,)],
'24d07797': [(log, ('2.8: AliceSummer Sensor IB Hash',)),                (add_ib_check_if_missing,)],
'b078ff22': [(log, ('2.8: AliceSummer Face IB Hash',)),                  (add_ib_check_if_missing,)],
'ebbe2894': [(log, ('2.8: AliceSummer Hair Shadow IB Hash',)),           (add_ib_check_if_missing,)],
'2c37d8c9': [(log, ('2.8: AliceSummer Weapon Sword IB Hash',)),          (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd515e182': [(log, ('2.8: AliceSummer Hair draw_vb',)),                  (add_section_if_missing, ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n'))],
'ad686c31': [(log, ('2.8: AliceSummer Hair position_vb',)),              (add_section_if_missing, ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n'))],
'b86d14b0': [(log, ('2.8: AliceSummer Hair texcoord_vb',)),              (add_section_if_missing, ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n'))],
'cf1202fd': [(log, ('2.8: AliceSummer Hair blend_vb',)),                 (add_section_if_missing, ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'd482d732': [(log, ('2.8: AliceSummer Hair shadow draw_vb',)),           (add_section_if_missing, ('ebbe2894', 'AliceSummer.HairShadow.IB', 'match_priority = 0\n'))],
'a3fb836a': [(log, ('2.8: AliceSummer Hair shadow position_vb',)),       (add_section_if_missing, ('ebbe2894', 'AliceSummer.HairShadow.IB', 'match_priority = 0\n'))],
'85fb0c65': [(log, ('2.8: AliceSummer Hair shadow texcoord_vb',)),       (add_section_if_missing, ('ebbe2894', 'AliceSummer.HairShadow.IB', 'match_priority = 0\n'))],
'14c96dd0': [(log, ('2.8: AliceSummer Hair shadow blend_vb',)),          (add_section_if_missing, ('ebbe2894', 'AliceSummer.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'a7fbdddb': [(log, ('2.8: AliceSummer Body draw_vb',)),                  (add_section_if_missing, ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n'))],
'75218916': [(log, ('2.8: AliceSummer Body position_vb',)),              (add_section_if_missing, ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n'))],
'3c686494': [(log, ('2.8: AliceSummer Body texcoord_vb',)),              (add_section_if_missing, ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n'))],
'7dc3bf5b': [(log, ('2.8: AliceSummer Body blend_vb',)),                 (add_section_if_missing, ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n'))],

# Sensor
'6f724c8e': [(log, ('2.8: AliceSummer Sensor draw_vb',)),                (add_section_if_missing, ('24d07797', 'AliceSummer.Sensor.IB', 'match_priority = 0\n'))],
'3246b6ca': [(log, ('2.8: AliceSummer Sensor position_vb',)),            (add_section_if_missing, ('24d07797', 'AliceSummer.Sensor.IB', 'match_priority = 0\n'))],
'a70f45bd': [(log, ('2.8: AliceSummer Sensor texcoord_vb',)),            (add_section_if_missing, ('24d07797', 'AliceSummer.Sensor.IB', 'match_priority = 0\n'))],
'ff4d1872': [(log, ('2.8: AliceSummer Sensor blend_vb',)),               (add_section_if_missing, ('24d07797', 'AliceSummer.Sensor.IB', 'match_priority = 0\n'))],

# Backpack
'f100ba28': [(log, ('2.8: AliceSummer Backpack draw_vb',)),              (add_section_if_missing, ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n'))],
'65d035e4': [(log, ('2.8: AliceSummer Backpack position_vb',)),          (add_section_if_missing, ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n'))],
'4d910650': [(log, ('2.8: AliceSummer Backpack texcoord_vb',)),          (add_section_if_missing, ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n'))],
'c715afa3': [(log, ('2.8: AliceSummer Backpack blend_vb',)),             (add_section_if_missing, ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n'))],

# Face
'70088a4a': [(log, ('2.8: AliceSummer Face draw_vb',)),                  (add_section_if_missing, ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n'))],
'4a1a190d': [(log, ('2.8: AliceSummer Face position_vb',)),              (add_section_if_missing, ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n'))],
'7c9dbd4a': [(log, ('2.8: AliceSummer Face texcoord_vb',)),              (add_section_if_missing, ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n'))],
'2326355e': [(log, ('2.8: AliceSummer Face blend_vb',)),                 (add_section_if_missing, ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n'))],

# Weapon - Sword
'4d92da0d': [(log, ('2.8: AliceSummer Weapon Sword draw_vb',)),          (add_section_if_missing, ('2c37d8c9', 'AliceSummer.WeaponSword.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'33fdeb6d': [
        (log,                           ('2.8: AliceSummer Face Diffuse Hash',)),
        (add_section_if_missing,        ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n')),
    ],
'9f3e582c': [
        (log,                           ('2.8: AliceSummer FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('b078ff22', 'AliceSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'91d2f9fd': [
        (log,                           ('2.8: AliceSummer Hair Diffuse Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'705caac9': [
        (log,                           ('2.8: AliceSummer HairA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'6c957d8f': [
        (log,                           ('2.8: AliceSummer Hair LightMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'03543db2': [
        (log,                           ('2.8: AliceSummer HairA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'bc4c87fd': [
        (log,                           ('2.8: AliceSummer Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'508530fe': [
        (log,                           ('2.8: AliceSummer HairA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'7283db21': [
        (log,                           ('2.8: AliceSummer Body Diffuse Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'18601d57': [
        (log,                           ('2.8: AliceSummer BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'8087d734': [
        (log,                           ('2.8: AliceSummer Body LightMap Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'3409fcce': [
        (log,                           ('2.8: AliceSummer BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'e4f01bb0': [
        (log,                           ('2.8: AliceSummer Body MaterialMap Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],
'212fc22a': [
        (log,                           ('2.8: AliceSummer BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === Sensor Textures ===
'bf0e4dab': [
        (log,                           ('2.8: AliceSummer Sensor Diffuse Hash',)),
        (add_section_if_missing,        ('24d07797', 'AliceSummer.Sensor.IB', 'match_priority = 0\n')),
    ],

# === Backpack & Weapon Textures ===
'6775ef8d': [
        (log,                           ('2.8: AliceSummer Backpack & Sword Diffuse Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2c37d8c9', 'AliceSummer.WeaponSword.IB', 'match_priority = 0\n')),
    ],
'4eff9bd8': [
        (log,                           ('2.8: AliceSummer BackpackA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],
'dbea86db': [
        (log,                           ('2.8: AliceSummer Backpack & Sword LightMap Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2c37d8c9', 'AliceSummer.WeaponSword.IB', 'match_priority = 0\n')),
    ],
'2a09a850': [
        (log,                           ('2.8: AliceSummer BackpackA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],
'21126e07': [
        (log,                           ('2.8: AliceSummer Backpack & Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2c37d8c9', 'AliceSummer.WeaponSword.IB', 'match_priority = 0\n')),
    ],
'1cd2807e': [
        (log,                           ('2.8: AliceSummer BackpackA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: AliceSummer Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2c37d8c9', 'AliceSummer.WeaponSword.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: AliceSummer HairA, BodyA, BackpackA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf8612e6', 'AliceSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2fcd160b', 'AliceSummer.Backpack.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AliceSummer',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}