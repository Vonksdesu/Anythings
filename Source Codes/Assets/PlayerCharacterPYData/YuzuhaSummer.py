"""
YuzuhaSummer Character Hash Commands
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
    Returns YuzuhaSummer's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'7a504287': [(log, ('2.8: YuzuhaSummer Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'b298482d': [(log, ('2.8: YuzuhaSummer Body IB Hash',)),                 (add_ib_check_if_missing,)],
'a8de520e': [(log, ('2.8: YuzuhaSummer Accessories IB Hash',)),          (add_ib_check_if_missing,)],
'14ac0d52': [(log, ('2.8: YuzuhaSummer Kama IB Hash',)),                 (add_ib_check_if_missing,)],
'507384ea': [(log, ('2.8: YuzuhaSummer Face IB Hash',)),                 (add_ib_check_if_missing,)],
'afb6117a': [(log, ('2.8: YuzuhaSummer Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'b34a880c': [(log, ('2.8: YuzuhaSummer Weapon Umbrella IB Hash',)),      (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'630debc9': [(log, ('2.8: YuzuhaSummer Hair draw_vb',)),                 (add_section_if_missing, ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n'))],
'051f9657': [(log, ('2.8: YuzuhaSummer Hair position_vb',)),             (add_section_if_missing, ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n'))],
'dc2821dc': [(log, ('2.8: YuzuhaSummer Hair texcoord_vb',)),             (add_section_if_missing, ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n'))],
'606c88ae': [(log, ('2.8: YuzuhaSummer Hair blend_vb',)),                (add_section_if_missing, ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'8a540628': [(log, ('2.8: YuzuhaSummer Hair Shadow draw_vb',)),          (add_section_if_missing, ('afb6117a', 'YuzuhaSummer.HairShadow.IB', 'match_priority = 0\n'))],
'3a4533fc': [(log, ('2.8: YuzuhaSummer Hair Shadow position_vb',)),      (add_section_if_missing, ('afb6117a', 'YuzuhaSummer.HairShadow.IB', 'match_priority = 0\n'))],
'a39c4806': [(log, ('2.8: YuzuhaSummer Hair Shadow texcoord_vb',)),      (add_section_if_missing, ('afb6117a', 'YuzuhaSummer.HairShadow.IB', 'match_priority = 0\n'))],
'9fc9b6f8': [(log, ('2.8: YuzuhaSummer Hair Shadow blend_vb',)),         (add_section_if_missing, ('afb6117a', 'YuzuhaSummer.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'07437c27': [(log, ('2.8: YuzuhaSummer Body draw_vb',)),                 (add_section_if_missing, ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n'))],
'2a7b9144': [(log, ('2.8: YuzuhaSummer Body position_vb',)),             (add_section_if_missing, ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n'))],
'0c9062c5': [(log, ('2.8: YuzuhaSummer Body texcoord_vb',)),             (add_section_if_missing, ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n'))],
'523cf99d': [(log, ('2.8: YuzuhaSummer Body blend_vb',)),                (add_section_if_missing, ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n'))],

# Accessories
'ca3209f7': [(log, ('2.8: YuzuhaSummer Accessories draw_vb Hash',)),      (add_section_if_missing, ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n'))],
'f271d524': [(log, ('2.8: YuzuhaSummer Accessories position_vb Hash',)),  (add_section_if_missing, ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n'))],
'ce14b4b7': [(log, ('2.8: YuzuhaSummer Accessories texcoord_vb Hash',)),  (add_section_if_missing, ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n'))],
'294d341c': [(log, ('2.8: YuzuhaSummer Accessories blend_vb Hash',)),     (add_section_if_missing, ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n'))],

# Kama / LeopardCat1
'b6e62152': [(log, ('2.8: YuzuhaSummer Kama draw_vb Hash',)),            (add_section_if_missing, ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n'))],
'9d4425e5': [(log, ('2.8: YuzuhaSummer Kama position_vb Hash',)),        (add_section_if_missing, ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n'))],
'a7394f34': [(log, ('2.8: YuzuhaSummer Kama texcoord_vb Hash',)),        (add_section_if_missing, ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n'))],
'2a45c137': [(log, ('2.8: YuzuhaSummer Kama blend_vb Hash',)),           (add_section_if_missing, ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n'))],

# Face
'3578d11c': [(log, ('2.8: YuzuhaSummer Face VertexLimit Hash',)),        (add_section_if_missing, ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n'))],
'0f6a425b': [(log, ('2.8: YuzuhaSummer Face position_vb Hash',)),        (add_section_if_missing, ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n'))],
'9d0f7ef5': [(log, ('2.8: YuzuhaSummer Face position_vb Hash',)),        (add_section_if_missing, ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n'))],
'52400cce': [(log, ('2.8: YuzuhaSummer Face blend_vb Hash',)),           (add_section_if_missing, ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella
'b36355ab': [(log, ('2.8: YuzuhaSummer Weapon Umbrella draw_vb Hash',)), (add_section_if_missing, ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n'))],
'79849b37': [(log, ('2.8: YuzuhaSummer Weapon Umbrella position_vb',)),  (add_section_if_missing, ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n'))],
'd5283f28': [(log, ('2.8: YuzuhaSummer Weapon Umbrella texcoord_vb',)),  (add_section_if_missing, ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n'))],
'd7204982': [(log, ('2.8: YuzuhaSummer Weapon Umbrella blend_vb',)),     (add_section_if_missing, ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'c8cb308c': [(log, ('2.0 -> 2.8: YuzuhaSummer Weapon Umbrella Diffuse [Legacy]',)), (update_hash, ('caeee529',))],
'dc683116': [(log, ('2.0 -> 2.8: YuzuhaSummer Weapon Umbrella LightMap [Legacy]',)), (update_hash, ('f74f81e8',))],
'114dafdf': [(log, ('2.0 -> 2.8: YuzuhaSummer Weapon Umbrella MaterialMap [Legacy]',)), (update_hash, ('6657efd2',))],

# === Face Textures ===
'59f9e66f': [
        (log,                           ('2.8: YuzuhaSummer Face Diffuse Hash',)),
        (add_section_if_missing,        ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n')),
    ],
'd394bc13': [
        (log,                           ('2.8: YuzuhaSummer FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('507384ea', 'YuzuhaSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'c9115930': [
        (log,                           ('2.8: YuzuhaSummer Hair Diffuse Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'521a3242': [
        (log,                           ('2.8: YuzuhaSummer Hair Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'a9730519': [
        (log,                           ('2.8: YuzuhaSummer Hair LightMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'c400f5b7': [
        (log,                           ('2.8: YuzuhaSummer Hair LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'4f5639e2': [
        (log,                           ('2.8: YuzuhaSummer Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'3f70d124': [
        (log,                           ('2.8: YuzuhaSummer Hair MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body & Kama Textures ===
'7fc53810': [
        (log,                           ('2.8: YuzuhaSummer Body Diffuse Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'4f4c2b65': [
        (log,                           ('2.8: YuzuhaSummer Body/Kama Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'ac06a4c8': [
        (log,                           ('2.8: YuzuhaSummer Body LightMap Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'c3e64779': [
        (log,                           ('2.8: YuzuhaSummer Body/Kama LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'58fd94ec': [
        (log,                           ('2.8: YuzuhaSummer Body MaterialMap Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
'ac2f3dcb': [
        (log,                           ('2.8: YuzuhaSummer Body/Kama MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],

# === Accessories Textures ===
'9f387d35': [
        (log,                           ('2.8: YuzuhaSummer Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'54591ef6': [
        (log,                           ('2.8: YuzuhaSummer Accessories Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'00bcfe90': [
        (log,                           ('2.8: YuzuhaSummer Accessories LightMap Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'a78340ed': [
        (log,                           ('2.8: YuzuhaSummer Accessories LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'c2c76575': [
        (log,                           ('2.8: YuzuhaSummer Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],
'1d0dabdb': [
        (log,                           ('2.8: YuzuhaSummer Accessories MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'caeee529': [
        (log,                           ('2.8: YuzuhaSummer Weapon Umbrella Diffuse Hash',)),
        (add_section_if_missing,        ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],
'f74f81e8': [
        (log,                           ('2.8: YuzuhaSummer Weapon Umbrella LightMap Hash',)),
        (add_section_if_missing,        ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],
'6657efd2': [
        (log,                           ('2.8: YuzuhaSummer Weapon Umbrella MaterialMap Hash',)),
        (add_section_if_missing,        ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: YuzuhaSummer Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('afb6117a', 'YuzuhaSummer.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b34a880c', 'YuzuhaSummer.WeaponUmbrella.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: YuzuhaSummer Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b298482d', 'YuzuhaSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaSummer.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaSummer.Kama.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YuzuhaSummer',
    'game_versions': ['2.8', '3.0'],
}