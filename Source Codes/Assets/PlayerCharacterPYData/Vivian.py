"""
Vivian Character Hash Commands
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
    Returns Vivian's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'c4eb6168': [(log, ('2.8: Vivian Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'cd609d98': [(log, ('2.8: Vivian Body IB Hash',)),                      (add_ib_check_if_missing,)],
'14602a61': [(log, ('2.8: Vivian Gem IB Hash',)),                       (add_ib_check_if_missing,)],
'39944f20': [(log, ('2.8: Vivian Face IB Hash',)),                      (add_ib_check_if_missing,)],
'548f7dff': [(log, ('2.8: Vivian Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'1b843cb1': [(log, ('2.8: Vivian Weapon Umbrella Expanded IB Hash',)),  (add_ib_check_if_missing,)],
'7232ac6f': [(log, ('2.8: Vivian Weapon Umbrella Folded IB Hash',)),    (add_ib_check_if_missing,)],
'28f8090e': [(log, ('2.8: Vivian Weapon Umbrella Face IB Hash',)),      (add_ib_check_if_missing,)],
'a031575e': [(log, ('2.8: Vivian Weapon Sword IB Hash',)),              (add_ib_check_if_missing,)],
'e69dfc8c': [(log, ('2.8: Vivian Weapon Thruster IB Hash',)),           (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'2e01f7f7': [(log, ('2.8: Vivian Hair draw_vb',)),                      (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n'))],
'71d0dfd9': [(log, ('2.8: Vivian Hair position_vb',)),                  (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n'))],
'406beb54': [(log, ('2.8: Vivian Hair texcoord_vb',)),                  (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n'))],
'ef4a8bb6': [(log, ('2.8: Vivian Hair blend_vb',)),                     (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'b1bf0e1a': [(log, ('2.8: Vivian Hair Shadow draw_vb',)),               (add_section_if_missing, ('548f7dff', 'Vivian.HairShadow.IB', 'match_priority = 0\n'))],
'a544d14e': [(log, ('2.8: Vivian Hair Shadow position_vb',)),           (add_section_if_missing, ('548f7dff', 'Vivian.HairShadow.IB', 'match_priority = 0\n'))],
'4a5054ba': [(log, ('2.8: Vivian Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('548f7dff', 'Vivian.HairShadow.IB', 'match_priority = 0\n'))],
'2376d129': [(log, ('2.8: Vivian Hair Shadow blend_vb',)),              (add_section_if_missing, ('548f7dff', 'Vivian.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'5c34690a': [(log, ('2.8: Vivian Body draw_vb',)),                      (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n'))],
'64a6b06d': [(log, ('2.8: Vivian Body position_vb',)),                  (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n'))],
'55dae493': [(log, ('2.8: Vivian Body texcoord_vb',)),                  (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n'))],
'e7122fe8': [(log, ('2.8: Vivian Body blend_vb',)),                     (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n'))],

# Gem
'8a6fd2f9': [(log, ('2.8: Vivian Gem draw_vb',)),                       (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n'))],
'3c32547b': [(log, ('2.8: Vivian Gem position_vb',)),                   (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n'))],
'45c0ac67': [(log, ('2.8: Vivian Gem texcoord_vb',)),                   (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n'))],
'a23da1ce': [(log, ('2.8: Vivian Gem blend_vb',)),                      (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n'))],

# Face
'fcf74fc0': [(log, ('2.8: Vivian Face VertexLimit',)),                  (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n'))],
'c6e5dc87': [(log, ('2.8: Vivian Face position_vb',)),                  (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n'))],
'0afe5a44': [(log, ('2.8: Vivian Face texcoord_vb',)),                  (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n'))],
'ef07b6f6': [(log, ('2.8: Vivian Face blend_vb',)),                     (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella Handle (Expanded)
'66cc3370': [(log, ('2.8: Vivian Weapon Umbrella Expanded draw_vb',)),   (add_section_if_missing, ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n'))],
'7c80f1d8': [(log, ('2.8: Vivian Weapon Umbrella Expanded position_vb',)), (add_section_if_missing, ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n'))],
'79ee2ea7': [(log, ('2.8: Vivian Weapon Umbrella Expanded texcoord_vb',)), (add_section_if_missing, ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n'))],
'5d4a63ca': [(log, ('2.8: Vivian Weapon Umbrella Expanded blend_vb',)),  (add_section_if_missing, ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella Handle (Folded)
'56ccb629': [(log, ('2.8: Vivian Weapon Umbrella Folded draw_vb',)),     (add_section_if_missing, ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n'))],
'd06d75e0': [(log, ('2.8: Vivian Weapon Umbrella Folded position_vb',)), (add_section_if_missing, ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n'))],
'2e01f6e0': [(log, ('2.8: Vivian Weapon Umbrella Folded texcoord_vb',)), (add_section_if_missing, ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n'))],
'b24f5c99': [(log, ('2.8: Vivian Weapon Umbrella Folded blend_vb',)),    (add_section_if_missing, ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n'))],

# Weapon - Umbrella Face
'd175e722': [(log, ('2.8: Vivian Weapon Umbrella Face draw_vb',)),       (add_section_if_missing, ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n'))],
'b586b07e': [(log, ('2.8: Vivian Weapon Umbrella Face position_vb',)),   (add_section_if_missing, ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n'))],
'2809e5db': [(log, ('2.8: Vivian Weapon Umbrella Face texcoord_vb',)),   (add_section_if_missing, ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n'))],
'd97d4c96': [(log, ('2.8: Vivian Weapon Umbrella Face blend_vb',)),      (add_section_if_missing, ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n'))],

# Weapon - Sword
'8413730c': [(log, ('2.8: Vivian Weapon Sword draw_vb',)),               (add_section_if_missing, ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n'))],
'cb21ccdf': [(log, ('2.8: Vivian Weapon Sword position_vb',)),           (add_section_if_missing, ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n'))],
'af180e46': [(log, ('2.8: Vivian Weapon Sword texcoord_vb',)),           (add_section_if_missing, ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n'))],
'12f34479': [(log, ('2.8: Vivian Weapon Sword blend_vb',)),              (add_section_if_missing, ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n'))],

# Weapon - Thruster
'cc2d7ad1': [(log, ('2.8: Vivian Weapon Thruster draw_vb',)),            (add_section_if_missing, ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n'))],
'30e3560c': [(log, ('2.8: Vivian Weapon Thruster position_vb',)),        (add_section_if_missing, ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n'))],
'c8ede4d4': [(log, ('2.8: Vivian Weapon Thruster texcoord_vb',)),        (add_section_if_missing, ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n'))],
'15002e84': [(log, ('2.8: Vivian Weapon Thruster blend_vb',)),           (add_section_if_missing, ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'9ec4d65f': [(log, ('1.0 -> 1.1: Vivian Weapon Diffuse 2048p Hash [Legacy]',)),     (update_hash, ('dd8a1851',))],
'756ebf6b': [(log, ('2.0 -> 2.8: Vivian Weapon Diffuse [Legacy]',)), (update_hash, ('e2327fb8',))],
'd96fe324': [(log, ('2.0 -> 2.8: Vivian Weapon LightMap [Legacy]',)), (update_hash, ('9277a2c1',))],
'6af50aef': [(log, ('2.0 -> 2.8: Vivian Weapon MaterialMap [Legacy]',)), (update_hash, ('dd8a1851',))],

# === Face Textures ===
'7b262ab6': [
        (log,                           ('2.8: Vivian FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('66b5da8e', 'Vivian.FaceA.Diffuse.1024')),
    ],
'66b5da8e': [
        (log,                           ('2.8: Vivian FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7b262ab6', 'Vivian.FaceA.Diffuse.2048')),
    ],

# === Hair Textures ===
'a84d933f': [
        (log,                           ('2.8: Vivian HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2df6f7b5', 'Vivian.HairA.Diffuse.1024')),
    ],
'2df6f7b5': [
        (log,                           ('2.8: Vivian HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a84d933f', 'Vivian.HairA.Diffuse.2048')),
    ],
'8e3a20ea': [
        (log,                           ('2.8: Vivian HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('36b80366', 'Vivian.HairA.LightMap.1024')),
    ],
'36b80366': [
        (log,                           ('2.8: Vivian HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8e3a20ea', 'Vivian.HairA.LightMap.2048')),
    ],
'2af66072': [
        (log,                           ('2.8: Vivian HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2d5b1412', 'Vivian.HairA.MaterialMap.1024')),
    ],
'2d5b1412': [
        (log,                           ('2.8: Vivian HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2af66072', 'Vivian.HairA.MaterialMap.2048')),
    ],

# === Body & Gem Textures ===
'0635e2dd': [
        (log,                           ('2.8: Vivian BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da41fbd6', 'Vivian.BodyA.Diffuse.1024')),
    ],
'da41fbd6': [
        (log,                           ('2.8: Vivian BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0635e2dd', 'Vivian.BodyA.Diffuse.2048')),
    ],
'e21c3a6b': [
        (log,                           ('2.8: Vivian BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a86e169', 'Vivian.BodyA.LightMap.1024')),
    ],
'4a86e169': [
        (log,                           ('2.8: Vivian BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e21c3a6b', 'Vivian.BodyA.LightMap.2048')),
    ],
'81f7d37c': [
        (log,                           ('2.8: Vivian BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fa650e6c', 'Vivian.BodyA.MaterialMap.1024')),
    ],
'fa650e6c': [
        (log,                           ('2.8: Vivian BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('81f7d37c', 'Vivian.BodyA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'e2327fb8': [
        (log,                           ('2.8: Vivian Weapon Umbrella Diffuse Hash',)),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],
'9277a2c1': [
        (log,                           ('2.8: Vivian Weapon Umbrella LightMap Hash',)),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],
'dd8a1851': [
        (log,                           ('2.8: Vivian Weapon Umbrella MaterialMap Hash',)),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],

# === Normal Map ===
'798adba3': [
        (log,                           ('2.8: Vivian Shared NormalMap Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],

# === Weapon Shared Textures ===
'bf6a1304': [
        (log,                           ('2.8: Vivian Weapon Umbrella/Sword Diffuse Hash',)),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],
'a33edccd': [
        (log,                           ('2.8: Vivian Weapon Umbrella/Sword LightMap Hash',)),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],
'ab4cde14': [
        (log,                           ('2.8: Vivian Weapon Umbrella/Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('1b843cb1', 'Vivian.WeaponUmbrellaExpanded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7232ac6f', 'Vivian.WeaponUmbrellaFolded.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('28f8090e', 'Vivian.WeaponUmbrellaFace.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a031575e', 'Vivian.WeaponSword.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e69dfc8c', 'Vivian.WeaponThruster.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Vivian',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}