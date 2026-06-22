"""
Belle Character Hash Commands
ZZZ Mod Fixer v3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Belle's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'bea4a483': [(log, ('2.8 -> 3.0: Belle Hair IB Hash [Legacy]',)),        (update_hash, ('3acf9aea',))],
'1817f3ca': [(log, ('2.8 -> 3.0: Belle Body IB Hash [Legacy]',)),        (update_hash, ('c2b4ce3a',))],
'9a9780a7': [(log, ('2.8: Belle Head IB Hash',)),                         (add_ib_check_if_missing,)],
'403eace9': [(log, ('2.8: Belle HairShadow IB Hash',)),                   (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'3acf9aea': [(log, ('3.0: Belle Hair / Hairpin IB Hash',)),               (add_ib_check_if_missing,)],
'c2b4ce3a': [(log, ('3.0: Belle Body IB Hash',)),                         (add_ib_check_if_missing,)],
'e6afd8d1': [(log, ('3.0: Belle Leg IB Hash',)),                         (add_ib_check_if_missing,)],
'07920753': [(log, ('3.0: Belle EarPendant IB Hash',)),                   (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'142ddbbc': [(log, ('2.8 -> 3.0: Belle Hair draw_vb Hash [Legacy]',)),    (update_hash, ('84a9dfca',))],
'a9673001': [(log, ('2.8 -> 3.0: Belle Hair position_vb Hash [Legacy]',)), (update_hash, ('a678dff4',))],
'11e38ebb': [(log, ('2.8 -> 3.0: Belle Hair texcoord_vb Hash [Legacy]',)), (update_hash, ('77932137',))],
'cc32660c': [(log, ('2.8 -> 3.0: Belle Hair blend_vb Hash [Legacy]',)),   (update_hash, ('6e583c52',))],

# Body
'ac1c8f80': [(log, ('2.8 -> 3.0: Belle Body draw_vb Hash [Legacy]',)),    (update_hash, ('bea2b94e',))],
'd2844c01': [(log, ('2.8 -> 3.0: Belle Body position_vb Hash [Legacy]',)), (update_hash, ('5838ad30',))],
'801edbf4': [(log, ('2.8 -> 3.0: Belle Body texcoord_vb Hash [Legacy]',)), (update_hash, ('40a897ab',))],
'c92a17d8': [(log, ('2.8 -> 3.0: Belle Body blend_vb Hash [Legacy]',)),   (update_hash, ('3ee01622',))],

# Face
'04abceb5': [(log, ('2.8: Belle Face draw_vb',)),                         (add_section_if_missing, ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('2.8: Belle Face position_vb',)),                     (add_section_if_missing, ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n'))],
'1de8fc08': [(log, ('2.8 -> 3.0: Belle Face texcoord_vb Hash [Legacy]',)), (update_hash, ('d3000b22',))],
'36138f65': [(log, ('2.8 -> 3.0: Belle Face blend_vb Hash [Legacy]',)),   (update_hash, ('6ade3fdc',))],

# === 3.0 Database Updates (Strict Sync) ===
# Hair VBs
'84a9dfca': [(log, ('3.0: Belle Hair draw_vb',)),                         (add_section_if_missing, ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n'))],
'a678dff4': [(log, ('3.0: Belle Hair position_vb',)),                     (add_section_if_missing, ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n'))],
'77932137': [(log, ('3.0: Belle Hair texcoord_vb',)),                     (add_section_if_missing, ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n'))],
'6e583c52': [(log, ('3.0: Belle Hair blend_vb',)),                        (add_section_if_missing, ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n'))],

# Body VBs
'bea2b94e': [(log, ('3.0: Belle Body draw_vb',)),                         (add_section_if_missing, ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n'))],
'5838ad30': [(log, ('3.0: Belle Body position_vb',)),                     (add_section_if_missing, ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n'))],
'40a897ab': [(log, ('3.0: Belle Body texcoord_vb',)),                     (add_section_if_missing, ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n'))],
'3ee01622': [(log, ('3.0: Belle Body blend_vb',)),                        (add_section_if_missing, ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n'))],

# Leg VBs
'7217e342': [(log, ('3.0: Belle Leg draw_vb',)),                          (add_section_if_missing, ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n'))],
'ca81bde5': [(log, ('3.0: Belle Leg position_vb',)),                      (add_section_if_missing, ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n'))],
'e317bb99': [(log, ('3.0: Belle Leg texcoord_vb',)),                      (add_section_if_missing, ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n'))],
'b4cd8580': [(log, ('3.0: Belle Leg blend_vb',)),                         (add_section_if_missing, ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n'))],

# Face VBs
'6ade3fdc': [(log, ('3.0: Belle Face blend_vb',)),                        (add_section_if_missing, ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n'))],
'd3000b22': [(log, ('3.0: Belle Face texcoord_vb',)),                     (add_section_if_missing, ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n'))],

# EarPendant VBs
'c4e3b1e8': [(log, ('3.0: Belle EarPendant draw_vb',)),                   (add_section_if_missing, ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n'))],
'66a4bab6': [(log, ('3.0: Belle EarPendant position_vb',)),               (add_section_if_missing, ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n'))],
'a2ee3518': [(log, ('3.0: Belle EarPendant texcoord_vb',)),               (add_section_if_missing, ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n'))],
'28720ee7': [(log, ('3.0: Belle EarPendant blend_vb',)),                  (add_section_if_missing, ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'd7ca821f': [(log, ('1.0 -> 1.1: Belle Body Blend Hash',)), (update_hash, ('c92a17d8',))],
'caf95576': [
        (log,                         ('1.0 -> 1.1: Belle Body Texcoord Hash',)),
        (update_hash,                 ('801edbf4',)),
        (log,                         ('1.0 -> 1.1: Belle Body Blend Remap',)),
        (update_buffer_blend_indices, (
            'd2844c01',
            (3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 126, 127),
            (6, 7, 3, 5, 4, 18, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 25, 24, 20, 22, 23, 38, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 47, 48, 53, 56, 45, 46, 49, 50, 51, 52, 54, 55, 60, 61, 66, 58, 59, 62, 63, 64, 65, 104, 95, 96, 97, 98, 99, 100, 101, 102, 103, 127, 126),
        ))
    ],

# === Face Textures ===
'77eef7e8': [
        (log,                           ('1.0: Belle HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'Belle.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('75ec3614', 'Belle.HeadA.Diffuse.2048')),
    ],
'75ec3614': [
        (log,                           ('1.0: Belle HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'Belle.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('77eef7e8', 'Belle.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'1ce58567': [
        (log,                           ('1.0: Belle HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('08f04d95', 'Belle.HairA.Diffuse.1024')),
    ],
'08f04d95': [
        (log,                           ('1.0: Belle HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1ce58567', 'Belle.HairA.Diffuse.2048')),
    ],
'f1ee2105': [(log, ('1.0 -> 2.5: Belle HairA LightMap 2048p Hash',)), (update_hash, ('7d562f53',))],
'7d562f53': [
        (log,                           ('2.5: Belle HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2e656f2f', 'Belle.HairA.LightMap.1024')),
    ],
'2e656f2f': [
        (log,                           ('1.0: Belle HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7d562f53', 'f1ee2105'), 'Belle.HairA.LightMap.2048')),
    ],
'24c47ca5': [(log, ('1.4 -> 1.5: Belle HairA MaterialMap 2048p Hash',)), (update_hash, ('34bdb036',))],
'34bdb036': [
        (log,                           ('1.5: Belle HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7542ef4b', '4b6ef993'), 'Belle.HairA.MaterialMap.1024')),
    ],
'4b6ef993': [(log, ('1.4 -> 1.5: Belle HairA MaterialMap 1024p Hash',)), (update_hash, ('7542ef4b',))],
'7542ef4b': [
        (log,                           ('1.5: Belle HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('34bdb036', '24c47ca5'), 'Belle.HairA.MaterialMap.2048')),
    ],
'89b147ff': [(log, ('1.0 -> 2.5: Belle HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('2.5: Belle Hair+Body NormalMap 2048p Hash (Shared)',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('6b55c039', 'c0bd8516'), 'Belle.HairBody.NormalMap.1024')),
    ],
'6b55c039': [
        (log,                           ('1.0: Belle HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '89b147ff'), 'Belle.HairA.NormalMap.2048')),
    ],

# === Body Textures ===
'd2960560': [(log, ('1.4 -> 1.5: Belle BodyA Diffuse 2048p Hash',)), (update_hash, ('24639b77',))],
'24639b77': [
        (log,                           ('1.5: Belle BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('b9c7f71b', '4454fb58'), 'Belle.BodyA.Diffuse.1024')),
    ],
'4454fb58': [(log, ('1.4 -> 1.5: Belle BodyA Diffuse 1024p Hash',)), (update_hash, ('b9c7f71b',))],
'b9c7f71b': [
        (log,                           ('1.5: Belle BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('24639b77', 'd2960560'), 'Belle.BodyA.Diffuse.2048')),
    ],
'bf286c84': [(log, ('1.4 -> 1.5: Belle BodyA LightMap 2048p Hash',)), (update_hash, ('7947679c',))],
'7947679c': [
        (log,                           ('1.5: Belle BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('a4d3687d', '2ed82c57'), 'Belle.BodyA.LightMap.1024')),
    ],
'2ed82c57': [(log, ('1.4 -> 1.5: Belle BodyA LightMap 1024p Hash',)), (update_hash, ('a4d3687d',))],
'a4d3687d': [
        (log,                           ('1.5: Belle BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7947679c', 'bf286c84'), 'Belle.BodyA.LightMap.2048')),
    ],
'33f28c6d': [
        (log,                           ('1.0: Belle BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b1abe877', 'Belle.BodyA.MaterialMap.1024')),
    ],
'b1abe877': [
        (log,                           ('1.0: Belle BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('33f28c6d', 'Belle.BodyA.MaterialMap.2048')),
    ],
'f04f7ab9': [(log, ('1.0 -> 2.5: Belle BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'c0bd8516': [
        (log,                           ('1.0: Belle BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', 'f04f7ab9'), 'Belle.BodyA.NormalMap.2048')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8 -> 3.0: Belle Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
    ],
'f44f330b': [
        (log,                           ('2.8: Belle HairA LightMap Hash',)),
        (add_section_if_missing,        ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Belle',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}