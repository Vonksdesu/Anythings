"""
Anton Character Hash Commands
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
    Returns Anton's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'6b95c80d': [(log, ('2.8: Anton Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'653fb27c': [(log, ('2.8: Anton Body IB Hash',)),                        (add_ib_check_if_missing,)],
'a21fcee4': [(log, ('2.8: Anton Jacket IB Hash',)),                      (add_ib_check_if_missing,)],
'a0201907': [(log, ('2.8: Anton Head IB Hash',)),                        (add_ib_check_if_missing,)],
'0112ffd6': [(log, ('2.8: Anton Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'a21ac290': [(log, ('2.8: Anton Weapon IB Hash',)),                      (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd46d8476': [(log, ('2.8: Anton Hair draw_vb',)),                        (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n'))],
'8ab64867': [(log, ('2.8: Anton Hair position_vb',)),                    (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n'))],
'bab585ea': [(log, ('2.8: Anton Hair texcoord_vb',)),                    (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n'))],
'884e7cc3': [(log, ('2.8: Anton Hair blend_vb',)),                       (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'52fa44ae': [(log, ('2.8: Anton Hair Shadow draw_vb',)),                 (add_section_if_missing, ('0112ffd6', 'Anton.HairShadow.IB', 'match_priority = 0\n'))],
'558ab813': [(log, ('2.8: Anton Hair Shadow position_vb',)),             (add_section_if_missing, ('0112ffd6', 'Anton.HairShadow.IB', 'match_priority = 0\n'))],
'1f1b89ae': [(log, ('2.8: Anton Hair Shadow texcoord_vb',)),             (add_section_if_missing, ('0112ffd6', 'Anton.HairShadow.IB', 'match_priority = 0\n'))],
'8d0bcd2b': [(log, ('2.8: Anton Hair Shadow blend_vb',)),                (add_section_if_missing, ('0112ffd6', 'Anton.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'9f262894': [(log, ('2.8: Anton Body draw_vb',)),                        (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n'))],
'339b1975': [(log, ('2.8: Anton Body position_vb',)),                    (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n'))],
'66217473': [(log, ('2.8: Anton Body texcoord_vb',)),                    (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n'))],
'76bc385f': [(log, ('2.8: Anton Body blend_vb',)),                       (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n'))],

# Jacket
'112ccbbd': [(log, ('2.8: Anton Jacket draw_vb',)),                      (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n'))],
'9f0a8d2e': [(log, ('2.8: Anton Jacket position_vb',)),                  (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n'))],
'1727e9e4': [(log, ('2.8: Anton Jacket texcoord_vb',)),                  (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n'))],
'3edd7ceb': [(log, ('2.8: Anton Jacket blend_vb',)),                     (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n'))],

# Face
'f7cda875': [(log, ('2.8: Anton Face VertexLimit Hash',)),                (add_section_if_missing, ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n'))],
'cddf3b32': [(log, ('2.8: Anton Face position_vb Hash',)),                (add_section_if_missing, ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n'))],
'144828a7': [(log, ('2.8: Anton Face texcoord_vb Hash',)),                (add_section_if_missing, ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n'))],
'ec9763c1': [(log, ('2.8: Anton Face blend_vb Hash',)),                   (add_section_if_missing, ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n'))],

# Weapon
'fa346a40': [(log, ('2.8: Anton Weapon VertexLimit Hash',)),              (add_section_if_missing, ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n'))],
'193b9ea3': [(log, ('2.8: Anton Weapon position_vb Hash',)),              (add_section_if_missing, ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n'))],
'65b52652': [(log, ('2.8: Anton Weapon texcoord_vb Hash',)),              (add_section_if_missing, ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n'))],
'2906a23f': [(log, ('2.8: Anton Weapon blend_vb Hash',)),                 (add_section_if_missing, ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'ee06579e': [(log, ('2.8: Anton HairA LightMap 2048p Hash [Legacy]',)),   (update_hash, ('41601dfa',))],
'21ee9a3f': [(log, ('2.8: Anton HairA LightMap 1024p Hash [Legacy]',)),   (update_hash, ('41601dfa',))],
'24caeb1f': [(log, ('2.8: Anton HairA MaterialMap 2048p Hash [Legacy]',)), (update_hash, ('d47c5823',))],
'6fc654e1': [(log, ('2.8: Anton HairA MaterialMap 1024p Hash [Legacy]',)), (update_hash, ('d47c5823',))],
'b216f758': [(log, ('2.8: Anton HairA NormalMap 2048p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'77ae203f': [(log, ('2.8: Anton HairA NormalMap 1024p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'1b4ad5b7': [(log, ('2.8: Anton BodyA NormalMap 2048p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'5b2ab0e0': [(log, ('2.8: Anton BodyA NormalMap 1024p Hash [Legacy]',)),    (update_hash, ('ebac056e',))],
'17cf1b74': [(log, ('2.8: Anton BodyA LightMap 2048p Hash [Legacy]',)),    (update_hash, ('ed6f4199',))],
'8e5ba7d0': [(log, ('2.8: Anton BodyA LightMap 1024p Hash [Legacy]',)),    (update_hash, ('ed6f4199',))],
'0238b0ff': [(log, ('2.8: Anton BodyA MaterialMap 2048p Hash [Legacy]',)), (update_hash, ('986c9716',))],
'b7ce5f0b': [(log, ('2.8: Anton BodyA MaterialMap 1024p Hash [Legacy]',)), (update_hash, ('986c9716',))],
'886a664a': [(log, ('2.8: Anton JacketA LightMap 2048p Hash [Legacy]',)),  (update_hash, ('ef7880e3',)),],
'c42628a5': [(log, ('2.8: Anton JacketA LightMap 1024p Hash [Legacy]',)),  (update_hash, ('ef7880e3',)),],
'd7517d0e': [(log, ('2.8: Anton JacketA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],
'ae3d5fb8': [(log, ('2.8: Anton JacketA NormalMap 1024p Hash [Legacy]',)), (update_hash, ('ebac056e',))],

# === Pembaruan Sinkronisasi Senjata v2.8 ===
'66f89e6e': [(log, ('2.0 -> 2.8: Anton Weapon Diffuse Hash [Legacy]',)),   (update_hash, ('dc3a9ef1',))],
'3eba6997': [(log, ('2.0 -> 2.8: Anton Weapon LightMap Hash [Legacy]',)),  (update_hash, ('cf503557',))],
'f9971d30': [(log, ('2.0 -> 2.8: Anton Weapon MaterialMap Hash [Legacy]',)), (update_hash, ('bd257544',))],

# === Face Textures ===
'15cb1aee': [
        (log,                           ('2.8: Anton HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('842119d6', 'Anton.HeadA.Diffuse.2048')),
    ],
'842119d6': [
        (log,                           ('2.8: Anton HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('15cb1aee', 'Anton.HeadA.Diffuse.1024')),
    ],
'654134c1': [
        (log,                           ('2.8: Anton HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ac7fb2e2', 'Anton.HeadA.LightMap.2048')),
    ],
'ac7fb2e2': [
        (log,                           ('2.8: Anton HeadA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('654134c1', 'Anton.HeadA.LightMap.1024')),
    ],

# === Hair Textures ===
'571aa398': [
        (log,                           ('2.8: Anton HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d4c4c604', 'Anton.HairA.Diffuse.1024')),
    ],
'd4c4c604': [
        (log,                           ('2.8: Anton HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('571aa398', 'Anton.HairA.Diffuse.2048')),
    ],
'41601dfa': [
        (log,                           ('2.8: Anton HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'f6e280b0': [
        (log,                           ('2.8: Anton Hair LightMap Target Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'd47c5823': [
        (log,                           ('2.8: Anton HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'05bd454d': [
        (log,                           ('2.8: Anton Hair MaterialMap Target Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'00abcf22': [
        (log,                           ('2.8: Anton BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('581a0958', 'Anton.BodyA.Diffuse.1024')),
    ],
'581a0958': [
        (log,                           ('2.8: Anton BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('00abcf22', 'Anton.BodyA.Diffuse.2048')),
    ],
'ed6f4199': [
        (log,                           ('2.8: Anton BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'a937bcee': [
        (log,                           ('2.8: Anton Body LightMap Target Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'986c9716': [
        (log,                           ('2.8: Anton BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'bb25e0f0': [
        (log,                           ('2.8: Anton Body MaterialMap Target Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],

# === Jacket Textures ===
'd4b15508': [
        (log,                           ('2.8: Anton JacketA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f7831517', 'Anton.JacketA.Diffuse.1024')),
    ],
'f7831517': [
        (log,                           ('2.8: Anton JacketA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d4b15508', 'Anton.JacketA.Diffuse.2048')),
    ],
'ef7880e3': [
        (log,                           ('2.8: Anton JacketA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'edb33cec': [
        (log,                           ('2.8: Anton Jacket LightMap Target Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'd36a2f7a': [
        (log,                           ('2.8: Anton JacketA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('75bccc40', 'Anton.JacketA.MaterialMap.1024')),
    ],
'75bccc40': [
        (log,                           ('2.8: Anton JacketA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d36a2f7a', 'Anton.JacketA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'dc3a9ef1': [
        (log,                           ('2.8: Anton Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n')),
    ],
'cf503557': [
        (log,                           ('2.8: Anton Weapon LightMap Hash',)),
        (add_section_if_missing,        ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n')),
    ],
'bd257544': [
        (log,                           ('2.8: Anton Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Anton Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0112ffd6', 'Anton.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Anton Shared NormalMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log,                           ('2.8: Anton Weapon NormalMap Hash',)),
        (add_section_if_missing,        ('a21ac290', 'Anton.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Anton',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}