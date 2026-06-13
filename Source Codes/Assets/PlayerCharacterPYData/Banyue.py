"""
Banyue Character Hash Commands
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
    Returns Banyue's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'f3b6e869': [(log, ('2.8: Banyue Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'698046e6': [(log, ('2.8: Banyue Body IB Hash',)),                      (add_ib_check_if_missing,)],
'5f855404': [(log, ('2.8: Banyue Legs IB Hash',)),                      (add_ib_check_if_missing,)],
'635709b5': [(log, ('2.8: Banyue BothArms IB Hash',)),                  (add_ib_check_if_missing,)],
'084eb825': [(log, ('2.8: Banyue PalmsBall IB Hash',)),                 (add_ib_check_if_missing,)],
'9bb1eb14': [(log, ('2.8: Banyue WeaponBall IB Hash',)),                (add_ib_check_if_missing,)],

# === VB Hashes ===
# BothArms
'8e08205b': [(log, ('2.8: Banyue BothArms draw_vb',)),                  (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n'))],
'121a1aa7': [(log, ('2.8: Banyue BothArms position_vb',)),              (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n'))],
'd17bb604': [(log, ('2.8: Banyue BothArms texcoord_vb',)),              (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n'))],
'0bc8c485': [(log, ('2.8: Banyue BothArms blend_vb',)),                 (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n'))],

# Legs
'ae8abe08': [(log, ('2.8: Banyue Legs draw_vb',)),                      (add_section_if_missing, ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n'))],
'dc2a8ff5': [(log, ('2.8: Banyue Legs position_vb',)),                  (add_section_if_missing, ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n'))],
'132c3f5c': [(log, ('2.8: Banyue Legs texcoord_vb',)),                  (add_section_if_missing, ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n'))],
'edc17446': [(log, ('2.8: Banyue Legs blend_vb',)),                     (add_section_if_missing, ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n'))],

# Body
'1aab74cc': [(log, ('2.8: Banyue Body draw_vb',)),                      (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n'))],
'6fab5f8b': [(log, ('2.8: Banyue Body position_vb',)),                  (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n'))],
'9b4cef87': [(log, ('2.8: Banyue Body texcoord_vb',)),                  (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n'))],
'dba0d45e': [(log, ('2.8: Banyue Body blend_vb',)),                     (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n'))],

# PalmsBall
'16698b4f': [(log, ('2.8: Banyue PalmsBall draw_vb',)),                 (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n'))],
'679f2627': [(log, ('2.8: Banyue PalmsBall position_vb',)),             (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n'))],
'daf0e9f9': [(log, ('2.8: Banyue PalmsBall texcoord_vb',)),             (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n'))],
'3a3a9a42': [(log, ('2.8: Banyue PalmsBall blend_vb',)),                (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n'))],

# WeaponBall
'00f0ed60': [(log, ('2.8: Banyue WeaponBall draw_vb',)),                (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n'))],
'289bb2ef': [(log, ('2.8: Banyue WeaponBall position_vb',)),            (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n'))],
'd6d66d05': [(log, ('2.8: Banyue WeaponBall texcoord_vb',)),            (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n'))],
'48237f26': [(log, ('2.8: Banyue WeaponBall blend_vb',)),               (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n'))],

# Face
'0a12bb17': [(log, ('2.8: Banyue Face draw_vb',)),                      (add_section_if_missing, ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n'))],
'8be7477c': [(log, ('2.8: Banyue Face position_vb',)),                  (add_section_if_missing, ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n'))],
'ec9b7916': [(log, ('2.8: Banyue Face texcoord_vb',)),                  (add_section_if_missing, ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n'))],
'bafd83bb': [(log, ('2.8: Banyue Face blend_vb',)),                     (add_section_if_missing, ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'b91ab7b9': [(log, ('2.0 -> 2.8: Banyue BothArms Diffuse [Legacy]',)), (update_hash, ('d6a9d46e',))],
'a2b682d6': [(log, ('2.0 -> 2.8: Banyue BothArms LightMap [Legacy]',)), (update_hash, ('46d2edd3',))],
'd6ac66fa': [(log, ('2.0 -> 2.8: Banyue BothArms MaterialMap [Legacy]',)), (update_hash, ('721a29de',))],
'd70384d8': [(log, ('2.0 -> 2.8: Banyue PalmsBall Diffuse [Legacy]',)), (update_hash, ('3b8e4eda',))],
'1be5d33e': [(log, ('2.0 -> 2.8: PalmsBall LightMap [Legacy]',)), (update_hash, ('4a7ef137',))],
'a0df0d6c': [(log, ('2.0 -> 2.8: PalmsBall MaterialMap [Legacy]',)), (update_hash, ('cc671a53',))],

# === Hair Textures ===
'0a1f42fb': [
        (log,                           ('2.8: Banyue HairA Diffuse Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'81cd7414': [
        (log,                           ('2.8: Banyue HairA LightMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'ef8ba12a': [
        (log,                           ('2.8: Banyue HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'b3b968a5': [
        (log,                           ('2.8: Banyue Body Diffuse Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'19c3125c': [
        (log,                           ('2.8: Banyue BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'cdecf7ef': [
        (log,                           ('2.8: Banyue Body LightMap Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'f44f6316': [
        (log,                           ('2.8: Banyue BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'77d743f8': [
        (log,                           ('2.8: Banyue Body MaterialMap Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'7099d2dc': [
        (log,                           ('2.8: Banyue BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],

# === BothArms Textures (v2.8 Target) ===
'd6a9d46e': [
        (log,                           ('2.8: Banyue BothArms Diffuse Hash',)),
        (add_section_if_missing,        ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],
'46d2edd3': [
        (log,                           ('2.8: Banyue BothArms LightMap Hash',)),
        (add_section_if_missing,        ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],
'721a29de': [
        (log,                           ('2.8: Banyue BothArms MaterialMap Hash',)),
        (add_section_if_missing,        ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],

# === PalmsBall & WeaponBall Shared Textures (v2.8 Target) ===
'3b8e4eda': [
        (log,                           ('2.8: Banyue PalmsBall/WeaponBall Diffuse Hash',)),
        (add_section_if_missing,        ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],
'4a7ef137': [
        (log,                           ('2.8: Banyue PalmsBall/WeaponBall LightMap Hash',)),
        (add_section_if_missing,        ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],
'cc671a53': [
        (log,                           ('2.8: Banyue PalmsBall/WeaponBall MaterialMap Hash',)),
        (add_section_if_missing,        ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],

# === Leg Textures ===
'950ca70a': [
        (log,                           ('2.8: Banyue Legs Diffuse Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
'a75cf25e': [
        (log,                           ('2.8: Banyue LegsA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
'62c9fcaa': [
        (log,                           ('2.8: Banyue Legs LightMap Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
'1003c4df': [
        (log,                           ('2.8: Banyue LegsA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
'8b0fcc7b': [
        (log,                           ('2.8: Banyue Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],
'1125ccff': [
        (log,                           ('2.8: Banyue LegsA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'fc9c6235': [
        (log,                           ('2.8: Banyue Face Diffuse Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'6c0d6d52': [
        (log,                           ('2.8: Banyue Face LightMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'ca2b8ca8': [
        (log,                           ('2.8: Banyue Face MaterialMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Banyue Shared NormalMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Banyue Hair/Legs/Body NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Banyue',
    'element': 'Fire',
    'faction': 'Yunkui Summit',
    'game_versions': ['2.8'],
}