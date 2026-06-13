"""
Trigger Character Hash Commands
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
    Returns Trigger's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'8e98ef9a': [(log, ('2.8: Trigger Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'7f32eeae': [(log, ('2.8: Trigger Body IB Hash',)),                      (add_ib_check_if_missing,)],
'40cd4182': [(log, ('2.8: Trigger Face IB Hash',)),                      (add_ib_check_if_missing,)],
'69c27d44': [(log, ('2.8: Trigger Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'f05e3a4a': [(log, ('2.8: Trigger Weapon Gun Body IB Hash',)),           (add_ib_check_if_missing,)],
'bb079ba3': [(log, ('2.8: Trigger Weapon Gun Stock IB Hash',)),          (add_ib_check_if_missing,)],
'f61f6acd': [(log, ('2.8: Trigger Weapon Magazine IB Hash',)),           (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'b0625293': [(log, ('2.8: Trigger Hair draw_vb Hash',)),                 (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n'))],
'f066913d': [(log, ('2.8: Trigger Hair position_vb Hash',)),             (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n'))],
'b12abbeb': [(log, ('2.8: Trigger Hair texcoord_vb Hash',)),             (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n'))],
'acd25c98': [(log, ('2.8: Trigger Hair blend_vb Hash',)),                (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n'))],

# Body
'5fdaccd2': [(log, ('2.8: Trigger Body draw_vb Hash',)),                 (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n'))],
'e4ae41fd': [(log, ('2.8: Trigger Body position_vb Hash',)),             (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n'))],
'b3c0a13c': [(log, ('2.8: Trigger Body texcoord_vb Hash',)),             (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n'))],
'e31a3b5f': [(log, ('2.8: Trigger Body blend_vb Hash',)),                (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n'))],

# Face
'8057c562': [(log, ('2.8: Trigger Face VertexLimit Hash',)),              (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n'))],
'dfc69ad0': [(log, ('2.8: Trigger Face Position Hash',)),                (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n'))],
'd4a12ab7': [(log, ('2.8: Trigger Face Texcoord Hash',)),                (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n'))],
'1a9a858c': [(log, ('2.8: Trigger Face Blend Hash',)),                   (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n'))],

# Weapon - Gun Body
'fa2ee314': [(log, ('2.8: Trigger Weapon Gun Body draw_vb Hash',)),      (add_section_if_missing, ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n'))],
'ac917a82': [(log, ('2.8: Trigger Weapon Gun Body position_vb Hash',)),  (add_section_if_missing, ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n'))],
'60fcff00': [(log, ('2.8: Trigger Weapon Gun Body texcoord_vb Hash',)),  (add_section_if_missing, ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n'))],
'ca8565b9': [(log, ('2.8: Trigger Weapon Gun Body blend_vb Hash',)),     (add_section_if_missing, ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n'))],

# Weapon - Gun Stock
'0cdfa94a': [(log, ('2.8: Trigger Weapon Gun Stock draw_vb Hash',)),      (add_section_if_missing, ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n'))],
'570ffcdc': [(log, ('2.8: Trigger Weapon Gun Stock position_vb Hash',)),  (add_section_if_missing, ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n'))],
'73555896': [(log, ('2.8: Trigger Weapon Gun Stock texcoord_vb Hash',)),  (add_section_if_missing, ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n'))],
'7ab2b542': [(log, ('2.8: Trigger Weapon Gun Stock blend_vb Hash',)),     (add_section_if_missing, ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n'))],

# Weapon - Magazine
'773c85f4': [(log, ('2.8: Trigger Weapon Magazine draw_vb Hash',)),       (add_section_if_missing, ('f61f6acd', 'Trigger.WeaponMagazine.IB', 'match_priority = 0\n'))],
'89c48e15': [(log, ('2.8: Trigger Weapon Magazine blend_vb Hash',)),      (add_section_if_missing, ('f61f6acd', 'Trigger.WeaponMagazine.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'88728785': [
        (log,                           ('2.8: Trigger FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cffc4b09', 'Trigger.FaceA.Diffuse.1024')),
    ],
'cffc4b09': [
        (log,                           ('2.8: Trigger FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('88728785', 'Trigger.FaceA.Diffuse.2048')),
    ],

# === Hair Textures ===
'e826a564': [
        (log,                           ('2.8: Trigger HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('984e7896', 'Trigger.HairA.Diffuse.1024')),
    ],
'984e7896': [
        (log,                           ('2.8: Trigger HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e826a564', 'Trigger.HairA.Diffuse.2048')),
    ],
'23f2a4cf': [
        (log,                           ('2.8: Trigger HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c321345c', 'Trigger.HairA.LightMap.1024')),
    ],
'c321345c': [
        (log,                           ('2.8: Trigger HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('23f2a4cf', 'Trigger.HairA.LightMap.2048')),
    ],
'b24f1752': [
        (log,                           ('2.8: Trigger HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4ee3c3fe', 'Trigger.HairA.MaterialMap.1024')),
    ],
'4ee3c3fe': [
        (log,                           ('2.8: Trigger HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b24f1752', 'Trigger.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'6631eadc': [
        (log,                           ('2.8: Trigger BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8cffa733', 'Trigger.BodyA.Diffuse.1024')),
    ],
'8cffa733': [
        (log,                           ('2.8: Trigger BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6631eadc', 'Trigger.BodyA.Diffuse.2048')),
    ],
'05250215': [
        (log,                           ('2.8: Trigger BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2c72b961', 'Trigger.BodyA.LightMap.1024')),
    ],
'2c72b961': [
        (log,                           ('2.8: Trigger BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('05250215', 'Trigger.BodyA.LightMap.2048')),
    ],
'985c5f52': [
        (log,                           ('2.8: Trigger BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cd507047', 'Trigger.BodyA.MaterialMap.1024')),
    ],
'cd507047': [
        (log,                           ('2.8: Trigger BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('985c5f52', 'Trigger.BodyA.MaterialMap.2048')),
    ],

# === Weapon Textures ===
'748df67a': [
        (log,                           ('2.8: Trigger Weapon Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f61f6acd', 'Trigger.WeaponMagazine.IB', 'match_priority = 0\n')),
    ],
'c7377a02': [
        (log,                           ('2.8: Trigger Weapon LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f61f6acd', 'Trigger.WeaponMagazine.IB', 'match_priority = 0\n')),
    ],
'799820a8': [
        (log,                           ('2.8: Trigger Weapon MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f61f6acd', 'Trigger.WeaponMagazine.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Trigger Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69c27d44', 'Trigger.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f05e3a4a', 'Trigger.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb079ba3', 'Trigger.WeaponStock.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f61f6acd', 'Trigger.WeaponMagazine.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Trigger Shared NormalMap Hash (Hair & Body) [Legacy]',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Trigger Weapon hashes ===
'19515c67': [
        (log,                           ('2.8: Trigger Weapon Diffuse Hash [New]',)),
        (add_section_if_missing,        (('f05e3a4a', 'bb079ba3', 'f61f6acd'), 'Trigger.Weapon.IB', 'match_priority = 0\n')),
    ],
'2236b80e': [
        (log,                           ('2.8: Trigger Weapon LightMap Hash [New]',)),
        (add_section_if_missing,        (('f05e3a4a', 'bb079ba3', 'f61f6acd'), 'Trigger.Weapon.IB', 'match_priority = 0\n')),
    ],
'a6d2b50e': [
        (log,                           ('2.8: Trigger Weapon MaterialMap Hash [New]',)),
        (add_section_if_missing,        (('f05e3a4a', 'bb079ba3', 'f61f6acd'), 'Trigger.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Trigger',
    'game_versions': ['2.8'],
}