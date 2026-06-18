"""
VelinaShadeOfLeisure Character Hash Commands
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
    Returns VelinaShadeOfLeisure's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'0479bb8f': [(log, ('3.0: VelinaShadeOfLeisure Body IB Hash',)),          (add_ib_check_if_missing,)],
'1914d1e4': [(log, ('3.0: VelinaShadeOfLeisure Eyebrows IB Hash',)),      (add_ib_check_if_missing,)],
'2f94c7e8': [(log, ('3.0: VelinaShadeOfLeisure Legs IB Hash',)),          (add_ib_check_if_missing,)],
'73685503': [(log, ('3.0: VelinaShadeOfLeisure Head IB Hash',)),          (add_ib_check_if_missing,)],
'6cfb2498': [(log, ('3.0: VelinaShadeOfLeisure Face IB Hash',)),          (add_ib_check_if_missing,)],
'5eb66b57': [(log, ('3.0: VelinaShadeOfLeisure Hair IB Hash',)),          (add_ib_check_if_missing,)],

# === VB Hashes ===
# Body
'cc427fff': [(log, ('3.0: VelinaShadeOfLeisure Body draw_vb',)),          (add_section_if_missing, ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n'))],
'6a0beedf': [(log, ('3.0: VelinaShadeOfLeisure Body position_vb',)),      (add_section_if_missing, ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n'))],
'5914c865': [(log, ('3.0: VelinaShadeOfLeisure Body texcoord_vb',)),      (add_section_if_missing, ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n'))],
'7bdd845e': [(log, ('3.0: VelinaShadeOfLeisure Body blend_vb',)),         (add_section_if_missing, ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n'))],

# Eyebrows
'2f828e6a': [(log, ('3.0: VelinaShadeOfLeisure Eyebrows draw_vb',)),      (add_section_if_missing, ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrows.IB', 'match_priority = 0\n'))],
'38d54a4d': [(log, ('3.0: VelinaShadeOfLeisure Eyebrows position_vb',)),  (add_section_if_missing, ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrows.IB', 'match_priority = 0\n'))],
'80e5ee4d': [(log, ('3.0: VelinaShadeOfLeisure Eyebrows texcoord_vb',)),  (add_section_if_missing, ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrows.IB', 'match_priority = 0\n'))],
'f18dd23f': [(log, ('3.0: VelinaShadeOfLeisure Eyebrows blend_vb',)),     (add_section_if_missing, ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrows.IB', 'match_priority = 0\n'))],

# Legs
'87cd2937': [(log, ('3.0: VelinaShadeOfLeisure Legs draw_vb',)),          (add_section_if_missing, ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n'))],
'938eb9f7': [(log, ('3.0: VelinaShadeOfLeisure Legs position_vb',)),      (add_section_if_missing, ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n'))],
'b49b9651': [(log, ('3.0: VelinaShadeOfLeisure Legs texcoord_vb',)),      (add_section_if_missing, ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n'))],
'112d2da2': [(log, ('3.0: VelinaShadeOfLeisure Legs blend_vb',)),         (add_section_if_missing, ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n'))],

# Head
'885c2ba8': [(log, ('3.0: VelinaShadeOfLeisure Head draw_vb',)),          (add_section_if_missing, ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n'))],
'f10329bb': [(log, ('3.0: VelinaShadeOfLeisure Head position_vb',)),      (add_section_if_missing, ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n'))],
'a71dc0ae': [(log, ('3.0: VelinaShadeOfLeisure Head texcoord_vb',)),      (add_section_if_missing, ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n'))],
'363488a6': [(log, ('3.0: VelinaShadeOfLeisure Head blend_vb',)),         (add_section_if_missing, ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n'))],

# Face
'19ead1b7': [(log, ('3.0: VelinaShadeOfLeisure Face draw_vb',)),          (add_section_if_missing, ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n'))],
'23f842f0': [(log, ('3.0: VelinaShadeOfLeisure Face position_vb',)),      (add_section_if_missing, ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n'))],
'641bedfb': [(log, ('3.0: VelinaShadeOfLeisure Face texcoord_vb',)),      (add_section_if_missing, ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n'))],
'98ecf569': [(log, ('3.0: VelinaShadeOfLeisure Face blend_vb',)),         (add_section_if_missing, ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n'))],

# Hair
'c60af8f1': [(log, ('3.0: VelinaShadeOfLeisure Hair draw_vb',)),          (add_section_if_missing, ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n'))],
'53954bd7': [(log, ('3.0: VelinaShadeOfLeisure Hair position_vb',)),      (add_section_if_missing, ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n'))],
'9f40d9d1': [(log, ('3.0: VelinaShadeOfLeisure Hair texcoord_vb',)),      (add_section_if_missing, ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n'))],
'a1c210e2': [(log, ('3.0: VelinaShadeOfLeisure Hair blend_vb',)),         (add_section_if_missing, ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'93ce2562': [
        (log,                           ('3.0: VelinaShadeOfLeisure Face Diffuse Hash',)),
        (add_section_if_missing,        ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'988ded22': [
        (log,                           ('3.0: VelinaShadeOfLeisure Body Diffuse Hash (Class A/C)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
    ],
'48ece6e8': [
        (log,                           ('3.0: VelinaShadeOfLeisure Body LightMap Hash (Class A/C)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
    ],
'ed40f87e': [
        (log,                           ('3.0: VelinaShadeOfLeisure Body MaterialMap Hash (Class A/C)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
    ],
'2ca3f765': [
        (log,                           ('3.0: VelinaShadeOfLeisure Body Diffuse Hash (Class B)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
    ],
'64b2da48': [
        (log,                           ('3.0: VelinaShadeOfLeisure Body LightMap Hash (Class B)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
    ],
'7c2d3cdb': [
        (log,                           ('3.0: VelinaShadeOfLeisure Body MaterialMap Hash (Class B)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
    ],

# === Legs Textures ===
'f786f1ab': [
        (log,                           ('3.0: VelinaShadeOfLeisure Legs Diffuse Hash',)),
        (add_section_if_missing,        ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n')),
    ],
'bd0acdee': [
        (log,                           ('3.0: VelinaShadeOfLeisure Legs LightMap Hash',)),
        (add_section_if_missing,        ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n')),
    ],
'ea9152d8': [
        (log,                           ('3.0: VelinaShadeOfLeisure Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n')),
    ],

# === Head & Hair Textures ===
'5e6e492c': [
        (log,                           ('3.0: VelinaShadeOfLeisure Head, Hair Diffuse Hash',)),
        (add_section_if_missing,        ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
    ],
'6b7dcb1b': [
        (log,                           ('3.0: VelinaShadeOfLeisure Head, Hair LightMap Hash',)),
        (add_section_if_missing,        ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
    ],
'18018e7a': [
        (log,                           ('3.0: VelinaShadeOfLeisure Head, Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: VelinaShadeOfLeisure Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: VelinaShadeOfLeisure Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2f94c7e8', 'VelinaShadeOfLeisure.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73685503', 'VelinaShadeOfLeisure.Head.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'VelinaShadeOfLeisure',
    'game_versions': ['3.0'],
}