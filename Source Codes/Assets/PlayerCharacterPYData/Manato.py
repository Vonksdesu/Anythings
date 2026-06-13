"""
Manato Character Hash Commands
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
    Returns Manato's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'de57398c': [(log, ('2.8: Manato Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'f4c1c6d9': [(log, ('2.8: Manato UpperBody IB Hash',)),                 (add_ib_check_if_missing,)],
'c0425328': [(log, ('2.8: Manato LowerBody IB Hash',)),                 (add_ib_check_if_missing,)],
'fe66c6d2': [(log, ('2.8: Manato Accessories IB Hash',)),              (add_ib_check_if_missing,)],
'f987f156': [(log, ('2.8: Manato Face IB Hash',)),                       (add_ib_check_if_missing,)],
'734da350': [(log, ('2.8: Manato Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'c1f10814': [(log, ('2.8: Manato Weapon IB Hash',)),                     (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'0932100e': [(log, ('2.8: Manato Hair draw_vb',)),                      (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n'))],
'4e68e014': [(log, ('2.8: Manato Hair position_vb',)),                  (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n'))],
'9fe810ff': [(log, ('2.8: Manato Hair texcoord_vb',)),                  (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n'))],
'b882d0c8': [(log, ('2.8: Manato Hair blend_vb',)),                     (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'18cf9af2': [(log, ('2.8: Manato Hair Shadow draw_vb',)),               (add_section_if_missing, ('734da350', 'Manato.HairShadow.IB', 'match_priority = 0\n'))],
'0da604ca': [(log, ('2.8: Manato Hair Shadow position_vb',)),           (add_section_if_missing, ('734da350', 'Manato.HairShadow.IB', 'match_priority = 0\n'))],
'ade3c45f': [(log, ('2.8: Manato Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('734da350', 'Manato.HairShadow.IB', 'match_priority = 0\n'))],
'bee7126f': [(log, ('2.8: Manato Hair Shadow blend_vb',)),              (add_section_if_missing, ('734da350', 'Manato.HairShadow.IB', 'match_priority = 0\n'))],

# UpperBody
'8524918a': [(log, ('2.8: Manato UpperBody draw_vb',)),                 (add_section_if_missing, ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n'))],
'9e173c09': [(log, ('2.8: Manato UpperBody position_vb',)),             (add_section_if_missing, ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n'))],
'7d36f969': [(log, ('2.8: Manato UpperBody texcoord_vb',)),             (add_section_if_missing, ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n'))],
'91048d22': [(log, ('2.8: Manato UpperBody blend_vb',)),                (add_section_if_missing, ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n'))],

# LowerBody
'2aa2324a': [(log, ('2.8: Manato LowerBody draw_vb',)),                 (add_section_if_missing, ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n'))],
'8fe3485a': [(log, ('2.8: Manato LowerBody position_vb',)),             (add_section_if_missing, ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n'))],
'918946ee': [(log, ('2.8: Manato LowerBody texcoord_vb',)),             (add_section_if_missing, ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n'))],
'd81e178a': [(log, ('2.8: Manato LowerBody blend_vb',)),                (add_section_if_missing, ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n'))],

# Accessories
'ff068e07': [(log, ('2.8: Manato Accessories draw_vb',)),               (add_section_if_missing, ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n'))],
'007cd149': [(log, ('2.8: Manato Accessories position_vb',)),           (add_section_if_missing, ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n'))],
'835ffec6': [(log, ('2.8: Manato Accessories texcoord_vb',)),           (add_section_if_missing, ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n'))],
'e9379036': [(log, ('2.8: Manato Accessories blend_vb',)),              (add_section_if_missing, ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n'))],

# Face
'ef07f453': [(log, ('2.8: Manato Face VertexLimit Hash',)),              (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n'))],
'd5156714': [(log, ('2.8: Manato Face position_vb Hash',)),              (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n'))],
'0fd41a37': [(log, ('2.8: Manato Face texcoord_vb Hash',)),              (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n'))],
'e5c84069': [(log, ('2.8: Manato Face blend_vb Hash',)),                 (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n'))],

# Weapon
'84fa3702': [(log, ('2.8: Manato Weapon VertexLimit Hash',)),            (add_section_if_missing, ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n'))],
'd4141703': [(log, ('2.8: Manato Weapon position_vb Hash',)),            (add_section_if_missing, ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n'))],
'f693b9de': [(log, ('2.8: Manato Weapon texcoord_vb Hash',)),            (add_section_if_missing, ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n'))],
'34a20b76': [(log, ('2.8: Manato Weapon blend_vb Hash',)),               (add_section_if_missing, ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'bd8621a4': [(log, ('2.0 -> 2.8: Manato Weapon Diffuse [Legacy]',)), (update_hash, ('ea7d80ff',))],
'38f2e62a': [(log, ('2.0 -> 2.8: Manato Weapon LightMap [Legacy]',)), (update_hash, ('c52d4279',))],
'bf621a3b': [(log, ('2.0 -> 2.8: Manato Weapon MaterialMap [Legacy]',)), (update_hash, ('aef57b5d',))],

# === Hair & LowerBody Textures ===
'07353b33': [
        (log,                           ('2.8: Manato Hair, LowerBody Diffuse Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'81a04fa6': [
        (log,                           ('2.8: Manato Hair, LowerBody Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'20447316': [
        (log,                           ('2.8: Manato Hair, LowerBody LightMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'2bfdcb76': [
        (log,                           ('2.8: Manato Hair, LowerBody LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'b8091cf0': [
        (log,                           ('2.8: Manato Hair, LowerBody MaterialMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],
'b9654ab9': [
        (log,                           ('2.8: Manato Hair, LowerBody MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
    ],

# === UpperBody & Accessories Textures ===
'9c659f1a': [
        (log,                           ('2.8: Manato UpperBody, Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'9e78d2c7': [
        (log,                           ('2.8: Manato UpperBody, Accessories Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'a15d0289': [
        (log,                           ('2.8: Manato UpperBody, Accessories LightMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'53c85c6a': [
        (log,                           ('2.8: Manato UpperBody, Accessories LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'92336a2f': [
        (log,                           ('2.8: Manato UpperBody, Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
'fdc49789': [
        (log,                           ('2.8: Manato UpperBody, Accessories MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'8de251ee': [
        (log,                           ('2.8: Manato Face Diffuse Hash',)),
        (add_section_if_missing,        ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
    ],
'6d1343ec': [
        (log,                           ('2.8: Manato Face Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'ea7d80ff': [
        (log,                           ('2.8: Manato Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n')),
    ],
'c52d4279': [
        (log,                           ('2.8: Manato Weapon LightMap Hash',)),
        (add_section_if_missing,        ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n')),
    ],
'aef57b5d': [
        (log,                           ('2.8: Manato Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: Manato Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c1f10814', 'Manato.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Manato Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Manato',
    'game_versions': ['2.8'],
}