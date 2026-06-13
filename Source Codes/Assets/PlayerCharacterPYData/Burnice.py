"""
Burnice Character Hash Commands
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
    Returns Burnice's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'f779fb81': [(log, ('2.8: Burnice Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'af63e974': [(log, ('2.8: Burnice Body IB Hash',)),                      (add_ib_check_if_missing,)],
'b3f6fcb3': [(log, ('2.8: Burnice Head IB Hash',)),                      (add_ib_check_if_missing,)],
'40aa11a7': [(log, ('2.8: Burnice Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'6b08674c': [(log, ('2.8: Burnice Weapon IB Hash',)),                    (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'c22b4efe': [(log, ('2.8: Burnice Hair draw_vb Hash',)),                 (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n'))],
'511006ba': [(log, ('2.8: Burnice Hair position_vb Hash',)),             (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n'))],
'c882e6eb': [(log, ('2.8: Burnice Hair texcoord_vb Hash',)),             (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n'))],
'68027115': [(log, ('2.8: Burnice Hair blend_vb Hash',)),                (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'164e3024': [(log, ('2.8: Burnice Hair Shadow draw_vb Hash',)),          (add_section_if_missing, ('40aa11a7', 'Burnice.HairShadow.IB', 'match_priority = 0\n'))],
'831534e5': [(log, ('2.8: Burnice Hair Shadow position_vb Hash',)),      (add_section_if_missing, ('40aa11a7', 'Burnice.HairShadow.IB', 'match_priority = 0\n'))],
'4d570d70': [(log, ('2.8: Burnice Hair Shadow texcoord_vb Hash',)),      (add_section_if_missing, ('40aa11a7', 'Burnice.HairShadow.IB', 'match_priority = 0\n'))],
'9d6bbd22': [(log, ('2.8: Burnice Hair Shadow blend_vb Hash',)),         (add_section_if_missing, ('40aa11a7', 'Burnice.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'be10c4bb': [(log, ('2.8: Burnice Body draw_vb Hash',)),                 (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n'))],
'208d5e15': [(log, ('2.8: Burnice Body position_vb Hash',)),             (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n'))],
'35826de5': [(log, ('2.8: Burnice Body texcoord_vb Hash',)),             (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n'))],
'c705bf55': [(log, ('2.8: Burnice Body blend_vb Hash',)),                (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n'))],

# Face
'19ead1b7': [(log, ('2.8: Burnice Face VertexLimit Hash',)),             (add_section_if_missing, ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n'))],
'23f842f0': [(log, ('2.8: Burnice Face position_vb Hash',)),             (add_section_if_missing, ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n'))],
'14b70725': [(log, ('2.8: Burnice Face texcoord_vb Hash',)),             (add_section_if_missing, ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n'))],
'12c38959': [(log, ('2.8: Burnice Face blend_vb Hash',)),                (add_section_if_missing, ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n'))],

# Weapon
'c7e24774': [(log, ('2.8: Burnice Weapon VertexLimit Hash',)),           (add_section_if_missing, ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n'))],
'36821275': [(log, ('2.8: Burnice Weapon position_vb Hash',)),           (add_section_if_missing, ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n'))],
'2981a076': [(log, ('2.8: Burnice Weapon texcoord_vb Hash',)),           (add_section_if_missing, ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n'))],
'a5ca368d': [(log, ('2.8: Burnice Weapon blend_vb Hash',)),              (add_section_if_missing, ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'c9c87bb1': [(log, ('1.3 -> 1.4: Burnice HeadA Diffuse 1024p Hash',)), (update_hash, ('68f0fb19',)),],
'e338bb82': [(log, ('1.3 -> 1.4: Burnice HeadA Diffuse 2048p Hash',)), (update_hash, ('c4b6bb10',)),],
'438cf629': [(log, ('1.2 -> 2.8: Burnice HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'0f2c69e2': [(log, ('1.2 -> 2.8: Burnice BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],

# === Pembaruan Sinkronisasi Senjata v2.8 ===
'78876ed2': [(log, ('2.0 -> 2.8: Burnice Weapon Diffuse Hash [Legacy]',)), (update_hash, ('5f6615b0',))],
'1ae23adc': [(log, ('2.0 -> 2.8: Burnice Weapon LightMap Hash [Legacy]',)), (update_hash, ('5ef426d0',))],
'b5cb92b3': [(log, ('2.0 -> 2.8: Burnice Weapon MaterialMap Hash [Legacy]',)), (update_hash, ('9b7dfc16',))],

# === Face Textures ===
'68f0fb19': [
        (log,                           ('2.8: Burnice HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('c4b6bb10', 'e338bb82'), 'Burnice.HeadA.Diffuse.2048')),
    ],
'c4b6bb10': [
        (log,                           ('2.8: Burnice HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('68f0fb19', 'c9c87bb1'), 'Burnice.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'609b50a9': [
        (log,                           ('2.8: Burnice HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4568c6b3', 'Burnice.HairA.Diffuse.1024')),
    ],
'4568c6b3': [
        (log,                           ('2.8: Burnice HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('609b50a9', 'Burnice.HairA.Diffuse.2048')),
    ],
'bf0042b9': [
        (log,                           ('2.8: Burnice HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('08770e8c', 'Burnice.HairA.LightMap.1024')),
    ],
'08770e8c': [
        (log,                           ('2.8: Burnice HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf0042b9', 'Burnice.HairA.LightMap.2048')),
    ],
'5f2840f1': [
        (log,                           ('2.8: Burnice HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3ae3ea20', 'Burnice.HairA.MaterialMap.1024')),
    ],
'3ae3ea20': [
        (log,                           ('2.8: Burnice HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5f2840f1', 'Burnice.HairA.MaterialMap.2048')),
    ],
'0050e0d2': [
        (log,                           ('2.8: Burnice HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Burnice.HairA.NormalMap.2048')),
    ],

# === Body Textures ===
'50bf6521': [
        (log,                           ('2.8: Burnice BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f0e67001', 'Burnice.BodyA.Diffuse.1024')),
    ],
'f0e67001': [
        (log,                           ('2.8: Burnice BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('50bf6521', 'Burnice.BodyA.Diffuse.2048')),
    ],
'f4e05ee7': [
        (log,                           ('2.8: Burnice BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0a3ba8ac', 'Burnice.BodyA.LightMap.1024')),
    ],
'0a3ba8ac': [
        (log,                           ('2.8: Burnice BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f4e05ee7', 'Burnice.BodyA.LightMap.2048')),
    ],
'c321481d': [
        (log,                           ('2.8: Burnice BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e37e7622', 'Burnice.BodyA.MaterialMap.1024')),
    ],
'e37e7622': [
        (log,                           ('2.8: Burnice BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c321481d', 'Burnice.BodyA.MaterialMap.2048')),
    ],
'0c4f338a': [
        (log,                           ('2.8: Burnice BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Burnice.BodyA.NormalMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'5f6615b0': [
        (log,                           ('2.8: Burnice Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n')),
    ],
'5ef426d0': [
        (log,                           ('2.8: Burnice Weapon LightMap Hash',)),
        (add_section_if_missing,        ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n')),
    ],
'9b7dfc16': [
        (log,                           ('2.8: Burnice Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Burnice Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6b08674c', 'Burnice.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Burnice HairA/BodyA NormalMap 2048p Hash (Shared) [Legacy]',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0050e0d2', 'Burnice.HairA.NormalMap.1024')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Burnice',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}