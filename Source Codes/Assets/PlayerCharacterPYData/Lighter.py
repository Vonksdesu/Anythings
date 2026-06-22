"""
Lighter Character Hash Commands
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
    Returns Lighter's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'542b8aa9': [(log, ('2.8: Lighter Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'8899e0fd': [(log, ('2.8: Lighter Body IB Hash',)),                      (add_ib_check_if_missing,)],
'dcc7bb78': [(log, ('2.8: Lighter Face IB Hash',)),                      (add_ib_check_if_missing,)],
'b20b7cd5': [(log, ('2.8: Lighter Glasses IB Hash',)),                   (add_ib_check_if_missing,)],
'cf4c4714': [(log, ('2.8: Lighter Hair Shadow IB Hash',)),              (add_ib_check_if_missing,)],
'2de659bd': [(log, ('2.8: Lighter Cloak IB Hash',)),                     (add_ib_check_if_missing,)],
'018b03f0': [(log, ('2.8: Lighter Weapon IB Hash',)),                    (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'bd669b85': [(log, ('2.8: Lighter Hair draw_vb',)),                     (add_section_if_missing, ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n'))],
'037b6287': [(log, ('2.8: Lighter Hair position_vb',)),                 (add_section_if_missing, ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n'))],
'22a08e39': [(log, ('2.8: Lighter Hair texcoord_vb',)),                 (add_section_if_missing, ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n'))],
'd88fa0aa': [(log, ('2.8: Lighter Hair blend_vb',)),                    (add_section_if_missing, ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'4104c8e0': [(log, ('2.8: Lighter Hair Shadow draw_vb',)),              (add_section_if_missing, ('cf4c4714', 'Lighter.HairShadow.IB', 'match_priority = 0\n'))],
'e144ad1c': [(log, ('2.8: Lighter Hair Shadow position_vb',)),          (add_section_if_missing, ('cf4c4714', 'Lighter.HairShadow.IB', 'match_priority = 0\n'))],
'7749cb20': [(log, ('2.8: Lighter Hair Shadow texcoord_vb',)),          (add_section_if_missing, ('cf4c4714', 'Lighter.HairShadow.IB', 'match_priority = 0\n'))],
'3abed50b': [(log, ('2.8: Lighter Hair Shadow blend_vb',)),             (add_section_if_missing, ('cf4c4714', 'Lighter.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'84ed822e': [(log, ('2.8: Lighter Body draw_vb',)),                     (add_section_if_missing, ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n'))],
'f6bbabb5': [(log, ('2.8: Lighter Body position_vb',)),                 (add_section_if_missing, ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n'))],
'e1ae7f38': [(log, ('2.8: Lighter Body texcoord_vb',)),                 (add_section_if_missing, ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n'))],
'da216bb6': [(log, ('2.8: Lighter Body blend_vb',)),                    (add_section_if_missing, ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n'))],

# Cloak
'701ad22d': [(log, ('2.8: Lighter Cloak draw_vb',)),                    (add_section_if_missing, ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n'))],
'b642df39': [(log, ('2.8: Lighter Cloak position_vb',)),                (add_section_if_missing, ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n'))],
'1f9a45b3': [(log, ('2.8: Lighter Cloak texcoord_vb',)),                (add_section_if_missing, ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n'))],
'609ecf0b': [(log, ('2.8: Lighter Cloak blend_vb',)),                   (add_section_if_missing, ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n'))],

# Glasses
'62623b11': [(log, ('2.8: Lighter Glasses draw_vb',)),                  (add_section_if_missing, ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n'))],
'fc862707': [(log, ('2.8: Lighter Glasses position_vb',)),              (add_section_if_missing, ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n'))],
'527dad23': [(log, ('2.8: Lighter Glasses texcoord_vb',)),              (add_section_if_missing, ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n'))],
'3395524c': [(log, ('2.8: Lighter Glasses blend_vb',)),                 (add_section_if_missing, ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n'))],

# Face
'aa77af05': [(log, ('2.8: Lighter Face VertexLimit',)),                 (add_section_if_missing, ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n'))],
'5841afbd': [(log, ('2.8: Lighter Face position_vb',)),                 (add_section_if_missing, ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n'))],
'af14829b': [(log, ('2.8: Lighter Face texcoord_vb',)),                 (add_section_if_missing, ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n'))],
'7edbb44e': [(log, ('2.8: Lighter Face blend_vb',)),                    (add_section_if_missing, ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n'))],

# Weapon
'390caccd': [(log, ('2.8: Lighter Weapon VertexLimit',)),               (add_section_if_missing, ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n'))],
'88aecee2': [(log, ('2.8: Lighter Weapon texcoord_vb',)),               (add_section_if_missing, ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n'))],
'e83ca18e': [(log, ('2.8: Lighter Weapon blend_vb',)),                  (add_section_if_missing, ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Updates ===
'039f30cf': [(log, ('1.3 -> 1.4: Lighter Face IB Hash',)),    (update_hash, ('dcc7bb78',))],
'0baec6b7': [(log, ('1.3 -> 1.4: Lighter Body Position Hash',)), (update_hash, ('5e461440',))],
'710bca71': [(log, ('1.3 -> 1.4: Lighter Body Texcoord Hash',)), (update_hash, ('25ad7289',))],
'5e461440': [(log, ('1.5 -> 1.6: Lighter Body Position Hash',)), (update_hash, ('f6bbabb5',))],
'25ad7289': [(log, ('1.5 -> 1.6: Lighter Body Texcoord Hash',)), (update_hash, ('e1ae7f38',))],
'ebac056e': [(log, ('2.8: Lighter Shared NormalMap Hash [Legacy]',)), (update_hash, ('798adba3',))],

# === Pembaruan Sinkronisasi 2.8 ===
'c5d60a1d': [(log, ('2.7 -> 2.8: Lighter Hair/Cloak Diffuse [Legacy]',)), (update_hash, ('4e088042',))],
'd5ba9ea6': [(log, ('2.7 -> 2.8: Lighter Hair/Cloak MaterialMap [Legacy]',)), (update_hash, ('d331b850',))],
'6506987b': [(log, ('2.0 -> 2.8: Lighter Weapon Diffuse [Legacy]',)), (update_hash, ('8b854866',))],
'939a2e18': [(log, ('2.0 -> 2.8: Lighter Weapon LightMap [Legacy]',)), (update_hash, ('547cbcd8',))],
'1684d3e4': [(log, ('2.0 -> 2.8: Lighter Weapon MaterialMap [Legacy]',)), (update_hash, ('3617c303',))],

# === Face Textures ===
'8ec33dd0': [
        (log,                           ('2.8: Lighter FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('dcc7bb78', '039f30cf'), 'Lighter.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4524e91a', 'Lighter.FaceA.Diffuse.2048')),
    ],
'4524e91a': [
        (log,                           ('2.8: Lighter FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('dcc7bb78', '039f30cf'), 'Lighter.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8ec33dd0', 'Lighter.FaceA.Diffuse.1024')),
    ],

# === Hair & Cloak Textures (v2.8 Target) ===
'1cd2d442': [
        (log,                           ('2.8: Lighter HairA Diffuse 1024p Hash (Old)',)),
        (update_hash,                   ('4e088042',)),
    ],
'8687f7b8': [
        (log,                           ('2.8: Lighter HairA MaterialMap 1024p Hash (Old)',)),
        (update_hash,                   ('d331b850',)),
    ],
'4e088042': [
        (log,                           ('2.8: Lighter Hair/Cloak Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1cd2d442', 'Lighter.HairA.Diffuse.1024')),
    ],
'd331b850': [
        (log,                           ('2.8: Lighter Hair/Cloak MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8687f7b8', 'Lighter.HairA.MaterialMap.1024')),
    ],
'0ee07935': [
        (log,                           ('2.8: Lighter Hair/Cloak Diffuse Target Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
    ],
'62ec7f01': [
        (log,                           ('2.8: Lighter HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6d3f91bc', 'Lighter.HairA.LightMap.2048')),
    ],
'99ad14f1': [
        (log,                           ('2.8: Lighter Hair MaterialMap Target Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
    ],
'6d3f91bc': [
        (log,                           ('2.8: Lighter HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('62ec7f01', 'Lighter.HairA.LightMap.1024')),
    ],

# === Body Textures ===
'be46890b': [
        (log,                           ('2.8: Lighter BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5ed96bf2', 'Lighter.BodyA.Diffuse.2048')),
    ],
'5b828635': [
        (log,                           ('2.8: Lighter BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da6f4dc0', 'Lighter.BodyA.LightMap.2048')),
    ],
'65f3bb7c': [
        (log,                           ('2.8: Lighter BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('94aebd7e', 'Lighter.BodyA.MaterialMap.2048')),
    ],
'5ed96bf2': [
        (log,                           ('2.8: Lighter BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('be46890b', 'Lighter.BodyA.Diffuse.1024')),
    ],
'da6f4dc0': [
        (log,                           ('2.8: Lighter BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5b828635', 'Lighter.BodyA.LightMap.1024')),
    ],
'94aebd7e': [
        (log,                           ('2.8: Lighter BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('65f3bb7c', 'Lighter.BodyA.MaterialMap.1024')),
    ],

# === Weapon Textures ===
'8b854866': [
        (log,                           ('2.8: Lighter Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n')),
    ],
'547cbcd8': [
        (log,                           ('2.8: Lighter Weapon LightMap Hash',)),
        (add_section_if_missing,        ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n')),
    ],
'3617c303': [
        (log,                           ('2.8: Lighter Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Lighter Shared NormalMap Hash',)),
        (add_section_if_missing,        ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf4c4714', 'Lighter.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('018b03f0', 'Lighter.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lighter',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}