"""
Nanyu Character Hash Commands
ZZZ Mod Fixer v2.8
Auto-generated from database mapping
Pembaruan Database 2.8 oleh AI & Komunitas
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Nanyu's hash commands dictionary.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
# === IB Hashes ===
'969152d4': [(log, ('2.8: Nanyu Hair IB Hash',)),         (add_ib_check_if_missing,)],
'17438fa9': [(log, ('2.8: Nanyu HairShadow IB Hash',)),   (add_ib_check_if_missing,)],
'cd884c0a': [(log, ('2.8: Nanyu Headband IB Hash',)),     (add_ib_check_if_missing,)],
'3b4190ce': [(log, ('2.8: Nanyu Wing IB Hash',)),         (add_ib_check_if_missing,)],
'4586e530': [(log, ('2.8: Nanyu Body IB Hash',)),         (add_ib_check_if_missing,)],
'ba598cf9': [(log, ('2.8: Nanyu Eyebrow IB Hash',)),      (add_ib_check_if_missing,)],
'd643e19a': [(log, ('2.8: Nanyu Face IB Hash',)),         (add_ib_check_if_missing,)],
'dcd7242e': [(log, ('2.8: Nanyu Weapon IB Hash',)),       (add_ib_check_if_missing,)],

# === Hash update 2.7 -> 2.8: Nanyu Headband/Wing/Body Diffuse ===
'fe06152c': [(log, ('2.7 -> 2.8: Nanyu Headband, Wing, Body Diffuse Hash',)), (update_hash, ('dc41fbbf',))],

# === Face & Eyebrow Textures ===
'b6e87aef': [
        (log,                           ('2.8: Nanyu FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('d643e19a', 'Nanyu.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba598cf9', 'Nanyu.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'd2e23730': [
        (log,                           ('2.8: Nanyu HairA Diffuse Hash',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],
'e3573bc8': [
        (log,                           ('2.8: Nanyu HairA LightMap Hash',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],
'687f57b8': [
        (log,                           ('2.8: Nanyu HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],

# === Headband, Wing & Body Shared Textures ===
'dc41fbbf': [
        (log,                           ('2.8: Nanyu Headband, Wing, Body Diffuse Hash',)),
        (add_section_if_missing,        ('cd884c0a', 'Nanyu.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3b4190ce', 'Nanyu.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4586e530', 'Nanyu.Body.IB', 'match_priority = 0\n')),
    ],
'ab51539c': [
        (log,                           ('2.8: Nanyu Headband, Wing, Body LightMap Hash',)),
        (add_section_if_missing,        ('cd884c0a', 'Nanyu.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3b4190ce', 'Nanyu.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4586e530', 'Nanyu.Body.IB', 'match_priority = 0\n')),
    ],
'958e389e': [
        (log,                           ('2.8: Nanyu Headband, Wing, Body MaterialMap Hash',)),
        (add_section_if_missing,        ('cd884c0a', 'Nanyu.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3b4190ce', 'Nanyu.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4586e530', 'Nanyu.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures ===
'84246d50': [
        (log,                           ('2.8: Nanyu WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('dcd7242e', 'Nanyu.Weapon.IB', 'match_priority = 0\n')),
    ],
'fcc325af': [
        (log,                           ('2.8: Nanyu WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('dcd7242e', 'Nanyu.Weapon.IB', 'match_priority = 0\n')),
    ],
'a64be703': [
        (log,                           ('2.8: Nanyu WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('dcd7242e', 'Nanyu.Weapon.IB', 'match_priority = 0\n')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# Hair VBs
'536345c3': [(log, ('2.8: Nanyu Hair draw_vb',))],
'd1a15d0e': [(log, ('2.8: Nanyu Hair position_vb',))],
'e67f6a3c': [(log, ('2.8: Nanyu Hair texcoord_vb',))],
'56699a62': [(log, ('2.8: Nanyu Hair blend_vb',))],

# Headband VBs
'5aac7571': [(log, ('2.8: Nanyu Headband draw_vb',))],
'74cbadea': [(log, ('2.8: Nanyu Headband position_vb',))],
'00cbd7a8': [(log, ('2.8: Nanyu Headband texcoord_vb',))],
'82509f4f': [(log, ('2.8: Nanyu Headband blend_vb',))],

# Wing VBs
'6ab572d9': [(log, ('2.8: Nanyu Wing draw_vb',))],
'b90d042a': [(log, ('2.8: Nanyu Wing position_vb',))],
'e062b6fc': [(log, ('2.8: Nanyu Wing texcoord_vb',))],
'4d677fbd': [(log, ('2.8: Nanyu Wing blend_vb',))],

# Body VBs
'5b0185fc': [(log, ('2.8: Nanyu Body draw_vb',))],
'd4908293': [(log, ('2.8: Nanyu Body position_vb',))],
'5ebf2446': [(log, ('2.8: Nanyu Body texcoord_vb',))],
'f43a1dba': [(log, ('2.8: Nanyu Body blend_vb',))],

# Face VBs
'd70f65c1': [(log, ('2.8: Nanyu Face draw_vb',))],
'ed1df686': [(log, ('2.8: Nanyu Face position_vb',))],
'45910aef': [(log, ('2.8: Nanyu Face texcoord_vb',))],
'93c1ec0c': [(log, ('2.8: Nanyu Face blend_vb',))],

# Shared NormalMap
'798adba3': [
        (log,                           ('2.8: Nanyu Shared NormalMap Hash',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cd884c0a', 'Nanyu.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3b4190ce', 'Nanyu.Wing.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Nanyu hashes ===
'11254966': [
        (log,                           ('2.8: Nanyu Headband Diffuse Hash [New]',)),
        (add_section_if_missing,        ('cd884c0a', 'Nanyu.Headband.IB', 'match_priority = 0\n')),
    ],
'1fd77103': [
        (log,                           ('2.8: Nanyu Eyebrow Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ba598cf9', 'Nanyu.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'5e50a4f2': [
        (log,                           ('2.8: Nanyu Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        ('dcd7242e', 'Nanyu.Weapon.IB', 'match_priority = 0\n')),
    ],
'766f3fca': [
        (log,                           ('2.8: Nanyu Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('dcd7242e', 'Nanyu.Weapon.IB', 'match_priority = 0\n')),
    ],
'a458a615': [
        (log,                           ('2.8: Nanyu Hair MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],
'acea6f2f': [
        (log,                           ('2.8: Nanyu Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        ('dcd7242e', 'Nanyu.Weapon.IB', 'match_priority = 0\n')),
    ],
'beb11b78': [
        (log,                           ('2.8: Nanyu Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('4586e530', 'Nanyu.Body.IB', 'match_priority = 0\n')),
    ],
'd94a0c41': [
        (log,                           ('2.8: Nanyu Hair LightMap Hash [New]',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],
'df39b77c': [
        (log,                           ('2.8: Nanyu Hair Diffuse Hash [New]',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Nanyu Shared NormalMap [New]',)),
        (add_section_if_missing,        ('969152d4', 'Nanyu.Hair.IB', 'match_priority = 0\n')),
    ],
'fee3d533': [
        (log,                           ('2.8: Nanyu Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('4586e530', 'Nanyu.Body.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Nanyu',
    'game_versions': ['2.8'],
}