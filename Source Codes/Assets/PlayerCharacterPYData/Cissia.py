"""
Cissia Character Hash Commands
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
    Returns Cissia's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'e4785f80': [(log, ('2.8: Cissia Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'8f34fc78': [(log, ('2.8: Cissia HairShadow IB Hash',)),                  (add_ib_check_if_missing,)],
'e5ced7d5': [(log, ('2.8: Cissia Tongue IB Hash',)),                      (add_ib_check_if_missing,)],
'ff2ec4d6': [(log, ('2.8: Cissia Body IB Hash',)),                        (add_ib_check_if_missing,)],
'4c11c155': [(log, ('2.8: Cissia Tail IB Hash',)),                        (add_ib_check_if_missing,)],
'7c01dc6b': [(log, ('2.8: Cissia Eyebrow IB Hash',)),                     (add_ib_check_if_missing,)],
'd1a31f0b': [(log, ('2.8: Cissia Face IB Hash',)),                        (add_ib_check_if_missing,)],
'29b5b0b0': [(log, ('2.8: Cissia SpearHandle IB Hash',)),                 (add_ib_check_if_missing,)],
'29123d5a': [(log, ('2.8: Cissia SpearHead IB Hash',)),                   (add_ib_check_if_missing,)],
'bad668cc': [(log, ('2.8: Cissia SpearBarrel IB Hash',)),                 (add_ib_check_if_missing,)],
'd49a5866': [(log, ('2.8: Cissia SpearChanging IB Hash',)),               (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'33b532e5': [(log, ('2.8: Cissia Hair draw_vb Hash',)),                  (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n'))],
'639456c7': [(log, ('2.8: Cissia Hair position_vb Hash',)),              (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n'))],
'a36d2401': [(log, ('2.8: Cissia Hair texcoord_vb Hash',)),              (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n'))],
'b93219f1': [(log, ('2.8: Cissia Hair blend_vb Hash',)),                 (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n'))],

# Tongue
'a3b04e84': [(log, ('2.8: Cissia Tongue draw_vb Hash',)),                (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n'))],
'3e82033f': [(log, ('2.8: Cissia Tongue position_vb Hash',)),            (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n'))],
'32f6d33a': [(log, ('2.8: Cissia Tongue texcoord_vb Hash',)),            (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n'))],
'c3082752': [(log, ('2.8: Cissia Tongue blend_vb Hash',)),               (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n'))],

# Body
'9645e284': [(log, ('2.8: Cissia Body draw_vb Hash',)),                  (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n'))],
'1a95227f': [(log, ('2.8: Cissia Body position_vb Hash',)),              (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n'))],
'e6527ff0': [(log, ('2.8: Cissia Body texcoord_vb Hash',)),              (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n'))],
'3b944072': [(log, ('2.8: Cissia Body blend_vb Hash',)),                 (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n'))],

# Tail
'3b4de0d1': [(log, ('2.8: Cissia Tail draw_vb Hash',)),                  (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n'))],
'efed0e09': [(log, ('2.8: Cissia Tail position_vb Hash',)),              (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n'))],
'8f017202': [(log, ('2.8: Cissia Tail texcoord_vb Hash',)),              (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n'))],
'90634c3b': [(log, ('2.8: Cissia Tail blend_vb Hash',)),                 (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n'))],

# Face
'a2d2a224': [(log, ('2.8: Cissia Face draw_vb Hash',)),                  (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n'))],
'98c03163': [(log, ('2.8: Cissia Face position_vb Hash',)),              (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n'))],
'dfc76798': [(log, ('2.8: Cissia Face texcoord_vb Hash',)),              (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n'))],
'ed3245f0': [(log, ('2.8: Cissia Face blend_vb Hash',)),                 (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n'))],

# Weapon - SpearHandle
'9af3bf00': [(log, ('2.8: Cissia Weapon SpearHandle draw_vb Hash',)),    (add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n'))],
'dee92405': [(log, ('2.8: Cissia Weapon SpearHandle position_vb Hash',)),(add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n'))],
'880e958d': [(log, ('2.8: Cissia Weapon SpearHandle texcoord_vb Hash',)),(add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n'))],
'6354dee4': [(log, ('2.8: Cissia Weapon SpearHandle blend_vb Hash',)),   (add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n'))],

# Weapon - SpearBarrel
'19bac37e': [(log, ('2.8: Cissia Weapon SpearBarrel draw_vb Hash',)),    (add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n'))],
'91e05512': [(log, ('2.8: Cissia Weapon SpearBarrel position_vb Hash',)),(add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n'))],
'2785fe49': [(log, ('2.8: Cissia Weapon SpearBarrel texcoord_vb Hash',)),(add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n'))],
'b813c97f': [(log, ('2.8: Cissia Weapon SpearBarrel blend_vb Hash',)),   (add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n'))],

# Weapon - SpearChanging
'7647eba5': [(log, ('2.8: Cissia Weapon SpearChanging draw_vb Hash',)),  (add_section_if_missing, ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n'))],
'5b71ede8': [(log, ('2.8: Cissia Weapon SpearChanging position_vb',)),  (add_section_if_missing, ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n'))],
'c37f63b8': [(log, ('2.8: Cissia Weapon SpearChanging texcoord_vb',)),  (add_section_if_missing, ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n'))],
'32b90f8b': [(log, ('2.8: Cissia Weapon SpearChanging blend_vb Hash',)), (add_section_if_missing, ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n'))],

# === Hash update 2.7 -> 2.8: Cissia Body/Spear Diffuse ===
'f5ecd616': [(log, ('2.8: Cissia BodyA, Spear Diffuse Hash [Legacy]',)), (update_hash, ('6d861173',))],

# === Face, Tongue & Eyebrow Textures ===
'c72539cd': [
        (log,                           ('2.8: Cissia FaceA, Tongue, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'9aa301f1': [
        (log,                           ('2.8: Cissia HairA Diffuse Hash',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'0c2d5ee2': [
        (log,                           ('2.8: Cissia HairA LightMap Hash',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'64a85915': [
        (log,                           ('2.8: Cissia HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification A) ===
'2638fa23': [
        (log,                           ('2.8: Cissia BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'4862ab5d': [
        (log,                           ('2.8: Cissia BodyA LightMap Hash',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'b0a060f2': [
        (log,                           ('2.8: Cissia BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],

# === Body, Tail & Spear Shared Textures (Classification B/C) ===
'6d861173': [
        (log,                           ('2.8: Cissia Body, Tail, Spear Diffuse Hash',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],
'090684bd': [
        (log,                           ('2.8: Cissia Body, Tail, Spear LightMap Hash',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],
'd59dc29c': [
        (log,                           ('2.8: Cissia Body, Tail, Spear MaterialMap Hash',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Cissia Shared NormalMap Hash',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Cissia Texture hashes ===
'b39896c4': [
        (log,                           ('2.8: Cissia Hair/Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'31674c56': [
        (log,                           ('2.8: Cissia Hair LightMap Hash [New]',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'abb852a0': [
        (log,                           ('2.8: Cissia Hair MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'8f55186a': [
        (log,                           ('2.8: Cissia Tongue/Face/Brows Diffuse Hash [New]',)),
        (add_section_if_missing,        ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'fcfeb117': [
        (log,                           ('2.8: Cissia Body Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'2b6d5c26': [
        (log,                           ('2.8: Cissia Body LightMap Hash [New]',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'e5edf7dd': [
        (log,                           ('2.8: Cissia Body MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'ec85e98d': [
        (log,                           ('2.8: Cissia Body/Tail/Spear Diffuse Hash [New]',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],
'6fadb6f5': [
        (log,                           ('2.8: Cissia Body/Tail/Spear LightMap Hash [New]',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],
'1d5d53cd': [
        (log,                           ('2.8: Cissia Body/Tail/Spear MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Cissia Shared NormalMap [New]',)),
        (add_section_if_missing,        ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d49a5866', 'Cissia.SpearChanging.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Cissia',
    'game_versions': ['2.8'],
}