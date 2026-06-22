"""
BelleBrillianceOfStars Character Hash Commands
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
    Returns BelleBrillianceOfStars's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'0a843a8f': [(log, ('3.0: BelleBrillianceOfStars Hat IB Hash',)),          (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('3.0: BelleBrillianceOfStars Face IB Hash',)),         (add_ib_check_if_missing,)],
'a6431856': [(log, ('3.0: BelleBrillianceOfStars Neck IB Hash',)),         (add_ib_check_if_missing,)],
'aa9ffb85': [(log, ('3.0: BelleBrillianceOfStars Hair IB Hash',)),         (add_ib_check_if_missing,)],
'a318b3c6': [(log, ('3.0: BelleBrillianceOfStars Extra IB Hash',)),        (add_ib_check_if_missing,)],
'b946c37f': [(log, ('3.0: BelleBrillianceOfStars Tie IB Hash',)),          (add_ib_check_if_missing,)],
'feb1c4cd': [(log, ('3.0: BelleBrillianceOfStars Body IB Hash',)),         (add_ib_check_if_missing,)],
'403eace9': [(log, ('3.0: BelleBrillianceOfStars HairShadow IB Hash',)),    (add_ib_check_if_missing,)],
'62711f82': [(log, ('3.0: BelleBrillianceOfStars Earrings IB Hash',)),      (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hat
'0a877d89': [(log, ('3.0: BelleBrillianceOfStars Hat draw_vb',)),          (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],
'74d2da11': [(log, ('3.0: BelleBrillianceOfStars Hat position_vb',)),      (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],
'801cd45d': [(log, ('3.0: BelleBrillianceOfStars Hat texcoord_vb',)),      (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],
'd5070379': [(log, ('3.0: BelleBrillianceOfStars Hat blend_vb',)),         (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],

# Face
'04abceb5': [(log, ('3.0: BelleBrillianceOfStars Face draw_vb',)),         (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('3.0: BelleBrillianceOfStars Face position_vb',)),     (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],
'd3000b22': [(log, ('3.0: BelleBrillianceOfStars Face texcoord_vb',)),     (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],
'359e4502': [(log, ('3.0: BelleBrillianceOfStars Face blend_vb',)),        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],

# Neck
'0e72bdb7': [(log, ('3.0: BelleBrillianceOfStars Neck draw_vb',)),         (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],
'd5c6a50f': [(log, ('3.0: BelleBrillianceOfStars Neck position_vb',)),     (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],
'07a15f8e': [(log, ('3.0: BelleBrillianceOfStars Neck texcoord_vb',)),     (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],
'57192494': [(log, ('3.0: BelleBrillianceOfStars Neck blend_vb',)),        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],

# Hair
'992d149f': [(log, ('3.0: BelleBrillianceOfStars Hair draw_vb',)),         (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],
'dbd537bb': [(log, ('3.0: BelleBrillianceOfStars Hair position_vb',)),     (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],
'0f1d7b96': [(log, ('3.0: BelleBrillianceOfStars Hair texcoord_vb',)),     (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],
'2cf18f34': [(log, ('3.0: BelleBrillianceOfStars Hair blend_vb',)),        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],

# Extra
'f6ed0e7b': [(log, ('3.0: BelleBrillianceOfStars Extra draw_vb',)),        (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],
'd9087948': [(log, ('3.0: BelleBrillianceOfStars Extra position_vb',)),    (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],
'1cfe1205': [(log, ('3.0: BelleBrillianceOfStars Extra texcoord_vb',)),    (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],
'82c81803': [(log, ('3.0: BelleBrillianceOfStars Extra blend_vb',)),       (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],

# Tie
'c0ee97be': [(log, ('3.0: BelleBrillianceOfStars Tie draw_vb',)),          (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],
'6aa2848f': [(log, ('3.0: BelleBrillianceOfStars Tie position_vb',)),      (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],
'88e81d00': [(log, ('3.0: BelleBrillianceOfStars Tie texcoord_vb',)),      (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],
'f83e837a': [(log, ('3.0: BelleBrillianceOfStars Tie blend_vb',)),         (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],

# Body
'76ceb325': [(log, ('3.0: BelleBrillianceOfStars Body draw_vb',)),         (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],
'df17d505': [(log, ('3.0: BelleBrillianceOfStars Body position_vb',)),     (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],
'3e19f179': [(log, ('3.0: BelleBrillianceOfStars Body texcoord_vb',)),     (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],
'987395ef': [(log, ('3.0: BelleBrillianceOfStars Body blend_vb',)),        (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],

# Earrings
'e2c8decf': [(log, ('3.0: BelleBrillianceOfStars Earrings draw_vb',)),      (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],
'29324995': [(log, ('3.0: BelleBrillianceOfStars Earrings position_vb',)),  (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],
'8da231b5': [(log, ('3.0: BelleBrillianceOfStars Earrings texcoord_vb',)),  (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],
'611f1c52': [(log, ('3.0: BelleBrillianceOfStars Earrings blend_vb',)),     (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'75ec3614': [
        (log,                           ('3.0: BelleBrillianceOfStars Face Diffuse Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],

# === Neck & Body Textures ===
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars Neck, Body Diffuse Hash',)),
        (add_section_if_missing,        ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars Neck, Body LightMap Hash',)),
        (add_section_if_missing,        ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars Neck, Body MaterialMap Hash',)),
        (add_section_if_missing,        ('a6431856', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'1ce58567': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair Diffuse Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log,                           ('3.0: WiseSummer Hair LightMap Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log,                           ('3.0: WiseSummer Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],

# === Hat, Extra, Tie, Earrings Textures ===
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars Hat, Extra, Tie, Earrings Diffuse Hash',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars Hat, Extra, Tie, Earrings LightMap Hash',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars Hat, Extra, Tie, Earrings MaterialMap Hash',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: BelleBrillianceOfStars Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: BelleBrillianceOfStars Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleBrillianceOfStars',
    'game_versions': ['3.0'],
}