"""
Nicole Character Hash Commands
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
    Returns Nicole's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'6847bbbd': [(log, ('2.8: Nicole Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'5a4c1ef3': [(log, ('2.8: Nicole Body IB Hash',)),                      (add_ib_check_if_missing,)],
'7435fc0e': [(log, ('2.8: Nicole Head IB Hash',)),                      (add_ib_check_if_missing,)],
'40e64ae2': [(log, ('2.8: Nicole Amillion IB Hash',)),                  (add_ib_check_if_missing,)],
'4ed9a81f': [(log, ('2.8: Nicole Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'f9befc51': [(log, ('2.8: Nicole Weapon IB Hash',)),                     (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'f6344432': [(log, ('2.8: Nicole Hair draw_vb Hash',)),                  (add_section_if_missing, ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n'))],
'199853eb': [(log, ('2.8: Nicole Hair position_vb Hash',)),              (add_section_if_missing, ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n'))],
'06e4fd79': [(log, ('2.8: Nicole Hair texcoord_vb Hash',)),              (add_section_if_missing, ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n'))],
'347e4a48': [(log, ('2.8: Nicole Hair blend_vb Hash',)),                 (add_section_if_missing, ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'4d61e6f3': [(log, ('2.8: Nicole Hair Shadow draw_vb Hash',)),           (add_section_if_missing, ('4ed9a81f', 'Nicole.HairShadow.IB', 'match_priority = 0\n'))],
'b408b261': [(log, ('2.8: Nicole Hair Shadow position_vb Hash',)),       (add_section_if_missing, ('4ed9a81f', 'Nicole.HairShadow.IB', 'match_priority = 0\n'))],
'322345a6': [(log, ('2.8: Nicole Hair Shadow texcoord_vb Hash',)),       (add_section_if_missing, ('4ed9a81f', 'Nicole.HairShadow.IB', 'match_priority = 0\n'))],
'ab4b28ad': [(log, ('2.8: Nicole Hair Shadow blend_vb Hash',)),          (add_section_if_missing, ('4ed9a81f', 'Nicole.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'8cc1262b': [(log, ('2.8: Nicole Body draw_vb Hash',)),                  (add_section_if_missing, ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n'))],
'89df5a07': [(log, ('2.8: Nicole Body position_vb Hash',)),              (add_section_if_missing, ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n'))],
'91c1b779': [(log, ('2.8: Nicole Body texcoord_vb Hash',)),              (add_section_if_missing, ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n'))],
'7ecda89f': [(log, ('2.8: Nicole Body blend_vb Hash',)),                 (add_section_if_missing, ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n'))],

# Amillion
'bb7fffe9': [(log, ('2.8: Nicole Amillion draw_vb Hash',)),              (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n'))],
'176bf3d7': [(log, ('2.8: Nicole Amillion position_vb Hash',)),          (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n'))],
'077c3500': [(log, ('2.8: Nicole Amillion texcoord_vb Hash',)),          (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n'))],
'4e1d9c9a': [(log, ('2.8: Nicole Amillion blend_vb Hash',)),             (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n'))],

# Face / Head
'9274e401': [(log, ('2.8: Nicole Face VertexLimit Hash',)),              (add_section_if_missing, ('7435fc0e', 'Nicole.Head.IB', 'match_priority = 0\n'))],
'5714e5e6': [(log, ('2.8: Nicole Face Texcoord Hash',)),                  (add_section_if_missing, ('7435fc0e', 'Nicole.Head.IB', 'match_priority = 0\n'))],
'b25ebcf6': [(log, ('2.8: Nicole Face Blend Hash',)),                     (add_section_if_missing, ('7435fc0e', 'Nicole.Head.IB', 'match_priority = 0\n'))],

# Weapon
'f6325378': [(log, ('2.8: Nicole Weapon VertexLimit Hash',)),            (add_section_if_missing, ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n'))],
'00c8b3c5': [(log, ('2.8: Nicole Weapon position_vb Hash',)),            (add_section_if_missing, ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n'))],
'14b0d6b6': [(log, ('2.8: Nicole Weapon texcoord_vb Hash',)),            (add_section_if_missing, ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n'))],
'2f427bdb': [(log, ('2.8: Nicole Weapon blend_vb Hash',)),               (add_section_if_missing, ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'1dfd9e16': [(log, ('1.0-1.7: Nicole HairA LightMap 2048p Hash',)),    (update_hash, ('8c9c25d5',)),],
'bffb4a66': [(log, ('1.0-1.7: Nicole HairA NormalMap 2048p Hash',)),    (update_hash, ('ebac056e',)),],
'8cf23419': [(log, ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'6abd3dd3': [(log, ('1.0-1.7: Nicole HeadA Diffuse 1024p Hash (Removed in 2.5) [Legacy]',)),],
'7a45adcd': [(log, ('1.0-1.7: Nicole HairA Diffuse 1024p Hash (Removed in 2.5) [Legacy]',)),],
'9adc04ed': [(log, ('1.0-1.7: Nicole HairA LightMap 1024p Hash (Removed in 2.5) [Legacy]',)),],
'b8db0209': [(log, ('1.0-1.7: Nicole HairA NormalMap 1024p Hash (Removed in 2.5) [Legacy]',)),],
'9ee9b402': [(log, ('1.0-1.7: Nicole BodyA, AmillionA Diffuse 1024p Hash (Removed in 2.5) [Legacy]',)),],
'2b5aa784': [(log, ('1.0-1.7: Nicole BodyA, AmillionA LightMap 1024p Hash (Removed in 2.5) [Legacy]',)),],
'bb33129d': [(log, ('1.0-1.7: Nicole BodyA, AmillionA MaterialMap 1024p Hash (Removed in 2.5) [Legacy]',)),],
'580df52d': [(log, ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 1024p Hash (Removed in 2.5) [Legacy]',)),],
'76e8ac35': [(log, ('2.8: Nicole Weapon Diffuse Part 2 [Legacy]',)),     (update_hash, ('f1af36a8',))],
'a365836f': [(log, ('2.8: Nicole Weapon LightMap [Legacy]',)),           (update_hash, ('6d5ee825',))],
'ad4bf30d': [(log, ('2.8: Nicole Weapon MaterialMap [Legacy]',)),        (update_hash, ('0fe671cc',))],
'fda56c66': [(log, ('2.8: Nicole Weapon Diffuse [Legacy]',)),            (update_hash, ('35951ccf',))],

# === Face Textures ===
'd1e84a34': [
        (log,                           ('2.8: Nicole HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7435fc0e', 'Nicole.Head.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'6d3868f9': [
        (log,                           ('2.8: Nicole HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'8c9c25d5': [
        (log,                           ('2.8: Nicole HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'f3c21e41': [
        (log,                           ('2.8: Nicole Hair LightMap Target Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'a05c2386': [
        (log,                           ('2.8: Nicole HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body & Amillion Shared Textures ===
'f86ffe2c': [
        (log,                           ('2.8: Nicole BodyA, AmillionA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'80855e0f': [
        (log,                           ('2.8: Nicole BodyA, AmillionA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'95cabef3': [
        (log,                           ('2.8: Nicole BodyA, AmillionA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures ===
'35951ccf': [
        (log,                           ('2.8: Nicole Weapon Diffuse Hash Part 1',)),
        (add_section_if_missing,        ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n')),
    ],
'f1af36a8': [
        (log,                           ('2.8: Nicole Weapon Diffuse Hash Part 2',)),
        (add_section_if_missing,        ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n')),
    ],
'6d5ee825': [
        (log,                           ('2.8: Nicole Weapon LightMap Hash',)),
        (add_section_if_missing,        ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n')),
    ],
'0fe671cc': [
        (log,                           ('2.8: Nicole Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Nicole Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f9befc51', 'Nicole.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4ed9a81f', 'Nicole.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Nicole HairA, BodyA NormalMap 2048p Hash [Legacy]',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Nicole',
    'game_versions': ['2.8'],
}