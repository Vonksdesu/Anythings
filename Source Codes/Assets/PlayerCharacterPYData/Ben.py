"""
Ben Character Hash Commands
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
    Returns Ben's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'9c4f1a9a': [(log, ('2.8: Ben Face IB Hash',)),                          (add_ib_check_if_missing,)],
'94288cca': [(log, ('2.8: Ben Body IB Hash',)),                          (add_ib_check_if_missing,)],
'4e4f3440': [(log, ('2.8: Ben Weapon IB Hash',)),                        (add_ib_check_if_missing,)],

# === VB Hashes ===
# Body
'dfd93ee5': [(log, ('2.8: Ben Body draw_vb Hash',)),                     (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n'))],
'b4db1979': [(log, ('2.8: Ben Body position_vb Hash',)),                 (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n'))],
'c7b58675': [(log, ('2.8: Ben Body texcoord_vb Hash',)),                 (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n'))],

# Face
'7e77201a': [(log, ('2.8: Ben Face VertexLimit Hash',)),                 (add_section_if_missing, ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n'))],
'18d26bd2': [(log, ('2.8: Ben Face blend_vb Hash',)),                    (add_section_if_missing, ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n'))],

# Weapon
'fcc2accc': [(log, ('2.8: Ben Weapon VertexLimit Hash',)),               (add_section_if_missing, ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n'))],
'3c5c930c': [(log, ('2.8: Ben Weapon position_vb Hash',)),               (add_section_if_missing, ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n'))],
'89932f55': [(log, ('2.8: Ben Weapon texcoord_vb Hash',)),               (add_section_if_missing, ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n'))],
'a0c80593': [(log, ('2.8: Ben Weapon blend_vb Hash [Legacy]',)),          (update_hash, ('7a0c8bf9',))],
'7a0c8bf9': [(log, ('2.8: Ben Weapon blend_vb Hash',)),                  (add_section_if_missing, ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n'))],

# === Body Updates ===
'a2f79d33': [(log, ('2.8: Ben Body Blend Hash (OLD)',)),                (update_hash, ('21dd67a7',))],
'21dd67a7': [(log, ('2.8: Ben Body Blend Hash',)),                      (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'00002f2c': [
        (log,                           ('2.8: Ben FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'cc195dc5': [
        (log,                           ('2.8: Ben FaceA LightMap Hash (OLD)',)),
        (update_hash,                   ('2fa5ffa7',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'2fa5ffa7': [
        (log,                           ('2.8: Ben FaceA LightMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'9372e123': [
        (log,                           ('2.8: Ben Face LightMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'0bbceea0': [
        (log,                           ('2.8: Ben FaceA MaterialMap Hash (OLD)',)),
        (update_hash,                   ('12e5120e',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'12e5120e': [
        (log,                           ('2.8: Ben FaceA MaterialMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'dd8c0b3a': [
        (log,                           ('2.8: Ben Face MaterialMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'0313ed95': [
        (log,                           ('2.8: Ben BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'cb84ed5e': [
        (log,                           ('2.8: Ben BodyA LightMap Hash (OLD)',)),
        (update_hash,                   ('d27a8f6b',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'd27a8f6b': [
        (log,                           ('2.8: Ben BodyA LightMap Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'9a724295': [
        (log,                           ('2.8: Ben Body LightMap Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'3f4f6bc0': [
        (log,                           ('2.8: Ben BodyA MaterialMap Hash (OLD)',)),
        (update_hash,                   ('2edd6f62',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'2edd6f62': [
        (log,                           ('2.8: Ben BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'3678fad4': [
        (log,                           ('2.8: Ben Body MaterialMap Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures ===
'fb05197d': [
        (log,                           ('2.8: Ben Weapon Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],
'ac04b14e': [
        (log,                           ('2.8: Ben Weapon LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],
'7eec482a': [
        (log,                           ('2.8: Ben Weapon MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Ben Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Ben Face/Body NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],

# === Legacy 1024p texture variants ===
'8d83daba': [(log, ('2.8: Ben FaceA Diffuse 1024p Hash [Legacy]',)),      (update_hash, ('00002f2c',))],
'1439d2b9': [(log, ('2.8: Ben FaceA LightMap 1024p Hash [Legacy]',)),     (update_hash, ('2fa5ffa7',))],
'd665246d': [(log, ('2.8: Ben FaceA MaterialMap 1024p Hash [Legacy]',)),  (update_hash, ('12e5120e',))],
'894ea737': [(log, ('2.8: Ben FaceA NormalMap 2048p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'ba809960': [(log, ('2.8: Ben FaceA NormalMap 1024p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'd8dc4645': [(log, ('2.8: Ben BodyA Diffuse 1024p Hash [Legacy]',)),      (update_hash, ('0313ed95',))],
'6a80c2d8': [(log, ('2.8: Ben BodyA LightMap 1024p Hash [Legacy]',)),     (update_hash, ('d27a8f6b',))],
'decc28c5': [(log, ('2.8: Ben BodyA MaterialMap 1024p Hash [Legacy]',)),  (update_hash, ('2edd6f62',))],
'1b79fa5c': [(log, ('2.8: Ben BodyA NormalMap 2048p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'f6ecc618': [(log, ('2.8: Ben BodyA NormalMap 1024p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],

# === New Database 2.8 Synced Ben Weapon hashes ===
'6fc3d991': [
        (log,                           ('2.8: Ben Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],
'bd88580a': [
        (log,                           ('2.8: Ben Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],
'beeef18a': [
        (log,                           ('2.8: Ben Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        ('4e4f3440', 'Ben.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ben',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}