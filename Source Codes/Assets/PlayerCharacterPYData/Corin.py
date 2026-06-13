"""
Corin Character Hash Commands
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
    Returns Corin's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
# === IB Hashes (Index Buffers) ===
'5a839fb2': [(log, ('1.0 -> 2.5: Corin Hair IB Hash',)), (add_ib_check_if_missing,)],
'e74620b5': [(log, ('1.0 -> 2.5: Corin Body IB Hash',)), (add_ib_check_if_missing,)],
'5f803336': [(log, ('1.0 -> 2.5: Corin Bear IB Hash',)), (add_ib_check_if_missing,)],
'a0c80593': [(log, ('1.0 -> 2.5: Corin Head IB Hash',)), (add_ib_check_if_missing,)],

# === VB Hashes (Vertex Buffers) ===
# Hair VBs
'7e7eee0d': [(log, ('2.5: Corin Hair Position VB Hash',))],
'5fa50113': [(log, ('2.5: Corin Hair Blend VB Hash',))],
'abc95b03': [(log, ('2.5: Corin Hair Texcoord VB Hash',))],
'8d999156': [(log, ('1.3 -> 1.4: Corin Hair Blend Hash (Old)',)), (update_hash, ('5fa50113',))],
'2cf242f4': [(log, ('1.3 -> 1.4: Corin Hair Texcoord Hash (Old)',)), (update_hash, ('abc95b03',))],

# Body VBs
'5dc40184': [(log, ('2.5: Corin Body Position VB Hash',))],
'aa71e514': [(log, ('2.5: Corin Body Blend VB Hash',))],
'4c6b7bda': [(log, ('2.5: Corin Body Texcoord VB Hash',))],

# Bear VBs
'4e1c9e44': [(log, ('2.5: Corin Bear Position VB Hash',))],
'6ffea6f6': [(log, ('2.5: Corin Bear Blend VB Hash',))],
'21987873': [(log, ('2.5: Corin Bear Texcoord VB Hash',))],

# === Texture Hashes - Face ===
'6d662824': [
        (log,                           ('1.0 -> 2.5: Corin HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0c80593', 'Corin.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('97022d3c', 'Corin.HeadA.Diffuse.1024')),
    ],
'97022d3c': [
        (log,                           ('1.0 -> 2.5: Corin HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0c80593', 'Corin.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6d662824', 'Corin.HeadA.Diffuse.2048')),
    ],

# === Texture Hashes - Hair ===
# Diffuse
'60526444': [
        (log,                           ('1.0 -> 2.5: Corin HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('651e96f8', 'Corin.HairA.Diffuse.1024')),
    ],
'651e96f8': [
        (log,                           ('1.0 -> 2.5: Corin HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('60526444', 'Corin.HairA.Diffuse.2048')),
    ],

# LightMap
'929aca42': [
        (log,                           ('1.0 -> 1.4: Corin HairA LightMap 2048p Hash (Old)',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (update_hash,                   ('74d66671',)),
    ],
'74d66671': [
        (log,                           ('2.5: Corin HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('edff2372', 'Corin.HairA.LightMap.1024')),
    ],
'edff2372': [
        (log,                           ('1.0 -> 2.5: Corin HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('74d66671', 'Corin.HairA.LightMap.2048')),
    ],

# MaterialMap
'c6398bc8': [
        (log,                           ('2.5: Corin HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
    ],

# NormalMap
'4a68ef99': [
        (log,                           ('1.0 -> 1.4: Corin HairA NormalMap 2048p Hash (Old)',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Corin Hair/Body/Bear Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ab8956c8', 'Corin.HairA.NormalMap.1024')),
    ],
'ab8956c8': [
        (log,                           ('1.0 -> 2.5: Corin HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Corin.HairA.NormalMap.2048')),
    ],

# === Texture Hashes - Body/Bear (Shared Textures) ===
# Diffuse
'af9d845a': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('681f5162', 'Corin.BodyA.Diffuse.1024')),
    ],
'681f5162': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('af9d845a', 'Corin.BodyA.Diffuse.2048')),
    ],

# LightMap
'75e05cdc': [
        (log,                           ('1.0 -> 1.4: Corin BodyA, BearA LightMap 2048p Hash (Old)',)),
        (update_hash,                   ('e1c1718f',)),
    ],
'e1c1718f': [
        (log,                           ('2.5: Corin BodyA, BearA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('af7eda82', 'Corin.BodyA.LightMap.1024')),
    ],
'af7eda82': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e1c1718f', 'Corin.BodyA.LightMap.2048')),
    ],

# MaterialMap
'50a0faea': [
        (log,                           ('1.0 -> 1.4: Corin BodyA, BearA MaterialMap 2048p Hash (Old)',)),
        (update_hash,                   ('e58d9767',)),
    ],
'e58d9767': [
        (log,                           ('2.5: Corin BodyA, BearA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('9dc9c0f6', 'Corin.BodyA.MaterialMap.1024')),
    ],
'9dc9c0f6': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e58d9767', 'Corin.BodyA.MaterialMap.2048')),
    ],

# NormalMap
'289f4c58': [
        (log,                           ('1.0 -> 1.4: Corin BodyA, BearA NormalMap 2048p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'640141d4': [
        (log,                           ('1.0 -> 2.5: Corin BodyA, BearA NormalMap 1024p Hash',)),
        (multiply_section_if_missing,   ('ebac056e', 'Corin.BodyA.NormalMap.2048')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# New Index Buffer (IB) Hashes
'294af6bd': [(log, ('2.8: Corin HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'6f2286a6': [(log, ('2.8: Corin Weapon IB Hash',)),     (add_ib_check_if_missing,)],

# Hair draw_vb & LightMap
'd345e472': [(log, ('2.8: Corin Hair draw_vb',))],
'0f300531': [
        (log,                           ('2.8: Corin HairA LightMap Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
    ],

# Hair Shadow VBs
'16399986': [(log, ('2.8: Corin HairShadow draw_vb',))],
'b3c22aee': [(log, ('2.8: Corin HairShadow position_vb',))],
'e134a479': [(log, ('2.8: Corin HairShadow texcoord_vb',))],
'81a22a15': [(log, ('2.8: Corin HairShadow blend_vb',))],

# Body draw_vb, LightMap, MaterialMap
'2eb162ef': [(log, ('2.8: Corin Body draw_vb',))],
'068be251': [
        (log,                           ('2.8: Corin BodyA LightMap Hash',)),
        (add_section_if_missing,        ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
    ],
'50ed6c50': [
        (log,                           ('2.8: Corin BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
    ],

# Bear draw_vb
'1a7ee1b5': [(log, ('2.8: Corin Bear draw_vb',))],

# Face VBs & Limits
'eda4d773': [(log, ('2.8: Corin Face VertexLimit',))],
'd7b64434': [(log, ('2.8: Corin Face Position',))],
'1c0725e4': [(log, ('2.8: Corin Face Texcoord',))],
'4892e6b4': [(log, ('2.8: Corin Face Blend',))],

# Weapon VBs & Limits
'6bf8f421': [(log, ('2.8: Corin Weapon VertexLimit',))],
'17a67595': [(log, ('2.8: Corin Weapon Position',))],
'f8da5b79': [(log, ('2.8: Corin Weapon Texcoord',))],
'df7728c8': [(log, ('2.8: Corin Weapon Blend',))],

# Weapon Textures
'be466746': [
        (log,                           ('2.8: Corin Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],
'd897d14c': [
        (log,                           ('2.8: Corin Weapon LightMap Hash',)),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],
'd97382e2': [
        (log,                           ('2.8: Corin Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log,                           ('2.8: Corin Shared NormalMap Hash',)),
        (add_section_if_missing,        ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Corin Weapon hashes ===
'8dd64c09': [
        (log,                           ('2.8: Corin Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],
'e8c22497': [
        (log,                           ('2.8: Corin Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],
'b921465e': [
        (log,                           ('2.8: Corin Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('6f2286a6', 'Corin.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Corin',
    'game_versions': ['2.8'],
}