"""
Orphie Character Hash Commands
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
    Returns Orphie's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'6988bfcd': [(log, ('2.8: Orphie Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'a5eac582': [(log, ('2.8: Orphie Body IB Hash',)),                      (add_ib_check_if_missing,)],
'80017921': [(log, ('2.8: Orphie Legs IB Hash',)),                      (add_ib_check_if_missing,)],
'3766fa59': [(log, ('2.8: Orphie MagusTail IB Hash',)),                 (add_ib_check_if_missing,)],
'389256d8': [(log, ('2.8: Orphie MagusNozzle IB Hash',)),               (add_ib_check_if_missing,)],
'2935f885': [(log, ('2.8: Orphie MagusDrum IB Hash',)),                 (add_ib_check_if_missing,)],
'ed85f33b': [(log, ('2.8: Orphie Face IB Hash',)),                      (add_ib_check_if_missing,)],
'd98415dc': [(log, ('2.8: Orphie Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'aa1404dd': [(log, ('2.8: Orphie Weapon Dagger IB Hash',)),              (add_ib_check_if_missing,)],
'e63d22c3': [(log, ('2.8: Orphie MagusEye IB Hash',)),                  (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'9f1dfc45': [(log, ('2.8: Orphie Hair draw_vb Hash',)),                 (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n'))],
'83c4fcaf': [(log, ('2.8: Orphie Hair position_vb Hash',)),             (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n'))],
'c721249c': [(log, ('2.8: Orphie Hair texcoord_vb Hash',)),             (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n'))],
'bb2a1769': [(log, ('2.8: Orphie Hair blend_vb Hash',)),                (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'79702a46': [(log, ('2.8: Orphie Hair Shadow draw_vb Hash',)),          (add_section_if_missing, ('d98415dc', 'Orphie.HairShadow.IB', 'match_priority = 0\n'))],
'd635bad0': [(log, ('2.8: Orphie Hair Shadow position_vb Hash',)),      (add_section_if_missing, ('d98415dc', 'Orphie.HairShadow.IB', 'match_priority = 0\n'))],
'd8779413': [(log, ('2.8: Orphie Hair Shadow texcoord_vb Hash',)),      (add_section_if_missing, ('d98415dc', 'Orphie.HairShadow.IB', 'match_priority = 0\n'))],
'48a78cdc': [(log, ('2.8: Orphie Hair Shadow blend_vb Hash',)),         (add_section_if_missing, ('d98415dc', 'Orphie.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'd4b12374': [(log, ('2.8: Orphie Body draw_vb Hash',)),                 (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n'))],
'e0269fbf': [(log, ('2.8: Orphie Body position_vb Hash',)),             (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n'))],
'd31ae32f': [(log, ('2.8: Orphie Body texcoord_vb Hash',)),             (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n'))],
'b823fb44': [(log, ('2.8: Orphie Body blend_vb Hash',)),                (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n'))],

# Legs
'f7b4360a': [(log, ('2.8: Orphie Legs draw_vb Hash',)),                 (add_section_if_missing, ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n'))],
'b4e15dc4': [(log, ('2.8: Orphie Legs position_vb Hash',)),             (add_section_if_missing, ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n'))],
'f74b4cea': [(log, ('2.8: Orphie Legs texcoord_vb Hash',)),             (add_section_if_missing, ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n'))],
'5ca9ed4e': [(log, ('2.8: Orphie Legs blend_vb Hash',)),                (add_section_if_missing, ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n'))],

# Face
'1542fac0': [(log, ('2.8: Orphie Face draw_vb Hash',)),                 (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n'))],
'2f506987': [(log, ('2.8: Orphie Face position_vb Hash',)),             (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n'))],
'48191f72': [(log, ('2.8: Orphie Face texcoord_vb Hash',)),             (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n'))],
'3cde4ca0': [(log, ('2.8: Orphie Face blend_vb Hash',)),                (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n'))],

# Weapon - Dagger
'6c9a0fb8': [(log, ('2.8: Orphie Weapon Dagger draw_vb Hash',)),         (add_section_if_missing, ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n'))],
'586b83df': [(log, ('2.8: Orphie Weapon Dagger position_vb Hash',)),     (add_section_if_missing, ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n'))],
'6b263148': [(log, ('2.8: Orphie Weapon Dagger texcoord_vb Hash',)),     (add_section_if_missing, ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n'))],
'7c7fd13b': [(log, ('2.8: Orphie Weapon Dagger blend_vb Hash',)),        (add_section_if_missing, ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n'))],

# Magus - Tail (MagusTail)
'fea2bd55': [(log, ('2.8: Orphie MagusTail draw_vb Hash',)),             (add_section_if_missing, ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n'))],
'f4a39978': [(log, ('2.8: Orphie MagusTail position_vb Hash',)),         (add_section_if_missing, ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n'))],
'f33946ec': [(log, ('2.8: Orphie MagusTail texcoord_vb Hash',)),         (add_section_if_missing, ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n'))],
'203664d5': [(log, ('2.8: Orphie MagusTail blend_vb Hash',)),            (add_section_if_missing, ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n'))],

# Magus - Head (MagusDrum)
'49393f27': [(log, ('2.8: Orphie MagusHead draw_vb Hash',)),             (add_section_if_missing, ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n'))],
'160ccb43': [(log, ('2.8: Orphie MagusHead position_vb Hash',)),         (add_section_if_missing, ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n'))],
'43b63f81': [(log, ('2.8: Orphie MagusHead texcoord_vb Hash',)),         (add_section_if_missing, ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n'))],
'17077e99': [(log, ('2.8: Orphie MagusHead blend_vb Hash',)),            (add_section_if_missing, ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n'))],

# Magus - Mouth (MagusNozzle)
'27b14e70': [(log, ('2.8: Orphie MagusMouth draw_vb Hash',)),            (add_section_if_missing, ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n'))],
'aeeebb95': [(log, ('2.8: Orphie MagusMouth position_vb Hash',)),        (add_section_if_missing, ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n'))],
'5662dd65': [(log, ('2.8: Orphie MagusMouth texcoord_vb Hash',)),        (add_section_if_missing, ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n'))],
'6fba1f7b': [(log, ('2.8: Orphie MagusMouth blend_vb Hash',)),           (add_section_if_missing, ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n'))],

# === Hair Textures ===
'78d4038b': [
        (log,                           ('2.8: Orphie Hair Diffuse Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'ce52779f': [
        (log,                           ('2.8: Orphie HairA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'643268b4': [
        (log,                           ('2.8: Orphie Hair LightMap Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'77abe83b': [
        (log,                           ('2.8: Orphie HairA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'ef6e3a3b': [
        (log,                           ('2.8: Orphie Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'94ed2491': [
        (log,                           ('2.8: Orphie HairA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'ca89cd72': [
        (log,                           ('2.8: Orphie Body Diffuse Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'c9bea5d7': [
        (log,                           ('2.8: Orphie BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'c797a191': [
        (log,                           ('2.8: Orphie Body LightMap Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'9a0406fe': [
        (log,                           ('2.8: Orphie BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'7f6aa298': [
        (log,                           ('2.8: Orphie Body MaterialMap Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'1daf926d': [
        (log,                           ('2.8: Orphie BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],

# === Legs Textures ===
'aaeb5f0f': [
        (log,                           ('2.8: Orphie Legs Diffuse Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'dd4120db': [
        (log,                           ('2.8: Orphie LegsA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'ec3855fa': [
        (log,                           ('2.8: Orphie Legs LightMap Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'a9ae84df': [
        (log,                           ('2.8: Orphie LegsA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'70ff1eca': [
        (log,                           ('2.8: Orphie Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],
'867ceb5b': [
        (log,                           ('2.8: Orphie LegsA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'66efca96': [
        (log,                           ('2.8: Orphie Face Diffuse Hash',)),
        (add_section_if_missing,        ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],
'0df52ae7': [
        (log,                           ('2.8: Orphie FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],

# === Magus & Weapon Shared Textures ===
'c64aea70': [
        (log,                           ('2.8: Orphie Dagger/Magus Diffuse Hash',)),
        (add_section_if_missing,        ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'dd80fa1d': [
        (log,                           ('2.8: Orphie Magus (Tail/Nozzle/Drum) Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'772b915b': [
        (log,                           ('2.8: Orphie Dagger/Magus LightMap Hash',)),
        (add_section_if_missing,        ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'92c6b20b': [
        (log,                           ('2.8: Orphie Magus (Tail/Nozzle/Drum) LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'c1650e3b': [
        (log,                           ('2.8: Orphie Dagger/Magus MaterialMap Hash',)),
        (add_section_if_missing,        ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'cb65982e': [
        (log,                           ('2.8: Orphie Magus (Tail/Nozzle/Drum) MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Orphie Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d98415dc', 'Orphie.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aa1404dd', 'Orphie.WeaponDagger.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Orphie Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Orphie',
    'game_versions': ['2.8'],
    'components': ['Hair', 'Body', 'Legs', 'MagusTail', 'MagusNozzle', 'MagusDrum', 'Face'],
}