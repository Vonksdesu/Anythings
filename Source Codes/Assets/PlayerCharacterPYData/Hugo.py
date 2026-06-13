"""
Hugo Character Hash Commands
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
    Returns Hugo's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'45ae7079': [(log, ('2.8: Hugo Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'b4765894': [(log, ('2.8: Hugo Body IB Hash',)),                        (add_ib_check_if_missing,)],
'ed26c53d': [(log, ('2.8: Hugo Coat IB Hash',)),                        (add_ib_check_if_missing,)],
'5db95af3': [(log, ('2.8: Hugo Badge IB Hash',)),                       (add_ib_check_if_missing,)],
'66b936fc': [(log, ('2.8: Hugo Face IB Hash',)),                        (add_ib_check_if_missing,)],
'b10cd0cb': [(log, ('2.8: Hugo Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'502e3af7': [(log, ('2.8: Hugo Hat IB Hash',)),                         (add_ib_check_if_missing,)],
'3876e8d9': [(log, ('2.8: Hugo Weapon Scythe IB Hash',)),               (add_ib_check_if_missing,)],
'c36d55cf': [(log, ('2.8: Hugo Weapon Dagger IB Hash',)),               (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'ab8eb2e6': [(log, ('2.8: Hugo Hair draw_vb',)),                        (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n'))],
'5ca107db': [(log, ('2.8: Hugo Hair position_vb',)),                    (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n'))],
'6815370e': [(log, ('2.8: Hugo Hair texcoord_vb',)),                    (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n'))],
'192f512e': [(log, ('2.8: Hugo Hair blend_vb',)),                       (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'f62bd189': [(log, ('2.8: Hugo Hair Shadow draw_vb',)),                 (add_section_if_missing, ('b10cd0cb', 'Hugo.HairShadow.IB', 'match_priority = 0\n'))],
'a02f2bed': [(log, ('2.8: Hugo Hair Shadow position_vb',)),             (add_section_if_missing, ('b10cd0cb', 'Hugo.HairShadow.IB', 'match_priority = 0\n'))],
'd3e741e2': [(log, ('2.8: Hugo Hair Shadow texcoord_vb',)),             (add_section_if_missing, ('b10cd0cb', 'Hugo.HairShadow.IB', 'match_priority = 0\n'))],
'75b5daef': [(log, ('2.8: Hugo Hair Shadow blend_vb',)),                (add_section_if_missing, ('b10cd0cb', 'Hugo.HairShadow.IB', 'match_priority = 0\n'))],

# Hat
'03d866ee': [(log, ('2.8: Hugo Hat draw_vb',)),                         (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n'))],
'5f316f49': [(log, ('2.8: Hugo Hat position_vb',)),                     (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n'))],
'8c6ea40f': [(log, ('2.8: Hugo Hat texcoord_vb',)),                     (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n'))],
'8b6d72a3': [(log, ('2.8: Hugo Hat blend_vb',)),                        (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n'))],

# Badge / Accessories
'dceadf77': [(log, ('2.8: Hugo Badge draw_vb',)),                       (add_section_if_missing, ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n'))],
'e150860c': [(log, ('2.8: Hugo Badge position_vb',)),                   (add_section_if_missing, ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n'))],
'62081bb7': [(log, ('2.8: Hugo Badge texcoord_vb',)),                   (add_section_if_missing, ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n'))],
'f591ad1a': [(log, ('2.8: Hugo Badge blend_vb',)),                      (add_section_if_missing, ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n'))],

# Body
'9557af37': [(log, ('2.8: Hugo Body draw_vb',)),                        (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n'))],
'78c37814': [(log, ('2.8: Hugo Body position_vb',)),                    (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n'))],
'ff82a5c5': [(log, ('2.8: Hugo Body texcoord_vb',)),                    (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n'))],
'757285ba': [(log, ('2.8: Hugo Body blend_vb',)),                       (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n'))],

# Coat / Jacket
'78d1f45f': [(log, ('2.8: Hugo Coat draw_vb',)),                        (add_section_if_missing, ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n'))],
'38efb2af': [(log, ('2.8: Hugo Coat position_vb',)),                    (add_section_if_missing, ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n'))],
'0e149ed0': [(log, ('2.8: Hugo Coat texcoord_vb',)),                    (add_section_if_missing, ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n'))],
'06bf72ed': [(log, ('2.8: Hugo Coat blend_vb',)),                       (add_section_if_missing, ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n'))],

# Face
'144bd078': [(log, ('2.8: Hugo Face VertexLimit Hash',)),                (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n'))],
'2e59433f': [(log, ('2.8: Hugo Face position_vb Hash',)),                (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n'))],
'99d2733a': [(log, ('2.8: Hugo Face texcoord_vb Hash',)),                (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n'))],
'7c087817': [(log, ('2.8: Hugo Face blend_vb Hash',)),                   (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n'))],

# Weapon - Scythe
'5fce83ff': [(log, ('2.8: Hugo Scythe Weapon draw_vb',)),                (add_section_if_missing, ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n'))],
'62ab3ad8': [(log, ('2.8: Hugo Scythe Weapon position_vb',)),            (add_section_if_missing, ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n'))],
'932eb21c': [(log, ('2.8: Hugo Scythe Weapon texcoord_vb',)),            (add_section_if_missing, ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n'))],
'7ed2b256': [(log, ('2.8: Hugo Scythe Weapon blend_vb',)),               (add_section_if_missing, ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n'))],

# Weapon - Dagger
'247b5b66': [(log, ('2.8: Hugo Dagger Weapon draw_vb',)),                (add_section_if_missing, ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n'))],
'8c936c4b': [(log, ('2.8: Hugo Dagger Weapon position_vb',)),            (add_section_if_missing, ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n'))],
'849665ce': [(log, ('2.8: Hugo Dagger Weapon texcoord_vb',)),            (add_section_if_missing, ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n'))],
'b64e3c83': [(log, ('2.8: Hugo Dagger Weapon blend_vb',)),               (add_section_if_missing, ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'a3064b0e': [
        (log,                           ('2.8: Hugo FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0f344a22', 'Hugo.FaceA.Diffuse.1024')),
    ],
'0f344a22': [
        (log,                           ('2.8: Hugo FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a3064b0e', 'Hugo.FaceA.Diffuse.2048')),
    ],

# === Hair Textures ===
'f50ebb37': [
        (log,                           ('2.8: Hugo HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bab642c6', 'Hugo.HairA.Diffuse.1024')),
    ],
'bab642c6': [
        (log,                           ('2.8: Hugo HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f50ebb37', 'Hugo.HairA.Diffuse.2048')),
    ],
'94daa8f7': [
        (log,                           ('2.8: Hugo HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dcf7c209', 'Hugo.HairA.LightMap.1024')),
    ],
'dcf7c209': [
        (log,                           ('2.8: Hugo HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('94daa8f7', 'Hugo.HairA.LightMap.2048')),
    ],
'9614f191': [
        (log,                           ('2.8: Hugo HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('144c15d0', 'Hugo.HairA.MaterialMap.1024')),
    ],
'144c15d0': [
        (log,                           ('2.8: Hugo HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9614f191', 'Hugo.HairA.MaterialMap.2048')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Hugo Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Hugo Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'7fa5eb2e': [
        (log,                           ('2.8: Hugo BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2841b582', 'Hugo.BodyA.Diffuse.1024')),
    ],
'2841b582': [
        (log,                           ('2.8: Hugo BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7fa5eb2e', 'Hugo.BodyA.Diffuse.2048')),
    ],
'f9911f83': [
        (log,                           ('2.8: Hugo BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9fd99d99', 'Hugo.BodyA.LightMap.1024')),
    ],
'9fd99d99': [
        (log,                           ('2.8: Hugo BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f9911f83', 'Hugo.BodyA.LightMap.2048')),
    ],
'c6fa84c9': [
        (log,                           ('2.8: Hugo BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e2333ede', 'Hugo.BodyA.MaterialMap.1024')),
    ],
'e2333ede': [
        (log,                           ('2.8: Hugo BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c6fa84c9', 'Hugo.BodyA.MaterialMap.2048')),
    ],

# === Coat / Jacket Textures ===
'348bc40f': [
        (log,                           ('2.8: Hugo CoatA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('481e8fe0', 'Hugo.CoatA.Diffuse.1024')),
    ],
'481e8fe0': [
        (log,                           ('2.8: Hugo CoatA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('348bc40f', 'Hugo.CoatA.Diffuse.2048')),
    ],
'0db80414': [
        (log,                           ('2.8: Hugo CoatA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a951a0cf', 'Hugo.CoatA.LightMap.1024')),
    ],
'a951a0cf': [
        (log,                           ('2.8: Hugo CoatA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0db80414', 'Hugo.CoatA.LightMap.2048')),
    ],
'25b33389': [
        (log,                           ('2.8: Hugo CoatA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ec648dcb', 'Hugo.CoatA.MaterialMap.1024')),
    ],
'ec648dcb': [
        (log,                           ('2.8: Hugo CoatA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('25b33389', 'Hugo.CoatA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'46b26208': [
        (log,                           ('2.8: Hugo Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n')),
    ],
'bc142031': [
        (log,                           ('2.8: Hugo Weapon LightMap Hash',)),
        (add_section_if_missing,        ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n')),
    ],
'8f82f802': [
        (log,                           ('2.8: Hugo Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('3876e8d9', 'Hugo.Scythe.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c36d55cf', 'Hugo.Dagger.IB', 'match_priority = 0\n')),
    ],

# === Legacy Weapon Updates ===
'6506987b': [(log, ('2.0 -> 2.8: Hugo Weapon Diffuse [Legacy]',)), (update_hash, ('46b26208',))],
'636f292d': [(log, ('2.0 -> 2.8: Hugo Weapon LightMap [Legacy]',)), (update_hash, ('bc142031',))],
'171b6643': [(log, ('2.0 -> 2.8: Hugo Weapon MaterialMap [Legacy]',)), (update_hash, ('8f82f802',))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Hugo',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}