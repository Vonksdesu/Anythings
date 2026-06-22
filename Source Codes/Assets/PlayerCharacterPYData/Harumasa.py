"""
Harumasa Character Hash Commands
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
    Returns Harumasa's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'6324de38': [(log, ('2.8: Harumasa Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'79679a10': [(log, ('2.8: Harumasa Body IB Hash',)),                      (add_ib_check_if_missing,)],
'aa7ba2dc': [(log, ('2.8: Harumasa Legs IB Hash',)),                      (add_ib_check_if_missing,)],
'b0688334': [(log, ('2.8: Harumasa Face IB Hash',)),                      (add_ib_check_if_missing,)],
'28ddcf0f': [(log, ('2.8: Harumasa Player IB Hash',)),                    (add_ib_check_if_missing,)],
'9bb92eee': [(log, ('2.8: Harumasa Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'30f715df': [(log, ('2.8: Harumasa Weapon Knife IB Hash',)),              (add_ib_check_if_missing,)],
'b92340c6': [(log, ('2.8: Harumasa Weapon Knife Sheath IB Hash',)),        (add_ib_check_if_missing,)],
'fdaa94b9': [(log, ('2.8: Harumasa Weapon Bow IB Hash',)),                (add_ib_check_if_missing,)],
'8ae5340d': [(log, ('2.8: Harumasa Weapon Arrow IB Hash',)),              (add_ib_check_if_missing,)],
'448ba3f6': [(log, ('2.8: Harumasa Weapon Quiver IB Hash',)),             (add_ib_check_if_missing,)],
'4785491b': [(log, ('2.8: Harumasa Weapon Bowstring IB Hash',)),          (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'9f75c05c': [(log, ('2.8: Harumasa Hair draw_vb',)),                     (add_section_if_missing, ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n'))],
'eddb9012': [(log, ('2.8: Harumasa Hair position_vb',)),                 (add_section_if_missing, ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n'))],
'4f45a9c5': [(log, ('2.8: Harumasa Hair texcoord_vb',)),                 (add_section_if_missing, ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n'))],
'2644c499': [(log, ('2.8: Harumasa Hair blend_vb',)),                    (add_section_if_missing, ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'2c64fa81': [(log, ('2.8: Harumasa Hair Shadow draw_vb',)),              (add_section_if_missing, ('9bb92eee', 'Harumasa.HairShadow.IB', 'match_priority = 0\n'))],
'2c094dd4': [(log, ('2.8: Harumasa Hair Shadow position_vb',)),          (add_section_if_missing, ('9bb92eee', 'Harumasa.HairShadow.IB', 'match_priority = 0\n'))],
'd1116809': [(log, ('2.8: Harumasa Hair Shadow texcoord_vb',)),          (add_section_if_missing, ('9bb92eee', 'Harumasa.HairShadow.IB', 'match_priority = 0\n'))],
'c39d129c': [(log, ('2.8: Harumasa Hair Shadow blend_vb',)),             (add_section_if_missing, ('9bb92eee', 'Harumasa.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'1fb92e46': [(log, ('2.8: Harumasa Body draw_vb',)),                     (add_section_if_missing, ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n'))],
'0899751e': [(log, ('2.8: Harumasa Body position_vb',)),                 (add_section_if_missing, ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n'))],
'e14fbc30': [(log, ('2.8: Harumasa Body texcoord_vb',)),                 (add_section_if_missing, ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n'))],
'347a0e9d': [(log, ('2.8: Harumasa Body blend_vb',)),                    (add_section_if_missing, ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n'))],

# Legs
'7fdd2495': [(log, ('2.8: Harumasa Legs draw_vb',)),                     (add_section_if_missing, ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n'))],
'5991a6b6': [(log, ('2.8: Harumasa Legs position_vb',)),                 (add_section_if_missing, ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n'))],
'9d044bbd': [(log, ('2.8: Harumasa Legs texcoord_vb',)),                 (add_section_if_missing, ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n'))],
'f58e77a5': [(log, ('2.8: Harumasa Legs blend_vb',)),                    (add_section_if_missing, ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n'))],

# Face
'747c3263': [(log, ('2.8: Harumasa Face VertexLimit Hash',)),            (add_section_if_missing, ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n'))],
'4e6ea124': [(log, ('2.8: Harumasa Face position_vb Hash',)),            (add_section_if_missing, ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n'))],
'48152e31': [(log, ('2.8: Harumasa Face texcoord_vb Hash',)),            (add_section_if_missing, ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n'))],
'4c813358': [(log, ('2.8: Harumasa Face blend_vb Hash',)),               (add_section_if_missing, ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n'))],

# Weapon - Knife
'a23df160': [(log, ('2.8: Harumasa Weapon Knife draw_vb',)),             (add_section_if_missing, ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n'))],
'e7eb0751': [(log, ('2.8: Harumasa Weapon Knife position_vb',)),         (add_section_if_missing, ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n'))],
'46a82ecd': [(log, ('2.8: Harumasa Weapon Knife texcoord_vb',)),         (add_section_if_missing, ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n'))],
'1dcdd87d': [(log, ('2.8: Harumasa Weapon Knife blend_vb',)),            (add_section_if_missing, ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n'))],

# Weapon - Knife Sheath
'80fadc88': [(log, ('2.8: Harumasa Weapon Knife Sheath draw_vb',)),       (add_section_if_missing, ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n'))],
'4d13c1da': [(log, ('2.8: Harumasa Weapon Knife Sheath position_vb',)),   (add_section_if_missing, ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n'))],
'8db5bfa8': [(log, ('2.8: Harumasa Weapon Knife Sheath texcoord_vb',)),   (add_section_if_missing, ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n'))],
'30c2db1a': [(log, ('2.8: Harumasa Weapon Knife Sheath blend_vb',)),      (add_section_if_missing, ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n'))],

# Weapon - Bow
'a385ad88': [(log, ('2.8: Harumasa Weapon Bow draw_vb Hash',)),          (add_section_if_missing, ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n'))],
'11ddc4c0': [(log, ('2.8: Harumasa Weapon Bow position_vb Hash',)),      (add_section_if_missing, ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n'))],
'0f901bce': [(log, ('2.8: Harumasa Weapon Bow texcoord_vb Hash',)),      (add_section_if_missing, ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n'))],
'd9d7d268': [(log, ('2.8: Harumasa Weapon Bow blend_vb Hash',)),         (add_section_if_missing, ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n'))],

# Weapon - Arrow
'5c7e0333': [(log, ('2.8: Harumasa Weapon Arrow draw_vb Hash',)),        (add_section_if_missing, ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n'))],
'8af12b9e': [(log, ('2.8: Harumasa Weapon Arrow position_vb Hash',)),    (add_section_if_missing, ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n'))],
'e696e4c6': [(log, ('2.8: Harumasa Weapon Arrow texcoord_vb Hash',)),    (add_section_if_missing, ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n'))],
'cbf4b91e': [(log, ('2.8: Harumasa Weapon Arrow blend_vb Hash',)),       (add_section_if_missing, ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n'))],

# Weapon - Quiver
'fc5a562a': [(log, ('2.8: Harumasa Weapon Quiver draw_vb Hash',)),       (add_section_if_missing, ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n'))],
'75e1907f': [(log, ('2.8: Harumasa Weapon Quiver position_vb Hash',)),   (add_section_if_missing, ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n'))],
'0d04cfb0': [(log, ('2.8: Harumasa Weapon Quiver texcoord_vb Hash',)),   (add_section_if_missing, ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n'))],
'ce8a5469': [(log, ('2.8: Harumasa Weapon Quiver blend_vb Hash',)),      (add_section_if_missing, ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n'))],

# Weapon - Bowstring
'b5c06ca5': [(log, ('2.8: Harumasa Weapon Bowstring draw_vb Hash',)),    (add_section_if_missing, ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n'))],
'84c629fe': [(log, ('2.8: Harumasa Weapon Bowstring position_vb Hash',)),(add_section_if_missing, ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n'))],
'62fe83fc': [(log, ('2.8: Harumasa Weapon Bowstring texcoord_vb Hash',)),(add_section_if_missing, ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n'))],
'02032760': [(log, ('2.8: Harumasa Weapon Bowstring blend_vb Hash',)),   (add_section_if_missing, ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n'))],

# Weapon - Radio
'545441d8': [(log, ('2.8: Harumasa Radio draw_vb Hash',)),               (add_section_if_missing, ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n'))],
'fa0083a4': [(log, ('2.8: Harumasa Radio position_vb Hash',)),           (add_section_if_missing, ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n'))],
'74c5fd55': [(log, ('2.8: Harumasa Radio texcoord_vb Hash',)),           (add_section_if_missing, ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n'))],
'999c8d00': [(log, ('2.8: Harumasa Radio blend_vb Hash',)),              (add_section_if_missing, ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'f51a89c1': [(log, ('1.4 -> 1.5: Harumasa Hair IB Hash',)), (update_hash, ('6324de38',))],
'fa851c10': [(log, ('1.4 -> 1.5: Harumasa Hair Draw Hash',)),     (update_hash, ('9f75c05c',))],
'f5727f53': [(log, ('1.4 -> 1.5: Harumasa Hair Position Hash',)), (update_hash, ('eddb9012',))],
'52787e7d': [(log, ('1.4 -> 1.5: Harumasa Hair Blend Hash',)),    (update_hash, ('2644c499',))],
'9879fba3': [(log, ('1.4 -> 1.5: Harumasa Hair Texcoord Hash',)), (update_hash, ('4f45a9c5',))],
'78bea30d': [(log, ('1.4 -> 1.5: Harumasa Body IB Hash',)), (update_hash, ('79679a10',))],
'cafffd37': [(log, ('1.4 -> 1.5: Harumasa Body Draw Hash',)),     (update_hash, ('1fb92e46',))],
'3fa41462': [(log, ('1.4 -> 1.5: Harumasa Body Position Hash',)), (update_hash, ('0899751e',))],
'c0b32d17': [(log, ('1.4 -> 1.5: Harumasa Body Blend Hash',)),    (update_hash, ('347a0e9d',))],
'95ee1030': [(log, ('1.4 -> 1.5: Harumasa Body Texcoord Hash',)), (update_hash, ('e14fbc30',))],
'ba52ac92': [(log, ('1.4 -> 1.5: Harumasa BodyA Diffuse 2048p Hash',)), (update_hash, ('49f8aaf6',))],
'cd1e0187': [(log, ('1.4 -> 1.5: Harumasa BodyA MaterialMap 2048p Hash',)), (update_hash, ('6d105f7e',))],
'e0b0c6eb': [(log, ('1.4 -> 1.5: Harumasa BodyA Diffuse 1024p Hash',)), (update_hash, ('999ec526',))],
'2b0017d5': [(log, ('1.4 -> 1.5: Harumasa BodyA MaterialMap 1024p Hash',)), (update_hash, ('c90264db',))],
'd4838b9d': [(log, ('1.4 -> 2.5: Harumasa HairA LightMap 2048p Hash [Legacy]',)), (update_hash, ('11041778',))],
'a1310b4f': [(log, ('1.4 -> 2.5: Harumasa HairA LightMap 1024p Hash [Legacy]',)), (update_hash, ('11041778',))],
'ba8e396b': [(log, ('1.4 -> 2.5: Harumasa LegsA MaterialMap 2048p Hash [Legacy]',)), (update_hash, ('72885950',))],
'bdbf66a1': [(log, ('1.4 -> 2.5: Harumasa LegsA MaterialMap 1024p Hash [Legacy]',)), (update_hash, ('72885950',))],

# === Pembaruan Sinkronisasi Quiver v2.8 ===
'e6cb774e': [(log, ('2.0 -> 2.8: Harumasa Quiver Diffuse Hash Part 2 [Legacy]',)), (update_hash, ('c776b2ac',))],
'56b0cd82': [(log, ('2.0 -> 2.8: Harumasa Quiver LightMap Hash Part 2 [Legacy]',)), (update_hash, ('0e38f04c',))],
'af798757': [(log, ('2.0 -> 2.8: Harumasa Quiver MaterialMap Hash Part 2 [Legacy]',)), (update_hash, ('ceb7b1fa',))],
'ebac056e': [(log, ('2.8: Harumasa Shared NormalMap Hash [Legacy]',)), (update_hash, ('798adba3',))],

# === Hair Textures ===
'b8f268ee': [
        (log,                           ('2.8: Harumasa HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5700ced5', 'Harumasa.HairA.Diffuse.1024')),
    ],
'5700ced5': [
        (log,                           ('2.8: Harumasa HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b8f268ee', 'Harumasa.HairA.Diffuse.2048')),
    ],
'54cc6a9a': [
        (log,                           ('2.8: Harumasa Hair LightMap Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
    ],
'11041778': [
        (log,                           ('2.8: Harumasa HairA LightMap Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
    ],
'7217c146': [
        (log,                           ('2.8: Harumasa HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c2c9ad2d', 'Harumasa.HairA.MaterialMap.1024')),
    ],
'c2c9ad2d': [
        (log,                           ('2.8: Harumasa HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7217c146', 'Harumasa.HairA.MaterialMap.2048')),
    ],

# === Legs Textures ===
'44d74a1a': [
        (log,                           ('2.8: Harumasa LegsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('897c74d5', 'Harumasa.LegsA.Diffuse.1024')),
    ],
'897c74d5': [
        (log,                           ('2.8: Harumasa LegsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('44d74a1a', 'Harumasa.LegsA.Diffuse.2048')),
    ],
'4b4d0ff6': [
        (log,                           ('2.8: Harumasa LegsA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('822ec07f', 'Harumasa.LegsA.LightMap.1024')),
    ],
'822ec07f': [
        (log,                           ('2.8: Harumasa LegsA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4b4d0ff6', 'Harumasa.LegsA.LightMap.2048')),
    ],
'72885950': [
        (log,                           ('2.8: Harumasa LegsA MaterialMap Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
    ],
'b84027c8': [
        (log,                           ('2.8: Harumasa Legs MaterialMap Hash',)),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'49f8aaf6': [
        (log,                           ('2.8: Harumasa BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('999ec526', 'e0b0c6eb'), 'Harumasa.BodyA.Diffuse.1024')),
    ],
'999ec526': [
        (log,                           ('2.8: Harumasa BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('49f8aaf6', 'ba52ac92'), 'Harumasa.BodyA.Diffuse.2048')),
    ],
'cc51476a': [
        (log,                           ('2.8: Harumasa BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2b1230cf', 'Harumasa.BodyA.LightMap.1024')),
    ],
'2b1230cf': [
        (log,                           ('2.8: Harumasa BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cc51476a', 'Harumasa.BodyA.LightMap.2048')),
    ],
'6d105f7e': [
        (log,                           ('2.8: Harumasa BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('c90264db', '2b0017d5'), 'Harumasa.BodyA.MaterialMap.1024')),
    ],
'c90264db': [
        (log,                           ('2.8: Harumasa BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('79679a10', '78bea30d'), 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('6d105f7e', 'cd1e0187'), 'Harumasa.BodyA.MaterialMap.2048')),
    ],

# === Face Textures ===
'4394c0b2': [
        (log,                           ('2.8: Harumasa FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c5596262', 'Harumasa.FaceA.Diffuse.1024')),
    ],
'c5596262': [
        (log,                           ('2.8: Harumasa FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4394c0b2', 'Harumasa.FaceA.Diffuse.2048')),
    ],

# === Player Textures ===
'81f189a2': [
        (log,                           ('2.8: Harumasa PlayerA Diffuse Hash',)),
        (add_section_if_missing,        ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n')),
    ],
'4302efb7': [
        (log,                           ('2.8: Harumasa PlayerA LightMap Hash',)),
        (add_section_if_missing,        ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n')),
    ],
'38b0417f': [
        (log,                           ('2.8: Harumasa PlayerA MaterialMap Hash',)),
        (add_section_if_missing,        ('28ddcf0f', 'Harumasa.Player.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures ===
'cc14d492': [
        (log,                           ('2.8: Harumasa Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n')),
    ],
'8d7254c3': [
        (log,                           ('2.8: Harumasa Weapon LightMap Hash',)),
        (add_section_if_missing,        ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n')),
    ],
'cf646184': [
        (log,                           ('2.8: Harumasa Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n')),
    ],

# === Weapon Quiver Textures (v2.8 Target) ===
'c776b2ac': [
        (log,                           ('2.8: Harumasa Quiver Diffuse Hash Part 2',)),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
    ],
'0e38f04c': [
        (log,                           ('2.8: Harumasa Quiver LightMap Hash Part 2',)),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
    ],
'ceb7b1fa': [
        (log,                           ('2.8: Harumasa Quiver MaterialMap Hash Part 2',)),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Harumasa Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9bb92eee', 'Harumasa.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('30f715df', 'Harumasa.WeaponKnife.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b92340c6', 'Harumasa.WeaponKnifeSheath.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fdaa94b9', 'Harumasa.WeaponBow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8ae5340d', 'Harumasa.WeaponArrow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('448ba3f6', 'Harumasa.WeaponQuiver.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4785491b', 'Harumasa.WeaponBowstring.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Harumasa',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}