"""
Yanagi Character Hash Commands
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
    Returns Yanagi's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'9e12899f': [(log, ('2.8: Yanagi Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'13c75775': [(log, ('2.8: Yanagi Ring IB Hash',)),                      (add_ib_check_if_missing,)],
'f478ee4c': [(log, ('2.8: Yanagi Body IB Hash',)),                      (add_ib_check_if_missing,)],
'44d9123b': [(log, ('2.8: Yanagi Glasses IB Hash',)),                   (add_ib_check_if_missing,)],
'0817204c': [(log, ('2.8: Yanagi Face IB Hash',)),                      (add_ib_check_if_missing,)],
'c1628e55': [(log, ('2.8: Yanagi Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'27d49f0b': [(log, ('2.8: Yanagi Weapon Scabbard IB Hash',)),            (add_ib_check_if_missing,)],
'2d7f2223': [(log, ('2.8: Yanagi Weapon Long Sword IB Hash',)),          (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'daba2b23': [(log, ('2.8: Yanagi Hair draw_vb Hash',)),                 (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n'))],
'0e52a354': [(log, ('2.8: Yanagi Hair position_vb Hash',)),             (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n'))],
'42ca0c9b': [(log, ('2.8: Yanagi Hair texcoord_vb Hash',)),             (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n'))],
'0bbe1d7d': [(log, ('2.8: Yanagi Hair blend_vb Hash',)),                (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'de0bb6f9': [(log, ('2.8: Yanagi Hair Shadow draw_vb Hash',)),          (add_section_if_missing, ('c1628e55', 'Yanagi.HairShadow.IB', 'match_priority = 0\n'))],
'9c8be112': [(log, ('2.8: Yanagi Hair Shadow position_vb Hash',)),      (add_section_if_missing, ('c1628e55', 'Yanagi.HairShadow.IB', 'match_priority = 0\n'))],
'bb35cc80': [(log, ('2.8: Yanagi Hair Shadow texcoord_vb Hash',)),      (add_section_if_missing, ('c1628e55', 'Yanagi.HairShadow.IB', 'match_priority = 0\n'))],
'eb448ade': [(log, ('2.8: Yanagi Hair Shadow blend_vb Hash',)),         (add_section_if_missing, ('c1628e55', 'Yanagi.HairShadow.IB', 'match_priority = 0\n'))],

# Ring
'01864eed': [(log, ('2.8: Yanagi Ring draw_vb Hash',)),                 (add_section_if_missing, ('13c75775', 'Yanagi.Ring.IB', 'match_priority = 0\n'))],
'fe235fbb': [(log, ('2.8: Yanagi Ring position_vb Hash',)),             (add_section_if_missing, ('13c75775', 'Yanagi.Ring.IB', 'match_priority = 0\n'))],
'49188dc8': [(log, ('2.8: Yanagi Ring texcoord_vb Hash',)),             (add_section_if_missing, ('13c75775', 'Yanagi.Ring.IB', 'match_priority = 0\n'))],
'07a1d434': [(log, ('2.8: Yanagi Ring blend_vb Hash',)),                (add_section_if_missing, ('13c75775', 'Yanagi.Ring.IB', 'match_priority = 0\n'))],

# Body
'2fe26340': [(log, ('2.8: Yanagi Body draw_vb Hash',)),                 (add_section_if_missing, ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n'))],
'7ff000de': [(log, ('2.8: Yanagi Body position_vb Hash',)),             (add_section_if_missing, ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n'))],
'f4fbc5c0': [(log, ('2.8: Yanagi Body texcoord_vb Hash',)),             (add_section_if_missing, ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n'))],

# Glasses / Lens
'178a1ff8': [(log, ('2.8: Yanagi Glasses draw_vb Hash',)),              (add_section_if_missing, ('44d9123b', 'Yanagi.Glasses.IB', 'match_priority = 0\n'))],
'8e3cf210': [(log, ('2.8: Yanagi Glasses position_vb Hash',)),          (add_section_if_missing, ('44d9123b', 'Yanagi.Glasses.IB', 'match_priority = 0\n'))],
'dd32963a': [(log, ('2.8: Yanagi Glasses texcoord_vb Hash',)),          (add_section_if_missing, ('44d9123b', 'Yanagi.Glasses.IB', 'match_priority = 0\n'))],
'6b5d6e39': [(log, ('2.8: Yanagi Glasses blend_vb Hash',)),             (add_section_if_missing, ('44d9123b', 'Yanagi.Glasses.IB', 'match_priority = 0\n'))],

# Face
'47323770': [(log, ('2.8: Yanagi Face VertexLimit Hash',)),              (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n'))],
'7d20a437': [(log, ('2.8: Yanagi Face position_vb Hash',)),              (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n'))],
'69c75b70': [(log, ('2.8: Yanagi Face texcoord_vb Hash',)),              (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n'))],
'4cb3e0ea': [(log, ('2.8: Yanagi Face blend_vb Hash',)),                 (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n'))],

# Weapon - Scabbard
'9e8cddbf': [(log, ('2.8: Yanagi Weapon Scabbard draw_vb Hash',)),       (add_section_if_missing, ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n'))],
'a07928b5': [(log, ('2.8: Yanagi Weapon Scabbard position_vb Hash',)),   (add_section_if_missing, ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n'))],
'c6d97eb4': [(log, ('2.8: Yanagi Weapon Scabbard texcoord_vb Hash',)),   (add_section_if_missing, ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n'))],
'74491025': [(log, ('2.8: Yanagi Weapon Scabbard blend_vb Hash',)),      (add_section_if_missing, ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n'))],

# Weapon - Long Sword
'b680db32': [(log, ('2.8: Yanagi Weapon Long Sword draw_vb Hash',)),     (add_section_if_missing, ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n'))],
'03634f2c': [(log, ('2.8: Yanagi Weapon Long Sword position_vb Hash',)), (add_section_if_missing, ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n'))],
'61f72721': [(log, ('2.8: Yanagi Weapon Long Sword texcoord_vb Hash',)), (add_section_if_missing, ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n'))],
'14b8daf0': [(log, ('2.8: Yanagi Weapon Long Sword blend_vb Hash',)),    (add_section_if_missing, ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n'))],

# === Hash Updates ===
'fd363c76': [(log, ('2.8: Yanagi Body blend [Legacy]',)),               (update_hash, ('b558d482',))],
'2e92fc77': [(log, ('2.8: Yanagi Glasses ib [Legacy]',)),               (update_hash, ('44d9123b',))],
'b558d482': [(log, ('2.8: Yanagi Body blend',)),                        (add_ib_check_if_missing,)],

# === Legacy Weapon Updates ===
'9ab64737': [(log, ('2.0 -> 2.8: Yanagi Weapon Diffuse [Legacy]',)), (update_hash, ('b2aca818',))],
'd9ac4e1e': [(log, ('2.0 -> 2.8: Yanagi Weapon LightMap [Legacy]',)), (update_hash, ('e4891108',))],
'd18079e5': [(log, ('2.0 -> 2.8: Yanagi Weapon MaterialMap [Legacy]',)), (update_hash, ('240ee9dc',))],
'ebac056e': [(log, ('2.8: Yanagi Shared NormalMap Hash [Legacy]',)), (update_hash, ('798adba3',))],

# === Face Textures ===
'cfe7ab46': [
        (log,                           ('2.8: Yanagi FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('95d9e92e', 'Yanagi.FaceA.Diffuse.2048')),
    ],
'95d9e92e': [
        (log,                           ('2.8: Yanagi FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cfe7ab46', 'Yanagi.FaceA.Diffuse.1024')),
    ],

# === Hair Textures ===
'4edb5c79': [
        (log,                           ('2.8: Yanagi HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ac5f6d76', 'Yanagi.HairA.Diffuse.2048')),
    ],
'5a43d985': [
        (log,                           ('2.8: Yanagi HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('99cfa935', 'Yanagi.HairA.LightMap.2048')),
    ],
'486e3c42': [
        (log,                           ('2.8: Yanagi HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f80b57f0', 'Yanagi.HairA.MaterialMap.2048')),
    ],
'ac5f6d76': [
        (log,                           ('2.8: Yanagi HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4edb5c79', 'Yanagi.HairA.Diffuse.1024')),
    ],
'99cfa935': [
        (log,                           ('2.8: Yanagi HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5a43d985', 'Yanagi.HairA.LightMap.1024')),
    ],
'f80b57f0': [
        (log,                           ('2.8: Yanagi HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('486e3c42', 'Yanagi.HairA.MaterialMap.1024')),
    ],

# === Body Textures ===
'c119dbd7': [
        (log,                           ('2.8: Yanagi BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c7c4f5c5', 'Yanagi.BodyA.Diffuse.2048')),
    ],
'f60602ec': [
        (log,                           ('2.8: Yanagi BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('616200aa', 'Yanagi.BodyA.LightMap.2048')),
    ],
'3ffcef9e': [
        (log,                           ('2.8: Yanagi Body LightMap Target Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
    ],
'b29f0188': [
        (log,                           ('2.8: Yanagi BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c2ae5d2b', 'Yanagi.BodyA.MaterialMap.2048')),
    ],
'c7c4f5c5': [
        (log,                           ('2.8: Yanagi BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c119dbd7', 'Yanagi.BodyA.Diffuse.1024')),
    ],
'616200aa': [
        (log,                           ('2.8: Yanagi BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f60602ec', 'Yanagi.BodyA.LightMap.1024')),
    ],
'c2ae5d2b': [
        (log,                           ('2.8: Yanagi BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b29f0188', 'Yanagi.BodyA.MaterialMap.1024')),
    ],

# === Weapon Textures (v2.8 Target) ===
'b2aca818': [
        (log,                           ('2.8: Yanagi Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n')),
    ],
'e4891108': [
        (log,                           ('2.8: Yanagi Weapon LightMap Hash',)),
        (add_section_if_missing,        ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n')),
    ],
'240ee9dc': [
        (log,                           ('2.8: Yanagi Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Yanagi Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('13c75775', 'Yanagi.Ring.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('44d9123b', 'Yanagi.Glasses.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c1628e55', 'Yanagi.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('27d49f0b', 'Yanagi.WeaponScabbard.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2d7f2223', 'Yanagi.WeaponLongSword.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yanagi',
    'game_versions': ['2.8'],
}