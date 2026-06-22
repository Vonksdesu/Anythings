"""
Piper Character Hash Commands
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
    Returns Piper's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'940454ef': [(log, ('2.8: Piper Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'585da98b': [(log, ('2.8: Piper Body IB Hash',)),                        (add_ib_check_if_missing,)],
'90bc5b0f': [(log, ('2.8: Piper Glasses IB Hash',)),                     (add_ib_check_if_missing,)],
'e11baad9': [(log, ('2.8: Piper Head IB Hash',)),                        (add_ib_check_if_missing,)],
'83736476': [(log, ('2.8: Piper Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'b79e0a74': [(log, ('2.8: Piper Weapon Ax IB Hash',)),                   (add_ib_check_if_missing,)],
'e85eae59': [(log, ('2.8: Piper Weapon Wheel IB Hash',)),                 (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'da8a2564': [(log, ('2.8: Piper Hair draw_vb Hash',)),                   (add_section_if_missing, ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n'))],
'c4619559': [(log, ('2.8: Piper Hair Position Hash',)),                  (add_section_if_missing, ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n'))],
'1c6d41af': [(log, ('2.8: Piper Hair Texcoord Hash',)),                  (add_section_if_missing, ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n'))],
'64697011': [(log, ('2.8: Piper Hair Blend Hash',)),                     (add_section_if_missing, ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'8babfd25': [(log, ('2.8: Piper Hair Shadow draw_vb',)),                 (add_section_if_missing, ('83736476', 'Piper.HairShadow.IB', 'match_priority = 0\n'))],
'd45a3d8d': [(log, ('2.8: Piper Hair Shadow position_vb',)),             (add_section_if_missing, ('83736476', 'Piper.HairShadow.IB', 'match_priority = 0\n'))],
'71574c65': [(log, ('2.8: Piper Hair Shadow texcoord_vb',)),             (add_section_if_missing, ('83736476', 'Piper.HairShadow.IB', 'match_priority = 0\n'))],
'f2390d9b': [(log, ('2.8: Piper Hair Shadow blend_vb [Legacy]',)),       (update_hash, ('f2390d9b',))],
'7f2390d9': [(log, ('2.8: Piper Hair Shadow blend_vb',)),                (add_section_if_missing, ('83736476', 'Piper.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'd28231af': [(log, ('2.8: Piper Body draw_vb Hash',)),                   (add_section_if_missing, ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n'))],
'ffe8fea7': [(log, ('2.8: Piper Body Position Hash',)),                  (add_section_if_missing, ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n'))],
'6357b120': [(log, ('2.8: Piper Body Texcoord Hash',)),                  (add_section_if_missing, ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n'))],
'3d329807': [(log, ('2.8: Piper Body Blend Hash',)),                     (add_section_if_missing, ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n'))],

# Glasses
'8db48e03': [(log, ('2.8: Piper Glasses draw_vb Hash',)),                (add_section_if_missing, ('90bc5b0f', 'Piper.Glasses.IB', 'match_priority = 0\n'))],
'17682368': [(log, ('2.8: Piper Glasses Position Hash',)),               (add_section_if_missing, ('90bc5b0f', 'Piper.Glasses.IB', 'match_priority = 0\n'))],
'e527157e': [(log, ('2.8: Piper Glasses Texcoord Hash',)),               (add_section_if_missing, ('90bc5b0f', 'Piper.Glasses.IB', 'match_priority = 0\n'))],
'16060a52': [(log, ('2.8: Piper Glasses Blend Hash',)),                  (add_section_if_missing, ('90bc5b0f', 'Piper.Glasses.IB', 'match_priority = 0\n'))],

# Face
'67362536': [(log, ('2.8: Piper Face VertexLimit Hash',)),               (add_section_if_missing, ('e11baad9', 'Piper.Head.IB', 'match_priority = 0\n'))],
'5d24b671': [(log, ('2.8: Piper Face position_vb Hash',)),               (add_section_if_missing, ('e11baad9', 'Piper.Head.IB', 'match_priority = 0\n'))],
'58468aba': [(log, ('2.8: Piper Face texcoord_vb Hash',)),               (add_section_if_missing, ('e11baad9', 'Piper.Head.IB', 'match_priority = 0\n'))],
'6059174c': [(log, ('2.8: Piper Face blend_vb Hash',)),                  (add_section_if_missing, ('e11baad9', 'Piper.Head.IB', 'match_priority = 0\n'))],

# Weapon - Ax (weapon武器-斧头)
'9c1cfb7d': [(log, ('2.8: Piper Weapon Ax draw_vb Hash',)),              (add_section_if_missing, ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n'))],
'6753bce4': [(log, ('2.8: Piper Weapon Ax position_vb Hash',)),          (add_section_if_missing, ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n'))],
'1f0dbd2b': [(log, ('2.8: Piper Weapon Ax texcoord_vb Hash',)),          (add_section_if_missing, ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n'))],
'731ab501': [(log, ('2.8: Piper Weapon Ax blend_vb Hash',)),             (add_section_if_missing, ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n'))],

# Weapon - Wheel (weapon武器-转轮)
'30ea10c9': [(log, ('2.8: Piper Weapon Wheel draw_vb Hash',)),            (add_section_if_missing, ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n'))],
'd221c027': [(log, ('2.8: Piper Weapon Wheel position_vb Hash',)),        (add_section_if_missing, ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n'))],
'b7790fd4': [(log, ('2.8: Piper Weapon Wheel texcoord_vb Hash',)),        (add_section_if_missing, ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n'))],
'ceec1b8e': [(log, ('2.8: Piper Weapon Wheel blend_vb Hash',)),           (add_section_if_missing, ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'fd1b9c29': [
        (log, ('1.1 -> 1.2: Piper Hair Texcoord Hash',)),
        (update_hash, ('8b6b17f8',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'8b6b17f8': [(log, ('1.3 -> 1.4: Piper Hair Texcoord Hash [Legacy]',)), (update_hash, ('1c6d41af',)),],
'b2f3e6aa': [(log, ('1.1 -> 1.2: Piper Body Position Hash [Legacy]',)), (update_hash, ('ffe8fea7',)),],
'764276de': [(log, ('1.2 -> 1.3: Piper Body Blend Hash [Legacy]',)),    (update_hash, ('3d329807',)),],
'a0d146b3': [(log, ('1.1 -> 1.2: Piper Body Texcoord Hash [Legacy]',)), (update_hash, ('a011f94e',)),],
'a011f94e': [(log, ('1.2 -> 1.3: Piper Body Texcoord Hash [Legacy]',)), (update_hash, ('6357b120',)),],
'621564e5': [(log, ('1.2 -> 1.3: Piper BodyA Diffuse 1024p Hash',)),    (update_hash, ('b450949d',))],
'b4b74e7e': [(log, ('1.2 -> 1.3: Piper BodyA Diffuse 2048p Hash',)),    (update_hash, ('fed40302',))],
'79953d32': [(log, ('1.0 -> 2.8: Piper HairA LightMap 2048p Hash [Legacy]',)), (update_hash, ('1146c5c3',))],
'92acb4d4': [(log, ('1.0 -> 2.8: Piper HairA LightMap 1024p Hash [Legacy]',)), (update_hash, ('46cbca7a',))],
'7ca957d8': [(log, ('1.0 -> 2.8: Piper HairA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],
'db7dccbf': [(log, ('1.0 -> 2.8: Piper HairA NormalMap 1024p Hash [Legacy]',)), (update_hash, ('8db36370',))],
'9cc2aaa0': [(log, ('1.0 -> 2.8: Piper BodyA LightMap 2048p Hash [Legacy]',)), (update_hash, ('a32c39b9',))],
'db9c7abf': [(log, ('1.0 -> 2.8: Piper BodyA LightMap 1024p Hash [Legacy]',)), (update_hash, ('a0dcd60a',))],
'51f1ec36': [(log, ('1.0 -> 2.8: Piper BodyA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],
'73a61e88': [(log, ('1.0 -> 2.8: Piper BodyA NormalMap 1024p Hash [Legacy]',)), (update_hash, ('8db36370',))],
'4b06ffe6': [(log, ('1.1 -> 1.2: Piper Face Diffuse 1024p Hash [Legacy]',)), (update_hash, ('f1c8f946',))],
'97a7862e': [(log, ('1.1 -> 1.2: Piper Face Diffuse 2048p Hash [Legacy]',)), (update_hash, ('3b2eb1d9',))],
'f1c8f946': [
        (log,                           ('1.2 -> 2.8: Piper HeadA Diffuse 1024p Hash [Legacy]',)),
        (update_hash,                   ('48c96e2e',)),
    ],

# === Pembaruan Sinkronisasi Senjata v2.8 ===
'7c5e2403': [(log, ('2.0 -> 2.8: Piper Weapon Diffuse [Legacy]',)), (update_hash, ('9880cefa',))],
'aa118562': [(log, ('2.0 -> 2.8: Piper Weapon LightMap [Legacy]',)), (update_hash, ('4345e1e7',))],
'2e830888': [(log, ('2.0 -> 2.8: Piper Weapon MaterialMap [Legacy]',)), (update_hash, ('d06e2ef0',))],

# === Face Textures ===
'48c96e2e': [
        (log,                           ('2.8: Piper HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('e11baad9', 'Piper.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3b2eb1d9', '97a7862e'), 'Piper.HeadA.Diffuse.2048')),
    ],
'3b2eb1d9': [
        (log,                           ('2.8: Piper HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('e11baad9', 'Piper.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('48c96e2e', 'f1c8f946', '4b06ffe6'), 'Piper.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'69ed4d11': [
        (log,                           ('2.8: Piper HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9b743eab', 'Piper.HairA.Diffuse.1024')),
    ],
'9b743eab': [
        (log,                           ('2.8: Piper HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('69ed4d11', 'Piper.HairA.Diffuse.2048')),
    ],
'6bd15459': [
        (log,                           ('2.8: Piper Hair LightMap Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
    ],
'1146c5c3': [
        (log,                           ('2.8: Piper HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('46cbca7a', 'Piper.HairA.LightMap.1024')),
    ],
'46cbca7a': [
        (log,                           ('2.8: Piper HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1146c5c3', 'Piper.HairA.LightMap.2048')),
    ],
'b3034dff': [
        (log,                           ('2.8: Piper HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('78c42c66', 'Piper.HairA.MaterialMap.1024')),
    ],
'78c42c66': [
        (log,                           ('2.8: Piper HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b3034dff', 'Piper.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'fed40302': [
        (log,                           ('2.8: Piper BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('b450949d', '621564e5'), 'Piper.BodyA.Diffuse.1024')),
    ],
'b450949d': [
        (log,                           ('2.8: Piper BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('fed40302', 'b4b74e7e'), 'Piper.BodyA.Diffuse.2048')),
    ],
'a32c39b9': [
        (log,                           ('2.8: Piper BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a0dcd60a', 'Piper.BodyA.LightMap.1024')),
    ],
'a0dcd60a': [
        (log,                           ('2.8: Piper BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a32c39b9', 'Piper.BodyA.LightMap.2048')),
    ],
'7a281673': [
        (log,                           ('2.8: Piper Body LightMap Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
    ],
'7fdee30d': [
        (log,                           ('2.8: Piper BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('73e72a1e', 'Piper.BodyA.MaterialMap.1024')),
    ],
'73e72a1e': [
        (log,                           ('2.8: Piper BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7fdee30d', 'Piper.BodyA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'9880cefa': [
        (log,                           ('2.8: Piper Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n')),
    ],
'4345e1e7': [
        (log,                           ('2.8: Piper Weapon LightMap Hash',)),
        (add_section_if_missing,        ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n')),
    ],
'd06e2ef0': [
        (log,                           ('2.8: Piper Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: Piper Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('90bc5b0f', 'Piper.Glasses.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b79e0a74', 'Piper.WeaponAx.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e85eae59', 'Piper.WeaponWheel.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Piper Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8db36370', 'Piper.Shared.NormalMap.1024')),
    ],
'8db36370': [
        (log,                           ('2.8: Piper Shared NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Piper.Shared.NormalMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Piper',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}