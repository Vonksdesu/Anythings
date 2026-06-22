"""
YixuanTrailsOfInk Character Hash Commands
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
    Returns YixuanTrailsOfInk's complete hash commands dictionary.
    """
    return {
# === IB Hashes ===
'ac8e9ee3': [(log, ('2.8: YixuanTrailsOfInk Hair IB Hash',)),       (add_ib_check_if_missing,)],
'd28b9c82': [(log, ('2.8: YixuanTrailsOfInk HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'95de0d39': [(log, ('2.8: YixuanTrailsOfInk Body IB Hash',)),       (add_ib_check_if_missing,)],
'064cd7d3': [(log, ('2.8: YixuanTrailsOfInk Bottle IB Hash',)),     (add_ib_check_if_missing,)],
'0fdae851': [(log, ('2.8: YixuanTrailsOfInk BottleGlass IB Hash',)),(add_ib_check_if_missing,)],
'892858fd': [(log, ('2.8: YixuanTrailsOfInk Hairpin IB Hash',)),    (add_ib_check_if_missing,)],
'8b067f99': [(log, ('2.8: YixuanTrailsOfInk Face IB Hash',)),       (add_ib_check_if_missing,)],
'ce38ac3b': [(log, ('2.8: YixuanTrailsOfInk WeaponBird IB Hash',)), (add_ib_check_if_missing,)],

# === VERTEX LIMITS ===
'ad3cd82a': [(log, ('2.8: YixuanTrailsOfInk Face VertexLimitVB',))],
'ccbbb7ea': [(log, ('2.8: YixuanTrailsOfInk WeaponBird VertexLimit',))],

# === VERTEX BUFFER (VB) HASHES ===
# Hair
'36a68b27': [(log, ('2.8: YixuanTrailsOfInk Hair draw_vb',))],
'cc898b44': [(log, ('2.8: YixuanTrailsOfInk Hair position_vb',))],
'd4841137': [(log, ('2.8: YixuanTrailsOfInk Hair texcoord_vb',))],
'd7eb400e': [(log, ('2.8: YixuanTrailsOfInk Hair blend_vb',))],

# Hair Shadow
'7f5aba6c': [(log, ('2.8: YixuanTrailsOfInk HairShadow draw_vb',))],
'c7748cbd': [(log, ('2.8: YixuanTrailsOfInk HairShadow position_vb',))],
'a07eb5cf': [(log, ('2.8: YixuanTrailsOfInk HairShadow texcoord_vb',))],
'07c7e48f': [(log, ('2.8: YixuanTrailsOfInk HairShadow blend_vb',))],

# Body (Skins)
'4e321bef': [(log, ('2.8: YixuanTrailsOfInk Body draw_vb',))],
'd1e95221': [(log, ('2.8: YixuanTrailsOfInk Body position_vb',))],
'6c57cdb1': [(log, ('2.8: YixuanTrailsOfInk Body texcoord_vb',))],
'b5c70816': [(log, ('2.8: YixuanTrailsOfInk Body blend_vb',))],

# Bottle (Skins)
'e0a315c0': [(log, ('2.8: YixuanTrailsOfInk Bottle draw_vb',))],
'f6564b67': [(log, ('2.8: YixuanTrailsOfInk Bottle position_vb',))],
'ee08ae2a': [(log, ('2.8: YixuanTrailsOfInk Bottle texcoord_vb',))],
'4df43644': [(log, ('2.8: YixuanTrailsOfInk Bottle blend_vb',))],

# Hairpin
'ba017cf3': [(log, ('2.8: YixuanTrailsOfInk Hairpin draw_vb',))],
'3194141e': [(log, ('2.8: YixuanTrailsOfInk Hairpin position_vb',))],
'b3123168': [(log, ('2.8: YixuanTrailsOfInk Hairpin texcoord_vb',))],
'de9d3ab7': [(log, ('2.8: YixuanTrailsOfInk Hairpin blend_vb',))],

# Face
'972e4b6d': [(log, ('2.8: YixuanTrailsOfInk Face position_vb',)), (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n'))],
'2e04aac2': [(log, ('2.8: YixuanTrailsOfInk Face texcoord_vb',)), (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n'))],
'4466e7ea': [(log, ('2.8: YixuanTrailsOfInk Face blend_vb',)), (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n'))],

# Weapon Bird
'9052084b': [(log, ('2.8: YixuanTrailsOfInk WeaponBird position_vb',)), (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n'))],
'f45313a0': [(log, ('2.8: YixuanTrailsOfInk WeaponBird texcoord_vb',)), (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n'))],
'3ac6dfc7': [(log, ('2.8: YixuanTrailsOfInk WeaponBird blend_vb',)), (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n'))],

# === TEXTURE HASHES ===
# Shared NormalMap
'798adba3': [
        (log,                           ('2.8: YixuanTrailsOfInk Shared NormalMap',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],

# Hair, Hairpin Shared Textures
'84fe943d': [
        (log,                           ('2.8: YixuanTrailsOfInk Hair Diffuse Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'5574ca9f': [
        (log,                           ('2.8: YixuanTrailsOfInk Hair LightMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'f4ac690c': [
        (log,                           ('2.8: YixuanTrailsOfInk Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],

# Body & Bottle Shared Textures (Classification A)
'5460dbe4': [
        (log,                           ('2.8: YixuanTrailsOfInk Body, Bottle Diffuse A Hash',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'7369431b': [
        (log,                           ('2.8: YixuanTrailsOfInk Body, Bottle LightMap A Hash',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'2d535255': [
        (log,                           ('2.8: YixuanTrailsOfInk Body, Bottle MaterialMap A Hash',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],

# Body & Bottle Shared Textures (Classification B)
'89509335': [
        (log,                           ('2.8: YixuanTrailsOfInk Body, Bottle Diffuse B Hash',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'ed7abe1d': [
        (log,                           ('2.8: YixuanTrailsOfInk Body, Bottle LightMap B Hash',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'229c5b0f': [
        (log,                           ('2.8: YixuanTrailsOfInk Body, Bottle MaterialMap B Hash',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],

# Hairpin Base Textures
'd7db2bc6': [
        (log,                           ('2.8: YixuanTrailsOfInk Hairpin Diffuse Hash',)),
        (add_section_if_missing,        ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'96f754a7': [
        (log,                           ('2.8: YixuanTrailsOfInk Hairpin LightMap Hash',)),
        (add_section_if_missing,        ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'aa1056a5': [
        (log,                           ('2.8: YixuanTrailsOfInk Hairpin MaterialMap Hash',)),
        (add_section_if_missing,        ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'7d9ee001': [
        (log,                           ('3.0: YixuanTrailsOfInk Face Diffuse Hash',)),
        (add_section_if_missing,        ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ],

# === Weapon Bird Textures ===
'677893d2': [
        (log,                           ('2.8: YixuanTrailsOfInk WeaponBird Diffuse Hash',)),
        (add_section_if_missing,        ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'd1ee41dc': [
        (log,                           ('2.8: YixuanTrailsOfInk WeaponBird LightMap Hash',)),
        (add_section_if_missing,        ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'23d4f666': [
        (log,                           ('2.8: YixuanTrailsOfInk WeaponBird MaterialMap Hash',)),
        (add_section_if_missing,        ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n')),
    ],

# === 2.8 Synced Skin-Specific Texture Hashes ===
'7e38b38b': [
        (log,                           ('2.8: YixuanTrailsOfInk Hair Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'086ac064': [
        (log,                           ('2.8: YixuanTrailsOfInk Hair LightMap Hash [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'83b02982': [
        (log,                           ('2.8: YixuanTrailsOfInk Hair MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'2a4f37a6': [
        (log,                           ('2.8: YixuanTrailsOfInk Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'5a291e85': [
        (log,                           ('2.8: YixuanTrailsOfInk Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'd28370ec': [
        (log,                           ('2.8: YixuanTrailsOfInk Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'fe2cc6f3': [
        (log,                           ('2.8: YixuanTrailsOfInk Bottle Diffuse Hash [New]',)),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'867e3b95': [
        (log,                           ('2.8: YixuanTrailsOfInk Bottle LightMap Hash [New]',)),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'c72a2356': [
        (log,                           ('2.8: YixuanTrailsOfInk Bottle MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'7683c132': [
        (log,                           ('2.8: YixuanTrailsOfInk Skin Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'a22695c9': [
        (log,                           ('2.8: YixuanTrailsOfInk Skin Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'7e6747ac': [
        (log,                           ('2.8: YixuanTrailsOfInk Skin Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'920caf66': [
        (log,                           ('2.8: YixuanTrailsOfInk WeaponBird Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'771d52eb': [
        (log,                           ('2.8: YixuanTrailsOfInk WeaponBird LightMap Hash [New]',)),
        (add_section_if_missing,        ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'dc3c5667': [
        (log,                           ('2.8: YixuanTrailsOfInk WeaponBird MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ce38ac3b', 'YixuanTrailsOfInk.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: YixuanTrailsOfInk Shared NormalMap [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],

# === Legacy 3.0 Texture Redirects ===
'9efd1605': [
        (log,                           ('2.8 -> 3.0: YixuanFace Diffuse Hash [Legacy]',)),
        (update_hash,                   ('7d9ee001',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YixuanTrailsOfInk',
    'game_versions': ['2.8', '3.0'],
}