"""
Dialyn Character Hash Commands
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
    Returns Dialyn's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'68f00074': [(log, ('2.8: Dialyn Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'af39a873': [(log, ('2.8: Dialyn Body IB Hash',)),                      (add_ib_check_if_missing,)],
'cd519abe': [(log, ('2.8: Dialyn PhoneCable IB Hash',)),                 (add_ib_check_if_missing,)],
'd860525e': [(log, ('2.8: Dialyn Brows IB Hash',)),                      (add_ib_check_if_missing,)],
'facb2461': [(log, ('2.8: Dialyn Face IB Hash',)),                      (add_ib_check_if_missing,)],
'59390f5a': [(log, ('2.8: Dialyn Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'1d8f8de6': [(log, ('2.8: Dialyn WeaponGrip IB Hash',)),                (add_ib_check_if_missing,)],
'caa3c4ef': [(log, ('2.8: Dialyn WeaponChakramA IB Hash',)),            (add_ib_check_if_missing,)],
'aae47bf3': [(log, ('2.8: Dialyn WeaponChakramB IB Hash',)),            (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'00e453e9': [(log, ('2.8: Dialyn Hair draw_vb',)),                      (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n'))],
'a486f1bb': [(log, ('2.8: Dialyn Hair position_vb',)),                  (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n'))],
'46019c5e': [(log, ('2.8: Dialyn Hair texcoord_vb',)),                  (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n'))],
'339f41eb': [(log, ('2.8: Dialyn Hair blend_vb',)),                     (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n'))],

# Body
'2e77bd1d': [(log, ('2.8: Dialyn Body draw_vb',)),                      (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n'))],
'ff36809b': [(log, ('2.8: Dialyn Body position_vb',)),                  (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n'))],
'3f2079bc': [(log, ('2.8: Dialyn Body texcoord_vb',)),                  (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n'))],
'3d7e53cf': [(log, ('2.8: Dialyn Body blend_vb',)),                     (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n'))],

# Telephone Cable
'38ce65ff': [(log, ('2.8: Dialyn Cable draw_vb',)),                     (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.IB', 'match_priority = 0\n'))],
'd0470351': [(log, ('2.8: Dialyn Cable position_vb',)),                 (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.IB', 'match_priority = 0\n'))],
'2e6484db': [(log, ('2.8: Dialyn Cable texcoord_vb',)),                 (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.IB', 'match_priority = 0\n'))],
'312b6e12': [(log, ('2.8: Dialyn Cable blend_vb',)),                    (add_section_if_missing, ('cd519abe', 'Dialyn.PhoneCable.IB', 'match_priority = 0\n'))],

# Eyebrow
'fecc9606': [(log, ('2.8: Dialyn Eyebrow draw_vb',)),                   (add_section_if_missing, ('d860525e', 'Dialyn.Brows.IB', 'match_priority = 0\n'))],
'c4de0541': [(log, ('2.8: Dialyn Eyebrow position_vb',)),               (add_section_if_missing, ('d860525e', 'Dialyn.Brows.IB', 'match_priority = 0\n'))],
'd90368ed': [(log, ('2.8: Dialyn Eyebrow texcoord_vb',)),               (add_section_if_missing, ('d860525e', 'Dialyn.Brows.IB', 'match_priority = 0\n'))],
'7ec67741': [(log, ('2.8: Dialyn Eyebrow blend_vb',)),                  (add_section_if_missing, ('d860525e', 'Dialyn.Brows.IB', 'match_priority = 0\n'))],

# Face
'fe5fb676': [(log, ('2.8: Dialyn Face draw_vb',)),                      (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n'))],
'c44d2531': [(log, ('2.8: Dialyn Face position_vb',)),                  (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n'))],
'f6c5296e': [(log, ('2.8: Dialyn Face texcoord_vb',)),                  (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n'))],
'08923d3e': [(log, ('2.8: Dialyn Face blend_vb',)),                     (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n'))],

# Weapon - Grip
'25f309c9': [(log, ('2.8: Dialyn WeaponGrip draw_vb',)),                (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n'))],

# Weapon - Chakram
'257c4603': [(log, ('2.8: Dialyn WeaponChakram draw_vb',)),             (add_section_if_missing, ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
                                                                        (add_section_if_missing, ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n'))],

# === Hash Updates ===
'6ff0e4ad': [(log, ('2.8: Dialyn Body blend [Legacy]',)),               (update_hash, ('3d7e53cf',))],

# === Pembaruan Sinkronisasi Senjata v2.8 ===
'87d209c3': [(log, ('2.0 -> 2.8: Dialyn Weapon Diffuse Hash [Legacy]',)), (update_hash, ('236576ee',))],
'a2264d99': [(log, ('2.0 -> 2.8: Dialyn Weapon LightMap Hash [Legacy]',)), (update_hash, ('036f72b3',))],
'7b07624c': [(log, ('2.0 -> 2.8: Dialyn Weapon MaterialMap Hash [Legacy]',)), (update_hash, ('4f0dc4f4',))],

# === Hair Textures (shared with PhoneCable) ===
'4dfbd393': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA Diffuse Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.Diffuse', 'match_priority = 0\n')),
    ],
'4f8d9492': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.Diffuse', 'match_priority = 0\n')),
    ],
'df9b8ecd': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA LightMap Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.LightMap', 'match_priority = 0\n')),
    ],
'a3f74f7d': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.LightMap', 'match_priority = 0\n')),
    ],
'5e6d6607': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA MaterialMap Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.MaterialMap', 'match_priority = 0\n')),
    ],
    '17aadaf6': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.MaterialMap', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Dialyn Shared NormalMap Hash (Hair, Body, Weapons & Cable)',)),
        (add_section_if_missing,        ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cd519abe', 'Dialyn.PhoneCable.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Dialyn HairA, PhoneCableA, BodyA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe', 'af39a873'), 'Dialyn.NormalMap', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'76ca930e': [
        (log,                           ('2.8: Dialyn BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.Diffuse', 'match_priority = 0\n')),
    ],
'52ea588e': [
        (log,                           ('2.8: Dialyn BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.Diffuse', 'match_priority = 0\n')),
    ],
'8c2fea9f': [
        (log,                           ('2.8: Dialyn BodyA LightMap Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.LightMap', 'match_priority = 0\n')),
    ],
'5cc175fe': [
        (log,                           ('2.8: Dialyn BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.LightMap', 'match_priority = 0\n')),
    ],
'a2425ea0': [
        (log,                           ('2.8: Dialyn BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.MaterialMap', 'match_priority = 0\n')),
    ],
'28a10401': [
        (log,                           ('2.8: Dialyn BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.MaterialMap', 'match_priority = 0\n')),
    ],

# === Face/Brows Textures ===
'56bc2921': [
        (log,                           ('2.8: Dialyn FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('facb2461', 'd860525e'), 'Dialyn.FaceA.Diffuse', 'match_priority = 0\n')),
    ],
'ad65abbf': [
        (log,                           ('2.8: Dialyn FaceA, BrowsA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        (('facb2461', 'd860525e'), 'Dialyn.FaceA.Diffuse', 'match_priority = 0\n')),
    ],

# === Weapon Textures (Pembaruan Sinkronisasi v2.8 Target) ===
'236576ee': [
        (log,                           ('2.8: Dialyn Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
    ],
'036f72b3': [
        (log,                           ('2.8: Dialyn Weapon LightMap Hash',)),
        (add_section_if_missing,        ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
    ],
'4f0dc4f4': [
        (log,                           ('2.8: Dialyn Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Dialyn',
    'game_versions': ['2.8'],
    'components': ['Hair', 'Body', 'PhoneCable', 'Brows', 'Face'],
}