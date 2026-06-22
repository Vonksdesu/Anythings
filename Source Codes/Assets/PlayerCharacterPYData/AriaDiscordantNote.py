"""
AriaDiscordantNote Character Hash Commands
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
    Returns AriaDiscordantNote's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'8a7ae9c2': [(log, ('2.8: AriaDiscordantNote Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'2d1b7798': [(log, ('2.8: AriaDiscordantNote HairShadow IB Hash',)),                (add_ib_check_if_missing,)],
'c6bb960b': [(log, ('2.8: AriaDiscordantNote Body IB Hash',)),                      (add_ib_check_if_missing,)],
'923c64c0': [(log, ('2.8: AriaDiscordantNote Leg IB Hash',)),                       (add_ib_check_if_missing,)],
'c0b0db5f': [(log, ('2.8: AriaDiscordantNote Eyebrow IB Hash',)),                   (add_ib_check_if_missing,)],
'27966f80': [(log, ('2.8: AriaDiscordantNote Face IB Hash',)),                      (add_ib_check_if_missing,)],
'16979e4f': [(log, ('2.8: AriaDiscordantNote Weapon IB Hash',)),                    (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'697c6c6a': [(log, ('2.8: AriaDiscordantNote Hair draw_vb',)),                      (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n'))],
'6a495335': [(log, ('2.8: AriaDiscordantNote Hair position_vb',)),                  (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n'))],
'bcde58e5': [(log, ('2.8: AriaDiscordantNote Hair texcoord_vb',)),                  (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n'))],
'8183ba3e': [(log, ('2.8: AriaDiscordantNote Hair blend_vb',)),                     (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n'))],

# Body
'1ece9f27': [(log, ('2.8: AriaDiscordantNote Body draw_vb',)),                      (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n'))],
'f84d5a49': [(log, ('2.8: AriaDiscordantNote Body position_vb',)),                  (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n'))],
'2046d6f4': [(log, ('2.8: AriaDiscordantNote Body texcoord_vb',)),                  (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n'))],
'56eaff1c': [(log, ('2.8: AriaDiscordantNote Body blend_vb',)),                     (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n'))],

# Leg
'80b5aa5e': [(log, ('2.8: AriaDiscordantNote Leg draw_vb',)),                       (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n'))],
'12e0707a': [(log, ('2.8: AriaDiscordantNote Leg position_vb',)),                   (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n'))],
'71977be5': [(log, ('2.8: AriaDiscordantNote Leg texcoord_vb',)),                   (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n'))],
'a7682298': [(log, ('2.8: AriaDiscordantNote Leg blend_vb',)),                      (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n'))],

# Eyebrow
'cd444ce7': [(log, ('2.8: AriaDiscordantNote Eyebrow draw_vb',)),                   (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n'))],
'b7d38cbb': [(log, ('2.8: AriaDiscordantNote Eyebrow texcoord_vb',)),               (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n'))],
'3b2d89e0': [(log, ('2.8: AriaDiscordantNote Eyebrow blend_vb',)),                  (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n'))],

# Face
'fc43d4db': [(log, ('2.8: AriaDiscordantNote Face draw_vb',)),                      (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n'))],
'c651479c': [(log, ('2.8: AriaDiscordantNote Face position_vb',)),                  (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n'))],
'39d7123a': [(log, ('2.8: AriaDiscordantNote Face texcoord_vb',)),                  (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n'))],
'3f418ccb': [(log, ('2.8: AriaDiscordantNote Face blend_vb',)),                     (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n'))],

# Weapon
'380bb1a8': [(log, ('2.8: AriaDiscordantNote Weapon draw_vb Hash',)),               (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'6146195d': [(log, ('2.0 -> 2.8: AriaDiscordantNote Face Diffuse [Legacy]',)),       (update_hash, ('1b2ae01f',))],
'd754c95b': [(log, ('2.0 -> 2.8: AriaDiscordantNote Hair/Leg Diffuse [Legacy]',)),   (update_hash, ('a34313c8',))],
'83d872c2': [(log, ('2.0 -> 2.8: AriaDiscordantNote Hair/Leg LightMap [Legacy]',)),  (update_hash, ('d378c273',))],
'e86b5691': [(log, ('2.0 -> 2.8: AriaDiscordantNote Hair/Leg MaterialMap [Legacy]',)), (update_hash, ('d3da0d5a',))],
'3c6bd181': [(log, ('2.0 -> 2.8: AriaDiscordantNote Body Diffuse [Legacy] Old',)),   (update_hash, ('677f73d9',))],
'303c63bc': [(log, ('2.0 -> 2.8: AriaDiscordantNote Body Diffuse [Legacy]',)),       (update_hash, ('677f73d9',))],
'a97204aa': [(log, ('2.0 -> 2.8: AriaDiscordantNote Body LightMap [Legacy]',)),      (update_hash, ('acee133c',))],
'2418c407': [(log, ('2.0 -> 2.8: AriaDiscordantNote Body MaterialMap [Legacy]',)),   (update_hash, ('6ac35f02',))],
'2c3a5d8d': [(log, ('2.0 -> 2.8: AriaDiscordantNote Weapon Diffuse [Legacy]',)),     (update_hash, ('adbfa4c4',))],
'4a0da1fb': [(log, ('2.0 -> 2.8: AriaDiscordantNote Weapon LightMap [Legacy]',)),    (update_hash, ('71966d3f',))],
'825f0b0b': [(log, ('2.0 -> 2.8: AriaDiscordantNote Weapon MaterialMap [Legacy]',)), (update_hash, ('328592b5',))],

# === Face & Eyebrow Textures (v2.8 Target) ===
'1b2ae01f': [
        (log,                           ('2.8: AriaDiscordantNote FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair & Leg Skin Textures (v2.8 Target) ===
'a34313c8': [
        (log,                           ('2.8: AriaDiscordantNote HairA, LegA Diffuse Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],
'd378c273': [
        (log,                           ('2.8: AriaDiscordantNote HairA, LegA LightMap Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],
'd3da0d5a': [
        (log,                           ('2.8: AriaDiscordantNote HairA, LegA MaterialMap Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],

# === Body Skin Textures (v2.8 Target) ===
'677f73d9': [
        (log,                           ('2.8: AriaDiscordantNote BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'acee133c': [
        (log,                           ('2.8: AriaDiscordantNote BodyA LightMap Hash',)),
        (add_section_if_missing,        ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'6ac35f02': [
        (log,                           ('2.8: AriaDiscordantNote BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Skin Textures (v2.8 Target) ===
'adbfa4c4': [
        (log,                           ('2.8: AriaDiscordantNote WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'71966d3f': [
        (log,                           ('2.8: AriaDiscordantNote WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'328592b5': [
        (log,                           ('2.8: AriaDiscordantNote WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: AriaDiscordantNote Shared NormalMap Hash',)),
        (add_section_if_missing,        ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: AriaDiscordantNote Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


CHARACTER_INFO = {
    'name': 'AriaDiscordantNote',
    'game_versions': ['2.8', '3.0'],
}