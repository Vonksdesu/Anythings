"""
Norma Character Hash Commands
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
    Returns Norma's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'31178971': [(log, ('3.0: Promeia Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'0ae14c24': [(log, ('3.0: Promeia Cloak IB Hash',)),                     (add_ib_check_if_missing,)],
'b386901d': [(log, ('3.0: Promeia CloakChest IB Hash',)),            (add_ib_check_if_missing,)],
'10c77d62': [(log, ('3.0: Promeia Chest IB Hash',)),                 (add_ib_check_if_missing,)],
'ec003379': [(log, ('3.0: Promeia Legs IB Hash',)),                  (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'a2150d3b': [(log, ('3.0: Norma Hair IB Hash',)),                       (add_ib_check_if_missing,)],
'7517a03f': [(log, ('3.0: Norma HairShadow IB Hash',)),                  (add_ib_check_if_missing,)],
'bcc7e369': [(log, ('3.0: WiseTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'773f390c': [(log, ('3.0: Norma Body IB Hash',)),                       (add_ib_check_if_missing,)],
'd3b2ed9a': [(log, ('3.0: Norma Eyebrow IB Hash',)),                     (add_ib_check_if_missing,)],
'4fafb136': [(log, ('3.0: Norma Face IB Hash',)),                        (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'62c935b1': [(log, ('3.0: Norma Hair draw_vb',)),                       (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],
'be624ee3': [(log, ('3.0: Norma Hair position_vb',)),                   (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],
'18e12e3a': [(log, ('3.0: Norma Hair texcoord_vb',)),                   (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],
'0a09cb32': [(log, ('3.0: Norma Hair blend_vb',)),                      (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],

# Hat
'152400a0': [(log, ('3.0: Norma Hat draw_vb',)),                        (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],
'80f2a2aa': [(log, ('3.0: Norma Hat position_vb',)),                    (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],
'6a8b4c03': [(log, ('3.0: Norma Hat texcoord_vb',)),                    (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],
'accaa8fd': [(log, ('3.0: Norma Hat blend_vb',)),                       (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],

# Body
'ab21b245': [(log, ('3.0: Norma Body draw_vb',)),                       (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],
'c149712f': [(log, ('3.0: Norma Body position_vb',)),                   (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],
'52235615': [(log, ('3.0: Norma Body texcoord_vb',)),                   (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],
'b10a84f3': [(log, ('3.0: Norma Body blend_vb',)),                      (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],

# Eyebrow
'b5bc1f91': [(log, ('3.0: Norma Eyebrow draw_vb',)),                    (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],
'15a1b43f': [(log, ('3.0: Norma Eyebrow position_vb',)),                (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],
'7acc7619': [(log, ('3.0: Norma Eyebrow texcoord_vb',)),                (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],
'11747958': [(log, ('3.0: Norma Eyebrow blend_vb',)),                   (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],

# Face
'8294facc': [(log, ('3.0: Norma Face draw_vb',)),                       (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],
'b886698b': [(log, ('3.0: Norma Face position_vb',)),                   (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],
'b1412ed9': [(log, ('3.0: Norma Face texcoord_vb',)),                   (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],
'cf3ce0a2': [(log, ('3.0: Norma Face blend_vb',)),                      (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],

# === Face & Eyebrow Shared Textures ===
'007dc9ec': [
        (log,                           ('3.0: Norma Face, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair & Hat Shared Textures ===
'9593fbbd': [
        (log,                           ('3.0: Norma Hair, Hat Diffuse Hash',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'a0010ed7': [
        (log,                           ('3.0: Norma Hair, Hat LightMap Hash',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'6493d4d4': [
        (log,                           ('3.0: Norma Hair, Hat MaterialMap Hash',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'8dbb873b': [
        (log,                           ('3.0: Norma Body Diffuse Hash',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'13e85378': [
        (log,                           ('3.0: Norma Body LightMap Hash',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'fcb3bd07': [
        (log,                           ('3.0: Norma Body MaterialMap Hash',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: Norma Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'fc98a89c': [
        (log,                           ('3.0: Norma Hair, Hat NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'37da98f5': [
        (log,                           ('3.0: Norma Body NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Norma',
    'game_versions': ['3.0'],
}