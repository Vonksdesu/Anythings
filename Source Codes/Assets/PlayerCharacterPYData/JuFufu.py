"""
JuFufu Character Hash Commands
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
    Returns JuFufu's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'a4fd9113': [(log, ('2.8: JuFufu Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'de303163': [(log, ('2.8: JuFufu Body IB Hash',)),                      (add_ib_check_if_missing,)],
'f8ab3141': [(log, ('2.8: JuFufu Tail IB Hash',)),                      (add_ib_check_if_missing,)],
'321768df': [(log, ('2.8: JuFufu Face IB Hash',)),                      (add_ib_check_if_missing,)],
'095f38e8': [(log, ('2.8: JuFufu Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'a27835bb': [(log, ('2.8: JuFufu Weapon Left Claw IB Hash',)),          (add_ib_check_if_missing,)],
'46e339a6': [(log, ('2.8: JuFufu Weapon Right Claw IB Hash',)),         (add_ib_check_if_missing,)],
'b51e30e5': [(log, ('2.8: JuFufu Weapon Tiger Prestige IB Hash',)),     (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'77d02cb1': [(log, ('2.8: JuFufu Hair draw_vb Hash',)),                  (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n'))],
'e836ec8f': [(log, ('2.8: JuFufu Hair position_vb Hash',)),              (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n'))],
'fbca830d': [(log, ('2.8: JuFufu Hair texcoord_vb Hash',)),              (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n'))],
'c9c19a97': [(log, ('2.8: JuFufu Hair blend_vb Hash',)),                 (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'e636c467': [(log, ('2.8: JuFufu Hair Shadow draw_vb Hash',)),           (add_section_if_missing, ('095f38e8', 'JuFufu.HairShadow.IB', 'match_priority = 0\n'))],
'f0e84fef': [(log, ('2.8: JuFufu Hair Shadow position_vb Hash',)),       (add_section_if_missing, ('095f38e8', 'JuFufu.HairShadow.IB', 'match_priority = 0\n'))],
'60d9a4fc': [(log, ('2.8: JuFufu Hair Shadow texcoord_vb Hash',)),       (add_section_if_missing, ('095f38e8', 'JuFufu.HairShadow.IB', 'match_priority = 0\n'))],
'b18001e6': [(log, ('2.8: JuFufu Hair Shadow blend_vb Hash',)),          (add_section_if_missing, ('095f38e8', 'JuFufu.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'5c076ce8': [(log, ('2.8: JuFufu Body draw_vb Hash',)),                  (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n'))],
'00ba64ca': [(log, ('2.8: JuFufu Body position_vb Hash',)),              (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n'))],
'2e086db7': [(log, ('2.8: JuFufu Body texcoord_vb Hash',)),              (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n'))],
'c06c0417': [(log, ('2.8: JuFufu Body blend_vb Hash',)),                 (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n'))],

# Tail
'c84e77d4': [(log, ('2.8: JuFufu Tail draw_vb Hash',)),                  (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n'))],
'c397375f': [(log, ('2.8: JuFufu Tail position_vb Hash',)),              (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n'))],
'9a198bcf': [(log, ('2.8: JuFufu Tail texcoord_vb Hash',)),              (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n'))],
'c8fa66e3': [(log, ('2.8: JuFufu Tail blend_vb Hash',)),                 (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n'))],

# Face
'd7802a0b': [(log, ('2.8: JuFufu Face VertexLimit Hash',)),              (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n'))],
'ed92b94c': [(log, ('2.8: JuFufu Face position_vb Hash',)),              (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n'))],
'8267358b': [(log, ('2.8: JuFufu Face texcoord_vb Hash',)),              (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n'))],
'512615d6': [(log, ('2.8: JuFufu Face blend_vb Hash',)),                 (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n'))],

# Weapon - Left Claw
'303b7a17': [(log, ('2.8: JuFufu Weapon Left Claw VertexLimit',)),       (add_section_if_missing, ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n'))],
'41006dfa': [(log, ('2.8: JuFufu Weapon Left Claw position_vb',)),       (add_section_if_missing, ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n'))],
'ce435978': [(log, ('2.8: JuFufu Weapon Left Claw texcoord_vb',)),       (add_section_if_missing, ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n'))],
'fbb7c2a6': [(log, ('2.8: JuFufu Weapon Left Claw blend_vb',)),          (add_section_if_missing, ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n'))],

# Weapon - Right Claw
'0468fc0c': [(log, ('2.8: JuFufu Weapon Right Claw VertexLimit',)),      (add_section_if_missing, ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n'))],
'45b2b661': [(log, ('2.8: JuFufu Weapon Right Claw position_vb',)),      (add_section_if_missing, ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n'))],
'395481f4': [(log, ('2.8: JuFufu Weapon Right Claw texcoord_vb',)),      (add_section_if_missing, ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n'))],
'18a54256': [(log, ('2.8: JuFufu Weapon Right Claw blend_vb',)),         (add_section_if_missing, ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n'))],

# Weapon - Tiger Prestige
'03768505': [(log, ('2.8: JuFufu Weapon Tiger Prestige VertexLimit',)),  (add_section_if_missing, ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n'))],
'245e6459': [(log, ('2.8: JuFufu Weapon Tiger Prestige position_vb',)),  (add_section_if_missing, ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n'))],
'1544d097': [(log, ('2.8: JuFufu Weapon Tiger Prestige texcoord_vb',)),  (add_section_if_missing, ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n'))],
'7778328f': [(log, ('2.8: JuFufu Weapon Tiger Prestige blend_vb',)),     (add_section_if_missing, ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates ===
'9a93726a': [(log, ('2.0 -> 2.8: JuFufu Claws Diffuse [Legacy]',)),      (update_hash, ('401f92e6',))],
'1738f744': [(log, ('2.0 -> 2.8: JuFufu Claws LightMap [Legacy]',)),     (update_hash, ('1b61ae30',))],
'7d54f20a': [(log, ('2.0 -> 2.8: JuFufu Claws MaterialMap [Legacy]',)),  (update_hash, ('e62eed48',))],
'27928ca3': [(log, ('2.0 -> 2.8: JuFufu Tiger Prestige Diffuse [Legacy]',)), (update_hash, ('094ac0a2',))],
'87e25f7d': [(log, ('2.0 -> 2.8: JuFufu Tiger Prestige LightMap [Legacy]',)), (update_hash, ('4bb30541',))],
'26d6f075': [(log, ('2.0 -> 2.8: JuFufu Tiger Prestige MaterialMap [Legacy]',)), (update_hash, ('9db94a04',))],

# === Face Textures ===
'134fbe43': [
        (log,                           ('2.8: JuFufu Face Diffuse Hash',)),
        (add_section_if_missing,        ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
    ],
'37b277db': [
        (log,                           ('2.8: JuFufu FaceA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair and Tail Shared Textures ===
'521f60ae': [
        (log,                           ('2.8: JuFufu Hair, Tail Diffuse Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'db3bdffa': [
        (log,                           ('2.8: JuFufu HairA, TailA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'29bb13b7': [
        (log,                           ('2.8: JuFufu Hair, Tail LightMap Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'5c948f7b': [
        (log,                           ('2.8: JuFufu HairA, TailA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'9355dcea': [
        (log,                           ('2.8: JuFufu Hair, Tail MaterialMap Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'9f4d4f72': [
        (log,                           ('2.8: JuFufu HairA, TailA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'3b372932': [
        (log,                           ('2.8: JuFufu Body Diffuse Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'16e4cac1': [
        (log,                           ('2.8: JuFufu BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'9d1ab7c4': [
        (log,                           ('2.8: JuFufu Body LightMap Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'c952431f': [
        (log,                           ('2.8: JuFufu BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'f72af17c': [
        (log,                           ('2.8: JuFufu Body MaterialMap Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'd555b4f8': [
        (log,                           ('2.8: JuFufu BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Left/Right Claws Shared Textures (v2.8 Target) ===
'401f92e6': [
        (log,                           ('2.8: JuFufu Claws Diffuse Hash',)),
        (add_section_if_missing,        ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n')),
    ],
'1b61ae30': [
        (log,                           ('2.8: JuFufu Claws LightMap Hash',)),
        (add_section_if_missing,        ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n')),
    ],
'e62eed48': [
        (log,                           ('2.8: JuFufu Claws MaterialMap Hash',)),
        (add_section_if_missing,        ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n')),
    ],

# === Weapon Tiger Prestige Textures (v2.8 Target) ===
'094ac0a2': [
        (log,                           ('2.8: JuFufu Tiger Prestige Diffuse Hash',)),
        (add_section_if_missing,        ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n')),
    ],
'4bb30541': [
        (log,                           ('2.8: JuFufu Tiger Prestige LightMap Hash',)),
        (add_section_if_missing,        ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n')),
    ],
'9db94a04': [
        (log,                           ('2.8: JuFufu Tiger Prestige MaterialMap Hash',)),
        (add_section_if_missing,        ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n')),
    ],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('2.8: JuFufu Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('095f38e8', 'JuFufu.HairShadow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a27835bb', 'JuFufu.LeftClaw.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('46e339a6', 'JuFufu.RightClaw.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b51e30e5', 'JuFufu.TigerPrestige.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: JuFufu Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JuFufu',
    'game_versions': ['2.8', '3.0'],
}