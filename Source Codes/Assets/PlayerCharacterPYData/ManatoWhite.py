"""
ManatoWhite Character Hash Commands
ZZZ Mod Fixer v2.5 / v2.8
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns ManatoWhite's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'de57398c': [(log, ('2.8: ManatoWhite Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'f4c1c6d9': [(log, ('2.8: ManatoWhite UpperBody IB Hash',)),             (add_ib_check_if_missing,)],
'c0425328': [(log, ('2.8: ManatoWhite LowerBody IB Hash',)),             (add_ib_check_if_missing,)],
'fe66c6d2': [(log, ('2.8: ManatoWhite Accessories IB Hash',)),           (add_ib_check_if_missing,)],
'f987f156': [(log, ('2.8: ManatoWhite Face IB Hash',)),                  (add_ib_check_if_missing,)],
'c1f10814': [(log, ('2.8: ManatoWhite Weapon IB Hash',)),                (add_ib_check_if_missing,)],

# === Face Textures ===
'6d1343ec': [
        (log,                           ('2.8: ManatoWhite Face Diffuse Hash',)),
        (add_section_if_missing,        ('f987f156', 'ManatoWhite.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair & LowerBody Textures ===
'c11e3a48': [
        (log,                           ('2.8: ManatoWhite Hair, LowerBody Diffuse Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhite.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhite.LowerBody.IB', 'match_priority = 0\n')),
    ],
'a886faaf': [
        (log,                           ('2.8: ManatoWhite Hair, LowerBody LightMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhite.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhite.LowerBody.IB', 'match_priority = 0\n')),
    ],
'd97b73ec': [
        (log,                           ('2.8: ManatoWhite Hair, LowerBody MaterialMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhite.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhite.LowerBody.IB', 'match_priority = 0\n')),
    ],

# === UpperBody & Accessories Textures ===
'efd9e33e': [
        (log,                           ('2.8: ManatoWhite UpperBody, Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhite.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhite.Accessories.IB', 'match_priority = 0\n')),
    ],
'43b47f20': [
        (log,                           ('2.8: ManatoWhite UpperBody, Accessories LightMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhite.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhite.Accessories.IB', 'match_priority = 0\n')),
    ],
'b467ed79': [
        (log,                           ('2.8: ManatoWhite UpperBody, Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhite.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhite.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'ea7d80ff': [
        (log,                           ('2.8: ManatoWhite Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('c1f10814', 'ManatoWhite.Weapon.IB', 'match_priority = 0\n')),
    ],
'c52d4279': [
        (log,                           ('2.8: ManatoWhite Weapon LightMap Hash',)),
        (add_section_if_missing,        ('c1f10814', 'ManatoWhite.Weapon.IB', 'match_priority = 0\n')),
    ],
'aef57b5d': [
        (log,                           ('2.8: ManatoWhite Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('c1f10814', 'ManatoWhite.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.8: ManatoWhite Shared NormalMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhite.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhite.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhite.LowerBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhite.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c1f10814', 'ManatoWhite.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ManatoWhite',
    'game_versions': ['2.8'],
}