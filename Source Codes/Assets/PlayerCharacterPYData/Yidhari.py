"""
Yidhari Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
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
    Returns Yidhari's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
# IB Hashes
'2022936e': [(log, ('2.5: Yidhari Hair IB Hash',)),   (add_ib_check_if_missing,)],
'12251f42': [(log, ('2.5: Yidhari Body IB Hash',)),   (add_ib_check_if_missing,)],
'4cb99618': [(log, ('2.5: Yidhari Tentacles IB Hash',)),   (add_ib_check_if_missing,)],
'1c164f7f': [(log, ('2.5: Yidhari RgbBars IB Hash',)),   (add_ib_check_if_missing,)],
'02072970': [(log, ('2.5: Yidhari Brows IB Hash',)),   (add_ib_check_if_missing,)],
'a2406060': [(log, ('2.5: Yidhari Face IB Hash',)),   (add_ib_check_if_missing,)],

# Hair Textures
'd0587bc2': [
        (log,                           ('2.5: Yidhari HairA Diffuse Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'42ef8882': [
        (log,                           ('2.5: Yidhari HairA LightMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'bc5d6f24': [
        (log,                           ('2.5: Yidhari HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures
'ca51f269': [
        (log,                           ('2.5: Yidhari BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'5b985a6f': [
        (log,                           ('2.5: Yidhari BodyA LightMap Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'0e91ed54': [
        (log,                           ('2.5: Yidhari BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],

# Tentacles Textures
'2156a161': [
        (log,                           ('2.5: Yidhari TentaclesA Diffuse Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'8bf59f48': [
        (log,                           ('2.5: Yidhari TentaclesA LightMap Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'e0bb4de9': [
        (log,                           ('2.5: Yidhari TentaclesA MaterialMap Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],

# Face/Brows Shared Diffuse Texture
'c6e0cfbe': [
        (log,                           ('2.5: Yidhari Face & Brows Diffuse Hash',)),
        (add_section_if_missing,        ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02072970', 'Yidhari.Brows.IB', 'match_priority = 0\n')),
    ],

# Shared NormalMap (Hair, Body, Tentacles)
'ebac056e': [
        (log,                           ('2.5: Yidhari Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# Hash Updates (v2.4 -> v2.8)
'9ad20501': [(log, ('2.4 -> 2.8: Yidhari Body LightMap Hash',)), (update_hash, ('381e8e5a',))],

# Target Hashes (Penyelarasan Validasi)
'381e8e5a': [
        (log,                           ('2.8: Yidhari Body LightMap Hash (Target)',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],

# New Index Buffer (IB) Hashes
'a5a5654d': [(log, ('2.8: Yidhari HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'bc96ab6e': [(log, ('2.8: Yidhari Weapon IB Hash',)),     (add_ib_check_if_missing,)],

# Hair draw_vb & VBs
'2736d089': [(log, ('2.8: Yidhari Hair draw_vb',))],
'4512a51e': [(log, ('2.8: Yidhari Hair position_vb',))],
'028c0d28': [(log, ('2.8: Yidhari Hair texcoord_vb',))],
'6a65d55c': [(log, ('2.8: Yidhari Hair blend_vb',))],

# Hair Shadow draw_vb & VBs
'225ffc91': [(log, ('2.8: Yidhari HairShadow draw_vb',))],
'e13a4a8c': [(log, ('2.8: Yidhari HairShadow position_vb',))],
'a74fecc6': [(log, ('2.8: Yidhari HairShadow texcoord_vb',))],
'7d881667': [(log, ('2.8: Yidhari HairShadow blend_vb',))],

# Body draw_vb & VBs
'471aa92a': [(log, ('2.8: Yidhari Body draw_vb',))],
'74f07fc5': [(log, ('2.8: Yidhari Body position_vb',))],
'2abc67fb': [(log, ('2.8: Yidhari Body texcoord_vb',))],
'eff05950': [(log, ('2.8: Yidhari Body blend_vb',))],

# Tail draw_vb & VBs
'bf5562d4': [(log, ('2.8: Yidhari Tail draw_vb',))],
'c9dab2d3': [(log, ('2.8: Yidhari Tail position_vb',))],
'344e456e': [(log, ('2.8: Yidhari Tail texcoord_vb',))],
'9b99674d': [(log, ('2.8: Yidhari Tail blend_vb',))],

# Eyebrow VBs & Limits
'534c2f9b': [(log, ('2.8: Yidhari Eyebrow VertexLimit',))],
'695ebcdc': [(log, ('2.8: Yidhari Eyebrow Position',))],
'cf1a7297': [(log, ('2.8: Yidhari Eyebrow Texcoord',))],
'ee532c5b': [(log, ('2.8: Yidhari Eyebrow Blend',))],

# Face VBs & Limits
'8abeb827': [(log, ('2.8: Yidhari Face VertexLimit',))],
'b0ac2b60': [(log, ('2.8: Yidhari Face Position',))],
'08316415': [(log, ('2.8: Yidhari Face Texcoord',))],
'de712ebf': [(log, ('2.8: Yidhari Face Blend',))],

# Weapon VBs & Limits
'6bc320f0': [(log, ('2.8: Yidhari Weapon VertexLimit',))],
'09c65b14': [(log, ('2.8: Yidhari Weapon Position',))],
'5a6fe39e': [(log, ('2.8: Yidhari Weapon Texcoord',))],
'f98b369d': [(log, ('2.8: Yidhari Weapon Blend',))],

# Texture Hashes (v2.8)
'aefe5860': [
        (log,                           ('2.8: Yidhari HairA Diffuse Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'222b6f58': [
        (log,                           ('2.8: Yidhari HairA LightMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'527ac41b': [
        (log,                           ('2.8: Yidhari HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log,                           ('2.8: Yidhari Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],
'89bec19d': [
        (log,                           ('2.8: Yidhari BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'9af65de7': [
        (log,                           ('2.8: Yidhari BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'067b0a15': [
        (log,                           ('2.8: Yidhari TailA Diffuse Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'6b99432e': [
        (log,                           ('2.8: Yidhari TailA LightMap Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'0bf712a3': [
        (log,                           ('2.8: Yidhari TailA MaterialMap Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'4753db8f': [
        (log,                           ('2.8: Yidhari FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02072970', 'Yidhari.Brows.IB', 'match_priority = 0\n')),
    ],
'85b7643e': [
        (log,                           ('2.8: Yidhari WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],
'cbb02c28': [
        (log,                           ('2.8: Yidhari WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],
'd17095b0': [
        (log,                           ('2.8: Yidhari WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Weapon Texture Hashes ===
'48889652': [
        (log,                           ('2.8: Yidhari Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],
'e6728419': [
        (log,                           ('2.8: Yidhari Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],
'42666703': [
        (log,                           ('2.8: Yidhari Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('bc96ab6e', 'Yidhari.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yidhari',
    'game_versions': ['2.8', '3.0'],
}