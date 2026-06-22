"""
Sunna Character Hash Commands
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
    Returns Sunna's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'904ecd0f': [(log, ('2.8: Sunna Hair IB Hash',)),              (add_ib_check_if_missing,)],
'3ab6d438': [(log, ('2.8: Sunna HairShadow IB Hash',)),        (add_ib_check_if_missing,)],
'b3c6ea5a': [(log, ('2.8: Sunna Body IB Hash',)),              (add_ib_check_if_missing,)],
'30ea5791': [(log, ('2.8: Sunna Eyebrow IB Hash',)),           (add_ib_check_if_missing,)],
'1a2c8573': [(log, ('2.8: Sunna Face IB Hash',)),              (add_ib_check_if_missing,)],
'0b9bd38f': [(log, ('2.8: Sunna DisplayScreen IB Hash',)),     (add_ib_check_if_missing,)],
'337a62c1': [(log, ('2.8: Sunna WeaponBackpack IB Hash',)),    (add_ib_check_if_missing,)],
'e7a17172': [(log, ('2.8: Sunna PaopaoFight IB Hash',)),       (add_ib_check_if_missing,)],
'07a82c9c': [(log, ('2.8: Sunna PaopaoIdle IB Hash',)),        (add_ib_check_if_missing,)],
'c811c294': [(log, ('2.8: Sunna Weapon IB Hash',)),            (add_ib_check_if_missing,)],
'0a237cd3': [(log, ('2.8: Sunna WeaponDeco1 IB Hash',)),       (add_ib_check_if_missing,)],
'8ad8f57d': [(log, ('2.8: Sunna WeaponDeco2 IB Hash',)),       (add_ib_check_if_missing,)],

# === PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT) ===
# Hair VBs
'cc070c66': [(log, ('2.8: Sunna Hair draw_vb',))],
'5c030eea': [(log, ('2.8: Sunna Hair position_vb',))],
'06bea24e': [(log, ('2.8: Sunna Hair texcoord_vb',))],
'0c183c3f': [(log, ('2.8: Sunna Hair blend_vb',))],

# Body VBs
'8991360f': [(log, ('2.8: Sunna Body draw_vb',))],
'6eb68b62': [(log, ('2.8: Sunna Body position_vb',))],
'712eb020': [(log, ('2.8: Sunna Body texcoord_vb',))],
'53661c9a': [(log, ('2.8: Sunna Body blend_vb',))],

# Eyebrow VBs
'9f0ab8cd': [(log, ('2.8: Sunna Eyebrow draw_vb',))],
'a5182b8a': [(log, ('2.8: Sunna Eyebrow position_vb',))],
'e3cc1981': [(log, ('2.8: Sunna Eyebrow texcoord_vb',))],
'f5daa764': [(log, ('2.8: Sunna Eyebrow blend_vb',))],

# Face VBs
'9679c257': [(log, ('2.8: Sunna Face draw_vb',))],
'ac6b5110': [(log, ('2.8: Sunna Face position_vb',))],
'506dc9e1': [(log, ('2.8: Sunna Face texcoord_vb',))],
'21299f88': [(log, ('2.8: Sunna Face blend_vb',))],

# DisplayScreen VBs
'dd676093': [(log, ('2.8: Sunna DisplayScreen draw_vb',))],
'6f7ae47c': [(log, ('2.8: Sunna DisplayScreen position_vb',))],
'541d5b0f': [(log, ('2.8: Sunna DisplayScreen texcoord_vb',))],
'2ef8be58': [(log, ('2.8: Sunna DisplayScreen blend_vb',))],

# WeaponBackpack VBs
'953975c0': [(log, ('2.8: Sunna WeaponBackpack draw_vb',))],
'a28ba31c': [(log, ('2.8: Sunna WeaponBackpack position_vb',))],
'b642db41': [(log, ('2.8: Sunna WeaponBackpack texcoord_vb',))],
'16e2d8ea': [(log, ('2.8: Sunna WeaponBackpack blend_vb',))],

# Paopao (Fight) VBs
'ffe207d5': [(log, ('2.8: Sunna PaopaoFight draw_vb',))],
'3a7143a6': [(log, ('2.8: Sunna PaopaoFight position_vb',))],
'62519e38': [(log, ('2.8: Sunna PaopaoFight texcoord_vb',))],
'38e2fe9f': [(log, ('2.8: Sunna PaopaoFight blend_vb',))],

# Paopao (Idle) VBs
'1a0cad46': [(log, ('2.8: Sunna PaopaoIdle position_vb',))],
'df0f6142': [(log, ('2.8: Sunna PaopaoIdle texcoord_vb',))],
'd4e13802': [(log, ('2.8: Sunna PaopaoIdle blend_vb',))],

# Hammer VBs
'6cbdb4d3': [(log, ('2.8: Sunna Weapon draw_vb',))],
'9220fbd5': [(log, ('2.8: Sunna Weapon position_vb',))],
'5d7fdc2e': [(log, ('2.8: Sunna Weapon texcoord_vb',))],
'4b46dfdc': [(log, ('2.8: Sunna Weapon blend_vb',))],

# HammerDeco1 VBs
'dab9d122': [(log, ('2.8: Sunna WeaponDeco1 draw_vb',))],
'0a41bae7': [(log, ('2.8: Sunna WeaponDeco1 position_vb',))],
'34dc63b4': [(log, ('2.8: Sunna WeaponDeco1 texcoord_vb',))],
'a5ecc7ea': [(log, ('2.8: Sunna WeaponDeco1 blend_vb',))],

# HammerDeco2 VBs
'84a9dfca': [(log, ('2.8: Sunna WeaponDeco2 draw_vb',))],
'81321ee9': [(log, ('2.8: Sunna WeaponDeco2 position_vb',))],
'33a66c47': [(log, ('2.8: Sunna WeaponDeco2 texcoord_vb',))],
'0d2178c5': [(log, ('2.8: Sunna WeaponDeco2 blend_vb',))],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: Sunna Shared NormalMap Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Sunna.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Sunna.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],

# === Face & Eyebrow Textures ===
'1ef66a60': [
        (log,                           ('2.8: Sunna FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'e85201e7': [
        (log,                           ('2.8: Sunna HairA Diffuse Hash',)),
        (add_section_if_missing,        ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'a2b36369': [
        (log,                           ('2.8: Sunna HairA LightMap Hash',)),
        (add_section_if_missing,        ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'ab3c12c0': [
        (log,                           ('2.8: Sunna HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'aa0f48fe': [
        (log,                           ('2.8: Sunna BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'3987c8c2': [
        (log,                           ('2.8: Sunna BodyA LightMap Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'1d459d73': [
        (log,                           ('2.8: Sunna BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],

# === Backpack Textures ===
'bde1bdad': [
        (log,                           ('2.8: Sunna WeaponBackpack Diffuse Hash',)),
        (add_section_if_missing,        ('337a62c1', 'Sunna.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'9368a6f9': [
        (log,                           ('2.8: Sunna WeaponBackpack LightMap Hash',)),
        (add_section_if_missing,        ('337a62c1', 'Sunna.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'508c297c': [
        (log,                           ('2.8: Sunna WeaponBackpack MaterialMap Hash',)),
        (add_section_if_missing,        ('337a62c1', 'Sunna.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],

# === Paopao Shared Textures (Fight & Idle state) ===
'be5cd451': [
        (log,                           ('2.8: Sunna Paopao Diffuse Hash',)),
        (add_section_if_missing,        ('e7a17172', 'Sunna.PaopaoFight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07a82c9c', 'Sunna.PaopaoIdle.IB', 'match_priority = 0\n')),
    ],
'945afd67': [
        (log,                           ('2.8: Sunna Paopao LightMap Hash',)),
        (add_section_if_missing,        ('e7a17172', 'Sunna.PaopaoFight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07a82c9c', 'Sunna.PaopaoIdle.IB', 'match_priority = 0\n')),
    ],
'e9783f84': [
        (log,                           ('2.8: Sunna Paopao MaterialMap Hash',)),
        (add_section_if_missing,        ('e7a17172', 'Sunna.PaopaoFight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07a82c9c', 'Sunna.PaopaoIdle.IB', 'match_priority = 0\n')),
    ],

# === Weapon & Decoration Shared Textures ===
'b9d9b7a7': [
        (log,                           ('2.8: Sunna Weapon, WeaponDeco Diffuse Hash',)),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Sunna.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Sunna.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],
'6c369f22': [
        (log,                           ('2.8: Sunna Weapon, WeaponDeco LightMap Hash',)),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Sunna.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Sunna.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],
'15cd94f7': [
        (log,                           ('2.8: Sunna Weapon, WeaponDeco MaterialMap Hash',)),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Sunna.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Sunna.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Sunna hashes ===
'2fcfee64': [
        (log,                           ('2.8: Sunna Hair Alternate Diffuse Hash [New]',)),
        (add_section_if_missing,        ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'8cd786f7': [
        (log,                           ('2.8: Sunna Hair Alternate LightMap Hash [New]',)),
        (add_section_if_missing,        ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'3f11dfd9': [
        (log,                           ('2.8: Sunna Hair Alternate MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'f051c211': [
        (log,                           ('2.8: Sunna Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'4aca364a': [
        (log,                           ('2.8: Sunna Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'f3f8895c': [
        (log,                           ('2.8: Sunna Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'c9b5c6ce': [
        (log,                           ('2.8: Sunna Face Diffuse Hash [New]',)),
        (add_section_if_missing,        ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
    ],
'6c04b56d': [
        (log,                           ('2.8: Sunna Backpack Diffuse Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'Sunna.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'39dac70b': [
        (log,                           ('2.8: Sunna Backpack LightMap Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'Sunna.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'95070f7f': [
        (log,                           ('2.8: Sunna Backpack MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'Sunna.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'7d8ac131': [
        (log,                           ('2.8: Sunna Paopao Diffuse Hash [New]',)),
        (add_section_if_missing,        (('e7a17172', '07a82c9c'), 'Sunna.Paopao.IB', 'match_priority = 0\n')),
    ],
'5c5b6aad': [
        (log,                           ('2.8: Sunna Paopao LightMap Hash [New]',)),
        (add_section_if_missing,        (('e7a17172', '07a82c9c'), 'Sunna.Paopao.IB', 'match_priority = 0\n')),
    ],
'3c4378db': [
        (log,                           ('2.8: Sunna Paopao MaterialMap Hash [New]',)),
        (add_section_if_missing,        (('e7a17172', '07a82c9c'), 'Sunna.Paopao.IB', 'match_priority = 0\n')),
    ],
'003c6497': [
        (log,                           ('2.8: Sunna Hammer Diffuse Hash [New]',)),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'4b4975a2': [
        (log,                           ('2.8: Sunna Hammer LightMap Hash [New]',)),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'635f5cc9': [
        (log,                           ('2.8: Sunna Hammer MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Sunna Shared NormalMap [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Sunna',
    'game_versions': ['2.8', '3.0'],
}