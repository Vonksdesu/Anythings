"""
Anby Character Hash Commands
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
    Returns Anby's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'5c0240db': [(log, ('2.8: Anby Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'4816de84': [(log, ('2.8: Anby Body IB Hash',)),                        (add_ib_check_if_missing,)],
'19df8e84': [(log, ('2.8: Anby Head IB Hash',)),                        (add_ib_check_if_missing,)],
'6f5e7cdb': [(log, ('2.8: Anby Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'92209737': [(log, ('2.8: Anby Weapon Scabbard IB Hash',)),              (add_ib_check_if_missing,)],
'5bb510c6': [(log, ('2.8: Anby Weapon Blade IB Hash',)),                 (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'91ffb01c': [(log, ('2.8: Anby Hair draw_vb Hash',)),                   (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n'))],
'9af848eb': [(log, ('2.8: Anby Hair position_vb Hash',)),               (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n'))],
'496a781d': [(log, ('2.8: Anby Hair texcoord_vb [v2.8 Target]',)),      (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n'))],
'313933a0': [(log, ('2.8: Anby Hair blend_vb Hash',)),                  (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'f6ed0e7b': [(log, ('2.8: Anby Hair Shadow draw_vb Hash',)),            (add_section_if_missing, ('6f5e7cdb', 'Anby.HairShadow.IB', 'match_priority = 0\n'))],
'd431dddb': [(log, ('2.8: Anby Hair Shadow position_vb Hash',)),        (add_section_if_missing, ('6f5e7cdb', 'Anby.HairShadow.IB', 'match_priority = 0\n'))],
'b62ac7fe': [(log, ('2.8: Anby Hair Shadow texcoord_vb Hash',)),        (add_section_if_missing, ('6f5e7cdb', 'Anby.HairShadow.IB', 'match_priority = 0\n'))],
'64fc015c': [(log, ('2.8: Anby Hair Shadow blend_vb Hash',)),           (add_section_if_missing, ('6f5e7cdb', 'Anby.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'45b2509c': [(log, ('2.8: Anby Body draw_vb Hash',)),                   (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n'))],
'1c9533eb': [(log, ('2.8: Anby Body position_vb Hash',)),               (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n'))],
'a33e8b5e': [(log, ('2.8: Anby Body texcoord_vb Hash',)),               (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n'))],
'137cbdbe': [(log, ('2.8: Anby Body blend_vb Hash',)),                  (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n'))],

# Face
'9f6aa443': [(log, ('2.8: Anby Face VertexLimit [v2.8 Target]',)),      (add_section_if_missing, ('19df8e84', 'Anby.Head.IB', 'match_priority = 0\n'))],
'a5e8de50': [(log, ('2.8: Anby Face Position Hash [v2.8 Target]',)),    (add_section_if_missing, ('19df8e84', 'Anby.Head.IB', 'match_priority = 0\n'))],
'f818271a': [(log, ('2.8: Anby Face Texcoord Hash',)),                  (add_section_if_missing, ('19df8e84', 'Anby.Head.IB', 'match_priority = 0\n'))],
'9680d55d': [(log, ('2.8: Anby Face Blend Hash',)),                     (add_section_if_missing, ('19df8e84', 'Anby.Head.IB', 'match_priority = 0\n'))],

# Weapon - Scabbard
'1500b06e': [(log, ('2.8: Anby Weapon Scabbard VertexLimit Hash',)),    (add_section_if_missing, ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n'))],
'332be630': [(log, ('2.8: Anby Weapon Scabbard position_vb Hash',)),    (add_section_if_missing, ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n'))],
'cec4d67b': [(log, ('2.8: Anby Weapon Scabbard texcoord_vb Hash',)),    (add_section_if_missing, ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n'))],
'dd507f00': [(log, ('2.8: Anby Weapon Scabbard blend_vb Hash',)),       (add_section_if_missing, ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n'))],

# Weapon - Blade
'baf7ad46': [(log, ('2.8: Anby Weapon Blade VertexLimit Hash',)),       (add_section_if_missing, ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n'))],
'47da5929': [(log, ('2.8: Anby Weapon Blade position_vb Hash',)),       (add_section_if_missing, ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n'))],
'58ec8ffb': [(log, ('2.8: Anby Weapon Blade texcoord_vb Hash',)),       (add_section_if_missing, ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n'))],
'0385188d': [(log, ('2.8: Anby Weapon Blade blend_vb Hash',)),          (add_section_if_missing, ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'39538886': [
        (log, ('1.1 -> 1.2: Anby Hair Texcoord Hash',)),
        (update_hash, ('496a781d',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'cc114f4f': [(log, ('2.8: Anby HeadA Diffuse 1024p Hash [Legacy]',)),   (update_hash, ('692c6d2b',))],
'2a29cb9b': [(log, ('2.8: Anby HeadA Diffuse 2048p Hash [Legacy]',)),   (update_hash, ('05d7b504',))],
'b54f2a3d': [(log, ('2.8: Anby HairA LightMap 2048p Hash [Legacy]',)),  (update_hash, ('057f3c55',))],
'9ceea795': [(log, ('2.8: Anby HairA LightMap 1024p Hash [Legacy]',)),  (update_hash, ('057f3c55',))],
'20890a00': [(log, ('2.8: Anby HairA NormalMap 2048p Hash [Legacy]',)),  (update_hash, ('ebac056e',))],
'3101f0da': [(log, ('2.8: Anby HairA NormalMap 1024p Hash [Legacy]',)),  (update_hash, ('ebac056e',))],
'b37c3b4e': [(log, ('2.8: Anby BodyA Diffuse 2048p Hash [Legacy]',)),   (update_hash, ('215ff74d',))],
'8bd7966f': [(log, ('2.8: Anby BodyA Diffuse 1024p Hash [Legacy]',)),   (update_hash, ('8df45cb8',))],
'7c24acc9': [(log, ('2.8: Anby BodyA LightMap 2048p Hash [Legacy]',)),   (update_hash, ('59b123c2',))],
'9cddbf1e': [(log, ('2.8: Anby BodyA LightMap 1024p Hash [Legacy]',)),   (update_hash, ('59b123c2',))],
'19226ead': [(log, ('2.8: Anby BodyA NormalMap 2048p Hash [Legacy]',)),   (update_hash, ('ebac056e',))],
'6346d69d': [(log, ('2.8: Anby BodyA NormalMap 1024p Hash [Legacy]',)),   (update_hash, ('ebac056e',))],

# === Pembaruan Sinkronisasi Senjata v2.8 ===
'85d97523': [(log, ('2.0 -> 2.8: Anby Weapon Diffuse Hash [Legacy]',)),   (update_hash, ('d487eaac',))],
'a5e8de50': [(log, ('2.0 -> 2.8: Anby Weapon LightMap Hash [Legacy]',)),  (update_hash, ('3de2dae5',))],
'd4ddc318': [(log, ('2.0 -> 2.8: Anby Weapon MaterialMap Hash [Legacy]',)), (update_hash, ('62f1b72e',))],

# === Face Textures ===
'692c6d2b': [
        (log,                           ('2.8: Anby HeadA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('05d7b504', '2a29cb9b'), 'Anby.HeadA.Diffuse.2048')),
    ],
'05d7b504': [
        (log,                           ('2.8: Anby HeadA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('692c6d2b', 'cc114f4f'), 'Anby.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'6ea0023c': [
        (log,                           ('2.8: Anby HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7c7f96d2', 'Anby.HairA.Diffuse.1024')),
    ],
'7c7f96d2': [
        (log,                           ('2.8: Anby HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6ea0023c', 'Anby.HairA.Diffuse.2048')),
    ],
'057f3c55': [
        (log,                           ('2.8: Anby HairA LightMap Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'476ab69c': [
        (log,                           ('2.8: Anby Hair LightMap Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'790278b4': [
        (log,                           ('2.8: Anby HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'215ff74d': [
        (log,                           ('2.8: Anby BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8df45cb8', '8bd7966f'), 'Anby.BodyA.Diffuse.1024')),
    ],
'8df45cb8': [
        (log,                           ('2.8: Anby BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('215ff74d', 'b37c3b4e'), 'Anby.BodyA.Diffuse.2048')),
    ],
'59b123c2': [
        (log,                           ('2.8: Anby BodyA LightMap Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'9b57e140': [
        (log,                           ('2.8: Anby Body LightMap Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'ccca3b8e': [
        (log,                           ('2.8: Anby BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1115f163', 'Anby.BodyA.MaterialMap.1024')),
    ],
'1115f163': [
        (log,                           ('2.8: Anby BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ccca3b8e', 'Anby.BodyA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Update Target) ===
'd487eaac': [
        (log,                           ('2.8: Anby Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n')),
    ],
'3de2dae5': [
        (log,                           ('2.8: Anby Weapon LightMap Hash',)),
        (add_section_if_missing,        ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n')),
    ],
'62f1b72e': [
        (log,                           ('2.8: Anby Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Anby Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6f5e7cdb', 'Anby.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('92209737', 'Anby.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5bb510c6', 'Anby.WeaponBlade.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Anby HairA & BodyA NormalMap Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Anby',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}