"""
WiseOathOfSkies Character Hash Commands
ZZZ Mod Fixer v3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WiseOathOfSkies's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'22fe3236': [(log, ('3.0: WiseOathOfSkies Body IB Hash',)),                 (add_ib_check_if_missing,)],
'8a1ec07e': [(log, ('3.0: WiseOathOfSkies Neck IB Hash',)),                 (add_ib_check_if_missing,)],
'f21a2bac': [(log, ('3.0: WiseOathOfSkies Tie IB Hash',)),                  (add_ib_check_if_missing,)],
'd5ca0411': [(log, ('3.0: WiseOathOfSkies Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'1fdaf388': [(log, ('3.0: WiseOathOfSkies Face IB Hash',)),                 (add_ib_check_if_missing,)],

# === VB Hashes ===
# Body
'164b2ccb': [(log, ('3.0: WiseOathOfSkies Body draw_vb',)),                 (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],
'4dcfe033': [(log, ('3.0: WiseOathOfSkies Body position_vb',)),             (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],
'0c2cc3dd': [(log, ('3.0: WiseOathOfSkies Body texcoord_vb',)),             (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],
'8bab814c': [(log, ('3.0: WiseOathOfSkies Body blend_vb',)),                (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],

# Neck
'c4a1fb46': [(log, ('3.0: WiseOathOfSkies Neck draw_vb',)),                 (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],
'6171b974': [(log, ('3.0: WiseOathOfSkies Neck position_vb',)),             (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],
'0da56abf': [(log, ('3.0: WiseOathOfSkies Neck texcoord_vb',)),             (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],
'98a06e7d': [(log, ('3.0: WiseOathOfSkies Neck blend_vb',)),                (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],

# Tie
'86f21a82': [(log, ('3.0: WiseOathOfSkies Tie draw_vb',)),                  (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],
'fb0a401a': [(log, ('3.0: WiseOathOfSkies Tie position_vb',)),              (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],
'052d4b48': [(log, ('3.0: WiseOathOfSkies Tie texcoord_vb',)),              (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],
'4b19b5b5': [(log, ('3.0: WiseOathOfSkies Tie blend_vb',)),                 (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],

# Hair
'ef9c0510': [(log, ('3.0: WiseOathOfSkies Hair draw_vb',)),                 (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],
'e8df7ff3': [(log, ('3.0: WiseOathOfSkies Hair position_vb',)),             (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],
'774071dd': [(log, ('3.0: WiseOathOfSkies Hair texcoord_vb',)),             (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],
'68e4f572': [(log, ('3.0: WiseOathOfSkies Hair blend_vb',)),                (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],

# Face
'6c4552bb': [(log, ('3.0: WiseOathOfSkies Face VertexLimit',)),             (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],
'5657c1fc': [(log, ('3.0: WiseOathOfSkies Face position_vb',)),             (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],
'c83b6cbf': [(log, ('3.0: WiseOathOfSkies Face texcoord_vb',)),             (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],
'015fbf96': [(log, ('3.0: WiseOathOfSkies Face blend_vb',)),                (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'5d75fddc': [
        (log,                           ('3.0: WiseOathOfSkies Face Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],

# === Body & Neck Textures ===
'b9dcce2e': [
        (log,                           ('3.0: WiseOathOfSkies Body, Neck Diffuse Hash',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],
'bd86c7c4': [
        (log,                           ('3.0: WiseOathOfSkies Body, Neck LightMap Hash',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],
'4d7473b1': [
        (log,                           ('3.0: WiseOathOfSkies Body, Neck MaterialMap Hash',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],

# === Tie Textures ===
'1024352b': [
        (log,                           ('3.0: WiseOathOfSkies Tie Diffuse Hash',)),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],
'e550cd81': [
        (log,                           ('3.0: WiseOathOfSkies Tie LightMap Hash',)),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],
'6649f407': [
        (log,                           ('3.0: WiseOathOfSkies Tie MaterialMap Hash',)),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'28005a5b': [
        (log,                           ('3.0: WiseOathOfSkies Hair Diffuse Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('3.0: WiseOathOfSkies Hair LightMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('3.0: WiseOathOfSkies Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: WiseOathOfSkies Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: WiseOathOfSkies Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseOathOfSkies',
    'game_versions': ['3.0'],
}