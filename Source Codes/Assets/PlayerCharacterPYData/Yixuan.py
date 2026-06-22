"""
Yixuan Character Hash Commands
ZZZ Mod Fixer v2.8 - Full Uncompromising Database (Strict Fixed Final v2)
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                    remove_section, remove_indexed_sections, capture_section,
                    create_new_section, transfer_indexed_sections,
                    multiply_section_if_missing, add_ib_check_if_missing,
                    add_section_if_missing, zzz_13_remap_texcoord,
                    zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Yixuan's complete hash commands dictionary.
    """
    return {
# === IB Hashes ===
'ac8e9ee3': [(log, ('2.8: Yixuan Hair IB Hash',)),       (add_ib_check_if_missing,)],
'd28b9c82': [(log, ('2.8: Yixuan HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'029c1f5a': [(log, ('2.8: Yixuan Body IB Hash',)),       (add_ib_check_if_missing,)],
'1630f2d0': [(log, ('2.8: Yixuan Bottle IB Hash',)),     (add_ib_check_if_missing,)],
'0fdae851': [(log, ('2.8: Yixuan BottleGlass IB Hash',)),(add_ib_check_if_missing,)],
'67c61080': [(log, ('2.8: Yixuan Coins IB Hash',)),      (add_ib_check_if_missing,)],
'892858fd': [(log, ('2.8: Yixuan Hairpin IB Hash',)),    (add_ib_check_if_missing,)],
'8c2fc05e': [(log, ('2.8: Yixuan Jacket IB Hash',)),     (add_ib_check_if_missing,)],
'8b067f99': [(log, ('2.8: Yixuan Face IB Hash',)),      (add_ib_check_if_missing,)],
'ce38ac3b': [(log, ('2.8: Yixuan WeaponBird IB Hash (Idle)',)),   (add_ib_check_if_missing,)],
'fd2cbc71': [(log, ('2.8: Yixuan WeaponBird IB Hash (Combat)',)), (add_ib_check_if_missing,)],

# === VERTEX LIMITS ===
'ad3cd82a': [(log, ('2.8: Yixuan Face VertexLimitVB',))],
'ccbbb7ea': [(log, ('2.8: Yixuan WeaponBird VertexLimit (Idle)',))],
'5a016c9b': [(log, ('2.8: Yixuan WeaponBird VertexLimit (Combat)',))],

# === VERTEX BUFFER (VB) HASHES ===
# Hair (头发)
'36a68b27': [(log, ('2.8: Yixuan Hair draw_vb',))],
'cc898b44': [(log, ('2.8: Yixuan Hair position_vb',))],
'd4841137': [(log, ('2.8: Yixuan Hair texcoord_vb',))],
'd7eb400e': [(log, ('2.8: Yixuan Hair blend_vb',))],

# Hair Shadow (头发阴影)
'7f5aba6c': [(log, ('2.8: Yixuan HairShadow draw_vb',))],
'c7748cbd': [(log, ('2.8: Yixuan HairShadow position_vb',))],
'a07eb5cf': [(log, ('2.8: Yixuan HairShadow texcoord_vb',))],
'07c7e48f': [(log, ('2.8: Yixuan HairShadow blend_vb',))],

# Body (身体)
'f922d854': [(log, ('2.8: Yixuan Body draw_vb',))],
'155737d9': [(log, ('2.8: Yixuan Body position_vb',))],
'7af146a0': [(log, ('2.8: Yixuan Body texcoord_vb',))],
'3e629c05': [(log, ('2.8: Yixuan Body blend_vb',))],

# Bottle (葫芦 - v2.5 -> v2.8)
'05466ddf': [(log, ('2.8: Yixuan Bottle draw_vb',))],
'8555098d': [(log, ('2.8: Yixuan Bottle position_vb',))],
'ff4b112b': [(log, ('2.8: Yixuan Bottle texcoord_vb',))],
'd89da8eb': [(log, ('2.8: Yixuan Bottle blend_vb',))],

# Coins (铜钱绳)
'ddaf88bc': [(log, ('2.8: Yixuan Coins draw_vb',))],
'eaf79039': [(log, ('2.8: Yixuan Coins position_vb',))],
'9714e6e6': [(log, ('2.8: Yixuan Coins texcoord_vb',))],
'ee9b9cfe': [(log, ('2.8: Yixuan Coins blend_vb',))],

# Hairpin (发簪)
'ba017cf3': [(log, ('2.8: Yixuan Hairpin draw_vb',))],
'3194141e': [(log, ('2.8: Yixuan Hairpin position_vb',))],
'b3123168': [(log, ('2.8: Yixuan Hairpin texcoord_vb',))],
'de9d3ab7': [(log, ('2.8: Yixuan Hairpin blend_vb',))],

# Jacket (夹克)
'73599fbb': [(log, ('2.8: Yixuan Jacket draw_vb',))],
'9b67bc72': [(log, ('2.8: Yixuan Jacket position_vb',))],
'9f95d565': [(log, ('2.8: Yixuan Jacket texcoord_vb',))],
'0ff3af5a': [(log, ('2.8: Yixuan Jacket blend_vb',))],

# Face (脸)
'972e4b6d': [(log, ('2.8: Yixuan Face position_vb',))],
'2e04aac2': [(log, ('2.8: Yixuan Face texcoord_vb',))],
'4466e7ea': [(log, ('2.8: Yixuan Face blend_vb',))],

# Weapon Bird (武器鸟 - non-combat)
'9052084b': [(log, ('2.8: Yixuan WeaponBird position_vb (Idle)',))],
'f45313a0': [(log, ('2.8: Yixuan WeaponBird texcoord_vb (Idle)',))],
'3ac6dfc7': [(log, ('2.8: Yixuan WeaponBird blend_vb (Idle)',))],

# Weapon Bird (武器鸟 - combat)
'1a201296': [(log, ('2.8: Yixuan WeaponBird position_vb (Combat)',))],
'1a0934e4': [(log, ('2.8: Yixuan WeaponBird texcoord_vb (Combat)',))],
'2ad5c986': [(log, ('2.8: Yixuan WeaponBird blend_vb (Combat)',))],

# === TEXTURE HASHES ===
# Shared NormalMap
'798adba3': [
        (log,                           ('2.8: Yixuan Shared NormalMap',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],

# Hair, Bottle, Coins Shared Textures
'84fe943d': [
        (log,                           ('2.8: Yixuan Hair/Bottle/Coins Diffuse Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
    ],
'5574ca9f': [
        (log,                           ('2.8: Yixuan Hair/Bottle/Coins LightMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
    ],
'f4ac690c': [
        (log,                           ('2.8: Yixuan Hair/Bottle/Coins MaterialMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
    ],

# Body and Hairpin Shared Textures
'd7db2bc6': [
        (log,                           ('2.8: Yixuan Body/Hairpin Diffuse Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'96f754a7': [
        (log,                           ('2.8: Yixuan Body/Hairpin LightMap Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'aa1056a5': [
        (log,                           ('2.8: Yixuan Body/Hairpin MaterialMap Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],

# Jacket Textures
'1fcedcc3': [
        (log,                           ('2.8: Yixuan Jacket Diffuse Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'c4d167c3': [
        (log,                           ('2.8: Yixuan Jacket LightMap Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'fd56fa4b': [
        (log,                           ('2.8: Yixuan Jacket MaterialMap Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],

# Face Textures (v2.5 -> v2.8)
'7d9ee001': [
        (log,                           ('2.5 -> 2.8: Yixuan Face Diffuse Hash',)),
        (update_hash,                   ('9efd1605',)),
    ],
'9efd1605': [
        (log,                           ('2.8: Yixuan Face Diffuse Hash (Target)',)),
        (add_section_if_missing,        ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
    ],

# Weapon Bird (Idle) Textures
'677893d2': [
        (log,                           ('2.8: Yixuan WeaponBird Diffuse Hash (Idle)',)),
        (add_section_if_missing,        ('ce38ac3b', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'd1ee41dc': [
        (log,                           ('2.8: Yixuan WeaponBird LightMap Hash (Idle)',)),
        (add_section_if_missing,        ('ce38ac3b', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'23d4f666': [
        (log,                           ('2.8: Yixuan WeaponBird MaterialMap Hash (Idle)',)),
        (add_section_if_missing,        ('ce38ac3b', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],

# Weapon Bird (Combat) Textures
'9263dc92': [
        (log,                           ('2.8: Yixuan WeaponBird Diffuse Hash (Combat)',)),
        (add_section_if_missing,        ('fd2cbc71', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'fc9ae2ff': [
        (log,                           ('2.8: Yixuan WeaponBird LightMap Hash (Combat)',)),
        (add_section_if_missing,        ('fd2cbc71', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'5e60bc3d': [
        (log,                           ('2.8: Yixuan WeaponBird MaterialMap Hash (Combat)',)),
        (add_section_if_missing,        ('fd2cbc71', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],

# === HISTORICAL UPDATES (v1.0 -> v2.8) ===
'0219df6e': [(log, ('1.0 -> 2.8: Yixuan Bottle IB Hash',)),           (update_hash, ('1630f2d0',))],
'55638d51': [(log, ('1.0 -> 2.8: Yixuan Bottle Blend Hash',)),        (update_hash, ('d89da8eb',))],
'd0ff2c18': [(log, ('1.0 -> 2.8: Yixuan Bottle Position Hash',)),     (update_hash, ('8555098d',))],
'f05da93a': [(log, ('1.0 -> 2.8: Yixuan Bottle Texcoord Hash',)),     (update_hash, ('ff4b112b',))],
'd000beae': [(log, ('1.0 -> 2.8: Yixuan Bottle Draw Hash',)),         (update_hash, ('05466ddf',))],

# === New Database 2.8 Synced Base Texture Hashes ===
'7e38b38b': [
        (log,                           ('2.8: Yixuan Hair Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'086ac064': [
        (log,                           ('2.8: Yixuan Hair LightMap Hash [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'83b02982': [
        (log,                           ('2.8: Yixuan Hair MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'2a4f37a6': [
        (log,                           ('2.8: Yixuan Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'5a291e85': [
        (log,                           ('2.8: Yixuan Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'd28370ec': [
        (log,                           ('2.8: Yixuan Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'e6dca725': [
        (log,                           ('2.8: Yixuan Jacket Diffuse Hash [New]',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'59b2daf9': [
        (log,                           ('2.8: Yixuan Jacket LightMap Hash [New]',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'bb581f1e': [
        (log,                           ('2.8: Yixuan Jacket MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'920caf66': [
        (log,                           ('2.8: Yixuan WeaponBird Idle Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ce38ac3b', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'771d52eb': [
        (log,                           ('2.8: Yixuan WeaponBird Idle LightMap Hash [New]',)),
        (add_section_if_missing,        ('ce38ac3b', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'dc3c5667': [
        (log,                           ('2.8: Yixuan WeaponBird Idle MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ce38ac3b', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'7f504f10': [
        (log,                           ('2.8: Yixuan WeaponBird Combat Diffuse Hash [New]',)),
        (add_section_if_missing,        ('fd2cbc71', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'96254967': [
        (log,                           ('2.8: Yixuan WeaponBird Combat LightMap Hash [New]',)),
        (add_section_if_missing,        ('fd2cbc71', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'4300c703': [
        (log,                           ('2.8: Yixuan WeaponBird Combat MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('fd2cbc71', 'Yixuan.WeaponBird.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Yixuan Shared NormalMap [New]',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Yixuan',
    'game_versions': ['2.8', '3.0'],
}