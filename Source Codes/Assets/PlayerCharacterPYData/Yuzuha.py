"""
Yuzuha Character Hash Commands
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
    Returns Yuzuha's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'7a504287': [(log, ('2.8: Yuzuha Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'5144c409': [(log, ('2.8: Yuzuha Body IB Hash',)),                      (add_ib_check_if_missing,)],
'73757570': [(log, ('2.8: Yuzuha Legs IB Hash',)),                      (add_ib_check_if_missing,)],
'e72984d1': [(log, ('2.8: Yuzuha Kama IB Hash',)),                      (add_ib_check_if_missing,)],
'507384ea': [(log, ('2.8: Yuzuha Face IB Hash',)),                      (add_ib_check_if_missing,)],
'afb6117a': [(log, ('2.8: Yuzuha Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'81bca595': [(log, ('2.8: Yuzuha LeopardCat2 IB Hash',)),               (add_ib_check_if_missing,)],
'cf3172e4': [(log, ('2.8: Yuzuha Straps IB Hash',)),                    (add_ib_check_if_missing,)],
'2686f517': [(log, ('2.8: Yuzuha Weapon Umbrella IB Hash',)),           (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'630debc9': [(log, ('2.8: Yuzuha Hair draw_vb',)),                      (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n'))],
'051f9657': [(log, ('2.8: Yuzuha Hair position_vb',)),                  (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n'))],
'dc2821dc': [(log, ('2.8: Yuzuha Hair texcoord_vb',)),                  (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n'))],
'606c88ae': [(log, ('2.8: Yuzuha Hair blend_vb',)),                     (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'8a540628': [(log, ('2.8: Yuzuha Hair Shadow draw_vb',)),               (add_section_if_missing, ('afb6117a', 'Yuzuha.HairShadow.IB', 'match_priority = 0\n'))],
'3a4533fc': [(log, ('2.8: Yuzuha Hair Shadow position_vb',)),           (add_section_if_missing, ('afb6117a', 'Yuzuha.HairShadow.IB', 'match_priority = 0\n'))],
'a39c4806': [(log, ('2.8: Yuzuha Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('afb6117a', 'Yuzuha.HairShadow.IB', 'match_priority = 0\n'))],
'9fc9b6f8': [(log, ('2.8: Yuzuha Hair Shadow blend_vb',)),              (add_section_if_missing, ('afb6117a', 'Yuzuha.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'2a99e69b': [(log, ('2.8: Yuzuha Body draw_vb',)),                      (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n'))],
'20d44382': [(log, ('2.8: Yuzuha Body position_vb',)),                  (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n'))],
'688588f1': [(log, ('2.8: Yuzuha Body texcoord_vb',)),                  (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n'))],
'0db66603': [(log, ('2.8: Yuzuha Body blend_vb',)),                     (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n'))],

# Legs
'93b3c078': [(log, ('2.8: Yuzuha Legs draw_vb',)),                      (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n'))],
'bc6a9f6f': [(log, ('2.8: Yuzuha Legs position_vb',)),                  (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n'))],
'882cf302': [(log, ('2.8: Yuzuha Legs texcoord_vb',)),                  (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n'))],
'6fe5c40e': [(log, ('2.8: Yuzuha Legs blend_vb',)),                     (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n'))],

# LeopardCat1
'1a6468e1': [(log, ('2.8: Yuzuha LeopardCat1 VertexLimit Hash',)),      (add_section_if_missing, ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n'))],
'773bdaa3': [(log, ('2.8: Yuzuha LeopardCat1 position_vb Hash',)),      (add_section_if_missing, ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n'))],
'a5097f50': [(log, ('2.8: Yuzuha LeopardCat1 texcoord_vb Hash',)),      (add_section_if_missing, ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n'))],
'085ab253': [(log, ('2.8: Yuzuha LeopardCat1 blend_vb Hash',)),         (add_section_if_missing, ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n'))],

# LeopardCat2
'39b6000b': [(log, ('2.8: Yuzuha LeopardCat2 draw_vb Hash',)),           (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n'))],
'9662128e': [(log, ('2.8: Yuzuha LeopardCat2 position_vb Hash',)),       (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n'))],
'f95d8b57': [(log, ('2.8: Yuzuha LeopardCat2 texcoord_vb Hash',)),       (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n'))],
'ba80c02b': [(log, ('2.8: Yuzuha LeopardCat2 blend_vb Hash',)),          (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n'))],

# Straps
'966e777b': [(log, ('2.8: Yuzuha Straps draw_vb Hash',)),                (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n'))],
'b543b8d8': [(log, ('2.8: Yuzuha Straps position_vb Hash',)),            (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n'))],
'4b13802b': [(log, ('2.8: Yuzuha Straps texcoord_vb Hash',)),            (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n'))],
'7ca97675': [(log, ('2.8: Yuzuha Straps blend_vb Hash',)),               (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n'))],

# Face
'3578d11c': [(log, ('2.8: Yuzuha Face VertexLimit Hash',)),              (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n'))],
'0f6a425b': [(log, ('2.8: Yuzuha Face position_vb Hash',)),              (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n'))],
'9d0f7ef5': [(log, ('2.8: Yuzuha Face texcoord_vb Hash',)),              (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n'))],
'52400cce': [(log, ('2.8: Yuzuha Face blend_vb Hash',)),                 (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella
'79c257b3': [(log, ('2.8: Yuzuha Weapon Umbrella VertexLimit Hash',)),   (add_section_if_missing, ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n'))],
'1686ac84': [(log, ('2.8: Yuzuha Weapon Umbrella position_vb Hash',)),   (add_section_if_missing, ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n'))],
'8a182e58': [(log, ('2.8: Yuzuha Weapon Umbrella texcoord_vb Hash',)),   (add_section_if_missing, ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n'))],
'7d11ecaa': [(log, ('2.8: Yuzuha Weapon Umbrella blend_vb Hash',)),      (add_section_if_missing, ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'68856c57': [(log, ('2.0 -> 2.8: Yuzuha Weapon Umbrella Diffuse [Legacy]',)), (update_hash, ('7139e5b0',))],
'4fe5c926': [(log, ('2.0 -> 2.8: Yuzuha Weapon Umbrella LightMap [Legacy]',)), (update_hash, ('9dcd6e8e',))],
'd0c14d9d': [(log, ('2.0 -> 2.8: Yuzuha Weapon Umbrella MaterialMap [Legacy]',)), (update_hash, ('85142f08',))],

# === Face Textures ===
'59f9e66f': [
        (log,                           ('2.8: Yuzuha Face Diffuse Hash',)),
        (add_section_if_missing,        ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
    ],
'd394bc13': [
        (log,                           ('2.8: Yuzuha FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair & Legs Shared Textures ===
'c9115930': [
        (log,                           ('2.8: Yuzuha Hair, Legs Diffuse Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'521a3242': [
        (log,                           ('2.8: Yuzuha Hair/Legs Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'a9730519': [
        (log,                           ('2.8: Yuzuha Hair, Legs LightMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'c400f5b7': [
        (log,                           ('2.8: Yuzuha Hair/Legs LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'4f5639e2': [
        (log,                           ('2.8: Yuzuha Hair, Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'3f70d124': [
        (log,                           ('2.8: Yuzuha Hair/Legs MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],

# === Body, Kama, LeopardCat & Straps Shared Textures ===
'1fabf669': [
        (log,                           ('2.8: Yuzuha Body, Kama, LeopardCat, Straps Diffuse Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'be85f061': [
        (log,                           ('2.8: Yuzuha Body/Kama Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
'eff3b0b0': [
        (log,                           ('2.8: Yuzuha Body, Kama, LeopardCat, Straps LightMap Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'ef192425': [
        (log,                           ('2.8: Yuzuha Body/Kama LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
'2fb36ecb': [
        (log,                           ('2.8: Yuzuha Body, Kama, LeopardCat, Straps MaterialMap Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'76e5c6b7': [
        (log,                           ('2.8: Yuzuha Body/Kama MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'7139e5b0': [
        (log,                           ('2.8: Yuzuha Weapon Umbrella Diffuse Hash',)),
        (add_section_if_missing,        ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],
'9dcd6e8e': [
        (log,                           ('2.8: Yuzuha Weapon Umbrella LightMap Hash',)),
        (add_section_if_missing,        ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],
'85142f08': [
        (log,                           ('2.8: Yuzuha Weapon Umbrella MaterialMap Hash',)),
        (add_section_if_missing,        ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: Yuzuha Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('afb6117a', 'Yuzuha.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2686f517', 'Yuzuha.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Yuzuha Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yuzuha',
    'game_versions': ['2.8', '3.0'],
}