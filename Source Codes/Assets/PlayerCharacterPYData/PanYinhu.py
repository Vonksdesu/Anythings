"""
PanYinhu Character Hash Commands
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
    Returns PanYinhu's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'cb1a6db9': [(log, ('2.8: PanYinhu Body IB Hash',)),                      (add_ib_check_if_missing,)],
'ff7e9b40': [(log, ('2.8: PanYinhu Hat IB Hash',)),                       (add_ib_check_if_missing,)],
'ebb6a59b': [(log, ('2.8: PanYinhu Face IB Hash',)),                      (add_ib_check_if_missing,)],
'b3556f6e': [(log, ('2.8: PanYinhu Weapon Bun IB Hash',)),                (add_ib_check_if_missing,)],
'45a8cd1b': [(log, ('2.8: PanYinhu Weapon Ladle IB Hash',)),              (add_ib_check_if_missing,)],

# === VB Hashes ===
# Body
'b375f26b': [(log, ('2.8: PanYinhu Body draw_vb Hash',)),                 (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n'))],
'aba31d2e': [(log, ('2.8: PanYinhu Body position_vb Hash',)),             (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n'))],
'cc541390': [(log, ('2.8: PanYinhu Body texcoord_vb Hash',)),             (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n'))],
'4727992f': [(log, ('2.8: PanYinhu Body blend_vb Hash',)),                (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n'))],

# Weapon - Bun (weapon武器-馒头)
'534c2f9b': [(log, ('2.8: PanYinhu Bun draw_vb Hash',)),                 (add_section_if_missing, ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n'))],
'4864dcdd': [(log, ('2.8: PanYinhu Bun position_vb Hash',)),             (add_section_if_missing, ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n'))],
'a6f599e3': [(log, ('2.8: PanYinhu Bun texcoord_vb Hash',)),             (add_section_if_missing, ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n'))],
'b88cf297': [(log, ('2.8: PanYinhu Bun blend_vb Hash',)),                (add_section_if_missing, ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n'))],

# Face
'682e8e8d': [(log, ('2.8: PanYinhu Face draw_vb Hash',)),                 (add_section_if_missing, ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n'))],
'1eee2121': [(log, ('2.8: PanYinhu Face texcoord_vb Hash',)),             (add_section_if_missing, ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n'))],
'4aae3329': [(log, ('2.8: PanYinhu Face blend_vb Hash',)),                (add_section_if_missing, ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n'))],

# Weapon - Ladle (weapon-武器-炒勺)
'2a45b03d': [(log, ('2.8: PanYinhu Ladle draw_vb Hash',)),               (add_section_if_missing, ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n'))],
'e56ae11f': [(log, ('2.8: PanYinhu Ladle position_vb Hash',)),           (add_section_if_missing, ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n'))],
'1a769e88': [(log, ('2.8: PanYinhu Ladle texcoord_vb Hash',)),           (add_section_if_missing, ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n'))],
'cd763e6d': [(log, ('2.8: PanYinhu Ladle blend_vb Hash',)),              (add_section_if_missing, ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n'))],

# Weapon - Wok (weapon-武器-炒锅)
'2e2d67ae': [(log, ('2.8: PanYinhu Wok draw_vb Hash',)),                 (add_section_if_missing, ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n'))],
'0ee4a87c': [(log, ('2.8: PanYinhu Wok position_vb Hash',)),             (add_section_if_missing, ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n'))],
'd569d88e': [(log, ('2.8: PanYinhu Wok texcoord_vb Hash',)),             (add_section_if_missing, ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n'))],
'd141908c': [(log, ('2.8: PanYinhu Wok blend_vb Hash',)),                (add_section_if_missing, ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n'))],

# === Bun & Body A/B + Hat B Shared Textures ===
'b20c7e8b': [
        (log,                           ('2.8: PanYinhu Bun & Body Diffuse Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n')),
    ],
'c0928025': [
        (log,                           ('2.8: PanYinhu Body A/B + Hat B Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'7967c15f': [
        (log,                           ('2.8: PanYinhu Bun & Body LightMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n')),
    ],
'7d3c4c3d': [
        (log,                           ('2.8: PanYinhu Body A/B + Hat B LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'2daeed33': [
        (log,                           ('2.8: PanYinhu Bun & Body MaterialMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n')),
    ],
'42fc25f0': [
        (log,                           ('2.8: PanYinhu Body A/B + Hat B MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],

# === Body C + Hat A, Ladle & Wok Shared Textures ===
'cf6afa84': [
        (log,                           ('2.8: PanYinhu Body C, Ladle, Wok Diffuse Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n')),
    ],
'f2433e17': [
        (log,                           ('2.8: PanYinhu Body C + Hat A Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'26454e30': [
        (log,                           ('2.8: PanYinhu Body C, Ladle, Wok LightMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n')),
    ],
'ddeaa4c3': [
        (log,                           ('2.8: PanYinhu Body C + Hat A LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],
'e0433c18': [
        (log,                           ('2.8: PanYinhu Body C, Ladle, Wok MaterialMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n')),
    ],
'de553410': [
        (log,                           ('2.8: PanYinhu Body C + Hat A MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
    ],

# === Body D + Face A Textures (Shared) ===
'452a0918': [
        (log,                           ('2.8: PanYinhu Face Diffuse Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'ed361b8f': [
        (log,                           ('2.8: PanYinhu Body D + Face A Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'3744882e': [
        (log,                           ('2.8: PanYinhu Face LightMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'96280008': [
        (log,                           ('2.8: PanYinhu Body D + Face A LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'18dd19bf': [
        (log,                           ('2.8: PanYinhu Face MaterialMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'57446a22': [
        (log,                           ('2.8: PanYinhu Body D + Face A MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: PanYinhu Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3556f6e', 'PanYinhu.WeaponBun.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('45a8cd1b', 'PanYinhu.WeaponLadle.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: PanYinhu Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhu',
    'game_versions': ['2.8'],
    'components': ['Body', 'Hat', 'Face'],
    'variants': {
        'Body': ['A', 'B', 'C', 'D'],
        'Hat': ['A', 'B'],
        'Face': ['A']
    },
}