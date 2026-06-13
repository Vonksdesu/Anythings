"""
NicoleCutie Character Hash Commands
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
    Returns NicoleCutie's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'776f5703': [(log, ('2.8: NicoleCutie Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'52842f31': [(log, ('2.8: NicoleCutie Body IB Hash',)),                 (add_ib_check_if_missing,)],
'262c96ff': [(log, ('2.8: NicoleCutie Phone IB Hash',)),                 (add_ib_check_if_missing,)],
'40e64ae2': [(log, ('2.8: NicoleCutie Amillion IB Hash',)),              (add_ib_check_if_missing,)],
'7435fc0e': [(log, ('2.8: NicoleCutie Face IB Hash',)),                 (add_ib_check_if_missing,)],
'4ed9a81f': [(log, ('2.8: NicoleCutie Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'f9befc51': [(log, ('2.8: NicoleCutie Weapon IB Hash',)),                (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'bafa609a': [(log, ('2.8: NicoleCutie Hair draw_vb',)),                 (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n'))],
'7b4b4f06': [(log, ('2.8: NicoleCutie Hair position_vb',)),             (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n'))],
'a09489fa': [(log, ('2.8: NicoleCutie Hair texcoord_vb',)),             (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n'))],
'0df63fc6': [(log, ('2.8: NicoleCutie Hair blend_vb',)),                (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'4d61e6f3': [(log, ('2.8: NicoleCutie Hair Shadow draw_vb',)),          (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.HairShadow.IB', 'match_priority = 0\n'))],
'b408b261': [(log, ('2.8: NicoleCutie Hair Shadow position_vb',)),      (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.HairShadow.IB', 'match_priority = 0\n'))],
'879a6522': [(log, ('2.8: NicoleCutie Hair Shadow texcoord_vb',)),      (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.HairShadow.IB', 'match_priority = 0\n'))],
'720296ff': [(log, ('2.8: NicoleCutie Hair Shadow blend_vb',)),         (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'4151c6c6': [(log, ('2.8: NicoleCutie Body draw_vb',)),                 (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n'))],
'dfab3761': [(log, ('2.8: NicoleCutie Body position_vb',)),             (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n'))],
'fa58977c': [(log, ('2.8: NicoleCutie Body texcoord_vb',)),             (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n'))],
'f9fb2aa0': [(log, ('2.8: NicoleCutie Body blend_vb',)),                (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n'))],

# Amillion
'bb7fffe9': [(log, ('2.8: NicoleCutie Amillion draw_vb',)),              (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n'))],
'176bf3d7': [(log, ('2.8: NicoleCutie Amillion position_vb',)),          (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n'))],
'077c3500': [(log, ('2.8: NicoleCutie Amillion texcoord_vb',)),          (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n'))],
'e1d9c9a8': [(log, ('2.8: NicoleCutie Amillion blend_vb [Legacy]',)),    (update_hash, ('4e1d9c9a',))],
'4e1d9c9a': [(log, ('2.8: NicoleCutie Amillion blend_vb',)),             (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n'))],

# Face
'9274e401': [(log, ('2.8: NicoleCutie Face draw_vb',)),                 (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n'))],
'a8667746': [(log, ('2.8: NicoleCutie Face position_vb',)),             (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n'))],
'5714e5e6': [(log, ('2.8: NicoleCutie Face texcoord_vb',)),             (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n'))],
'b25ebcf6': [(log, ('2.8: NicoleCutie Face blend_vb',)),                (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n'))],

# Weapon
'f6325378': [(log, ('2.8: NicoleCutie Weapon draw_vb',)),               (add_section_if_missing, ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n'))],
'00c8b3c5': [(log, ('2.8: NicoleCutie Weapon position_vb',)),           (add_section_if_missing, ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n'))],
'14b0d6b6': [(log, ('2.8: NicoleCutie Weapon texcoord_vb',)),           (add_section_if_missing, ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n'))],
'2f427bdb': [(log, ('2.8: NicoleCutie Weapon blend_vb',)),              (add_section_if_missing, ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n'))],

# Mobile Phone
'63d1bd6f': [(log, ('2.8: NicoleCutie Phone draw_vb',)),                 (add_section_if_missing, ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n'))],
'ef68beba': [(log, ('2.8: NicoleCutie Phone position_vb',)),             (add_section_if_missing, ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n'))],
'8424f0ec': [(log, ('2.8: NicoleCutie Phone texcoord_vb',)),             (add_section_if_missing, ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n'))],
'cbce3456': [(log, ('2.8: NicoleCutie Phone blend_vb',)),                (add_section_if_missing, ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'33fdeb6d': [
        (log,                           ('2.8: NicoleCutie Face Diffuse Hash',)),
        (add_section_if_missing,        ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'd1e84a34': [
        (log,                           ('2.8: NicoleCutie FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'cdaa9ab5': [
        (log,                           ('2.8: NicoleCutie HairA Diffuse Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'0e55f39d': [
        (log,                           ('2.8: NicoleCutie Hair Diffuse Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'4c8b0bce': [
        (log,                           ('2.8: NicoleCutie HairA LightMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'b3ef7388': [
        (log,                           ('2.8: NicoleCutie Hair LightMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'a05c2386': [
        (log,                           ('2.8: NicoleCutie HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body & Amillion Shared Textures ===
'4af0010c': [
        (log,                           ('2.8: NicoleCutie BodyA, AmillionA Diffuse Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'b2bd144b': [
        (log,                           ('2.8: NicoleCutie Body Diffuse Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'c45a93a3': [
        (log,                           ('2.8: NicoleCutie BodyA, AmillionA LightMap Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'5fcde3a6': [
        (log,                           ('2.8: NicoleCutie Body LightMap Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'592cee08': [
        (log,                           ('2.8: NicoleCutie BodyA, AmillionA MaterialMap Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'76774ee7': [
        (log,                           ('2.8: NicoleCutie Body MaterialMap Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],

# === Phone Textures ===
'6986beb1': [
        (log,                           ('2.8: NicoleCutie PhoneA Diffuse Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'd484bf22': [
        (log,                           ('2.8: NicoleCutie Phone Diffuse Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'4ae94b82': [
        (log,                           ('2.8: NicoleCutie PhoneA LightMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'8d3aca36': [
        (log,                           ('2.8: NicoleCutie Phone LightMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'4bbaadb9': [
        (log,                           ('2.8: NicoleCutie PhoneA MaterialMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'f8db9ea5': [
        (log,                           ('2.8: NicoleCutie Phone MaterialMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures ===
'89699adb': [
        (log,                           ('2.8: NicoleCutie Weapon Diffuse Hash 1',)),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
    ],
'b6f0f975': [
        (log,                           ('2.8: NicoleCutie Weapon Diffuse Hash 2',)),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
    ],
'b89dc4e4': [
        (log,                           ('2.8: NicoleCutie Weapon LightMap Hash 1',)),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
    ],
'df7b84ed': [
        (log,                           ('2.8: NicoleCutie Weapon LightMap Hash 2',)),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
    ],
'48f45547': [
        (log,                           ('2.8: NicoleCutie Weapon MaterialMap Hash 1',)),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
    ],
'5c298267': [
        (log,                           ('2.8: NicoleCutie Weapon MaterialMap Hash 2',)),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
    ],

# === NicoleSkin Weapon Texture Updates ===
'028c6ebf': [(log, ('2.8: NicoleCutie Weapon MaterialMap 2 [Legacy]',)),   (update_hash, ('5c298267',))],
'28d0438d': [(log, ('2.8: NicoleCutie Weapon LightMap 1 [Legacy]',)),       (update_hash, ('b89dc4e4',))],
'67f0bd9c': [(log, ('2.8: NicoleCutie Weapon Diffuse 1 [Legacy]',)),        (update_hash, ('89699adb',))],
'7672fb0c': [(log, ('2.8: NicoleCutie Weapon Diffuse 2 [Legacy]',)),        (update_hash, ('b6f0f975',))],
'c03d03de': [(log, ('2.8: NicoleCutie Weapon LightMap 2 [Legacy]',)),       (update_hash, ('df7b84ed',))],
'f1304abf': [(log, ('2.8: NicoleCutie Weapon MaterialMap 1 [Legacy]',)),   (update_hash, ('48f45547',))],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: NicoleCutie Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f9befc51', 'NicoleCutie.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4ed9a81f', 'NicoleCutie.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: NicoleCutie HairA, BodyA, PhoneA, AmillionA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NicoleCutie',
    'game_versions': ['2.8'],
}