"""
Pyrois Character Hash Commands
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
    Returns Pyrois's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'd98c8923': [(log, ('3.0: Pyrois Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'd347d859': [(log, ('3.0: Pyrois Body IB Hash',)),                      (add_ib_check_if_missing,)],
'0a7c1023': [(log, ('3.0: Pyrois Arm IB Hash',)),                       (add_ib_check_if_missing,)],
'585b0241': [(log, ('3.0: Pyrois Sword IB Hash',)),                     (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'6204c171': [(log, ('3.0: Pyrois Hair draw_vb',)),                      (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n'))],
'7fdd4865': [(log, ('3.0: Pyrois Hair position_vb',)),                  (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n'))],
'764bcab3': [(log, ('3.0: Pyrois Hair texcoord_vb',)),                  (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n'))],
'b502aa23': [(log, ('3.0: Pyrois Hair blend_vb',)),                     (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n'))],

# Body
'5bbaca72': [(log, ('3.0: Pyrois Body draw_vb',)),                      (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n'))],
'c1f14931': [(log, ('3.0: Pyrois Body position_vb',)),                  (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n'))],
'337fe1ee': [(log, ('3.0: Pyrois Body texcoord_vb',)),                  (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n'))],
'789800b3': [(log, ('3.0: Pyrois Body blend_vb',)),                     (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n'))],

# Arm
'8e155d0d': [(log, ('3.0: Pyrois Arm draw_vb',)),                       (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n'))],
'a816b4ec': [(log, ('3.0: Pyrois Arm position_vb',)),                   (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n'))],
'1abe00b9': [(log, ('3.0: Pyrois Arm texcoord_vb',)),                   (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n'))],
'a946c036': [(log, ('3.0: Pyrois Arm blend_vb',)),                      (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n'))],

# Sword
'c942b027': [(log, ('3.0: Pyrois Sword draw_vb',)),                     (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n'))],
'899ea8ea': [(log, ('3.0: Pyrois Sword position_vb',)),                 (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n'))],
'bc7a3429': [(log, ('3.0: Pyrois Sword texcoord_vb',)),                 (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n'))],
'd51ce897': [(log, ('3.0: Pyrois Sword blend_vb',)),                    (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n'))],

# === Hair Textures ===
'28b3c245': [
        (log,                           ('3.0: Pyrois Hair Diffuse Hash',)),
        (add_section_if_missing,        ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'0d24e396': [
        (log,                           ('3.0: Pyrois Hair LightMap Hash',)),
        (add_section_if_missing,        ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'bd5b0984': [
        (log,                           ('3.0: Pyrois Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body & Arm Shared Textures ===
'ef11e537': [
        (log,                           ('3.0: Pyrois Body, Arm Diffuse Hash',)),
        (add_section_if_missing,        ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],
'c7a6063b': [
        (log,                           ('3.0: Pyrois Body, Arm LightMap Hash',)),
        (add_section_if_missing,        ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],
'd81be7b3': [
        (log,                           ('3.0: Pyrois Body, Arm MaterialMap Hash',)),
        (add_section_if_missing,        ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],

# === Sword Textures ===
'bda9d364': [
        (log,                           ('3.0: Pyrois Sword Diffuse Hash',)),
        (add_section_if_missing,        ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'6bc7e6b2': [
        (log,                           ('3.0: Pyrois Sword LightMap Hash',)),
        (add_section_if_missing,        ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'a71b1a4a': [
        (log,                           ('3.0: Pyrois Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: Pyrois Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: Pyrois Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pyrois',
    'game_versions': ['3.0'],
}