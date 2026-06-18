"""
WiseSummer Character Hash Commands
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
    Returns WiseSummer's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'1fdaf388': [(log, ('2.8: WiseSummer Face IB Hash (shared with Wise)',)), (add_ib_check_if_missing,)],
'4fe696c8': [(log, ('2.8 -> 3.0: WiseSummer Body IB Hash [Legacy]',)), (update_hash, ('19a3f02e',))],
'cb272754': [(log, ('2.8 -> 3.0: WiseSummer Hair IB Hash [Legacy]',)), (update_hash, ('0ec31440',))],
'3f771e63': [(log, ('2.8: WiseSummer HairShadow IB Hash',)),            (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'0ec31440': [(log, ('3.0: WiseSummer Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'19a3f02e': [(log, ('3.0: WiseSummer Body IB Hash',)),                  (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'77045a80': [(log, ('2.8: WiseSummer Hair draw_vb',)),                  (add_section_if_missing, ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],
'16ac44f6': [(log, ('2.8: WiseSummer Hair position_vb',)),              (add_section_if_missing, ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],
'5c5bde90': [(log, ('2.8: WiseSummer Hair texcoord_vb',)),              (add_section_if_missing, ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],
'82396952': [(log, ('2.8: WiseSummer Hair blend_vb',)),                 (add_section_if_missing, ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'8e9a12c7': [(log, ('2.8: WiseSummer HairShadow draw_vb',)),            (add_section_if_missing, ('3f771e63', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
'14fff21a': [(log, ('2.8: WiseSummer HairShadow position_vb',)),        (add_section_if_missing, ('3f771e63', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
'49d81f9a': [(log, ('2.8: WiseSummer HairShadow texcoord_vb',)),        (add_section_if_missing, ('3f771e63', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
'a2c79f8d': [(log, ('2.8: WiseSummer HairShadow blend_vb',)),           (add_section_if_missing, ('3f771e63', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'18e704a8': [(log, ('2.8: WiseSummer Body draw_vb',)),                  (add_section_if_missing, ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],
'd6c86c1e': [(log, ('2.8: WiseSummer Body position_vb',)),              (add_section_if_missing, ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],
'acfe9fe4': [(log, ('2.8: WiseSummer Body texcoord_vb',)),              (add_section_if_missing, ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],
'd4147320': [(log, ('2.8: WiseSummer Body blend_vb',)),                 (add_section_if_missing, ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],

# Face
'6c4552bb': [(log, ('2.8: WiseSummer Face VertexLimit',)),              (add_section_if_missing, ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n'))],
'5657c1fc': [(log, ('2.8: WiseSummer Face Position',)),                 (add_section_if_missing, ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n'))],
'c83b6cbf': [(log, ('2.8: WiseSummer Face Texcoord',)),                 (add_section_if_missing, ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n'))],
'757bc7cc': [(log, ('2.8: WiseSummer Face Blend',)),                    (add_section_if_missing, ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n'))],

# === 3.0 Database Updates (Strict Sync) ===
# Hair VBs
'20f40e82': [(log, ('3.0: WiseSummer Hair draw_vb',)),                  (add_section_if_missing, ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],
'1a6be2b0': [(log, ('3.0: WiseSummer Hair position_vb',)),              (add_section_if_missing, ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],
'951a90bf': [(log, ('3.0: WiseSummer Hair texcoord_vb',)),              (add_section_if_missing, ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],
'16c55ecc': [(log, ('3.0: WiseSummer Hair blend_vb',)),                 (add_section_if_missing, ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n'))],

# Body VBs
'44accf08': [(log, ('3.0: WiseSummer Body draw_vb',)),                  (add_section_if_missing, ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],
'71a703c7': [(log, ('3.0: WiseSummer Body position_vb',)),              (add_section_if_missing, ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],
'31d424fc': [(log, ('3.0: WiseSummer Body texcoord_vb',)),              (add_section_if_missing, ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],
'9ab40475': [(log, ('3.0: WiseSummer Body blend_vb',)),                 (add_section_if_missing, ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'5d75fddc': [
        (log,                           ('2.8: WiseSummer Face Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
    ],
'588d7d2d': [
        (log,                           ('2.8: WiseSummer FaceA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'5907afda': [
        (log,                           ('2.8: WiseSummer BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'7a142a7d': [
        (log,                           ('2.8: WiseSummer BodyA LightMap Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'd6996446': [
        (log,                           ('2.8: WiseSummer BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'd476035d': [
        (log,                           ('2.8: WiseSummer BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'0fa8f99c': [
        (log,                           ('2.8: WiseSummer BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'c2c8606e': [
        (log,                           ('2.8: WiseSummer FaceA, BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'28005a5b': [
        (log,                           ('2.8: WiseSummer HairA Diffuse Hash',)),
        (add_section_if_missing,        (('cb272754', 'f6cac296'), 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'cb0d0c22': [
        (log,                           ('2.8: WiseSummer HairA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('2.8: WiseSummer HairA LightMap Hash',)),
        (add_section_if_missing,        (('cb272754', 'f6cac296'), 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'33368e12': [
        (log,                           ('2.8: WiseSummer HairA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('2.8: WiseSummer HairA MaterialMap Hash',)),
        (add_section_if_missing,        (('cb272754', 'f6cac296'), 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'd9383a15': [
        (log,                           ('2.8: WiseSummer HairA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: WiseSummer Shared NormalMap Hash',)),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: WiseSummer BodyA, HairA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseSummer',
    'game_versions': ['2.8', '3.0'],
}