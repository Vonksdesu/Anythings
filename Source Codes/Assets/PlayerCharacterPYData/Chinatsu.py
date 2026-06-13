"""
Chinatsu Character Hash Commands
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
    Returns Chinatsu's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'904ecd0f': [(log, ('2.8: Chinatsu Hair IB Hash',)),              (add_ib_check_if_missing,)],
'3ab6d438': [(log, ('2.8: Chinatsu HairShadow IB Hash',)),        (add_ib_check_if_missing,)],
'b3c6ea5a': [(log, ('2.8: Chinatsu Body IB Hash',)),              (add_ib_check_if_missing,)],
'30ea5791': [(log, ('2.8: Chinatsu Eyebrow IB Hash',)),           (add_ib_check_if_missing,)],
'1a2c8573': [(log, ('2.8: Chinatsu Face IB Hash',)),              (add_ib_check_if_missing,)],
'0b9bd38f': [(log, ('2.8: Chinatsu DisplayScreen IB Hash',)),     (add_ib_check_if_missing,)],
'337a62c1': [(log, ('2.8: Chinatsu WeaponBackpack IB Hash',)),    (add_ib_check_if_missing,)],
'e7a17172': [(log, ('2.8: Chinatsu PaopaoFight IB Hash',)),       (add_ib_check_if_missing,)],
'07a82c9c': [(log, ('2.8: Chinatsu PaopaoIdle IB Hash',)),        (add_ib_check_if_missing,)],
'c811c294': [(log, ('2.8: Chinatsu Weapon IB Hash',)),            (add_ib_check_if_missing,)],
'0a237cd3': [(log, ('2.8: Chinatsu WeaponDeco1 IB Hash',)),       (add_ib_check_if_missing,)],
'8ad8f57d': [(log, ('2.8: Chinatsu WeaponDeco2 IB Hash',)),       (add_ib_check_if_missing,)],

# === PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT) ===
# Hair VBs
'cc070c66': [(log, ('2.8: Chinatsu Hair draw_vb',))],
'5c030eea': [(log, ('2.8: Chinatsu Hair position_vb',))],
'06bea24e': [(log, ('2.8: Chinatsu Hair texcoord_vb',))],
'0c183c3f': [(log, ('2.8: Chinatsu Hair blend_vb',))],

# Body VBs
'8991360f': [(log, ('2.8: Chinatsu Body draw_vb',))],
'6eb68b62': [(log, ('2.8: Chinatsu Body position_vb',))],
'712eb020': [(log, ('2.8: Chinatsu Body texcoord_vb',))],
'53661c9a': [(log, ('2.8: Chinatsu Body blend_vb',))],

# Eyebrow VBs
'9f0ab8cd': [(log, ('2.8: Chinatsu Eyebrow draw_vb',))],
'a5182b8a': [(log, ('2.8: Chinatsu Eyebrow position_vb',))],
'e3cc1981': [(log, ('2.8: Chinatsu Eyebrow texcoord_vb',))],
'f5daa764': [(log, ('2.8: Chinatsu Eyebrow blend_vb',))],

# Face VBs
'9679c257': [(log, ('2.8: Chinatsu Face draw_vb',))],
'ac6b5110': [(log, ('2.8: Chinatsu Face position_vb',))],
'506dc9e1': [(log, ('2.8: Chinatsu Face texcoord_vb',))],
'21299f88': [(log, ('2.8: Chinatsu Face blend_vb',))],

# DisplayScreen VBs
'dd676093': [(log, ('2.8: Chinatsu DisplayScreen draw_vb',))],
'6f7ae47c': [(log, ('2.8: Chinatsu DisplayScreen position_vb',))],
'541d5b0f': [(log, ('2.8: Chinatsu DisplayScreen texcoord_vb',))],
'2ef8be58': [(log, ('2.8: Chinatsu DisplayScreen blend_vb',))],

# WeaponBackpack VBs
'953975c0': [(log, ('2.8: Chinatsu WeaponBackpack draw_vb',))],
'a28ba31c': [(log, ('2.8: Chinatsu WeaponBackpack position_vb',))],
'b642db41': [(log, ('2.8: Chinatsu WeaponBackpack texcoord_vb',))],
'16e2d8ea': [(log, ('2.8: Chinatsu WeaponBackpack blend_vb',))],

# Paopao (Fight) VBs
'ffe207d5': [(log, ('2.8: Chinatsu PaopaoFight draw_vb',))],
'3a7143a6': [(log, ('2.8: Chinatsu PaopaoFight position_vb',))],
'62519e38': [(log, ('2.8: Chinatsu PaopaoFight texcoord_vb',))],
'38e2fe9f': [(log, ('2.8: Chinatsu PaopaoFight blend_vb',))],

# Paopao (Idle) VBs
'1a0cad46': [(log, ('2.8: Chinatsu PaopaoIdle position_vb',))],
'df0f6142': [(log, ('2.8: Chinatsu PaopaoIdle texcoord_vb',))],
'd4e13802': [(log, ('2.8: Chinatsu PaopaoIdle blend_vb',))],

# Hammer VBs
'6cbdb4d3': [(log, ('2.8: Chinatsu Weapon draw_vb',))],
'9220fbd5': [(log, ('2.8: Chinatsu Weapon position_vb',))],
'5d7fdc2e': [(log, ('2.8: Chinatsu Weapon texcoord_vb',))],
'4b46dfdc': [(log, ('2.8: Chinatsu Weapon blend_vb',))],

# HammerDeco1 VBs
'dab9d122': [(log, ('2.8: Chinatsu WeaponDeco1 draw_vb',))],
'0a41bae7': [(log, ('2.8: Chinatsu WeaponDeco1 position_vb',))],
'34dc63b4': [(log, ('2.8: Chinatsu WeaponDeco1 texcoord_vb',))],
'a5ecc7ea': [(log, ('2.8: Chinatsu WeaponDeco1 blend_vb',))],

# HammerDeco2 VBs
'84a9dfca': [(log, ('2.8: Chinatsu WeaponDeco2 draw_vb',))],
'81321ee9': [(log, ('2.8: Chinatsu WeaponDeco2 position_vb',))],
'33a66c47': [(log, ('2.8: Chinatsu WeaponDeco2 texcoord_vb',))],
'0d2178c5': [(log, ('2.8: Chinatsu WeaponDeco2 blend_vb',))],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: Chinatsu Shared NormalMap Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Chinatsu.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Chinatsu.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],

# === Face & Eyebrow Textures ===
'1ef66a60': [
        (log,                           ('2.8: Chinatsu FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('1a2c8573', 'Chinatsu.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30ea5791', 'Chinatsu.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'e85201e7': [
        (log,                           ('2.8: Chinatsu HairA Diffuse Hash',)),
        (add_section_if_missing,        ('904ecd0f', 'Chinatsu.Hair.IB', 'match_priority = 0\n')),
    ],
'a2b36369': [
        (log,                           ('2.8: Chinatsu HairA LightMap Hash',)),
        (add_section_if_missing,        ('904ecd0f', 'Chinatsu.Hair.IB', 'match_priority = 0\n')),
    ],
'ab3c12c0': [
        (log,                           ('2.8: Chinatsu HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('904ecd0f', 'Chinatsu.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'aa0f48fe': [
        (log,                           ('2.8: Chinatsu BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],
'3987c8c2': [
        (log,                           ('2.8: Chinatsu BodyA LightMap Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],
'1d459d73': [
        (log,                           ('2.8: Chinatsu BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],

# === Backpack Textures ===
'bde1bdad': [
        (log,                           ('2.8: Chinatsu WeaponBackpack Diffuse Hash',)),
        (add_section_if_missing,        ('337a62c1', 'Chinatsu.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'9368a6f9': [
        (log,                           ('2.8: Chinatsu WeaponBackpack LightMap Hash',)),
        (add_section_if_missing,        ('337a62c1', 'Chinatsu.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'508c297c': [
        (log,                           ('2.8: Chinatsu WeaponBackpack MaterialMap Hash',)),
        (add_section_if_missing,        ('337a62c1', 'Chinatsu.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],

# === Paopao Shared Textures (Fight & Idle state) ===
'be5cd451': [
        (log,                           ('2.8: Chinatsu Paopao Diffuse Hash',)),
        (add_section_if_missing,        ('e7a17172', 'Chinatsu.PaopaoFight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07a82c9c', 'Chinatsu.PaopaoIdle.IB', 'match_priority = 0\n')),
    ],
'945afd67': [
        (log,                           ('2.8: Chinatsu Paopao LightMap Hash',)),
        (add_section_if_missing,        ('e7a17172', 'Chinatsu.PaopaoFight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07a82c9c', 'Chinatsu.PaopaoIdle.IB', 'match_priority = 0\n')),
    ],
'e9783f84': [
        (log,                           ('2.8: Chinatsu Paopao MaterialMap Hash',)),
        (add_section_if_missing,        ('e7a17172', 'Chinatsu.PaopaoFight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07a82c9c', 'Chinatsu.PaopaoIdle.IB', 'match_priority = 0\n')),
    ],

# === Weapon & Decoration Shared Textures ===
'b9d9b7a7': [
        (log,                           ('2.8: Chinatsu Weapon, WeaponDeco Diffuse Hash',)),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Chinatsu.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Chinatsu.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],
'6c369f22': [
        (log,                           ('2.8: Chinatsu Weapon, WeaponDeco LightMap Hash',)),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Chinatsu.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Chinatsu.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],
'15cd94f7': [
        (log,                           ('2.8: Chinatsu Weapon, WeaponDeco MaterialMap Hash',)),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a237cd3', 'Chinatsu.WeaponDeco1.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ad8f57d', 'Chinatsu.WeaponDeco2.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Chinatsu hashes ===
'2fcfee64': [
        (log,                           ('2.8: Chinatsu Hair Alternate Diffuse Hash [New]',)),
        (add_section_if_missing,        ('904ecd0f', 'Chinatsu.Hair.IB', 'match_priority = 0\n')),
    ],
'8cd786f7': [
        (log,                           ('2.8: Chinatsu Hair Alternate LightMap Hash [New]',)),
        (add_section_if_missing,        ('904ecd0f', 'Chinatsu.Hair.IB', 'match_priority = 0\n')),
    ],
'3f11dfd9': [
        (log,                           ('2.8: Chinatsu Hair Alternate MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('904ecd0f', 'Chinatsu.Hair.IB', 'match_priority = 0\n')),
    ],
'f051c211': [
        (log,                           ('2.8: Chinatsu Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],
'4aca364a': [
        (log,                           ('2.8: Chinatsu Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],
'f3f8895c': [
        (log,                           ('2.8: Chinatsu Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],
'c9b5c6ce': [
        (log,                           ('2.8: Chinatsu Face Diffuse Hash [New]',)),
        (add_section_if_missing,        ('1a2c8573', 'Chinatsu.Face.IB', 'match_priority = 0\n')),
    ],
'6c04b56d': [
        (log,                           ('2.8: Chinatsu Backpack Diffuse Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'Chinatsu.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'39dac70b': [
        (log,                           ('2.8: Chinatsu Backpack LightMap Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'Chinatsu.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'95070f7f': [
        (log,                           ('2.8: Chinatsu Backpack MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'Chinatsu.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'7d8ac131': [
        (log,                           ('2.8: Chinatsu Paopao Diffuse Hash [New]',)),
        (add_section_if_missing,        (('e7a17172', '07a82c9c'), 'Chinatsu.Paopao.IB', 'match_priority = 0\n')),
    ],
'5c5b6aad': [
        (log,                           ('2.8: Chinatsu Paopao LightMap Hash [New]',)),
        (add_section_if_missing,        (('e7a17172', '07a82c9c'), 'Chinatsu.Paopao.IB', 'match_priority = 0\n')),
    ],
'3c4378db': [
        (log,                           ('2.8: Chinatsu Paopao MaterialMap Hash [New]',)),
        (add_section_if_missing,        (('e7a17172', '07a82c9c'), 'Chinatsu.Paopao.IB', 'match_priority = 0\n')),
    ],
'003c6497': [
        (log,                           ('2.8: Chinatsu Hammer Diffuse Hash [New]',)),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
    ],
'4b4975a2': [
        (log,                           ('2.8: Chinatsu Hammer LightMap Hash [New]',)),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
    ],
'635f5cc9': [
        (log,                           ('2.8: Chinatsu Hammer MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('c811c294', 'Chinatsu.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Chinatsu Shared NormalMap [New]',)),
        (add_section_if_missing,        ('b3c6ea5a', 'Chinatsu.Body.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Chinatsu',
    'game_versions': ['2.8'],
}