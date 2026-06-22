"""
NangongYuRhapsodyMuse Character Hash Commands
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
    Returns NangongYuRhapsodyMuse's hash commands dictionary.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
# === IB Hashes ===
'969152d4': [(log, ('2.8: NangongYuRhapsodyMuse Hair IB Hash',)),        (add_ib_check_if_missing,)],
'17438fa9': [(log, ('2.8: NangongYuRhapsodyMuse HairShadow IB Hash',)),  (add_ib_check_if_missing,)],
'cd884c0a': [(log, ('2.8: NangongYuRhapsodyMuse Headband IB Hash',)),    (add_ib_check_if_missing,)],
'5b186a44': [(log, ('2.8: NangongYuRhapsodyMuse Wing IB Hash',)),        (add_ib_check_if_missing,)],
'5f2741ff': [(log, ('2.8: NangongYuRhapsodyMuse Body IB Hash',)),        (add_ib_check_if_missing,)],
'ba598cf9': [(log, ('2.8: NangongYuRhapsodyMuse Eyebrow IB Hash',)),     (add_ib_check_if_missing,)],
'd643e19a': [(log, ('2.8: NangongYuRhapsodyMuse Face IB Hash',)),        (add_ib_check_if_missing,)],
'dcd7242e': [(log, ('2.8: NangongYuRhapsodyMuse Weapon IB Hash',)),      (add_ib_check_if_missing,)],

# === Face & Eyebrow Textures (shared with Nanyu base) ===
'b6e87aef': [
        (log,                           ('2.8: NangongYuRhapsodyMuse FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba598cf9', 'NangongYuRhapsodyMuse.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures (Diffuse berbeda dari base) ===
'4fa2f495': [
        (log,                           ('2.8: NangongYuRhapsodyMuse HairA Diffuse Hash',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'e3573bc8': [
        (log,                           ('2.8: NangongYuRhapsodyMuse HairA LightMap Hash',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'687f57b8': [
        (log,                           ('2.8: NangongYuRhapsodyMuse HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],

# === Headband, Wing & Body Skin Textures ===
'263aba53': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Headband, Wing, Body Diffuse Hash',)),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5b186a44', 'NangongYuRhapsodyMuse.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],
'79423b33': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Headband, Wing, Body LightMap Hash',)),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5b186a44', 'NangongYuRhapsodyMuse.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],
'1786d968': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Headband, Wing, Body MaterialMap Hash',)),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5b186a44', 'NangongYuRhapsodyMuse.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (Diffuse berbeda dari base) ===
'08ff63ac': [
        (log,                           ('2.8: NangongYuRhapsodyMuse WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'fcc325af': [
        (log,                           ('2.8: NangongYuRhapsodyMuse WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'a64be703': [
        (log,                           ('2.8: NangongYuRhapsodyMuse WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# Hair VBs
'536345c3': [(log, ('2.8: NangongYuRhapsodyMuse Hair draw_vb',))],
'd1a15d0e': [(log, ('2.8: NangongYuRhapsodyMuse Hair position_vb',))],
'e67f6a3c': [(log, ('2.8: NangongYuRhapsodyMuse Hair texcoord_vb',))],
'56699a62': [(log, ('2.8: NangongYuRhapsodyMuse Hair blend_vb',))],

# Headband VBs
'5aac7571': [(log, ('2.8: NangongYuRhapsodyMuse Headband draw_vb',))],
'74cbadea': [(log, ('2.8: NangongYuRhapsodyMuse Headband position_vb',))],
'00cbd7a8': [(log, ('2.8: NangongYuRhapsodyMuse Headband texcoord_vb',))],
'82509f4f': [(log, ('2.8: NangongYuRhapsodyMuse Headband blend_vb',))],

# Wing VBs
'4f3fcef0': [(log, ('2.8: NangongYuRhapsodyMuse Wing draw_vb',))],
'f0922b32': [(log, ('2.8: NangongYuRhapsodyMuse Wing position_vb',))],
'f1ca59db': [(log, ('2.8: NangongYuRhapsodyMuse Wing texcoord_vb',))],
'701bb859': [(log, ('2.8: NangongYuRhapsodyMuse Wing blend_vb',))],

# Body VBs
'6f39c5ff': [(log, ('2.8: NangongYuRhapsodyMuse Body draw_vb',))],
'6a7b86e3': [(log, ('2.8: NangongYuRhapsodyMuse Body position_vb',))],
'584ee20f': [(log, ('2.8: NangongYuRhapsodyMuse Body texcoord_vb',))],
'bcfea595': [(log, ('2.8: NangongYuRhapsodyMuse Body blend_vb',))],

# Face VBs
'd70f65c1': [(log, ('2.8: NangongYuRhapsodyMuse Face draw_vb',))],
'ed1df686': [(log, ('2.8: NangongYuRhapsodyMuse Face position_vb',))],
'45910aef': [(log, ('2.8: NangongYuRhapsodyMuse Face texcoord_vb',))],
'93c1ec0c': [(log, ('2.8: NangongYuRhapsodyMuse Face blend_vb',))],

# Shared NormalMap
'798adba3': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Shared NormalMap Hash',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5b186a44', 'NangongYuRhapsodyMuse.Wing.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced NangongYuRhapsodyMuse hashes ===
'1fd77103': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Eyebrow Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ba598cf9', 'NangongYuRhapsodyMuse.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'46c73033': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Headband Diffuse Hash [New]',)),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'5a026445': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Hair Diffuse Hash [New]',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'5e50a4f2': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'766f3fca': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'a458a615': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Hair MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'c17bc21d': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Headband LightMap Hash [New]',)),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'cf34f106': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'd94a0c41': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Hair LightMap Hash [New]',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'e8200d09': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Headband MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: NangongYuRhapsodyMuse Shared NormalMap [New]',)),
        (add_section_if_missing,        ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'NangongYuRhapsodyMuse',
    'game_versions': ['2.8', '3.0'],
}