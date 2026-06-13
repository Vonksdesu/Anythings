"""
Lucia Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json
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
    Returns Lucia's hash commands dictionary.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
# === Hair Component ===
'340fc999': [(log, ('2.5: Lucia Hair IB Hash',)),           (add_ib_check_if_missing,)],
'78043df0': [(log, ('2.5: Lucia Hair Position Hash',))],
'97dde567': [(log, ('2.5: Lucia Hair Texcoord Hash',))],
'bfd60db5': [(log, ('2.5: Lucia Hair Blend Hash',))],

# === Body Component ===
'd39c304d': [(log, ('2.5: Lucia Body IB Hash',)),           (add_ib_check_if_missing,)],
'234c641a': [(log, ('2.5: Lucia Body Position Hash',))],
'0400f04f': [(log, ('2.5: Lucia Body Texcoord Hash',))],
'3f4f9fa9': [(log, ('2.5: Lucia Body Blend Hash',))],

# === Cape Component ===
'cd80d116': [(log, ('2.5: Lucia Cape IB Hash',)),           (add_ib_check_if_missing,)],
'08ae4b5d': [(log, ('2.5: Lucia Cape Position Hash',))],
'dd0e570f': [(log, ('2.5: Lucia Cape Texcoord Hash',))],
'b917fca5': [(log, ('2.5: Lucia Cape Blend Hash',))],

# === CapeExtra Component ===
'692a4e10': [(log, ('2.5: Lucia CapeExtra IB Hash',)),      (add_ib_check_if_missing,)],
'c035f6bd': [(log, ('2.5: Lucia CapeExtra Position Hash',))],
'90f30bc1': [(log, ('2.5: Lucia CapeExtra Texcoord Hash',))],
'946dc2ff': [(log, ('2.5: Lucia CapeExtra Blend Hash',))],

# === Face Component ===
'6986f28e': [(log, ('2.5: Lucia Face IB Hash',)),           (add_ib_check_if_missing,)],

# === Face Textures ===
'20a6224d': [
        (log,                           ('2.5: Lucia FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures (Shared between HairA and HairB) ===
'5b0b47c9': [
        (log,                           ('2.5: Lucia Hair Diffuse Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'243feee8': [
        (log,                           ('2.5: Lucia Hair LightMap Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'211a5700': [
        (log,                           ('2.5: Lucia Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Lucia NormalMap Hash (Shared across components)',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Shared between BodyA and BodyB) ===
'2ca45943': [
        (log,                           ('2.5: Lucia Body Diffuse Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'f117c868': [
        (log,                           ('2.5: Lucia Body LightMap Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'a16861d2': [
        (log,                           ('2.5: Lucia Body MaterialMap Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# New Index Buffer (IB) Hashes
'7be43e2b': [(log, ('2.8: Lucia HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'84eaa4c6': [(log, ('2.8: Lucia Eyebrow IB Hash',)),    (add_ib_check_if_missing,)],
'5cca4239': [(log, ('2.8: Lucia Scepter IB Hash',)),    (add_ib_check_if_missing,)],
'ebc05d0c': [(log, ('2.8: Lucia Book IB Hash',)),       (add_ib_check_if_missing,)],

# Hair draw_vb
'fed6eef6': [(log, ('2.8: Lucia Hair draw_vb',))],

# Hair Shadow VBs
'0695fa38': [(log, ('2.8: Lucia HairShadow draw_vb',))],
'82729474': [(log, ('2.8: Lucia HairShadow position_vb',))],
'38f2daa7': [(log, ('2.8: Lucia HairShadow texcoord_vb',))],
'9662cc92': [(log, ('2.8: Lucia HairShadow blend_vb',))],

# Cape VBs
'6533c56a': [(log, ('2.8: Lucia Cape draw_vb',))],
'5f21562d': [(log, ('2.8: Lucia Cape position_vb',))],

# CapeExtra VB
'439208cc': [(log, ('2.8: Lucia CapeExtra draw_vb',))],

# Body draw_vb
'b3a498b5': [(log, ('2.8: Lucia Body draw_vb',))],

# Eyebrow VBs
'f917cafc': [(log, ('2.8: Lucia Eyebrow draw_vb',))],
'c30559bb': [(log, ('2.8: Lucia Eyebrow position_vb',))],
'05342ce9': [(log, ('2.8: Lucia Eyebrow texcoord_vb',))],
'8893a84c': [(log, ('2.8: Lucia Eyebrow blend_vb',))],

# Face VBs & Limits
'7915db83': [(log, ('2.8: Lucia Face VertexLimit',))],
'430748c4': [(log, ('2.8: Face Position',))],
'9648c6d3': [(log, ('2.8: Face Texcoord',))],
'925947a7': [(log, ('2.8: Face Blend',))],

# Scepter VBs & Limits
'73acb40f': [(log, ('2.8: Lucia Scepter VertexLimit',))],
'adc940e0': [(log, ('2.8: Lucia Scepter Position',))],
'9f2822c3': [(log, ('2.8: Lucia Scepter Texcoord',))],
'7a83c0d2': [(log, ('2.8: Lucia Scepter Blend',))],

# Book VBs & Limits
'08ecb686': [(log, ('2.8: Lucia Book VertexLimit',))],
'0ee71df8': [(log, ('2.8: Lucia Book Position',))],
'2d98213f': [(log, ('2.8: Lucia Book Texcoord',))],
'b1ebb25d': [(log, ('2.8: Lucia Book Blend',))],

# Texture Hashes (v2.8)
'ab461f68': [
        (log,                           ('2.8: Lucia Hair Diffuse Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'dda3939e': [
        (log,                           ('2.8: Lucia Hair LightMap Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'c09e5350': [
        (log,                           ('2.8: Lucia Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'614c9ad5': [
        (log,                           ('2.8: Lucia Body Diffuse Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'30b94be9': [
        (log,                           ('2.8: Lucia Body LightMap Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'c0fe7e43': [
        (log,                           ('2.8: Lucia Body MaterialMap Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'12ec6e26': [
        (log,                           ('2.8: Lucia Face, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('84eaa4c6', 'Lucia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'8d72bc12': [
        (log,                           ('2.8: Lucia Weapons Diffuse Hash',)),
        (add_section_if_missing,        ('5cca4239', 'Lucia.Scepter.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebc05d0c', 'Lucia.Book.IB', 'match_priority = 0\n')),
    ],
'84e4fd19': [
        (log,                           ('2.8: Lucia Weapons LightMap Hash',)),
        (add_section_if_missing,        ('5cca4239', 'Lucia.Scepter.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebc05d0c', 'Lucia.Book.IB', 'match_priority = 0\n')),
    ],
'009caccb': [
        (log,                           ('2.8: Lucia Weapons MaterialMap Hash',)),
        (add_section_if_missing,        ('5cca4239', 'Lucia.Scepter.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebc05d0c', 'Lucia.Book.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Lucia Weapon hashes ===
'5a602448': [
        (log,                           ('2.8: Lucia Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        (('5cca4239', 'ebc05d0c'), 'Lucia.Weapon.IB', 'match_priority = 0\n')),
    ],
'e2e48852': [
        (log,                           ('2.8: Lucia Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        (('5cca4239', 'ebc05d0c'), 'Lucia.Weapon.IB', 'match_priority = 0\n')),
    ],
'74814017': [
        (log,                           ('2.8: Lucia Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        (('5cca4239', 'ebc05d0c'), 'Lucia.Weapon.IB', 'match_priority = 0\n')),
    ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Lucia',
    'game_versions': ['2.8'],
}