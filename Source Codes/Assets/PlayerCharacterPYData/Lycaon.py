"""
Lycaon Character Hash Commands
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
    Returns Lycaon's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'060bc1ad': [(log, ('2.8: Lycaon Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'6749b6e7': [(log, ('2.8: Lycaon Body IB Hash',)),                      (add_ib_check_if_missing,)],
'5e710f36': [(log, ('2.8: Lycaon Mask IB Hash',)),                      (add_ib_check_if_missing,)],
'22a1347b': [(log, ('2.8: Lycaon Legs IB Hash',)),                      (add_ib_check_if_missing,)],
'6ffdfccb': [(log, ('2.8: Lycaon Head IB Hash',)),                      (add_ib_check_if_missing,)],
'd4e17891': [(log, ('2.8: Lycaon Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'c28ea8d7': [(log, ('2.8: Lycaon Pocket Watch IB Hash',)),              (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'cc59d8d6': [(log, ('2.8: Lycaon Hair Draw Hash',)),                    (add_section_if_missing, ('060bc1ad', 'Lycaon.Hair.IB', 'match_priority = 0\n'))],
'31eda4d5': [(log, ('2.8: Lycaon Hair Position Hash',)),                (add_section_if_missing, ('060bc1ad', 'Lycaon.Hair.IB', 'match_priority = 0\n'))],
'b092c043': [(log, ('2.8: Lycaon Hair Texcoord Hash',)),                (add_section_if_missing, ('060bc1ad', 'Lycaon.Hair.IB', 'match_priority = 0\n'))],
'3ab9a7a4': [(log, ('2.8: Lycaon Hair Blend Hash',)),                   (add_section_if_missing, ('060bc1ad', 'Lycaon.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'57b9efa5': [(log, ('2.8: Lycaon Hair Shadow Draw Hash',)),              (add_section_if_missing, ('d4e17891', 'Lycaon.HairShadow.IB', 'match_priority = 0\n'))],
'a80a83ac': [(log, ('2.8: Lycaon Hair Shadow Position Hash',)),          (add_section_if_missing, ('d4e17891', 'Lycaon.HairShadow.IB', 'match_priority = 0\n'))],
'9efb6f38': [(log, ('2.8: Lycaon Hair Shadow Texcoord Hash',)),          (add_section_if_missing, ('d4e17891', 'Lycaon.HairShadow.IB', 'match_priority = 0\n'))],
'2e258296': [(log, ('2.8: Lycaon Hair Shadow Blend Hash',)),             (add_section_if_missing, ('d4e17891', 'Lycaon.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'25418598': [(log, ('2.8: Lycaon Body Draw Hash',)),                    (add_section_if_missing, ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n'))],
'8c7775ae': [(log, ('2.8: Lycaon Body Position Hash',)),                (add_section_if_missing, ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n'))],
'b950fda5': [(log, ('2.8: Lycaon Body Texcoord Hash',)),                (add_section_if_missing, ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n'))],
'f2d1a929': [(log, ('2.8: Lycaon Body Blend Hash',)),                   (add_section_if_missing, ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n'))],

# Pocket Watch
'a68f96bb': [(log, ('2.8: Lycaon Pocket Watch Draw Hash',)),            (add_section_if_missing, ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n'))],
'5fbc1146': [(log, ('2.8: Lycaon Pocket Watch Position Hash',)),        (add_section_if_missing, ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n'))],
'c6926d98': [(log, ('2.8: Lycaon Pocket Watch Texcoord Hash',)),        (add_section_if_missing, ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n'))],
'3107902a': [(log, ('2.8: Lycaon Pocket Watch Blend Hash',)),           (add_section_if_missing, ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n'))],

# Legs
'916a8726': [(log, ('2.8: Lycaon Legs Draw Hash',)),                    (add_section_if_missing, ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n'))],
'30ba2096': [(log, ('2.8: Lycaon Legs Position Hash',)),                (add_section_if_missing, ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n'))],
'ab4b6359': [(log, ('2.8: Lycaon Legs Texcoord Hash',)),                (add_section_if_missing, ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n'))],
'7d08bead': [(log, ('2.8: Lycaon Legs Blend Hash',)),                   (add_section_if_missing, ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n'))],

# Mask
'a11680ef': [(log, ('2.8: Lycaon Mask Draw Hash',)),                    (add_section_if_missing, ('5e710f36', 'Lycaon.Mask.IB', 'match_priority = 0\n'))],
'ffbc21b0': [(log, ('2.8: Lycaon Mask Position Hash',)),                (add_section_if_missing, ('5e710f36', 'Lycaon.Mask.IB', 'match_priority = 0\n'))],
'911a4bae': [(log, ('2.8: Lycaon Mask Texcoord Hash',)),                (add_section_if_missing, ('5e710f36', 'Lycaon.Mask.IB', 'match_priority = 0\n'))],
'8a7db58c': [(log, ('2.8: Lycaon Mask Blend Hash',)),                   (add_section_if_missing, ('5e710f36', 'Lycaon.Mask.IB', 'match_priority = 0\n'))],

# Head
'44277f65': [(log, ('2.8: Lycaon Head Draw Hash',)),                    (add_section_if_missing, ('6ffdfccb', 'Lycaon.Head.IB', 'match_priority = 0\n'))],
'7e35ec22': [(log, ('2.8: Lycaon Head Position Hash',)),                (add_section_if_missing, ('6ffdfccb', 'Lycaon.Head.IB', 'match_priority = 0\n'))],
'3adaebb3': [(log, ('2.8: Lycaon Head Texcoord Hash',)),                (add_section_if_missing, ('6ffdfccb', 'Lycaon.Head.IB', 'match_priority = 0\n'))],
'e2d4c532': [(log, ('2.8: Lycaon Head Blend Hash',)),                   (add_section_if_missing, ('6ffdfccb', 'Lycaon.Head.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'395572dc': [(log, ('1.3 -> 1.4: Lycaon Hair Texcoord Hash',)), (update_hash, ('b092c043',))],
'25196b7a': [(log, ('1.3 -> 1.4: Lycaon Body IB Hash',)), (update_hash, ('6749b6e7',))],
'2a340ed5': [(log, ('1.3 -> 1.4: Lycaon Body Draw Hash',)),     (update_hash, ('25418598',))],
'949e688a': [(log, ('1.3 -> 1.4: Lycaon Body Texcoord Hash',)), (update_hash, ('b950fda5',))],
'b68056b4': [
        (log, ('1.3 -> 1.4: Lycaon Body Position Hash',)),
        (update_hash, ('8c7775ae',)),
        (log, ('1.3 -> 1.4: Lycaon Body Blend Remap',)),
        (update_buffer_blend_indices, (
            '8c7775ae',
            (50, 51, 89, 90,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110),
            (51, 50, 90, 89, 669, 669, 669, 669, 669, 669, 669, 669, 669,  98,  99, 100, 101)
        ))
    ],
'a485180e': [
        (log,                         ('1.3 -> 1.4: Lycaon Body Blend Remap',)),
        (update_hash,                 ('f2d1a929',)),
        (update_buffer_blend_indices, (
            'f2d1a929',
            (50, 51, 89, 90,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110),
            (51, 50, 90, 89, 669, 669, 669, 669, 669, 669, 669, 669, 669,  98,  99, 100, 101)
        )),
    ],
'7074f97e': [(log, ('1.5 -> 1.6: Lycaon Head Draw Hash',)),     (update_hash, ('44277f65',))],
'4a666a39': [(log, ('1.5 -> 1.6: Lycaon Head Position Hash',)), (update_hash, ('7e35ec22',))],
'c862a611': [(log, ('1.5 -> 1.6: Lycaon Head Blend Hash',)),    (update_hash, ('e2d4c532',))],
'690f441f': [(log, ('1.? -> 1.?: Lycaon Head Texcoord Hash',)), (update_hash, ('b1edaf35',))],
'b1edaf35': [(log, ('1.? -> 1.6: Lycaon Head Texcoord Hash',)), (update_hash, ('3adaebb3',))],
'7341e07b': [(log, ('1.5 -> 1.6: Lycaon Head IB Hash',)),       (update_hash, ('6ffdfccb',))],
'4f098897': [(log, ('1.5 -> 1.6: Lycaon Head Diffuse 1024p Hash',)), (update_hash, ('2cc208a7',))],

# === Pembaruan Sinkronisasi Diffuse Bodi v2.8 ===
'7169ec86': [(log, ('2.4 -> 2.5: Lycaon BodyA Diffuse [Legacy]',)), (update_hash, ('4cb6928e',))],

# === Face Textures ===
'2cc208a7': [
        (log,                           ('2.8: Lycaon HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('6ffdfccb', '7341e07b'), 'Lycaon.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7077ebb1', 'd14f3284'), 'Lycaon.HeadA.Diffuse.2048')),
    ],
'd14f3284': [(log, ('1.5 -> 1.6: Lycaon HeadA Diffuse 2048p Hash',)), (update_hash, ('7077ebb1',))],
'7077ebb1': [
        (log,                           ('2.8: Lycaon HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('6ffdfccb', '7341e07b'), 'Lycaon.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('2cc208a7', '4f098897'), 'Lycaon.HeadA.Diffuse.1024')),
    ],

# === Hair & Mask Textures ===
'61aaace5': [
        (log,                           ('2.8: Lycaon HairA, MaskA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('3bd1b7e6', 'Lycaon.HairA.Diffuse.1024')),
    ],
'3bd1b7e6': [
        (log,                           ('2.8: Lycaon HairA, MaskA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('61aaace5', 'Lycaon.HairA.Diffuse.2048')),
    ],
'3d6eb388': [(log, ('1.3 -> 1.4: Lycaon HairA, MaskA LightMap 2048p Hash',)), (update_hash, ('04d061fe',))],
'04d061fe': [
        (log,                           ('1.4 -> 2.5: Lycaon HairA, MaskA LightMap 2048p Hash',)),
        (update_hash,                   ('f7daa6d9',)),
        (multiply_section_if_missing,   (('4d878953', '4d4e8986'), 'Lycaon.HairA.LightMap.1024')),
    ],
'f7daa6d9': [
        (log,                           ('2.8: Lycaon HairA, MaskA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('ea10b0bb', 'Lycaon.HairA.LightMap.1024')),
    ],
'4d4e8986': [(log, ('1.3 -> 1.4: Lycaon HairA, MaskA LightMap 1024p Hash',)), (update_hash, ('4d878953',))],
'4d878953': [
        (log,                           ('1.4 -> 2.5: Lycaon HairA, MaskA LightMap 1024p Hash',)),
        (update_hash,                   ('ea10b0bb',)),
        (multiply_section_if_missing,   (('04d061fe', '3d6eb388'), 'Lycaon.HairA.LightMap.2048')),
    ],
'ea10b0bb': [
        (log,                           ('2.8: Lycaon HairA, MaskA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   (('f7daa6d9', '04d061fe', '3d6eb388'), 'Lycaon.HairA.LightMap.2048')),
    ],
'7c129f48': [
        (log,                           ('2.8: Lycaon Hair LightMap Hash',)),
        (add_section_if_missing,        ('060bc1ad', 'Lycaon.Hair.IB', 'match_priority = 0\n')),
    ],
'02bfcc69': [
        (log,                           ('2.8: Lycaon HairA, MaskA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('ba0f8320', 'Lycaon.HairA.MaterialMap.1024')),
    ],
'ba0f8320': [
        (log,                           ('2.8: Lycaon HairA, MaskA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('02bfcc69', 'Lycaon.HairA.MaterialMap.2048')),
    ],
'5817e801': [
        (log,                           ('2.8: Lycaon HairA, MaskA NormalMap 2048p Hash',)),
        (multiply_section_if_missing,   ('71925b2f', 'Lycaon.HairA.NormalMap.1024')),
    ],
'71925b2f': [
        (log,                           ('2.8: Lycaon HairA, MaskA NormalMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5817e801', 'Lycaon.HairA.NormalMap.2048')),
    ],

# === Body & Pocket Watch Textures (v2.8 Target) ===
'4cb6928e': [
        (log,                           ('2.8: Lycaon Body/Pocket Watch Diffuse Target Hash',)),
        (add_section_if_missing,        ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n')),
    ],
'7a22ad61': [
        (log,                           ('2.8: Lycaon Body/Pocket Watch Diffuse Target Hash [Legacy]',)),
        (add_section_if_missing,        ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n')),
    ],
'565aa8be': [(log, ('1.3 -> 1.4: Lycaon Body LightMap 2048p Hash',)), (update_hash, ('814db5bf',))],
'814db5bf': [
        (log,                           ('1.4 -> 2.5: Lycaon BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('fbf5a9b5',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('122c655e', '7ea75154'), 'Lycaon.BodyA.LightMap.1024')),
    ],
'fbf5a9b5': [
        (log,                           ('2.8: Lycaon BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c5635a53', 'Lycaon.BodyA.LightMap.1024')),
    ],
'7ea75154': [(log, ('1.3 -> 1.4: Lycaon Body LightMap 1024p Hash',)), (update_hash, ('122c655e',))],
'122c655e': [
        (log,                           ('1.4 -> 2.5: Lycaon BodyA LightMap 1024p Hash',)),
        (update_hash,                   ('c5635a53',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('814db5bf', '565aa8be'), 'Lycaon.BodyA.LightMap.2048')),
    ],
'c5635a53': [
        (log,                           ('2.8: Lycaon BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('fbf5a9b5', '814db5bf', '565aa8be'), 'Lycaon.BodyA.LightMap.2048')),
    ],
'391855b7': [
        (log,                           ('2.8: Lycaon Body & Pocket Watch LightMap Hash',)),
        (add_section_if_missing,        ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c28ea8d7', 'Lycaon.PocketWatch.IB', 'match_priority = 0\n')),
    ],
'5a321eae': [
        (log,                           ('2.8: Lycaon BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7cca7d7e', 'Lycaon.BodyA.MaterialMap.1024')),
    ],
'7cca7d7e': [
        (log,                           ('2.8: Lycaon BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5a321eae', 'Lycaon.BodyA.MaterialMap.2048')),
    ],
'c8fd1702': [
        (log,                           ('2.8: Lycaon BodyA NormalMap 2048p Hash',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bac2b2e2', 'Lycaon.BodyA.NormalMap.1024')),
    ],
'bac2b2e2': [
        (log,                           ('2.8: Lycaon BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('6749b6e7', '25196b7a'), 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c8fd1702', 'Lycaon.BodyA.NormalMap.2048')),
    ],

# === Legs Textures ===
'd947066b': [
        (log,                           ('2.8: Lycaon LegsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('89bd4d58', 'Lycaon.LegsA.Diffuse.1024')),
    ],
'89bd4d58': [
        (log,                           ('2.8: Lycaon LegsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d947066b', 'Lycaon.LegsA.Diffuse.2048')),
    ],
'072e6786': [
        (log,                           ('2.8: Lycaon LegsA LightMap 2048p Hash (Old)',)),
        (update_hash,                   ('57b175c5',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3dfdab95', 'Lycaon.LegsA.LightMap.1024')),
    ],
'57b175c5': [
        (log,                           ('2.8: Lycaon LegsA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9b0df25b', 'Lycaon.LegsA.LightMap.1024')),
    ],
'3dfdab95': [
        (log,                           ('2.8: Lycaon LegsA LightMap 1024p Hash (Old)',)),
        (update_hash,                   ('9b0df25b',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('072e6786', 'Lycaon.LegsA.LightMap.2048')),
    ],
'9bcd5f77': [
        (log,                           ('2.8: Lycaon Legs LightMap Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
    ],
'9b0df25b': [
        (log,                           ('2.8: Lycaon LegsA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('57b175c5', '072e6786'), 'Lycaon.LegsA.LightMap.2048')),
    ],
'4a4ea6dc': [
        (log,                           ('2.8: Lycaon LegsA MaterialMap 2048p Hash (Old)',)),
        (update_hash,                   ('4b18f890',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('288e7fbd', 'Lycaon.LegsA.MaterialMap.1024')),
    ],
'4b18f890': [
        (log,                           ('2.8: Lycaon LegsA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1de27b3a', 'Lycaon.LegsA.MaterialMap.1024')),
    ],
'288e7fbd': [
        (log,                           ('2.8: Lycaon LegsA MaterialMap 1024p Hash (Old)',)),
        (update_hash,                   ('1de27b3a',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a4ea6dc', 'Lycaon.LegsA.MaterialMap.2048')),
    ],
'1de27b3a': [
        (log,                           ('2.8: Lycaon LegsA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4b18f890', '4a4ea6dc'), 'Lycaon.LegsA.MaterialMap.2048')),
    ],
'b4e95c1d': [
        (log,                           ('2.8: Lycaon Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
    ],
'72f53876': [
        (log,                           ('2.8: Lycaon LegsA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a6efc854', 'Lycaon.LegsA.NormalMap.1024')),
    ],
'a6efc854': [
        (log,                           ('2.8: Lycaon LegsA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('72f53876', 'Lycaon.LegsA.NormalMap.2048')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Lycaon Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('060bc1ad', 'Lycaon.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6749b6e7', 'Lycaon.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5e710f36', 'Lycaon.Mask.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('22a1347b', 'Lycaon.Legs.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Lycaon Shared NormalMap 2048p Hash [Legacy]',)),
        (multiply_section_if_missing,   ('5db3d704', 'Lycaon.Shared.NormalMap.1024')),
    ],
'5db3d704': [
        (log,                           ('2.8: Lycaon Shared NormalMap 1024p Hash [Legacy]',)),
        (multiply_section_if_missing,   ('ebac056e', 'Lycaon.Shared.NormalMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lycaon',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}