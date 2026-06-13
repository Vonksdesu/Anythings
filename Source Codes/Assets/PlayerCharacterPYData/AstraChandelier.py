"""
AstraChandelier Character Hash Commands
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
    Returns AstraChandelier's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'53cdac6c': [(log, ('2.8: AstraChandelier Hair IB Hash',)),              (add_ib_check_if_missing,)],
'02d8a2cb': [(log, ('2.8: AstraChandelier Body IB Hash',)),              (add_ib_check_if_missing,)],
'51831437': [(log, ('2.8: AstraChandelier Face IB Hash',)),              (add_ib_check_if_missing,)],
'93d55a49': [(log, ('2.8: AstraChandelier Hair Shadow IB Hash',)),       (add_ib_check_if_missing,)],
'702b018e': [(log, ('2.8: AstraChandelier Weapon Body IB Hash',)),       (add_ib_check_if_missing,)],
'f4f5348d': [(log, ('2.8: AstraChandelier Weapon Disc IB Hash',)),       (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd3c951b9': [(log, ('2.8: AstraChandelier Hair draw_vb',)),             (add_section_if_missing, ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n'))],
'ee3c305a': [(log, ('2.8: AstraChandelier Hair position_vb',)),         (add_section_if_missing, ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n'))],
'8ba0b335': [(log, ('2.8: AstraChandelier Hair texcoord_vb',)),         (add_section_if_missing, ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n'))],
'c3c08f85': [(log, ('2.8: AstraChandelier Hair blend_vb',)),            (add_section_if_missing, ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'5e1e12aa': [(log, ('2.8: AstraChandelier Hair Shadow draw_vb',)),      (add_section_if_missing, ('93d55a49', 'AstraChandelier.HairShadow.IB', 'match_priority = 0\n'))],
'a378328a': [(log, ('2.8: AstraChandelier Hair Shadow position_vb',)),  (add_section_if_missing, ('93d55a49', 'AstraChandelier.HairShadow.IB', 'match_priority = 0\n'))],
'c4456161': [(log, ('2.8: AstraChandelier Hair Shadow texcoord_vb',)),  (add_section_if_missing, ('93d55a49', 'AstraChandelier.HairShadow.IB', 'match_priority = 0\n'))],
'81ef699b': [(log, ('2.8: AstraChandelier Hair Shadow blend_vb',)),     (add_section_if_missing, ('93d55a49', 'AstraChandelier.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'645d075e': [(log, ('2.8: AstraChandelier Body draw_vb',)),             (add_section_if_missing, ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n'))],
'43f58537': [(log, ('2.8: AstraChandelier Body position_vb',)),         (add_section_if_missing, ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n'))],
'f1e37ebf': [(log, ('2.8: AstraChandelier Body texcoord_vb',)),         (add_section_if_missing, ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n'))],
'b72fadfc': [(log, ('2.8: AstraChandelier Body blend_vb',)),            (add_section_if_missing, ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n'))],

# Face
'5c578f85': [(log, ('2.8: AstraChandelier Face draw_vb',)),             (add_section_if_missing, ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n'))],
'66451cc2': [(log, ('2.8: AstraChandelier Face position_vb',)),         (add_section_if_missing, ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n'))],
'ffac76ac': [(log, ('2.8: AstraChandelier Face texcoord_vb',)),         (add_section_if_missing, ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n'))],
'7e05c11a': [(log, ('2.8: AstraChandelier Face blend_vb',)),            (add_section_if_missing, ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n'))],

# Weapon - Body
'ca16b939': [(log, ('2.8: AstraChandelier Weapon Body draw_vb',)),       (add_section_if_missing, ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n'))],
'9879faf3': [(log, ('2.8: AstraChandelier Weapon Body position_vb',)),   (add_section_if_missing, ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n'))],
'b3e27d5f': [(log, ('2.8: AstraChandelier Weapon Body texcoord_vb',)),   (add_section_if_missing, ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n'))],
'4a4fb44e': [(log, ('2.8: AstraChandelier Weapon Body blend_vb',)),      (add_section_if_missing, ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n'))],

# Weapon - Disc
'7ed93255': [(log, ('2.8: AstraChandelier Weapon Disc draw_vb',)),       (add_section_if_missing, ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n'))],
'b8a9ba2e': [(log, ('2.8: AstraChandelier Weapon Disc position_vb',)),   (add_section_if_missing, ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n'))],
'd6d5743e': [(log, ('2.8: AstraChandelier Weapon Disc texcoord_vb',)),   (add_section_if_missing, ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n'))],
'cb9405e1': [(log, ('2.8: AstraChandelier Weapon Disc blend_vb',)),      (add_section_if_missing, ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'd652aa31': [(log, ('2.0 -> 2.8: AstraChandelier Weapon Diffuse [Legacy]',)), (update_hash, ('b5a20274',))],
'91c63955': [(log, ('2.0 -> 2.8: AstraChandelier Weapon LightMap [Legacy]',)), (update_hash, ('57c44e60',))],
'98e011bc': [(log, ('2.0 -> 2.8: AstraChandelier Weapon MaterialMap [Legacy]',)), (update_hash, ('fdb82c44',))],

# === Hair Textures ===
'e634238a': [
        (log,                           ('2.8: AstraChandelier HairA Diffuse Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'56c71ea2': [
        (log,                           ('2.8: AstraChandelier Hair Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'34f0706c': [
        (log,                           ('2.8: AstraChandelier HairA LightMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'fd3ca2a6': [
        (log,                           ('2.8: AstraChandelier Hair LightMap Hash (Shared)',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'883a578f': [
        (log,                           ('2.8: AstraChandelier HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'759c15e0': [
        (log,                           ('2.8: AstraChandelier Hair MaterialMap Hash (Shared)',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'7301ca3a': [
        (log,                           ('2.8: AstraChandelier BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'8212713f': [
        (log,                           ('2.8: AstraChandelier Body Diffuse Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'7ce9f1db': [(log, ('2.8: AstraChandelier BodyA LightMap Hash [Legacy]',)),   (update_hash, ('515f9beb',))],
'515f9beb': [
        (log,                           ('2.8: AstraChandelier BodyA LightMap Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'cf8ecb3b': [
        (log,                           ('2.8: AstraChandelier Body LightMap Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'56abc3a3': [(log, ('2.8: AstraChandelier BodyA MaterialMap Hash [Legacy]',)),   (update_hash, ('fa2f509f',))],
'fa2f509f': [
        (log,                           ('2.8: AstraChandelier BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'03df0be9': [
        (log,                           ('2.8: AstraChandelier Body MaterialMap Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],

# === Face Component ===
'c41341b2': [
        (log,                           ('2.8: AstraChandelier FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n')),
    ],
'3283b8be': [
        (log,                           ('2.8: AstraChandelier Face Diffuse Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraChandelier.Face.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'b5a20274': [
        (log,                           ('2.8: AstraChandelier Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n')),
    ],
'57c44e60': [
        (log,                           ('2.8: AstraChandelier Weapon LightMap Hash',)),
        (add_section_if_missing,        ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n')),
    ],
'fdb82c44': [
        (log,                           ('2.8: AstraChandelier Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: AstraChandelier Shared NormalMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('702b018e', 'AstraChandelier.WeaponBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4f5348d', 'AstraChandelier.WeaponDisc.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: AstraChandelier Hair/Body NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraChandelier.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02d8a2cb', 'AstraChandelier.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AstraChandelier',
    'element': 'Fire',
    'faction': 'Obol Squad',
    'game_versions': ['2.8'],
}