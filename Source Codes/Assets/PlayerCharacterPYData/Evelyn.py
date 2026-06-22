"""
Evelyn Character Hash Commands
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
    Returns Evelyn's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
'10a5bde2': [(log, ('2.5: Evelyn Hair IB Hash',)),      (add_ib_check_if_missing,)],
'04b53ecd': [(log, ('2.5: Evelyn Body IB Hash',)),      (add_ib_check_if_missing,)],
'bb6d1023': [(log, ('2.5: Evelyn Jacket IB Hash',)),    (add_ib_check_if_missing,)],
'b3eaedb0': [(log, ('2.5: Evelyn Shoulders IB Hash',)), (add_ib_check_if_missing,)],
'ddf4efa6': [(log, ('2.5: Evelyn Face IB Hash',)),      (add_ib_check_if_missing,)],
'8e1d1a6f': [
        (log,                           ('2.5: Evelyn FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bc090438', 'Evelyn.FaceA.Diffuse.1024')),
    ],
'bc090438': [
        (log,                           ('2.5: Evelyn FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8e1d1a6f', 'Evelyn.FaceA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Evelyn Shared NormalMap Hash (Hair, Jacket, Body, Shoulder)',)),
        (add_section_if_missing,        ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3eaedb0', 'Evelyn.Shoulders.IB', 'match_priority = 0\n')),
    ],
'0e5c3c97': [
        (log,                           ('2.5: Evelyn Hair, Jacket Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('65a7592d', 'Evelyn.Hair.Diffuse.1024')),
    ],
'e1434e0d': [
        (log,                           ('2.5: Evelyn Hair, Jacket LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('eb414a98', 'Evelyn.Hair.LightMap.1024')),
    ],
'b2718585': [
        (log,                           ('2.5: Evelyn Hair, Jacket MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e680f0c7', 'Evelyn.Hair.MaterialMap.1024')),
    ],
'65a7592d': [
        (log,                           ('2.5: Evelyn Hair, Jacket Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('0e5c3c97', 'Evelyn.Hair.Diffuse.2048')),
    ],
'eb414a98': [
        (log,                           ('2.5: Evelyn Hair, Jacket LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e1434e0d', 'Evelyn.Hair.LightMap.2048')),
    ],
'e680f0c7': [
        (log,                           ('2.5: Evelyn Hair, Jacket MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('b2718585', 'Evelyn.Hair.MaterialMap.2048')),
    ],
'a59b14c0': [
        (log,                           ('2.5: Evelyn Body, Shoulder Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('93033898', 'Evelyn.Body.Diffuse.1024')),
    ],
'd022d32c': [
        (log,                           ('2.5: Evelyn Body, Shoulder LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('16aab2ab', 'Evelyn.Body.LightMap.1024')),
    ],
'8624e4e4': [
        (log,                           ('2.5: Evelyn Body, Shoulder MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('716561f0', 'Evelyn.Body.MaterialMap.1024')),
    ],
'93033898': [
        (log,                           ('2.5: Evelyn Body, Shoulder Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a59b14c0', 'Evelyn.Body.Diffuse.2048')),
    ],
'16aab2ab': [
        (log,                           ('2.5: Evelyn Body, Shoulder LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d022d32c', 'Evelyn.Body.LightMap.2048')),
    ],
'716561f0': [
        (log,                           ('2.5: Evelyn Body, Shoulder MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('8624e4e4', 'Evelyn.Body.MaterialMap.2048')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# New Index Buffer (IB) Hashes
'8ed17e5a': [(log, ('2.8: Evelyn HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'2488810a': [(log, ('2.8: Evelyn HairpinRibbon IB Hash',)), (add_ib_check_if_missing,)],
'78699e6c': [(log, ('2.8: Evelyn DaggerActive IB Hash',)), (add_ib_check_if_missing,)],
'7fb7467f': [(log, ('2.8: Evelyn DaggerSheathed IB Hash',)), (add_ib_check_if_missing,)],
'af10bd11': [(log, ('2.8: Evelyn SilkString IB Hash',)), (add_ib_check_if_missing,)],

# Hair VBs
'798bc78b': [(log, ('2.8: Evelyn Hair draw_vb',))],
'c2fe4e27': [(log, ('2.8: Evelyn Hair position_vb',))],
'066f6115': [(log, ('2.8: Evelyn Hair texcoord_vb',))],
'b43809d2': [(log, ('2.8: Evelyn Hair blend_vb',))],

# Hair Shadow VBs
'28913abf': [(log, ('2.8: Evelyn HairShadow draw_vb',))],
'1251bc38': [(log, ('2.8: Evelyn HairShadow position_vb',))],
'bf111b37': [(log, ('2.8: Evelyn HairShadow texcoord_vb',))],
'94ce70dd': [(log, ('2.8: Evelyn HairShadow blend_vb',))],

# Hairpin Ribbon VBs
'98a87a48': [(log, ('2.8: Evelyn HairpinRibbon draw_vb',))],
'f1076f2a': [(log, ('2.8: Evelyn HairpinRibbon position_vb',))],
'63d18ae4': [(log, ('2.8: Evelyn HairpinRibbon texcoord_vb',))],
'35070aca': [(log, ('2.8: Evelyn HairpinRibbon blend_vb',))],

# Jacket VBs
'1fb9dfe2': [(log, ('2.8: Evelyn Jacket draw_vb',))],
'4edb27d5': [(log, ('2.8: Evelyn Jacket position_vb',))],
'8b3ed55f': [(log, ('2.8: Evelyn Jacket texcoord_vb',))],
'022d390f': [(log, ('2.8: Evelyn Jacket blend_vb',))],

# Shoulder VBs
'356f6430': [(log, ('2.8: Evelyn Shoulder draw_vb',))],
'2b77b077': [(log, ('2.8: Evelyn Shoulder position_vb',))],
'3cecd299': [(log, ('2.8: Evelyn Shoulder texcoord_vb',))],
'a6b42907': [(log, ('2.8: Evelyn Shoulder blend_vb',))],

# Body VBs
'02b04234': [(log, ('2.8: Evelyn Body draw_vb',))],
'67eafa06': [(log, ('2.8: Evelyn Body position_vb',))],
'26f9ba95': [(log, ('2.8: Evelyn Body texcoord_vb',))],
'5ea06832': [(log, ('2.8: Evelyn Body blend_vb',))],

# Face VBs & Limits
'c6afc18c': [(log, ('2.8: Evelyn Face VertexLimit',))],
'fcbd52cb': [(log, ('2.8: Evelyn Face Position',))],
'aa2f560e': [(log, ('2.8: Evelyn Face Texcoord',))],
'f9fc3c8b': [(log, ('2.8: Evelyn Face Blend',))],

# Weapon Active VBs & Limits
'3ae20915': [(log, ('2.8: Evelyn DaggerActive VertexLimit',))],
'99c7c611': [(log, ('2.8: Evelyn DaggerActive Blend',))],

# Penyelarasan Sinkronisasi v2.8 (SilkString VertexLimit)
'4ff726df': [
        (log,                           ('2.8: Evelyn SilkString VertexLimit',)),
        (add_section_if_missing,        ('af10bd11', 'Evelyn.SilkString.IB', 'match_priority = 0\n')),
    ],

# Texture Hashes (v2.8)
'798adba3': [
        (log,                           ('2.8: Evelyn Shared NormalMap Hash',)),
        (add_section_if_missing,        ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3eaedb0', 'Evelyn.Shoulders.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('78699e6c', 'Evelyn.DaggerActive.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Evelyn',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}