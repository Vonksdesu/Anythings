"""
Promeia Character Hash Commands
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
    Returns Promeia's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'31178971': [(log, ('2.8: Promeia Hair IB Hash',)),            (add_ib_check_if_missing,)],
'ff223b2c': [(log, ('2.8: Promeia HairShadow IB Hash',)),      (add_ib_check_if_missing,)],
'36e794ea': [(log, ('2.8: Promeia BodyPinioned IB Hash',)),    (add_ib_check_if_missing,)],
'62a6b4bd': [(log, ('2.8: Promeia BodyNormal IB Hash',)),      (add_ib_check_if_missing,)],
'93f1f568': [(log, ('2.8: Promeia Clothes IB Hash',)),         (add_ib_check_if_missing,)],
'fd054d1d': [(log, ('2.8: Promeia Leg IB Hash',)),             (add_ib_check_if_missing,)],
'e032287a': [(log, ('2.8: Promeia Eyebrow IB Hash',)),         (add_ib_check_if_missing,)],
'ef3c4506': [(log, ('2.8: Promeia Face IB Hash',)),            (add_ib_check_if_missing,)],
'8995db58': [(log, ('2.8: Promeia Weapon IB Hash',)),          (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'0ae14c24': [(log, ('3.0: Promeia Cloak IB Hash',)),                 (add_ib_check_if_missing,)],
'b386901d': [(log, ('3.0: Promeia CloakChest IB Hash',)),            (add_ib_check_if_missing,)],
'10c77d62': [(log, ('3.0: Promeia Chest IB Hash',)),                 (add_ib_check_if_missing,)],
'ec003379': [(log, ('3.0: Promeia Legs IB Hash',)),                  (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'2d4c7c18': [(log, ('2.8: Promeia Hair draw_vb Hash',)),                 (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],
'681aceaa': [(log, ('2.8: Promeia Hair position_vb Hash',)),             (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],
'84d40d91': [(log, ('2.8: Promeia Hair texcoord_vb Hash',)),             (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],
'3d4a4881': [(log, ('2.8: Promeia Hair blend_vb Hash',)),                (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],

# Body - Pinioned State (BodyPinioned)
'19ad87f6': [(log, ('2.8: Promeia BodyPinioned draw_vb Hash',)),         (add_section_if_missing, ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n'))],
'ffaa183a': [(log, ('2.8: Promeia BodyPinioned position_vb Hash',)),     (add_section_if_missing, ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n'))],
'2a9842a1': [(log, ('2.8: Promeia BodyPinioned texcoord_vb Hash',)),     (add_section_if_missing, ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n'))],
'dae4abd0': [(log, ('2.8: Promeia BodyPinioned blend_vb Hash',)),        (add_section_if_missing, ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n'))],

# Body - Normal State (BodyNormal)
'9cce6ba2': [
        (log,                           ('2.8 -> 3.0: Promeia BodyNormal / Chest draw_vb Hash',)),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
    ],
'bf938187': [(log, ('2.8: Promeia BodyNormal position_vb Hash',)),       (add_section_if_missing, ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n'))],
'd99d21e0': [(log, ('2.8: Promeia BodyNormal texcoord_vb Hash',)),       (add_section_if_missing, ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n'))],
'575d8b1b': [(log, ('2.8: Promeia BodyNormal blend_vb Hash',)),          (add_section_if_missing, ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n'))],

# Clothes
'947f29ae': [
        (log,                           ('2.8 -> 3.0: Promeia Clothes / Cloak draw_vb Hash',)),
        (add_section_if_missing,        ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],
'1d63183b': [(log, ('2.8: Promeia Clothes position_vb Hash',)),          (add_section_if_missing, ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n'))],
'826446a7': [(log, ('2.8: Promeia Clothes texcoord_vb Hash',)),          (add_section_if_missing, ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n'))],
'58f42be3': [(log, ('2.8: Promeia Clothes blend_vb Hash',)),             (add_section_if_missing, ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n'))],

# Leg
'dfb01010': [
        (log,                           ('2.8 -> 3.0: Promeia Leg / Legs draw_vb Hash',)),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
'0b822797': [(log, ('2.8: Promeia Leg position_vb Hash',)),              (add_section_if_missing, ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n'))],
'f5fd0e92': [(log, ('2.8: Promeia Leg texcoord_vb Hash',)),              (add_section_if_missing, ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n'))],
'9839b071': [(log, ('2.8: Promeia Leg blend_vb Hash',)),                 (add_section_if_missing, ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n'))],

# Eyebrow
'a1d5b256': [(log, ('2.8: Promeia Eyebrow draw_vb Hash',)),              (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],
'9bc72111': [(log, ('2.8: Promeia Eyebrow position_vb Hash',)),          (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],
'd3d65ca5': [(log, ('2.8: Promeia Eyebrow texcoord_vb Hash',)),          (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],
'42594132': [(log, ('2.8: Promeia Eyebrow blend_vb Hash',)),             (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],

# Face
'32a38de6': [(log, ('2.8: Promeia Face draw_vb Hash',)),                 (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],
'08b11ea1': [(log, ('2.8: Promeia Face position_vb Hash',)),             (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],
'dcd61276': [(log, ('2.8: Promeia Face texcoord_vb Hash',)),             (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],
'bf5b785d': [(log, ('2.8: Promeia Face blend_vb Hash',)),                (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],

# Weapon - Ring Blade
'0a06059e': [(log, ('2.8: Promeia Weapon draw_vb Hash',)),               (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],
'd242b77a': [(log, ('2.8: Promeia Weapon position_vb Hash',)),           (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],
'f2f5bd28': [(log, ('2.8: Promeia Weapon texcoord_vb Hash',)),           (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],
'a864dc82': [(log, ('2.8: Promeia Weapon blend_vb Hash',)),              (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'328fa0cf': [(log, ('2.0 -> 2.8: Promeia Face/Eyebrow Diffuse [Legacy]',)), (update_hash, ('9b293811',))],
'a0add414': [(log, ('2.0 -> 2.8: Promeia Hair Diffuse [Legacy]',)),        (update_hash, ('c96de436',))],
'5c509f54': [(log, ('2.0 -> 2.8: Promeia Hair LightMap [Legacy]',)),       (update_hash, ('e34356a6',))],
'1f96c5d7': [(log, ('2.0 -> 2.8: Promeia Hair MaterialMap [Legacy]',)),    (update_hash, ('6bed1450',))],
'7d2d3a9e': [(log, ('2.0 -> 2.8: Promeia Body/Leg Diffuse [Legacy]',)),    (update_hash, ('ae109401',))],
'70ca6de8': [(log, ('2.0 -> 2.8: Promeia Body/Leg LightMap [Legacy]',)),   (update_hash, ('3864f20c',))],
'af976ad8': [(log, ('2.0 -> 2.8: Promeia Body/Leg MaterialMap [Legacy]',)), (update_hash, ('d57df6aa',))],
'406b1373': [(log, ('2.0 -> 2.8: Promeia Clothes Diffuse [Legacy]',)),     (update_hash, ('b9367016',))],
'044d2d39': [(log, ('2.0 -> 2.8: Promeia Clothes LightMap [Legacy]',)),    (update_hash, ('d743acd0',))],
'01a5ba27': [(log, ('2.0 -> 2.8: Promeia Clothes MaterialMap [Legacy]',)), (update_hash, ('31d7cbad',))],
'138bcaa1': [(log, ('2.0 -> 2.8: Promeia Weapon Diffuse [Legacy]',)),      (update_hash, ('d1399215',))],
'5e59380e': [(log, ('2.0 -> 2.8: Promeia Weapon LightMap [Legacy]',)),     (update_hash, ('369f0efd',))],
'09271c02': [(log, ('2.0 -> 2.8: Promeia Weapon MaterialMap [Legacy]',)),  (update_hash, ('a179a69c',))],
'ebac056e': [(log, ('2.8: Promeia Shared NormalMap [Legacy]',)),           (update_hash, ('798adba3',))],

# === 3.0 Database Updates (Strict Sync) ===
# Cloak VBs
'f6cc27b6': [(log, ('3.0: Promeia Cloak position_vb',)),             (add_section_if_missing, ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n'))],
'bf00cc95': [(log, ('3.0: Promeia Cloak texcoord_vb',)),             (add_section_if_missing, ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n'))],
'4b0d6867': [(log, ('3.0: Promeia Cloak blend_vb',)),                (add_section_if_missing, ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n'))],

# CloakChest VBs
'dd86f5ae': [(log, ('3.0: Promeia CloakChest draw_vb',)),            (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],
'68e2baef': [(log, ('3.0: Promeia CloakChest position_vb',)),        (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],
'6fe5f8c1': [(log, ('3.0: Promeia CloakChest texcoord_vb',)),        (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],
'112582ea': [(log, ('3.0: Promeia CloakChest blend_vb',)),           (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],

# Chest VBs
'2dbfe8c9': [(log, ('3.0: Promeia Chest position_vb',)),             (add_section_if_missing, ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n'))],
'1fc95f5b': [(log, ('3.0: Promeia Chest texcoord_vb',)),             (add_section_if_missing, ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n'))],
'ee35cc06': [(log, ('3.0: Promeia Chest blend_vb',)),                (add_section_if_missing, ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n'))],

# Legs VBs
'4c1d0a70': [(log, ('3.0: Promeia Legs position_vb',)),             (add_section_if_missing, ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n'))],
'03d6f933': [(log, ('3.0: Promeia Legs texcoord_vb',)),             (add_section_if_missing, ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n'))],
'65bba179': [(log, ('3.0: Promeia Legs blend_vb',)),                (add_section_if_missing, ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n'))],

# === Face & Eyebrow Textures (v2.8 Target) ===
'9b293811': [
        (log,                           ('2.8: Promeia FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures (v2.8 Target) ===
'c96de436': [
        (log,                           ('2.8: Promeia HairA Diffuse Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'e34356a6': [
        (log,                           ('2.8: Promeia HairA LightMap Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'6bed1450': [
        (log,                           ('2.8: Promeia HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body (Pinioned & Normal) & Leg Shared Textures (v2.8 Target) ===
'ae109401': [
        (log,                           ('2.8 -> 3.0: Promeia Body, Leg Diffuse Hash',)),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
'3864f20c': [
        (log,                           ('2.8 -> 3.0: Promeia Body, Leg LightMap Hash',)),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
'd57df6aa': [
        (log,                           ('2.8 -> 3.0: Promeia Body, Leg MaterialMap Hash',)),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],

# === Cloak Textures (v3.0 Target) ===
'e1492a53': [
        (log,                           ('3.0: Promeia Cloak Diffuse Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],
'9bf7f5cc': [
        (log,                           ('3.0: Promeia Cloak LightMap Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],
'd37b40a9': [
        (log,                           ('3.0: Promeia Cloak MaterialMap Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],

# === Clothes Textures (v2.8 Target) ===
'b9367016': [
        (log,                           ('2.8: Promeia Clothes Diffuse Hash',)),
        (add_section_if_missing,        ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],
'd743acd0': [
        (log,                           ('2.8: Promeia Clothes LightMap Hash',)),
        (add_section_if_missing,        ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],
'31d7cbad': [
        (log,                           ('2.8: Promeia Clothes MaterialMap Hash',)),
        (add_section_if_missing,        ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'd1399215': [
        (log,                           ('2.8: Promeia WeaponA Diffuse Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'369f0efd': [
        (log,                           ('2.8: Promeia WeaponA LightMap Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'a179a69c': [
        (log,                           ('2.8: Promeia WeaponA MaterialMap Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8 -> 3.0: Promeia Shared NormalMap Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Promeia',
    'game_versions': ['2.8', '3.0'],
}