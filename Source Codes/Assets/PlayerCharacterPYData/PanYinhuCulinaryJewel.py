"""
PanYinhuCulinaryJewel Character Hash Commands
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
    Returns PanYinhuCulinaryJewel's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'b518e540': [(log, ('2.8: PanYinhuCulinaryJewel Body IB Hash',)),        (add_ib_check_if_missing,)],
'ebb6a59b': [(log, ('2.8: PanYinhuCulinaryJewel Face IB Hash',)),        (add_ib_check_if_missing,)],
'ca72c1f0': [(log, ('2.8: PanYinhuCulinaryJewel WeaponLadle IB Hash',)), (add_ib_check_if_missing,)],
'12d52f05': [(log, ('2.8: PanYinhuCulinaryJewel WeaponPan IB Hash',)),   (add_ib_check_if_missing,)],

# === VB Hashes ===
# Body
'56b1d7f1': [(log, ('2.8: PanYinhuCulinaryJewel Body draw_vb Hash',)),             (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n'))],
'db608bcf': [(log, ('2.8: PanYinhuCulinaryJewel Body position_vb Hash',)),         (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n'))],
'f5b6e5b5': [(log, ('2.8: PanYinhuCulinaryJewel Body texcoord_vb Hash',)),         (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n'))],
'06f47d71': [(log, ('2.8: PanYinhuCulinaryJewel Body blend_vb Hash',)),            (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n'))],

# Face
'682e8e8d': [(log, ('2.8: PanYinhuCulinaryJewel Face draw_vb Hash',)),             (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n'))],
'1eee2121': [(log, ('2.8: PanYinhuCulinaryJewel Face texcoord_vb Hash',)),         (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n'))],
'4aae3329': [(log, ('2.8: PanYinhuCulinaryJewel Face blend_vb Hash',)),            (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n'))],

# Weapon - Ladle
'9f8e2d91': [(log, ('2.8: PanYinhuCulinaryJewel Ladle draw_vb Hash',)),            (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n'))],
'f6855ee8': [(log, ('2.8: PanYinhuCulinaryJewel Ladle position_vb Hash',)),        (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n'))],
'f29f44e5': [(log, ('2.8: PanYinhuCulinaryJewel Ladle texcoord_vb Hash',)),        (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n'))],
'644a4506': [(log, ('2.8: PanYinhuCulinaryJewel Ladle blend_vb Hash',)),           (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n'))],

# Weapon - Pan
'759a4b9f': [(log, ('2.8: PanYinhuCulinaryJewel Pan draw_vb Hash',)),              (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n'))],
'7e980f75': [(log, ('2.8: PanYinhuCulinaryJewel Pan position_vb Hash',)),          (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n'))],
'7353a8ed': [(log, ('2.8: PanYinhuCulinaryJewel Pan texcoord_vb Hash',)),          (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n'))],
'c39d130e': [(log, ('2.8: PanYinhuCulinaryJewel Pan blend_vb Hash',)),             (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'0cab7a7b': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyA Diffuse [Legacy]',)), (update_hash, ('e9a912e7',))],
'91bfe5cd': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyA LightMap [Legacy]',)), (update_hash, ('54c0f79a',))],
'78cbb2e4': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyA MaterialMap [Legacy]',)), (update_hash, ('7498bd49',))],
'b3775104': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyB Diffuse [Legacy]',)), (update_hash, ('8459c5e8',))],
'240da72f': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyB LightMap [Legacy]',)), (update_hash, ('c7bdc86b',))],
'bf25d6f7': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyB MaterialMap [Legacy]',)), (update_hash, ('c50582f7',))],
'48c0fbcc': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyC Diffuse [Legacy]',)), (update_hash, ('10e8bc53',))],
'eceb77a3': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyC LightMap [Legacy]',)), (update_hash, ('1da6b5bf',))],
'40dea057': [(log, ('2.0 -> 2.8: PanYinhuCulinaryJewel BodyC MaterialMap [Legacy]',)), (update_hash, ('eb5755d6',))],

# === Face Textures ===
'ed361b8f': [
        (log,                           ('3.0: PanYinhuCulinaryJewel Face Diffuse Hash',)),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'452a0918': [
        (log,                           ('2.8 -> 3.0: PanYinhuCulinaryJewel Face Diffuse Hash [Legacy]',)),
        (update_hash,                   ('ed361b8f',)),
    ],
'96280008': [
        (log,                           ('3.0: PanYinhuCulinaryJewel Face LightMap Hash',)),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'3744882e': [
        (log,                           ('2.8 -> 3.0: PanYinhuCulinaryJewel Face LightMap Hash [Legacy]',)),
        (update_hash,                   ('96280008',)),
    ],
'57446a22': [
        (log,                           ('3.0: PanYinhuCulinaryJewel Face MaterialMap Hash',)),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'18dd19bf': [
        (log,                           ('2.8 -> 3.0: PanYinhuCulinaryJewel Face MaterialMap Hash [Legacy]',)),
        (update_hash,                   ('57446a22',)),
    ],

# === Body Textures (Classification A/D - upper clothes) ===
'e9a912e7': [
        (log,                           ('2.8: PanYinhuCulinaryJewel BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'54c0f79a': [
        (log,                           ('2.8: PanYinhuCulinaryJewel BodyA LightMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'7498bd49': [
        (log,                           ('2.8: PanYinhuCulinaryJewel BodyA MaterialMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification B - lower body) ===
'8459c5e8': [
        (log,                           ('2.8: PanYinhuCulinaryJewel BodyB Diffuse Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'c7bdc86b': [
        (log,                           ('2.8: PanYinhuCulinaryJewel BodyB LightMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'c50582f7': [
        (log,                           ('2.8: PanYinhuCulinaryJewel BodyB MaterialMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],

# === Body, Ladle & Pan Shared Textures (Classification C - apron/accessories) ===
'10e8bc53': [
        (log,                           ('2.8: PanYinhuCulinaryJewel Body, Ladle, Pan Diffuse Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n')),
    ],
'1da6b5bf': [
        (log,                           ('2.8: PanYinhuCulinaryJewel Body, Ladle, Pan LightMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n')),
    ],
'eb5755d6': [
        (log,                           ('2.8: PanYinhuCulinaryJewel Body, Ladle, Pan MaterialMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: PanYinhuCulinaryJewel Shared NormalMap Hash',)),
        (add_section_if_missing,        ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ca72c1f0', 'PanYinhuCulinaryJewel.WeaponLadle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12d52f05', 'PanYinhuCulinaryJewel.WeaponPan.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: PanYinhuCulinaryJewel Shared NormalMap Hash [Legacy]',)),
        (update_hash,                   ('798adba3',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhuCulinaryJewel',
    'game_versions': ['2.8', '3.0'],
}