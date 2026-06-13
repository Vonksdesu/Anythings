"""
ChinatsuSkin Character Hash Commands
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
    Returns ChinatsuSkin's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'a6d82ba5': [(log, ('2.8: ChinatsuSkin Hair IB Hash',)),           (add_ib_check_if_missing,)],
'4803b5d7': [(log, ('2.8: ChinatsuSkin HairShadow IB Hash',)),     (add_ib_check_if_missing,)],
'ee17c9a2': [(log, ('2.8: ChinatsuSkin Body IB Hash',)),           (add_ib_check_if_missing,)],
'30ea5791': [(log, ('2.8: ChinatsuSkin Eyebrow IB Hash',)),        (add_ib_check_if_missing,)],
'1a2c8573': [(log, ('2.8: ChinatsuSkin Face IB Hash',)),           (add_ib_check_if_missing,)],
'337a62c1': [(log, ('2.8: ChinatsuSkin WeaponBackpack IB Hash',)), (add_ib_check_if_missing,)],
'07a82c9c': [(log, ('2.8: ChinatsuSkin Paopao IB Hash',)),         (add_ib_check_if_missing,)],

# === Hash update 2.6 -> 2.8: ChinatsuSkin Hair IB + VB hashes ===
'6cc4d486': [(log, ('2.6 -> 2.8: ChinatsuSkin Hair IB Hash',)),       (update_hash, ('a6d82ba5',))],
'22c82346': [(log, ('2.6 -> 2.8: ChinatsuSkin Hair Draw Hash',)),      (update_hash, ('74cc56df',))],
'327644ee': [(log, ('2.6 -> 2.8: ChinatsuSkin Hair Position Hash',)),  (update_hash, ('4b93d8eb',))],
'5e70dde6': [(log, ('2.6 -> 2.8: ChinatsuSkin Hair Texcoord Hash',)),  (update_hash, ('b9030f86',))],
'79de92c7': [(log, ('2.6 -> 2.8: ChinatsuSkin Hair Blend Hash',)),     (update_hash, ('4a795f2a',))],
'c77b3235': [(log, ('2.6 -> 2.8: ChinatsuSkin Body Position Hash',)),  (update_hash, ('25cf6bf7',))],
'0c6b95ca': [(log, ('2.6 -> 2.8: ChinatsuSkin Body Texcoord Hash',)),  (update_hash, ('7a31eb8b',))],

# === Target Hashes (Penyelarasan Validasi) ===
'74cc56df': [(log, ('2.8: ChinatsuSkin Hair Draw Hash (Target)',))],
'4b93d8eb': [(log, ('2.8: ChinatsuSkin Hair Position Hash (Target)',))],
'b9030f86': [(log, ('2.8: ChinatsuSkin Hair Texcoord Hash (Target)',))],
'4a795f2a': [(log, ('2.8: ChinatsuSkin Hair Blend Hash (Target)',))],
'25cf6bf7': [(log, ('2.8: ChinatsuSkin Body Position Hash (Target)',))],
'7a31eb8b': [(log, ('2.8: ChinatsuSkin Body Texcoord Hash (Target)',))],

# === PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT) ===
# Body draw_vb & blend_vb
'7353a665': [(log, ('2.8: ChinatsuSkin Body draw_vb',))],
'9b65412a': [(log, ('2.8: ChinatsuSkin Body blend_vb',))],

# Eyebrow VBs
'9f0ab8cd': [(log, ('2.8: ChinatsuSkin Eyebrow draw_vb',))],
'a5182b8a': [(log, ('2.8: ChinatsuSkin Eyebrow position_vb',))],
'e3cc1981': [(log, ('2.8: ChinatsuSkin Eyebrow texcoord_vb',))],
'f5daa764': [(log, ('2.8: ChinatsuSkin Eyebrow blend_vb',))],

# Face VBs
'9679c257': [(log, ('2.8: ChinatsuSkin Face draw_vb',))],
'ac6b5110': [(log, ('2.8: ChinatsuSkin Face position_vb',))],
'506dc9e1': [(log, ('2.8: ChinatsuSkin Face texcoord_vb',))],
'21299f88': [(log, ('2.8: ChinatsuSkin Face blend_vb',))],

# WeaponBackpack VBs
'953975c0': [(log, ('2.8: ChinatsuSkin WeaponBackpack draw_vb',))],
'a28ba31c': [(log, ('2.8: ChinatsuSkin WeaponBackpack position_vb',))],
'b642db41': [(log, ('2.8: ChinatsuSkin WeaponBackpack texcoord_vb',))],
'16e2d8ea': [(log, ('2.8: ChinatsuSkin WeaponBackpack blend_vb',))],

# Paopao VBs
'ffe207d5': [(log, ('2.8: ChinatsuSkin Paopao draw_vb',))],
'1a0cad46': [(log, ('2.8: ChinatsuSkin Paopao position_vb',))],
'df0f6142': [(log, ('2.8: ChinatsuSkin Paopao texcoord_vb',))],
'd4e13802': [(log, ('2.8: ChinatsuSkin Paopao blend_vb',))],

# Texture Hashes (v2.8)
'798adba3': [
        (log,                           ('2.8: ChinatsuSkin Shared NormalMap Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
'e85201e7': [
        (log,                           ('2.8: ChinatsuSkin Base Hair Diffuse Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'a2b36369': [
        (log,                           ('2.8: ChinatsuSkin Base Hair LightMap Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'ab3c12c0': [
        (log,                           ('2.8: ChinatsuSkin Base Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],

# === Face & Eyebrow Textures (shared with Chinatsu base) ===
'1ef66a60': [
        (log,                           ('2.8: ChinatsuSkin FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('1a2c8573', 'ChinatsuSkin.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30ea5791', 'ChinatsuSkin.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Skin Textures ===
'8de1219d': [
        (log,                           ('2.8: ChinatsuSkin HairA Diffuse Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'9795e08f': [
        (log,                           ('2.8: ChinatsuSkin HairA LightMap Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'f240844c': [
        (log,                           ('2.8: ChinatsuSkin HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Skin Textures ===
'5715ebbe': [
        (log,                           ('2.8: ChinatsuSkin BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
'335f4f3e': [
        (log,                           ('2.8: ChinatsuSkin BodyA LightMap Hash',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
'68807c0b': [
        (log,                           ('2.8: ChinatsuSkin BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],

# === Backpack Skin Textures ===
'37f00c45': [
        (log,                           ('2.8: ChinatsuSkin WeaponBackpack Diffuse Hash',)),
        (add_section_if_missing,        ('337a62c1', 'ChinatsuSkin.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'9368a6f9': [
        (log,                           ('2.8: ChinatsuSkin WeaponBackpack LightMap Hash',)),
        (add_section_if_missing,        ('337a62c1', 'ChinatsuSkin.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'508c297c': [
        (log,                           ('2.8: ChinatsuSkin WeaponBackpack MaterialMap Hash',)),
        (add_section_if_missing,        ('337a62c1', 'ChinatsuSkin.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],

# === Paopao Textures (shared with base) ===
'be5cd451': [
        (log,                           ('2.8: ChinatsuSkin Paopao Diffuse Hash',)),
        (add_section_if_missing,        ('07a82c9c', 'ChinatsuSkin.Paopao.IB', 'match_priority = 0\n')),
    ],
'945afd67': [
        (log,                           ('2.8: ChinatsuSkin Paopao LightMap Hash',)),
        (add_section_if_missing,        ('07a82c9c', 'ChinatsuSkin.Paopao.IB', 'match_priority = 0\n')),
    ],
'e9783f84': [
        (log,                           ('2.8: ChinatsuSkin Paopao MaterialMap Hash',)),
        (add_section_if_missing,        ('07a82c9c', 'ChinatsuSkin.Paopao.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced ChinatsuSkin hashes ===
'e5acd978': [
        (log,                           ('2.8: ChinatsuSkin Hair Diffuse Hash [New]',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'2fcfee64': [
        (log,                           ('2.8: ChinatsuSkin Hair Alternate Diffuse Hash [New]',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'87ce81a5': [
        (log,                           ('2.8: ChinatsuSkin Hair LightMap Hash [New]',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'8cd786f7': [
        (log,                           ('2.8: ChinatsuSkin Hair Alternate LightMap Hash [New]',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'5ae5a95b': [
        (log,                           ('2.8: ChinatsuSkin Hair MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'3f11dfd9': [
        (log,                           ('2.8: ChinatsuSkin Hair Alternate MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('a6d82ba5', 'ChinatsuSkin.Hair.IB', 'match_priority = 0\n')),
    ],
'db757608': [
        (log,                           ('2.8: ChinatsuSkin Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
'c9724602': [
        (log,                           ('2.8: ChinatsuSkin Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
'719036d1': [
        (log,                           ('2.8: ChinatsuSkin Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
'c9b5c6ce': [
        (log,                           ('2.8: ChinatsuSkin Face Diffuse Hash [New]',)),
        (add_section_if_missing,        ('1a2c8573', 'ChinatsuSkin.Face.IB', 'match_priority = 0\n')),
    ],
'ad73df94': [
        (log,                           ('2.8: ChinatsuSkin Backpack Diffuse Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'ChinatsuSkin.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'39dac70b': [
        (log,                           ('2.8: ChinatsuSkin Backpack LightMap Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'ChinatsuSkin.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'95070f7f': [
        (log,                           ('2.8: ChinatsuSkin Backpack MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('337a62c1', 'ChinatsuSkin.WeaponBackpack.IB', 'match_priority = 0\n')),
    ],
'7d8ac131': [
        (log,                           ('2.8: ChinatsuSkin Paopao Diffuse Hash [New]',)),
        (add_section_if_missing,        ('07a82c9c', 'ChinatsuSkin.Paopao.IB', 'match_priority = 0\n')),
    ],
'5c5b6aad': [
        (log,                           ('2.8: ChinatsuSkin Paopao LightMap Hash [New]',)),
        (add_section_if_missing,        ('07a82c9c', 'ChinatsuSkin.Paopao.IB', 'match_priority = 0\n')),
    ],
'3c4378db': [
        (log,                           ('2.8: ChinatsuSkin Paopao MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('07a82c9c', 'ChinatsuSkin.Paopao.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: ChinatsuSkin Shared NormalMap [New]',)),
        (add_section_if_missing,        ('ee17c9a2', 'ChinatsuSkin.Body.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'ChinatsuSkin',
    'game_versions': ['2.8'],
}