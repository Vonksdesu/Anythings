"""
VivianSummer Character Hash Commands
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
    Returns VivianSummer's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'4108c0da': [(log, ('2.8: VivianSummer Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'3060793b': [(log, ('2.8: VivianSummer Body IB Hash',)),                 (add_ib_check_if_missing,)],
'ec7b047c': [(log, ('2.8: VivianSummer Gem IB Hash',)),                  (add_ib_check_if_missing,)],
'39944f20': [(log, ('2.8: VivianSummer Face IB Hash',)),                 (add_ib_check_if_missing,)],
'b79903af': [(log, ('2.8: VivianSummer Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'4adf1f7a': [(log, ('2.8: VivianSummer Weapon Umbrella Handle IB',)),     (add_ib_check_if_missing,)],
'15c97ffc': [(log, ('2.8: VivianSummer Weapon Umbrella Face IB',)),       (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'713a8587': [(log, ('2.8: VivianSummer Hair draw_vb',)),                 (add_section_if_missing, ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n'))],
'bec9acb0': [(log, ('2.8: VivianSummer Hair position_vb',)),             (add_section_if_missing, ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n'))],
'128d277f': [(log, ('2.8: VivianSummer Hair texcoord_vb',)),             (add_section_if_missing, ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n'))],
'5b569848': [(log, ('2.8: VivianSummer Hair blend_vb',)),                (add_section_if_missing, ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'9898740f': [(log, ('2.8: VivianSummer Hair Shadow draw_vb',)),          (add_section_if_missing, ('b79903af', 'VivianSummer.HairShadow.IB', 'match_priority = 0\n'))],
'bbb7d4b1': [(log, ('2.8: VivianSummer Hair Shadow position_vb',)),      (add_section_if_missing, ('b79903af', 'VivianSummer.HairShadow.IB', 'match_priority = 0\n'))],
'fa9735df': [(log, ('2.8: VivianSummer Hair Shadow texcoord_vb',)),      (add_section_if_missing, ('b79903af', 'VivianSummer.HairShadow.IB', 'match_priority = 0\n'))],
'1853b047': [(log, ('2.8: VivianSummer Hair Shadow blend_vb',)),         (add_section_if_missing, ('b79903af', 'VivianSummer.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'd96480bc': [(log, ('2.8: VivianSummer Body draw_vb',)),                 (add_section_if_missing, ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n'))],
'5e46216b': [(log, ('2.8: VivianSummer Body position_vb',)),             (add_section_if_missing, ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n'))],
'fb44f88a': [(log, ('2.8: VivianSummer Body texcoord_vb',)),             (add_section_if_missing, ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n'))],
'723bccec': [(log, ('2.8: VivianSummer Body blend_vb',)),                (add_section_if_missing, ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n'))],

# Gem
'9829025f': [(log, ('2.8: VivianSummer Gem draw_vb',)),                  (add_section_if_missing, ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n'))],
'3c88ea03': [(log, ('2.8: VivianSummer Gem position_vb',)),              (add_section_if_missing, ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n'))],
'a55d2f46': [(log, ('2.8: VivianSummer Gem texcoord_vb',)),              (add_section_if_missing, ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n'))],
'53a21868': [(log, ('2.8: VivianSummer Gem blend_vb',)),                 (add_section_if_missing, ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n'))],

# Face
'fcf74fc0': [(log, ('2.8: VivianSummer Face VertexLimit Hash',)),        (add_section_if_missing, ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n'))],
'c6e5dc87': [(log, ('2.8: VivianSummer Face position_vb Hash',)),        (add_section_if_missing, ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n'))],
'0afe5a44': [(log, ('2.8: VivianSummer Face texcoord_vb Hash',)),        (add_section_if_missing, ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n'))],
'ef07b6f6': [(log, ('2.8: VivianSummer Face blend_vb Hash',)),           (add_section_if_missing, ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella Handle
'bd5b581e': [(log, ('2.8: VivianSummer Weapon Handle VertexLimit',)),    (add_section_if_missing, ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n'))],
'117996c2': [(log, ('2.8: VivianSummer Weapon Handle position_vb',)),    (add_section_if_missing, ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n'))],
'fa34947b': [(log, ('2.8: VivianSummer Weapon Handle texcoord_vb',)),    (add_section_if_missing, ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n'))],
'ee28f6c2': [(log, ('2.8: VivianSummer Weapon Handle blend_vb',)),       (add_section_if_missing, ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella Face
'7f5aba6c': [(log, ('2.8: VivianSummer Weapon Face VertexLimit',)),      (add_section_if_missing, ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n'))],
'd4bb64cc': [(log, ('2.8: VivianSummer Weapon Face position_vb',)),      (add_section_if_missing, ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n'))],
'bd66871a': [(log, ('2.8: VivianSummer Weapon Face texcoord_vb',)),      (add_section_if_missing, ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n'))],
'431b0b24': [(log, ('2.8: VivianSummer Weapon Face blend_vb',)),         (add_section_if_missing, ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'756ebf6b': [(log, ('2.0 -> 2.8: VivianSummer Weapon Diffuse [Legacy]',)), (update_hash, ('1dbeec1f',))],
'd96fe324': [(log, ('2.0 -> 2.8: VivianSummer Weapon LightMap [Legacy]',)), (update_hash, ('7270dab3',))],
'6af50aef': [(log, ('2.0 -> 2.8: VivianSummer Weapon MaterialMap [Legacy]',)), (update_hash, ('6ecc2389',))],

# === Face Textures ===
'7b262ab6': [
        (log,                           ('2.8: VivianSummer FaceA Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n')),
    ],
'66b5da8e': [
        (log,                           ('2.8: VivianSummer FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('39944f20', 'VivianSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: VivianSummer Shared NormalMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],

# === Hair, BodyC/D, Gem Shared Textures ===
'15dcce65': [
        (log,                           ('2.8: VivianSummer HairA, BodyC, BodyD, GemA Diffuse Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'427be7bd': [
        (log,                           ('2.8: VivianSummer Hair Diffuse Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: VivianSummer HairA, BodyA, GemA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'8a82d289': [
        (log,                           ('2.8: VivianSummer HairA, BodyC, BodyD, GemA LightMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'45b67c0b': [
        (log,                           ('2.8: VivianSummer Hair LightMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'c23ddbea': [
        (log,                           ('2.8: VivianSummer HairA, BodyC, BodyD, GemA MaterialMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianSummer.Gem.IB', 'match_priority = 0\n')),
    ],
'cdb06288': [
        (log,                           ('2.8: VivianSummer Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# === Hair Shared with Base Vivian ===
'a84d933f': [
        (log,                           ('2.8: VivianSummer HairB, HairC Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'2df6f7b5': [
        (log,                           ('2.8: VivianSummer Hair Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'8e3a20ea': [
        (log,                           ('2.8: VivianSummer HairB, HairC LightMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'36b80366': [
        (log,                           ('2.8: VivianSummer Hair LightMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'2af66072': [
        (log,                           ('2.8: VivianSummer HairB, HairC MaterialMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'2d5b1412': [
        (log,                           ('2.8: VivianSummer Hair MaterialMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'136b3e29': [
        (log,                           ('2.8: VivianSummer BodyA, BodyB Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'1ea05046': [
        (log,                           ('2.8: VivianSummer Body Diffuse Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'69a6a15f': [
        (log,                           ('2.8: VivianSummer BodyA, BodyB LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'e8bb6a0f': [
        (log,                           ('2.8: VivianSummer Body LightMap Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'527c3676': [
        (log,                           ('2.8: VivianSummer BodyA, BodyB MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],
'909ea74d': [
        (log,                           ('2.8: VivianSummer Body MaterialMap Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'1dbeec1f': [
        (log,                           ('2.8: VivianSummer Weapon Umbrella Diffuse Hash',)),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],
'7270dab3': [
        (log,                           ('2.8: VivianSummer Weapon Umbrella LightMap Hash',)),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],
'6ecc2389': [
        (log,                           ('2.8: VivianSummer Weapon Umbrella MaterialMap Hash',)),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],

# === Weapon Shared Textures ===
'bf6a1304': [
        (log,                           ('2.8: VivianSummer Weapon Umbrella/Sword Diffuse Hash',)),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],
'a33edccd': [
        (log,                           ('2.8: VivianSummer Weapon Umbrella/Sword LightMap Hash',)),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],
'ab4cde14': [
        (log,                           ('2.8: VivianSummer Weapon Umbrella/Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('4adf1f7a', 'VivianSummer.WeaponHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('15c97ffc', 'VivianSummer.WeaponFace.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'VivianSummer',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}