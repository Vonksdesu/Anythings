"""
Billy Character Hash Commands
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
    Returns Billy's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'21e98aeb': [(log, ('2.8: Billy Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'3371580a': [(log, ('2.8: Billy Body IB Hash',)),                        (add_ib_check_if_missing,)],
'dc7978f3': [(log, ('2.8: Billy Head IB Hash',)),                        (add_ib_check_if_missing,)],
'9f671d6b': [(log, ('2.8: Billy Weapon Right-Gun IB Hash',)),            (add_ib_check_if_missing,)],
'1fd6dbf3': [(log, ('2.8: Billy Weapon Left-Gun IB Hash',)),             (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'3e4c0174': [(log, ('2.8: Billy Hair draw_vb',)),                        (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n'))],
'5783253e': [(log, ('2.8: Billy Hair position_vb',)),                    (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n'))],
'5d6b7415': [(log, ('2.8: Billy Hair texcoord_vb',)),                    (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n'))],
'cc5695a9': [(log, ('2.8: Billy Hair blend_vb',)),                       (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n'))],

# Body
'2e9d0312': [(log, ('2.8: Billy Body draw_vb',)),                        (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n'))],
'36a0392d': [(log, ('2.8: Billy Body position_vb',)),                    (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n'))],
'89eeb1af': [(log, ('2.8: Billy Body texcoord_vb',)),                    (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n'))],
'771fdae9': [(log, ('2.8: Billy Body blend_vb',)),                       (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n'))],

# Face / Head
'd776fbbe': [(log, ('2.8: Billy Head VertexLimit Hash',)),               (add_section_if_missing, ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n'))],
'ed6468f9': [(log, ('2.8: Billy Head position_vb Hash',)),               (add_section_if_missing, ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n'))],
'b19e644f': [(log, ('2.8: Billy Head texcoord_vb Hash',)),               (add_section_if_missing, ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n'))],
'26b0deb9': [(log, ('2.8: Billy Head blend_vb Hash',)),                  (add_section_if_missing, ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'e5f2fc35': [(log, ('1.0->2.8: Billy HeadA NormalMap 2048p Hash',)),    (update_hash, ('ebac056e',))],
'9f02ef2b': [(log, ('1.0->2.8: Billy HeadA LightMap 2048p Hash',)),     (update_hash, ('cf4769ce',))],
'd166c3e5': [(log, ('1.0->2.8: Billy HeadA MaterialMap 2048p Hash',)), (update_hash, ('3a7d88a1',))],
'0475db07': [(log, ('1.0->2.8: Billy HairA Diffuse 2048p Hash',)),       (update_hash, ('ff939fb7',))],
'4817b1bc': [(log, ('1.0->2.8: Billy HairA LightMap 2048p Hash',)),      (update_hash, ('b6e1da4b',))],
'47bbe297': [(log, ('1.0->2.8: Billy HairA NormalMap 2048p Hash',)),      (update_hash, ('798adba3',))],
'789b054e': [(log, ('1.0->2.8: Billy BodyA LightMap 2048p Hash',)),      (update_hash, ('6305a7f4',))],
'56b5953e': [(log, ('1.0->2.8: Billy BodyA NormalMap 2048p Hash',)),      (update_hash, ('ebac056e',))],

# === Pembaruan Sinkronisasi Senjata v2.8 ===
'3a1ee1d7': [(log, ('2.0 -> 2.8: Billy Weapon Diffuse Hash [Legacy]',)),   (update_hash, ('3541c183',))],
'4b0a8224': [(log, ('2.0 -> 2.8: Billy Weapon LightMap Hash [Legacy]',)),  (update_hash, ('6f6aad09',))],
'49782d36': [(log, ('2.0 -> 2.8: Billy Weapon MaterialMap Hash [Legacy]',)), (update_hash, ('11af0644',))],

# === Face Textures ===
'a1d68c9e': [
        (log,                           ('2.8: Billy HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6f8a9cdb', 'Billy.HeadA.Diffuse.2048')),
    ],
'6f8a9cdb': [
        (log,                           ('2.8: Billy HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a1d68c9e', 'Billy.HeadA.Diffuse.1024')),
    ],
'eed0cd5f': [
        (log,                           ('2.8: Billy HeadA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Billy.HeadA.NormalMap.2048')),
    ],
'877e1a0d': [
        (log,                           ('2.8: Billy HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cf4769ce', 'Billy.HeadA.LightMap.2048')),
    ],
'cf4769ce': [
        (log,                           ('2.8: Billy HeadA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('877e1a0d', 'Billy.HeadA.LightMap.1024')),
    ],
'f5a507da': [
        (log,                           ('2.8: Billy Face LightMap Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
    ],
'dc2f2dd2': [
        (log,                           ('2.8: Billy HeadA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3a7d88a1', 'Billy.HeadA.MaterialMap.2048')),
    ],
'3a7d88a1': [
        (log,                           ('2.8: Billy HeadA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc2f2dd2', 'Billy.HeadA.MaterialMap.1024')),
    ],
'e534abc0': [
        (log,                           ('2.8: Billy Face MaterialMap Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'6a6a1c79': [
        (log,                           ('2.8: Billy Hair Diffuse Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'ff939fb7': [
        (log,                           ('2.8: Billy HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c0360c81', 'Billy.HairA.Diffuse.1024')),
    ],
'c0360c81': [
        (log,                           ('2.8: Billy HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ff939fb7', 'Billy.HairA.Diffuse.2048')),
    ],
'b6e1da4b': [
        (log,                           ('2.8: Billy HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d269a0a1', 'Billy.HairA.LightMap.1024')),
    ],
'd269a0a1': [
        (log,                           ('2.8: Billy HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b6e1da4b', 'Billy.HairA.LightMap.2048')),
    ],
'2edbc842': [
        (log,                           ('2.8: Billy Hair LightMap Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'058d85b5': [
        (log,                           ('2.8: Billy HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'399d9865': [
        (log,                           ('2.8: Billy BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('af07a583', 'Billy.BodyA.Diffuse.1024')),
    ],
'af07a583': [
        (log,                           ('2.8: Billy BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('399d9865', 'Billy.BodyA.Diffuse.2048')),
    ],
'6305a7f4': [
        (log,                           ('2.8: Billy BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0d5d374f', 'Billy.BodyA.LightMap.1024')),
    ],
'0d5d374f': [
        (log,                           ('2.8: Billy BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6305a7f4', 'Billy.BodyA.LightMap.2048')),
    ],
'adc2ec7c': [
        (log,                           ('2.8: Billy Body LightMap Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
    ],
'9cb20fa9': [
        (log,                           ('2.8: Billy BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b3cabf65', 'Billy.BodyA.MaterialMap.1024')),
    ],
'b3cabf65': [
        (log,                           ('2.8: Billy BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9cb20fa9', 'Billy.BodyA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'3541c183': [
        (log,                           ('2.8: Billy Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('9f671d6b', 'Billy.WeaponRight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1fd6dbf3', 'Billy.WeaponLeft.IB', 'match_priority = 0\n')),
    ],
'6f6aad09': [
        (log,                           ('2.8: Billy Weapon LightMap Hash',)),
        (add_section_if_missing,        ('9f671d6b', 'Billy.WeaponRight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1fd6dbf3', 'Billy.WeaponLeft.IB', 'match_priority = 0\n')),
    ],
'11af0644': [
        (log,                           ('2.8: Billy Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('9f671d6b', 'Billy.WeaponRight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1fd6dbf3', 'Billy.WeaponLeft.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Billy Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9f671d6b', 'Billy.WeaponRight.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1fd6dbf3', 'Billy.WeaponLeft.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log,                           ('2.8: Billy Hair Shared NormalMap Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'27185819': [
        (log,                           ('2.8: Billy HairA NormalMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('798adba3', 'Billy.HairA.NormalMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.8: Billy BodyA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('71d95d5d', 'Billy.BodyA.NormalMap.1024')),
    ],
'71d95d5d': [
        (log,                           ('2.8: Billy BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Billy.BodyA.NormalMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Billy',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}