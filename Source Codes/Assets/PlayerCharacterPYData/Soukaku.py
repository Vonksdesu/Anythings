"""
Soukaku Character Hash Commands
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
    Returns Soukaku's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'fe70c7a3': [(log, ('2.8: Soukaku Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'ced49ff8': [(log, ('2.8: Soukaku Body IB Hash',)),                      (add_ib_check_if_missing,)],
'1315178e': [(log, ('2.8: Soukaku Mask IB Hash',)),                      (add_ib_check_if_missing,)],
'020f9ac6': [(log, ('2.8: Soukaku Head/Face IB Hash',)),                 (add_ib_check_if_missing,)],
'c0ef468f': [(log, ('2.8: Soukaku Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'931476f6': [(log, ('2.8: Soukaku Weapon IB Hash',)),                    (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'5432bbb8': [(log, ('2.8: Soukaku Hair draw_vb',)),                      (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n'))],
'beac45e4': [(log, ('2.8: Soukaku Hair position_vb',)),                  (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n'))],
'43fb429d': [(log, ('2.8: Soukaku Hair texcoord_vb',)),                  (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n'))],
'f65883f3': [(log, ('2.8: Soukaku Hair blend_vb',)),                     (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'4ece0220': [(log, ('2.8: Soukaku Hair Shadow draw_vb',)),                (add_section_if_missing, ('c0ef468f', 'Soukaku.HairShadow.IB', 'match_priority = 0\n'))],
'bbcd9e5a': [(log, ('2.8: Soukaku Hair Shadow position_vb',)),            (add_section_if_missing, ('c0ef468f', 'Soukaku.HairShadow.IB', 'match_priority = 0\n'))],
'9ab82a7f': [(log, ('2.8: Soukaku Hair Shadow texcoord_vb',)),            (add_section_if_missing, ('c0ef468f', 'Soukaku.HairShadow.IB', 'match_priority = 0\n'))],
'd586de2b': [(log, ('2.8: Soukaku Hair Shadow blend_vb',)),               (add_section_if_missing, ('c0ef468f', 'Soukaku.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'ff00994d': [(log, ('2.8: Soukaku Body draw_vb',)),                      (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n'))],
'a426e353': [(log, ('2.8: Soukaku Body position_vb',)),                  (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n'))],
'176fb4d5': [(log, ('2.8: Soukaku Body texcoord_vb',)),                  (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n'))],
'dbbbafef': [(log, ('2.8: Soukaku Body blend_vb',)),                     (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n'))],

# Mask
'ddd3fb88': [(log, ('2.8: Soukaku Mask draw_vb',)),                      (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n'))],
'3a6a6326': [(log, ('2.8: Soukaku Mask position_vb',)),                  (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n'))],
'e261ddc0': [(log, ('2.8: Soukaku Mask texcoord_vb',)),                  (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n'))],
'5c5d1e7c': [(log, ('2.8: Soukaku Mask blend_vb',)),                     (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n'))],

# Face / Head
'd06e95fd': [(log, ('2.8: Soukaku Face VertexLimit Hash',)),              (add_section_if_missing, ('020f9ac6', 'Soukaku.Head.IB', 'match_priority = 0\n'))],
'ea7c06ba': [(log, ('2.8: Soukaku Face position_vb Hash',)),              (add_section_if_missing, ('020f9ac6', 'Soukaku.Head.IB', 'match_priority = 0\n'))],
'c2db08f0': [(log, ('2.8: Soukaku Face texcoord_vb Hash',)),              (add_section_if_missing, ('020f9ac6', 'Soukaku.Head.IB', 'match_priority = 0\n'))],
'2d187d8f': [(log, ('2.8: Soukaku Face blend_vb Hash',)),                 (add_section_if_missing, ('020f9ac6', 'Soukaku.Head.IB', 'match_priority = 0\n'))],

# Weapon
'66f9d07c': [(log, ('2.8: Soukaku Weapon VertexLimit Hash',)),            (add_section_if_missing, ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n'))],
'6b63687a': [(log, ('2.8: Soukaku Weapon position_vb Hash',)),            (add_section_if_missing, ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n'))],
'c18afef0': [(log, ('2.8: Soukaku Weapon texcoord_vb Hash',)),            (add_section_if_missing, ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n'))],
'6bf775f7': [(log, ('2.8: Soukaku Weapon blend_vb Hash',)),               (add_section_if_missing, ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'01f7369e': [(log, ('1.0 - 1.1: Soukaku Head IB Hash',)), (update_hash, ('020f9ac6',))],
'd148b6b9': [(log, ('2.0 -> 2.8: Soukaku Weapon Diffuse [Legacy]',)), (update_hash, ('67177563',))],
'a9ddf03d': [(log, ('2.0 -> 2.8: Soukaku Weapon LightMap [Legacy]',)), (update_hash, ('7c4efb96',))],
'39d92e17': [(log, ('2.0 -> 2.8: Soukaku Weapon MaterialMap [Legacy]',)), (update_hash, ('d0796da7',))],

# === Face Textures ===
'2ceacde6': [
        (log,                           ('2.8: Soukaku HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('427b39a4', 'Soukaku.HeadA.Diffuse.2048')),
    ],
'c20a8c82': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA LightMap 1024p Hash [Deprecated]',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('17110d01', 'Soukaku.HeadA.Diffuse.2048')),
    ],
'427b39a4': [
        (log,                           ('2.8: Soukaku HeadA/FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2ceacde6', 'Soukaku.HeadA.Diffuse.1024')),
    ],
'17110d01': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA LightMap 2048p Hash [Deprecated]',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c20a8c82', 'Soukaku.HeadA.Diffuse.1024')),
    ],

# === Hair & Mask Textures ===
'32ea0d00': [
        (log,                           ('2.8: Soukaku HairA/MaskA Diffuse 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('34a3ff5b', 'Soukaku.HairA.Diffuse.1024')),
    ],
'34a3ff5b': [
        (log,                           ('2.8: Soukaku HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('32ea0d00', 'Soukaku.HairA.Diffuse.2048')),
    ],
'5966c5e3': [
        (log,                           ('2.8: Soukaku Hair/Mask LightMap Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'04654e94': [(log, ('1.0 - 1.7: Soukaku HairA LightMap 2048p Hash',)), (update_hash, ('a70e24a2',))],
'7bbb3d02': [(log, ('1.0 - 1.7: Soukaku HairA LightMap 1024p Hash [Deprecated]',))],
'a70e24a2': [
        (log,                           ('2.8: Soukaku HairA/MaskA LightMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'd1444c52': [
        (log,                           ('2.8: Soukaku HairA/MaskA MaterialMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('218689cf', 'Soukaku.HairA.MaterialMap.1024')),
    ],
'218689cf': [
        (log,                           ('2.8: Soukaku HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d1444c52', 'Soukaku.HairA.MaterialMap.2048')),
    ],
'8498ee4d': [(log, ('1.0 - 1.7: Soukaku HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'0003126a': [(log, ('1.0 - 1.7: Soukaku HairA NormalMap 1024p Hash [Deprecated]',))],

# === Body Textures ===
'ee31954b': [
        (log,                           ('2.8: Soukaku BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6f5d31fc', 'Soukaku.BodyA.Diffuse.1024')),
    ],
'6f5d31fc': [
        (log,                           ('2.8: Soukaku BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ee31954b', 'Soukaku.BodyA.Diffuse.2048')),
    ],
'112a36a4': [
        (log,                           ('2.8: Soukaku BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c0f0bb74', 'Soukaku.BodyA.LightMap.1024')),
    ],
'c0f0bb74': [
        (log,                           ('2.8: Soukaku BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('112a36a4', 'Soukaku.BodyA.LightMap.2048')),
    ],
'd638ddf9': [
        (log,                           ('2.8: Soukaku BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1ec28297', 'Soukaku.BodyA.MaterialMap.1024')),
    ],
'1ec28297': [
        (log,                           ('2.8: Soukaku BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d638ddf9', 'Soukaku.BodyA.MaterialMap.2048')),
    ],
'363e3d70': [(log, ('1.0 - 1.7: Soukaku BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'77c48d32': [(log, ('1.0 - 1.7: Soukaku BodyA NormalMap 1024p Hash [Deprecated]',))],

# === Weapon Textures (v2.8 Target) ===
'67177563': [
        (log,                           ('2.8: Soukaku Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n')),
    ],
'7c4efb96': [
        (log,                           ('2.8: Soukaku Weapon LightMap Hash',)),
        (add_section_if_missing,        ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n')),
    ],
'd0796da7': [
        (log,                           ('2.8: Soukaku Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Soukaku Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('931476f6', 'Soukaku.Weapon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Soukaku HairA/BodyA NormalMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soukaku',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}