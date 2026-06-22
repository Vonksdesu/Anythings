"""
Pulchra Character Hash Commands
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
    Returns Pulchra's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'bd385763': [(log, ('2.8: Pulchra Body (Hair) IB Hash',)),                 (add_ib_check_if_missing,)],
'5b30f4da': [(log, ('2.8: Pulchra Mask IB Hash',)),                      (add_ib_check_if_missing,)],
'62de5837': [(log, ('2.8: Pulchra Face IB Hash',)),                      (add_ib_check_if_missing,)],
'243cdff6': [(log, ('2.8: Pulchra Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'425a7565': [(log, ('2.8: Pulchra Waist Supply IB Hash',)),              (add_ib_check_if_missing,)],
'96cb7dc9': [(log, ('2.8: Pulchra Wrist Supply IB Hash',)),              (add_ib_check_if_missing,)],
'5b644956': [(log, ('2.8: Pulchra Weapon Left-Gun IB Hash',)),            (add_ib_check_if_missing,)],
'bfc94dff': [(log, ('2.8: Pulchra Weapon Right-Gun IB Hash',)),           (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair Shadow
'096ad3f4': [(log, ('2.8: Pulchra Hair Shadow draw_vb',)),               (add_section_if_missing, ('243cdff6', 'Pulchra.HairShadow.IB', 'match_priority = 0\n'))],
'3dba047b': [(log, ('2.8: Pulchra Hair Shadow position_vb',)),           (add_section_if_missing, ('243cdff6', 'Pulchra.HairShadow.IB', 'match_priority = 0\n'))],
'09fcf321': [(log, ('2.8: Pulchra Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('243cdff6', 'Pulchra.HairShadow.IB', 'match_priority = 0\n'))],
'6b643cdd': [(log, ('2.8: Pulchra Hair Shadow blend_vb',)),              (add_section_if_missing, ('243cdff6', 'Pulchra.HairShadow.IB', 'match_priority = 0\n'))],

# Mask
'992028e7': [(log, ('2.8: Pulchra Mask draw_vb Hash',)),                 (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n'))],
'eed9f960': [(log, ('2.8: Pulchra Mask position_vb Hash',)),             (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n'))],
'0e117b28': [(log, ('2.8: Pulchra Mask texcoord_vb Hash',)),             (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n'))],
'0db288cb': [(log, ('2.8: Pulchra Mask blend_vb Hash',)),                (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n'))],

# Body
'2be39a26': [(log, ('2.8: Pulchra Body draw_vb Hash',)),                 (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n'))],
'a74c8d89': [(log, ('2.8: Pulchra Body position_vb Hash',)),             (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n'))],
'5204f58d': [(log, ('2.8: Pulchra Body texcoord_vb Hash',)),             (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n'))],
'9381fa0b': [(log, ('2.8: Pulchra Body blend_vb Hash',)),                (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n'))],

# Waist Supply
'ec497419': [(log, ('2.8: Pulchra Waist Supply draw_vb Hash',)),         (add_section_if_missing, ('425a7565', 'Pulchra.Waist.IB', 'match_priority = 0\n'))],
'5391a870': [(log, ('2.8: Pulchra Waist Supply blend_vb Hash',)),        (add_section_if_missing, ('425a7565', 'Pulchra.Waist.IB', 'match_priority = 0\n'))],

# Wrist Supply
'29a6299d': [(log, ('2.8: Pulchra Wrist Supply draw_vb Hash',)),         (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n'))],
'8329562b': [(log, ('2.8: Pulchra Wrist Supply position_vb Hash',)),     (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n'))],
'caa1f21c': [(log, ('2.8: Pulchra Wrist Supply texcoord_vb Hash',)),     (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n'))],
'55119041': [(log, ('2.8: Pulchra Wrist Supply blend_vb Hash',)),        (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n'))],

# Face
'd704bf57': [(log, ('2.8: Pulchra Face VertexLimit Hash',)),              (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n'))],
'ed162c10': [(log, ('2.8: Pulchra Face position_vb Hash',)),              (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n'))],
'2a29bb4e': [(log, ('2.8: Pulchra Face texcoord_vb Hash',)),              (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n'))],
'7e443147': [(log, ('2.8: Pulchra Face blend_vb Hash',)),                 (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'128c8f2e': [(log, ('2.0 -> 2.8: Pulchra Mask Diffuse [Legacy]',)), (update_hash, ('46bab365',))],
'e522177c': [(log, ('2.0 -> 2.8: Pulchra Mask LightMap [Legacy]',)), (update_hash, ('03d28ecd',))],
'ebac056e': [(log, ('2.8: Pulchra Shared NormalMap Hash [Legacy]',)), (update_hash, ('798adba3',))],

# === Face Textures ===
'1626aafe': [
        (log,                           ('2.8: Pulchra FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('32f923f1', 'Pulchra.FaceA.Diffuse.1024')),
    ],
'32f923f1': [
        (log,                           ('2.8: Pulchra FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1626aafe', 'Pulchra.FaceA.Diffuse.2048')),
    ],

# === Hair Textures (BodyB) ===
'57be79d6': [
        (log,                           ('2.8: Pulchra HairB Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fb0a816a', 'Pulchra.HairB.Diffuse.1024')),
    ],
'fb0a816a': [
        (log,                           ('2.8: Pulchra HairB Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('57be79d6', 'Pulchra.HairB.Diffuse.2048')),
    ],
'12c44063': [
        (log,                           ('2.8: Pulchra HairB LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f475e822', 'Pulchra.HairB.LightMap.1024')),
    ],
'f475e822': [
        (log,                           ('2.8: Pulchra HairB LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('12c44063', 'Pulchra.HairB.LightMap.2048')),
    ],
'a553df20': [
        (log,                           ('2.8: Pulchra HairB MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('64d75415', 'Pulchra.HairB.MaterialMap.1024')),
    ],
'64d75415': [
        (log,                           ('2.8: Pulchra HairB MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a553df20', 'Pulchra.HairB.MaterialMap.2048')),
    ],

# === Body Textures (BodyA) ===
'7fc03353': [
        (log,                           ('2.8: Pulchra BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf7eba0f', 'Pulchra.BodyA.Diffuse.1024')),
    ],
'bf7eba0f': [
        (log,                           ('2.8: Pulchra BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7fc03353', 'Pulchra.BodyA.Diffuse.2048')),
    ],
'd8462af0': [
        (log,                           ('2.8: Pulchra BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('47040200', 'Pulchra.BodyA.LightMap.1024')),
    ],
'47040200': [
        (log,                           ('2.8: Pulchra BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d8462af0', 'Pulchra.BodyA.LightMap.2048')),
    ],
'd404b789': [
        (log,                           ('2.8: Pulchra BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a66a11d0', 'Pulchra.BodyA.MaterialMap.1024')),
    ],
'a66a11d0': [
        (log,                           ('2.8: Pulchra BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d404b789', 'Pulchra.BodyA.MaterialMap.2048')),
    ],

# === Mask & Weapon Textures (v2.8 Target) ===
'46bab365': [
        (log,                           ('2.8: Pulchra Mask Diffuse Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'03d28ecd': [
        (log,                           ('2.8: Pulchra Mask LightMap Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'6b141146': [
        (log,                           ('2.8: Pulchra Mask MaterialMap Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],

# === Waist & Wrist Pouches Textures (v2.8 Target) ===
'ebd6c100': [
        (log,                           ('2.8: Pulchra Pouches Diffuse Hash',)),
        (add_section_if_missing,        ('425a7565', 'Pulchra.Waist.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n')),
    ],
'6f17d782': [
        (log,                           ('2.8: Pulchra Pouches LightMap Hash',)),
        (add_section_if_missing,        ('425a7565', 'Pulchra.Waist.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n')),
    ],
'b8e1e3f6': [
        (log,                           ('2.8: Pulchra Pouches MaterialMap Hash',)),
        (add_section_if_missing,        ('425a7565', 'Pulchra.Waist.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Pulchra Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('243cdff6', 'Pulchra.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5b644956', 'Pulchra.WeaponLeft.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bfc94dff', 'Pulchra.WeaponRight.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log,                           ('2.8: Pulchra Shared NormalMap Hash (Pouches)',)),
        (add_section_if_missing,        ('425a7565', 'Pulchra.Waist.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('96cb7dc9', 'Pulchra.Wrist.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pulchra',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}