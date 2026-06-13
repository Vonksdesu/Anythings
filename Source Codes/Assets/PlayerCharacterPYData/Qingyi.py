"""
Qingyi Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
Pembaruan Database 2.8 oleh AI & Komunitas
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Qingyi's hash commands dictionary.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
'f6e96452': [(log, ('1.1: Qingyi Head IB Hash',)), (add_ib_check_if_missing,)],
'3cacba0a': [(log, ('1.1: Qingyi Hair IB Hash',)), (add_ib_check_if_missing,)],
'195857d8': [(log, ('1.1: Qingyi Body IB Hash',)), (add_ib_check_if_missing,)],
'8e8426df': [(log, ('2.5: Qingyi Bottle IB Hash',)), (add_ib_check_if_missing,)],
'd915de65': [
        (log, ('1 -> 1.1: Qingyi Body IB Hash',)),
        (update_hash, ('195857d8',)),
    ],
'0287b8fb': [
        (log, ('1 -> 1.1: Qingyi Body Blend Hash',)),
        (update_hash, ('88a6f633',)),
    ],
'dd421c3a': [
        (log, ('1 -> 1.1: Qingyi Body Position Hash',)),
        (update_hash, ('ac54012f',)),
    ],
'00487185': [
        (log, ('1 -> 1.1: Qingyi Body Texcoord Hash',)),
        (update_hash, ('4cbe7fbe',)),
    ],
'b1f382cd': [
        (log, ('1 -> 1.1: Qingyi Body Draw Hash',)),
        (update_hash, ('7be61bce',)),
    ],
'33f6d1f2': [
        (log, ('2 -> 1.1: Qingyi Hair IB Hash',)),
        (update_hash, ('3cacba0a',)),
    ],
'd196bd5c': [
        (log, ('2 -> 1.1: Qingyi Hair Blend Hash',)),
        (update_hash, ('6e7650bc',)),
    ],
'b6e5374d': [
        (log, ('2 -> 1.1: Qingyi Hair Position Hash',)),
        (update_hash, ('dd08951b',)),
    ],
'dae0117f': [
        (log, ('2 -> 1.1: Qingyi Hair Texcoord Hash',)),
        (update_hash, ('0643440c',)),
    ],
'6a52010a': [
        (log, ('2 -> 1.1: Qingyi Hair Draw Hash',)),
        (update_hash, ('7b43d317',)),
    ],
'0b75cd32': [
        (log,                           ('1.1: Qingyi HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f6e96452', 'Qingyi.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a58b5444', 'Qingyi.HeadA.Diffuse.1024')),
    ],
'a58b5444': [
        (log,                           ('1.1: Qingyi HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f6e96452', 'Qingyi.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0b75cd32', 'Qingyi.HeadA.Diffuse.2048')),
    ],
'0643440c': [
        (log, ('1.1 -> 1.2: Qingyi Hair Texcoord Hash',)),
        (update_hash, ('53a2b66e',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'3212a0ca': [
        (log,                           ('1.1: Qingyi HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a472db9a', 'Qingyi.HairA.Diffuse.1024')),
    ],
'2910fbd0': [
        (log,                           ('1.1 -> 2.5: Qingyi HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Qingyi Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
    ],
'6e3ac847': [
        (log,                           ('1.1: Qingyi HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('683414c1', 'Qingyi.HairA.LightMap.1024')),
    ],
'4a77fd3b': [
        (log,                           ('1.1: Qingyi HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bfefa200', 'Qingyi.HairA.MaterialMap.1024')),
    ],
'a472db9a': [
        (log,                           ('1.1: Qingyi HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3212a0ca', 'Qingyi.HairA.Diffuse.2048')),
    ],
'fc1847a9': [
        (log,                           ('1.1: Qingyi HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2910fbd0', 'Qingyi.HairA.NormalMap.2048')),
    ],
'683414c1': [
        (log,                           ('1.1: Qingyi HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6e3ac847', 'Qingyi.HairA.LightMap.2048')),
    ],
'bfefa200': [
        (log,                           ('1.1: Qingyi HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a77fd3b', 'Qingyi.HairA.MaterialMap.2048')),
    ],
'1fa7e18e': [
        (log,                           ('1.1: Qingyi BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('aa3c1147', 'Qingyi.BodyA.Diffuse.1024')),
    ],
'542c6b04': [
        (log,                           ('1.1 -> 2.5: Qingyi BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'35c2a022': [
        (log,                           ('1.1: Qingyi BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a484257', 'Qingyi.BodyA.LightMap.1024')),
    ],
'41054bb6': [
        (log,                           ('1.1: Qingyi BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4e561ee5', 'Qingyi.BodyA.MaterialMap.1024')),
    ],
'aa3c1147': [
        (log,                           ('1.1: Qingyi BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1fa7e18e', 'Qingyi.BodyA.Diffuse.2048')),
    ],
'4fbf05be': [
        (log,                           ('1.1: Qingyi BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('542c6b04', 'Qingyi.BodyA.NormalMap.2048')),
    ],
'4a484257': [
        (log,                           ('1.1: Qingyi BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('35c2a022', 'Qingyi.BodyA.LightMap.2048')),
    ],
'4e561ee5': [
        (log,                           ('1.1: Qingyi BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('41054bb6', 'Qingyi.BodyA.MaterialMap.2048')),
    ],

# === Legacy Weapon Updates ===
'46406a81': [(log, ('2.0 -> 2.8: Qingyi Weapon Diffuse [Legacy]',)), (update_hash, ('330dfe54',))],
'22b43462': [(log, ('2.0 -> 2.8: Qingyi Weapon LightMap [Legacy]',)), (update_hash, ('2d703fde',))],
'39e8fda1': [(log, ('2.0 -> 2.8: Qingyi Weapon MaterialMap [Legacy]',)), (update_hash, ('8d6da65b',))],

# === PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT) ===
# New Index Buffer (IB) Hashes
'0a94bfd8': [(log, ('2.8: Qingyi HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'6b62986f': [(log, ('2.8: Qingyi Weapon IB Hash',)),     (add_ib_check_if_missing,)],

# Hair VBs
'7b43d317': [(log, ('2.8: Qingyi Hair draw_vb',))],
'dd08951b': [(log, ('2.8: Qingyi Hair position_vb',))],
'53a2b66e': [(log, ('2.8: Qingyi Hair texcoord_vb',))],
'6e7650bc': [(log, ('2.8: Qingyi Hair blend_vb',))],

# Hair Shadow VBs
'472bb581': [(log, ('2.8: Qingyi HairShadow draw_vb',))],
'0971a397': [(log, ('2.8: Qingyi HairShadow position_vb',))],
'ee99ded9': [(log, ('2.8: Qingyi HairShadow texcoord_vb',))],
'b7ce94d8': [(log, ('2.8: Qingyi HairShadow blend_vb',))],

# Body VBs
'7be61bce': [(log, ('2.8: Qingyi Body draw_vb',))],
'ac54012f': [(log, ('2.8: Qingyi Body position_vb',))],
'4cbe7fbe': [(log, ('2.8: Qingyi Body texcoord_vb',))],
'88a6f633': [(log, ('2.8: Qingyi Body blend_vb',))],

# Kettle VBs
'fca2b042': [(log, ('2.8: Qingyi Kettle draw_vb',))],
'24282218': [(log, ('2.8: Qingyi Kettle position_vb',))],
'1707933f': [(log, ('2.8: Qingyi Kettle texcoord_vb',))],
'807eb474': [(log, ('2.8: Qingyi Kettle blend_vb',))],

# Face VBs & Limits
'9f6aa443': [(log, ('2.8: Qingyi Face VertexLimit',))],
'a5783704': [(log, ('2.8: Face Position',))],
'6a492df0': [(log, ('2.8: Face Texcoord',))],
'57c9f0a3': [(log, ('2.8: Face Blend',))],

# Weapon VBs & Limits
'e5a4128b': [(log, ('2.8: Qingyi Weapon VertexLimit',))],
'fb916456': [(log, ('2.8: Qingyi Weapon Position',))],
'8658ef62': [(log, ('2.8: Qingyi Weapon Texcoord',))],
'f75514db': [(log, ('2.8: Qingyi Weapon Blend',))],

# Texture Hashes (v2.8 Target)
'330dfe54': [
        (log,                           ('2.8: Qingyi Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('6b62986f', 'Qingyi.Weapon.IB', 'match_priority = 0\n')),
    ],
'2d703fde': [
        (log,                           ('2.8: Qingyi Weapon LightMap Hash',)),
        (add_section_if_missing,        ('6b62986f', 'Qingyi.Weapon.IB', 'match_priority = 0\n')),
    ],
'8d6da65b': [
        (log,                           ('2.8: Qingyi Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('6b62986f', 'Qingyi.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log,                           ('2.8: Qingyi Shared NormalMap Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6b62986f', 'Qingyi.Weapon.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Qingyi',
    'game_versions': ['2.8'],
}