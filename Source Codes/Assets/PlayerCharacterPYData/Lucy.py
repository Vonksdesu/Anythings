"""
Lucy Character Hash Commands
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
    Returns Lucy's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'69ad9d08': [(log, ('2.8: Lucy Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'272dd7f6': [(log, ('2.8: Lucy Snout IB Hash',)),                       (add_ib_check_if_missing,)],
'9b6370f6': [(log, ('2.8: Lucy Belt IB Hash',)),                        (add_ib_check_if_missing,)],
'be5f4c7d': [(log, ('2.8: Lucy Body IB Hash',)),                        (add_ib_check_if_missing,)],
'1fe6e084': [(log, ('2.8: Lucy RedCloth IB Hash',)),                    (add_ib_check_if_missing,)],
'a0ed04de': [(log, ('2.8: Lucy Helmet IB Hash',)),                      (add_ib_check_if_missing,)],
'df3e3965': [(log, ('2.8: Lucy Head IB Hash',)),                        (add_ib_check_if_missing,)],
'ae17c1f9': [(log, ('2.8: Lucy Hair Shadow IB Hash',)),                  (add_ib_check_if_missing,)],
'cff7ddad': [(log, ('2.8: Lucy Weapon IB Hash',)),                      (add_ib_check_if_missing,)],
'e47150d9': [(log, ('2.8: Lucy Little Pig IB Hash',)),                  (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'5661afc3': [(log, ('2.8: Lucy Hair draw_vb',)),                        (add_section_if_missing, ('69ad9d08', 'Lucy.Hair.IB', 'match_priority = 0\n'))],
'6c733c84': [(log, ('2.8: Lucy Hair position_vb',)),                    (add_section_if_missing, ('69ad9d08', 'Lucy.Hair.IB', 'match_priority = 0\n'))],
'c8810832': [(log, ('2.8: Lucy Hair texcoord_vb',)),                    (add_section_if_missing, ('69ad9d08', 'Lucy.Hair.IB', 'match_priority = 0\n'))],
'a37c7537': [(log, ('2.8: Lucy Hair blend_vb',)),                       (add_section_if_missing, ('69ad9d08', 'Lucy.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'dac5a216': [(log, ('2.8: Lucy Hair Shadow draw_vb',)),                 (add_section_if_missing, ('ae17c1f9', 'Lucy.HairShadow.IB', 'match_priority = 0\n'))],
'04fcc509': [(log, ('2.8: Lucy Hair Shadow position_vb',)),             (add_section_if_missing, ('ae17c1f9', 'Lucy.HairShadow.IB', 'match_priority = 0\n'))],
'2fbb8fa1': [(log, ('2.8: Lucy Hair Shadow texcoord_vb',)),             (add_section_if_missing, ('ae17c1f9', 'Lucy.HairShadow.IB', 'match_priority = 0\n'))],
'5e691bac': [(log, ('2.8: Lucy Hair Shadow blend_vb',)),                (add_section_if_missing, ('ae17c1f9', 'Lucy.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'da79199a': [(log, ('2.8: Lucy Body draw_vb',)),                        (add_section_if_missing, ('be5f4c7d', 'Lucy.Body.IB', 'match_priority = 0\n'))],
'246b93e2': [(log, ('2.8: Lucy Body position_vb',)),                    (add_section_if_missing, ('be5f4c7d', 'Lucy.Body.IB', 'match_priority = 0\n'))],
'f60dbb9e': [(log, ('2.8: Lucy Body texcoord_vb',)),                    (add_section_if_missing, ('be5f4c7d', 'Lucy.Body.IB', 'match_priority = 0\n'))],
'66948a0f': [(log, ('2.8: Lucy Body blend_vb',)),                       (add_section_if_missing, ('be5f4c7d', 'Lucy.Body.IB', 'match_priority = 0\n'))],

# Helmet
'66cc3370': [(log, ('2.8: Lucy Helmet draw_vb',)),                      (add_section_if_missing, ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n'))],
'637e5139': [(log, ('2.8: Lucy Helmet position_vb',)),                  (add_section_if_missing, ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n'))],
'0d4e37c6': [(log, ('2.8: Lucy Helmet texcoord_vb',)),                  (add_section_if_missing, ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n'))],
'31f19e78': [(log, ('2.8: Lucy Helmet blend_vb',)),                     (add_section_if_missing, ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n'))],

# Snout
'9328313b': [(log, ('2.8: Lucy Snout draw_vb',)),                       (add_section_if_missing, ('272dd7f6', 'Lucy.Snout.IB', 'match_priority = 0\n'))],
'5fb8059e': [(log, ('2.8: Lucy Snout position_vb',)),                   (add_section_if_missing, ('272dd7f6', 'Lucy.Snout.IB', 'match_priority = 0\n'))],
'856c6618': [(log, ('2.8: Lucy Snout texcoord_vb',)),                   (add_section_if_missing, ('272dd7f6', 'Lucy.Snout.IB', 'match_priority = 0\n'))],
'b4cf5b8d': [(log, ('2.8: Lucy Snout blend_vb',)),                      (add_section_if_missing, ('272dd7f6', 'Lucy.Snout.IB', 'match_priority = 0\n'))],

# Belt
'7e98735e': [(log, ('2.8: Lucy Belt draw_vb',)),                        (add_section_if_missing, ('9b6370f6', 'Lucy.Belt.IB', 'match_priority = 0\n'))],
'90e47227': [(log, ('2.8: Lucy Belt position_vb',)),                    (add_section_if_missing, ('9b6370f6', 'Lucy.Belt.IB', 'match_priority = 0\n'))],
'170cc13e': [(log, ('2.8: Lucy Belt texcoord_vb',)),                    (add_section_if_missing, ('9b6370f6', 'Lucy.Belt.IB', 'match_priority = 0\n'))],
'9759ce48': [(log, ('2.8: Lucy Belt blend_vb',)),                       (add_section_if_missing, ('9b6370f6', 'Lucy.Belt.IB', 'match_priority = 0\n'))],

# RedCloth
'fa7b1c96': [(log, ('2.8: Lucy RedCloth draw_vb',)),                    (add_section_if_missing, ('1fe6e084', 'Lucy.RedCloth.IB', 'match_priority = 0\n'))],
'2f5719df': [(log, ('2.8: Lucy RedCloth position_vb',)),                (add_section_if_missing, ('1fe6e084', 'Lucy.RedCloth.IB', 'match_priority = 0\n'))],
'c789d6f4': [(log, ('2.8: Lucy RedCloth texcoord_vb',)),                (add_section_if_missing, ('1fe6e084', 'Lucy.RedCloth.IB', 'match_priority = 0\n'))],
'55decc93': [(log, ('2.8: Lucy RedCloth blend_vb',)),                   (add_section_if_missing, ('1fe6e084', 'Lucy.RedCloth.IB', 'match_priority = 0\n'))],

# Face / Head
'2db957ac': [(log, ('2.8: Lucy Face VertexLimit Hash',)),                (add_section_if_missing, ('df3e3965', 'Lucy.Head.IB', 'match_priority = 0\n'))],
'17abc4eb': [(log, ('2.8: Lucy Face position_vb Hash',)),                (add_section_if_missing, ('df3e3965', 'Lucy.Head.IB', 'match_priority = 0\n'))],
'1ca0ae1a': [(log, ('2.8: Lucy Face texcoord_vb Hash',)),                (add_section_if_missing, ('df3e3965', 'Lucy.Head.IB', 'match_priority = 0\n'))],
'a2054778': [(log, ('2.8: Lucy Face blend_vb Hash',)),                   (add_section_if_missing, ('df3e3965', 'Lucy.Head.IB', 'match_priority = 0\n'))],

# Weapon
'e5672032': [(log, ('2.8: Lucy Weapon VertexLimit Hash',)),              (add_section_if_missing, ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n'))],
'92a82477': [(log, ('2.8: Lucy Weapon position_vb Hash',)),              (add_section_if_missing, ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n'))],
'c5b8f21d': [(log, ('2.8: Lucy Weapon texcoord_vb Hash',)),              (add_section_if_missing, ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n'))],
'6f2d0bd2': [(log, ('2.8: Lucy Weapon blend_vb Hash',)),                 (add_section_if_missing, ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n'))],

# Little Pig
'36c6660d': [(log, ('2.8: Lucy Little Pig draw_vb Hash',)),              (add_section_if_missing, ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n'))],
'9429b8ba': [(log, ('2.8: Lucy Little Pig position_vb Hash',)),          (add_section_if_missing, ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n'))],
'b0e5b7b3': [(log, ('2.8: Lucy Little Pig texcoord_vb Hash',)),          (add_section_if_missing, ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n'))],
'e5774525': [(log, ('2.8: Lucy Little Pig blend_vb Hash',)),             (add_section_if_missing, ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'5315f036': [(log, ('1.2 -> 1.3: Lucy Hair Blend Hash',)),    (update_hash, ('a37c7537',))],
'751e21a5': [(log, ('1.2 -> 1.3: Lucy Hair Texcoord Hash',)), (update_hash, ('c8810832',))],
'198e99d7': [
        (log, ('1.2 -> 1.3: Lucy Hair IB Hash',)),
        (update_hash, ('69ad9d08',)),
        (transfer_indexed_sections, {
            'src_indices': ['0', '-1'],
            'trg_indices': ['0', '5253'],
        })
    ],
'5da9dafc': [(log, ('1.2 -> 1.3: Lucy Body Position Hash',)), (update_hash, ('246b93e2',))],
'b94b02e8': [(log, ('1.2 -> 1.3: Lucy Body Blend Hash',)),    (update_hash, ('66948a0f',))],
'00f11ea6': [(log, ('1.2 -> 1.3: Lucy Body Texcoord Hash',)), (update_hash, ('f60dbb9e',))],
'e0ad50ed': [(log, ('1.2 -> 1.3: Lucy Body IB Hash',)),       (update_hash, ('be5f4c7d',))],
'fca15ccb': [(log, ('1.2 -> 1.3: Lucy Head IB Hash',)),       (update_hash, ('df3e3965',))],
'483b418a': [(log, ('1.2 -> 1.3: Lucy HeadA Diffuse 1024p Hash',)), (update_hash, ('2578d35b',))],
'2a6df536': [(log, ('1.2 -> 1.3: Lucy HeadA Diffuse 1024p Hash',)), (update_hash, ('4e2d5baa',))],

# === Pembaruan Sinkronisasi Senjata & Little Pig v2.8 ===
'922bd542': [(log, ('2.0 -> 2.8: Lucy Weapon Diffuse [Legacy]',)), (update_hash, ('a580ad12',))],
'795a7681': [(log, ('2.0 -> 2.8: Lucy Weapon LightMap [Legacy]',)), (update_hash, ('b4f4dfdc',))],
'18709331': [(log, ('2.0 -> 2.8: Lucy Weapon MaterialMap [Legacy]',)), (update_hash, ('7e203979',))],
'2514c4b7': [(log, ('2.0 -> 2.8: Lucy Little Pig Diffuse [Legacy]',)), (update_hash, ('30bf583f',))],
'04c652ba': [(log, ('2.0 -> 2.8: Lucy Little Pig LightMap [Legacy]',)), (update_hash, ('13c237a3',))],
'62833532': [(log, ('2.0 -> 2.8: Lucy Little Pig MaterialMap [Legacy]',)), (update_hash, ('84d36706',))],

# === Face Textures ===
'2578d35b': [
        (log,                           ('2.8: Lucy HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('df3e3965', 'fca15ccb'), 'Lucy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4e2d5baa', '2a6df536'), 'Lucy.HeadA.Diffuse.2048')),
    ],
'4e2d5baa': [
        (log,                           ('2.8: Lucy HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('df3e3965', 'fca15ccb'), 'Lucy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('2578d35b', '483b418a'), 'Lucy.HeadA.Diffuse.1024')),
    ],

# === Hair, Snout, Belt Shared Textures ===
'b50eb71c': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA Diffuse 1024p Hash',)),     (update_hash, ('753baa45',))],
'd1241cfc': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA MaterialMap 1024p Hash',)), (update_hash, ('368f931c',))],
'aa513afa': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA Diffuse 2048p Hash',)),     (update_hash, ('0fa60fe1',))],
'919b608c': [(log, ('1.2 -> 1.3: Lucy HairA, SnoutA, BeltA MaterialMap 2048p Hash',)), (update_hash, ('068aba7f',))],
'0fa60fe1': [
        (log,                           ('2.8: Lucy HairA, SnoutA, BeltA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('753baa45', 'b50eb71c'), 'Lucy.HairA.Diffuse.1024')),
    ],
'753baa45': [
        (log,                           ('2.8: Lucy HairA, SnoutA, BeltA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('0fa60fe1', 'aa513afa'), 'Lucy.HairA.Diffuse.2048')),
    ],
'1a3b30ba': [
        (log,                           ('2.8: Lucy HairA, SnoutA, BeltA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('810c0878', 'Lucy.HairA.LightMap.1024')),
    ],
'810c0878': [
        (log,                           ('2.8: Lucy HairA, SnoutA, BeltA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('1a3b30ba', 'Lucy.HairA.LightMap.2048')),
    ],
'068aba7f': [
        (log,                           ('2.8: Lucy HairA, SnoutA, BeltA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   (('368f931c', 'd1241cfc'), 'Lucy.HairA.MaterialMap.1024')),
    ],
'368f931c': [
        (log,                           ('2.8: Lucy HairA, SnoutA, BeltA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   (('068aba7f', '919b608c'), 'Lucy.HairA.MaterialMap.2048')),
    ],
'edcb9661': [(log, ('1.0 -> 2.8: Lucy HairA, SnoutA, BeltA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'9114c7c7': [(log, ('1.0 -> 2.8: Lucy HairA, SnoutA, BeltA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],

# === Body & RedCloth Shared Textures ===
'474c7aa2': [
        (log,                           ('2.8: Lucy BodyA, RedClothA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('f810e7ac', 'Lucy.BodyA.Diffuse.1024')),
    ],
'f810e7ac': [
        (log,                           ('2.8: Lucy BodyA, RedClothA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('474c7aa2', 'Lucy.BodyA.Diffuse.2048')),
    ],
'855d9fa3': [
        (log,                           ('2.8: Lucy BodyA, RedClothA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e89f7814', 'Lucy.BodyA.LightMap.1024')),
    ],
'e89f7814': [
        (log,                           ('2.8: Lucy BodyA, RedClothA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('855d9fa3', 'Lucy.BodyA.LightMap.2048')),
    ],
'1fd24fd8': [
        (log,                           ('2.8: Lucy BodyA, RedClothA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('86ca6cfd', 'Lucy.BodyA.MaterialMap.1024')),
    ],
'86ca6cfd': [
        (log,                           ('2.8: Lucy BodyA, RedClothA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('1fd24fd8', 'Lucy.BodyA.MaterialMap.2048')),
    ],
'463b4f55': [(log, ('1.0 -> 2.8: Lucy BodyA, RedClothA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'1711cafd': [(log, ('1.0 -> 2.8: Lucy BodyA, RedClothA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],

# === Helmet Textures ===
'a0be0ed3': [
        (log,                           ('2.8: Lucy HelmetA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('919ab7e5', 'Lucy.HelmetA.Diffuse.1024')),
    ],
'919ab7e5': [
        (log,                           ('2.8: Lucy HelmetA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a0be0ed3', 'Lucy.HelmetA.Diffuse.2048')),
    ],
'8d9a16c7': [
        (log,                           ('2.8: Lucy HelmetA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6a8fca92', 'Lucy.HelmetA.LightMap.1024')),
    ],
'6a8fca92': [
        (log,                           ('2.8: Lucy HelmetA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8d9a16c7', 'Lucy.HelmetA.LightMap.2048')),
    ],
'b3013a33': [(log, ('1.0 -> 2.8: Lucy HelmetA MaterialMap 2048p Hash',)), (update_hash, ('0a99d9d5',))],
'4227db77': [(log, ('1.0 -> 2.8: Lucy HelmetA MaterialMap 1024p Hash',)), (update_hash, ('0a99d9d5',))],
'2243086f': [
        (log,                           ('2.8: Lucy Helmet MaterialMap Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
    ],
'ca5fd23a': [(log, ('1.0 -> 2.8: Lucy HelmetA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'f4d44970': [(log, ('1.0 -> 2.8: Lucy HelmetA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],
'0a99d9d5': [
        (log,                           ('2.8: Lucy HelmetA MaterialMap Hash',)),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4227db77', 'b3013a33'), 'Lucy.HelmetA.MaterialMap')),
    ],

# === Weapon Textures (v2.8 Target) ===
'a580ad12': [
        (log,                           ('2.8: Lucy Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n')),
    ],
'b4f4dfdc': [
        (log,                           ('2.8: Lucy Weapon LightMap Hash',)),
        (add_section_if_missing,        ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n')),
    ],
'7e203979': [
        (log,                           ('2.8: Lucy Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Little Pig Textures (v2.8 Target) ===
'30bf583f': [
        (log,                           ('2.8: Lucy Little Pig Diffuse Hash',)),
        (add_section_if_missing,        ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n')),
    ],
'13c237a3': [
        (log,                           ('2.8: Lucy Little Pig LightMap Hash',)),
        (add_section_if_missing,        ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n')),
    ],
'84d36706': [
        (log,                           ('2.8: Lucy Little Pig MaterialMap Hash',)),
        (add_section_if_missing,        ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Lucy Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('69ad9d08', 'Lucy.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('be5f4c7d', 'Lucy.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a0ed04de', 'Lucy.Helmet.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('272dd7f6', 'Lucy.Snout.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9b6370f6', 'Lucy.Belt.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1fe6e084', 'Lucy.RedCloth.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cff7ddad', 'Lucy.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e47150d9', 'Lucy.LittlePig.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Lucy Shared NormalMap Hash (All Components)',)),
        (multiply_section_if_missing,   (('edcb9661', '9114c7c7', '463b4f55', '1711cafd', 'ca5fd23a', 'f4d44970'), 'Lucy.Shared.NormalMap')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lucy',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}