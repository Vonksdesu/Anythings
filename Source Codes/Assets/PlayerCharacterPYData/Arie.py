"""
Arie Character Hash Commands
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
    Returns Arie's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'8a7ae9c2': [(log, ('2.8: Arie Hair IB Hash',)),                         (add_ib_check_if_missing,)],
'2d1b7798': [(log, ('2.8: Arie HairShadow IB Hash',)),                   (add_ib_check_if_missing,)],
'8c5b553a': [(log, ('2.8: Arie Body IB Hash',)),                         (add_ib_check_if_missing,)],
'e6ff7471': [(log, ('2.8: Arie Leg IB Hash',)),                          (add_ib_check_if_missing,)],
'c0b0db5f': [(log, ('2.8: Arie Eyebrow IB Hash',)),                      (add_ib_check_if_missing,)],
'27966f80': [(log, ('2.8: Arie Face IB Hash',)),                         (add_ib_check_if_missing,)],
'16979e4f': [(log, ('2.8: Arie Weapon IB Hash',)),                       (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'697c6c6a': [(log, ('2.8: Arie Hair draw_vb',)),                         (add_section_if_missing, ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n'))],
'6a495335': [(log, ('2.8: Arie Hair position_vb',)),                     (add_section_if_missing, ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n'))],
'bcde58e5': [(log, ('2.8: Arie Hair texcoord_vb',)),                     (add_section_if_missing, ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n'))],
'8183ba3e': [(log, ('2.8: Arie Hair blend_vb',)),                        (add_section_if_missing, ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n'))],

# Body
'72cea90b': [(log, ('2.8: Arie Body draw_vb',)),                         (add_section_if_missing, ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n'))],
'be8eacb4': [(log, ('2.8: Arie Body position_vb',)),                     (add_section_if_missing, ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n'))],
'7bdc71a8': [(log, ('2.8: Arie Body texcoord_vb',)),                     (add_section_if_missing, ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n'))],
'a08b2a67': [(log, ('2.8: Arie Body blend_vb',)),                        (add_section_if_missing, ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n'))],

# Leg
'964f2afe': [(log, ('2.8: Arie Leg draw_vb',)),                          (add_section_if_missing, ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n'))],
'bd9b3d7d': [(log, ('2.8: Arie Leg position_vb',)),                      (add_section_if_missing, ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n'))],
'2ff0ce5d': [(log, ('2.8: Arie Leg texcoord_vb',)),                      (add_section_if_missing, ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n'))],
'3060206a': [(log, ('2.8: Arie Leg blend_vb',)),                         (add_section_if_missing, ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n'))],

# Eyebrow
'cd444ce7': [(log, ('2.8: Arie Eyebrow draw_vb',)),                      (add_section_if_missing, ('c0b0db5f', 'Arie.Eyebrow.IB', 'match_priority = 0\n'))],
'b7d38cbb': [(log, ('2.8: Arie Eyebrow texcoord_vb',)),                  (add_section_if_missing, ('c0b0db5f', 'Arie.Eyebrow.IB', 'match_priority = 0\n'))],
'3b2d89e0': [(log, ('2.8: Arie Eyebrow blend_vb',)),                     (add_section_if_missing, ('c0b0db5f', 'Arie.Eyebrow.IB', 'match_priority = 0\n'))],

# Face
'fc43d4db': [(log, ('2.8: Arie Face draw_vb',)),                         (add_section_if_missing, ('27966f80', 'Arie.Face.IB', 'match_priority = 0\n'))],
'c651479c': [(log, ('2.8: Arie Face position_vb',)),                     (add_section_if_missing, ('27966f80', 'Arie.Face.IB', 'match_priority = 0\n'))],
'39d7123a': [(log, ('2.8: Arie Face texcoord_vb',)),                     (add_section_if_missing, ('27966f80', 'Arie.Face.IB', 'match_priority = 0\n'))],
'3f418ccb': [(log, ('2.8: Arie Face blend_vb',)),                        (add_section_if_missing, ('27966f80', 'Arie.Face.IB', 'match_priority = 0\n'))],

# Weapon
'380bb1a8': [(log, ('2.8: Arie Weapon draw_vb Hash',)),                  (add_section_if_missing, ('16979e4f', 'Arie.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'6146195d': [(log, ('2.0 -> 2.8: Arie Face Diffuse [Legacy]',)),          (update_hash, ('1b2ae01f',))],
'dc18e71c': [(log, ('2.0 -> 2.8: Arie Hair/Leg Diffuse [Legacy]',)),      (update_hash, ('a572a368',))],
'34583b2b': [(log, ('2.0 -> 2.8: Arie Hair/Leg LightMap [Legacy]',)),     (update_hash, ('34c4faaa',))],
'e32c606c': [(log, ('2.0 -> 2.8: Arie Hair/Leg MaterialMap [Legacy]',)),  (update_hash, ('4309b48e',))],
'fda652ce': [(log, ('2.0 -> 2.8: Arie Body Diffuse [Legacy]',)),          (update_hash, ('a33c5da6',))],
'f575fc9d': [(log, ('2.0 -> 2.8: Arie Body LightMap [Legacy]',)),         (update_hash, ('ab389fa7',))],
'aaec2e94': [(log, ('2.0 -> 2.8: Arie Body MaterialMap [Legacy]',)),      (update_hash, ('40eff501',))],
'5ec4228a': [(log, ('2.0 -> 2.8: Arie Weapon Diffuse [Legacy]',)),       (update_hash, ('f797551b',))],
'e180bd1c': [(log, ('2.0 -> 2.8: Arie Weapon LightMap [Legacy]',)),      (update_hash, ('6c620c16',))],
'777472dd': [(log, ('2.0 -> 2.8: Arie Weapon MaterialMap [Legacy]',)),   (update_hash, ('9e9d8560',))],

# === Face & Eyebrow Textures (v2.8 Target) ===
'1b2ae01f': [
        (log,                           ('2.8: Arie FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('27966f80', 'Arie.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0b0db5f', 'Arie.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair & Leg Shared Textures (v2.8 Target) ===
'a572a368': [
        (log,                           ('2.8: Arie HairA, LegA Diffuse Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n')),
    ],
'34c4faaa': [
        (log,                           ('2.8: Arie HairA, LegA LightMap Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n')),
    ],
'4309b48e': [
        (log,                           ('2.8: Arie HairA, LegA MaterialMap Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (v2.8 Target) ===
'a33c5da6': [
        (log,                           ('2.8: Arie BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n')),
    ],
'ab389fa7': [
        (log,                           ('2.8: Arie BodyA LightMap Hash',)),
        (add_section_if_missing,        ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n')),
    ],
'40eff501': [
        (log,                           ('2.8: Arie BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'f797551b': [
        (log,                           ('2.8: Arie WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('16979e4f', 'Arie.Weapon.IB', 'match_priority = 0\n')),
    ],
'6c620c16': [
        (log,                           ('2.8: Arie WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('16979e4f', 'Arie.Weapon.IB', 'match_priority = 0\n')),
    ],
'9e9d8560': [
        (log,                           ('2.8: Arie WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('16979e4f', 'Arie.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Arie Shared NormalMap Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('16979e4f', 'Arie.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Arie Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('8a7ae9c2', 'Arie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8c5b553a', 'Arie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6ff7471', 'Arie.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('16979e4f', 'Arie.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Arie',
    'game_versions': ['2.8'],
}