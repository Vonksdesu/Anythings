"""
Koleda Character Hash Commands
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
    Returns Koleda's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'242a8d48': [(log, ('2.8: Koleda Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'3afb3865': [(log, ('2.8: Koleda Body IB Hash',)),                      (add_ib_check_if_missing,)],
'0e74656e': [(log, ('2.8: Koleda Head IB Hash',)),                      (add_ib_check_if_missing,)],
'67230c9f': [(log, ('2.8: Koleda Hair Shadow IB Hash',)),               (add_ib_check_if_missing,)],
'2f2167a0': [(log, ('2.8: Koleda Weapon IB Hash',)),                    (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'366e92ac': [(log, ('2.8: Koleda Hair draw_vb',)),                      (add_section_if_missing, ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n'))],
'e5de61e4': [(log, ('2.8: Koleda Hair position_vb',)),                  (add_section_if_missing, ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n'))],
'e35571a9': [(log, ('2.8: Koleda Hair texcoord_vb Hash (v2.8 Target)',)),(add_section_if_missing, ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n'))],
'c6b75898': [(log, ('2.8: Koleda Hair blend_vb',)),                     (add_section_if_missing, ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'231aab5a': [(log, ('2.8: Koleda Hair Shadow draw_vb',)),               (add_section_if_missing, ('67230c9f', 'Koleda.HairShadow.IB', 'match_priority = 0\n'))],
'7c0d67d5': [(log, ('2.8: Koleda Hair Shadow position_vb',)),           (add_section_if_missing, ('67230c9f', 'Koleda.HairShadow.IB', 'match_priority = 0\n'))],
'4a06c423': [(log, ('2.8: Koleda Hair Shadow texcoord_vb',)),           (add_section_if_missing, ('67230c9f', 'Koleda.HairShadow.IB', 'match_priority = 0\n'))],
'2d32c8fd': [(log, ('2.8: Koleda Hair Shadow blend_vb',)),              (add_section_if_missing, ('67230c9f', 'Koleda.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'2c856fbc': [(log, ('2.8: Koleda Body draw_vb',)),                      (add_section_if_missing, ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n'))],
'28b188d4': [(log, ('2.8: Koleda Body position_vb',)),                  (add_section_if_missing, ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n'))],
'38b31082': [(log, ('2.8: Koleda Body texcoord_vb Hash (v2.8 Target)',)),(add_section_if_missing, ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n'))],
'ad8e1d95': [(log, ('2.8: Koleda Body blend_vb',)),                     (add_section_if_missing, ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n'))],

# Face / Head
'78e1fa18': [(log, ('2.8: Koleda Face VertexLimit Hash',)),              (add_section_if_missing, ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n'))],
'42f3695f': [(log, ('2.8: Koleda Face position_vb Hash',)),              (add_section_if_missing, ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n'))],
'f41b27e6': [(log, ('2.8: Koleda Face texcoord_vb Hash',)),              (add_section_if_missing, ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n'))],
'cd9babc2': [(log, ('2.8: Koleda Face blend_vb Hash',)),                 (add_section_if_missing, ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n'))],

# Weapon
'e22c571d': [(log, ('2.8: Koleda Weapon VertexLimit Hash',)),            (add_section_if_missing, ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n'))],
'897140f5': [(log, ('2.8: Koleda Weapon position_vb Hash',)),            (add_section_if_missing, ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n'))],
'6d2ee590': [(log, ('2.8: Koleda Weapon texcoord_vb Hash',)),            (add_section_if_missing, ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n'))],
'5ef33d0a': [(log, ('2.8: Koleda Weapon blend_vb Hash',)),               (add_section_if_missing, ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Remapping ===
'1a9b182a': [
        (log,            ('1.2 -> 1.3: Koleda Hair Texcoord Hash',)),
        (update_hash,    ('e35571a9',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '13_koleda_hair',
            ('4B','2e','2f','2e'),
            ('4B','2f','2f','2f')
        )),
    ],
'e3021a32': [
        (log,            ('1.2 -> 1.3: Koleda Body Texcoord Hash',)),
        (update_hash,    ('38b31082',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '13_koleda_body',
            ('4B','2e','2f','2e'),
            ('4B','2f','2f','2f')
        )),
    ],

# === Legacy Weapon Updates ===
'1fe2b399': [(log, ('2.0 -> 2.8: Koleda Weapon Diffuse [Legacy]',)), (update_hash, ('9ccded50',))],
'1da699e7': [(log, ('2.0 -> 2.8: Koleda Weapon LightMap [Legacy]',)), (update_hash, ('0c993237',))],
'12f1688d': [(log, ('2.0 -> 2.8: Koleda Weapon MaterialMap [Legacy]',)), (update_hash, ('af1fbaa3',))],

# === Face Textures ===
'f1045670': [
        (log,                           ('2.8: Koleda HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('200db5c4', 'Koleda.HeadA.Diffuse.2048')),
    ],
'200db5c4': [
        (log,                           ('2.8: Koleda HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('0e74656e', 'Koleda.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f1045670', 'Koleda.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'e8e89f00': [
        (log,                           ('2.8: Koleda HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b0046e5a', 'Koleda.HairA.Diffuse.1024')),
    ],
'b0046e5a': [
        (log,                           ('2.8: Koleda HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e8e89f00', 'Koleda.HairA.Diffuse.2048')),
    ],
'1b33709a': [
        (log,                           ('2.8: Koleda Hair LightMap Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
    ],
'8042506d': [
        (log,                           ('2.8: Koleda HairA LightMap 2048p Hash [Legacy]',)),
        (update_hash,                   ('a451ca03',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('144ab293', 'Koleda.HairA.LightMap.1024')),
    ],
'a451ca03': [
        (log,                           ('2.8: Koleda HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('144ab293', 'Koleda.HairA.LightMap.1024')),
    ],
'144ab293': [
        (log,                           ('2.8: Koleda HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a451ca03', 'Koleda.HairA.LightMap.2048')),
    ],
'058d85b5': [
        (log,                           ('2.8: Koleda HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'337fd6a2': [
        (log,                           ('2.8: Koleda BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ce10237d', 'Koleda.BodyA.Diffuse.1024')),
    ],
'ce10237d': [
        (log,                           ('2.8: Koleda BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('337fd6a2', 'Koleda.BodyA.Diffuse.2048')),
    ],
'78e0f9f5': [
        (log,                           ('2.8: Koleda BodyA LightMap 2048p Hash [Legacy]',)),
        (update_hash,                   ('7c1bce32',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('db58787e', 'Koleda.BodyA.LightMap.1024')),
    ],
'7c1bce32': [
        (log,                           ('2.8: Koleda BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('db58787e', 'Koleda.BodyA.LightMap.1024')),
    ],
'db58787e': [
        (log,                           ('2.8: Koleda BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7c1bce32', 'Koleda.BodyA.LightMap.2048')),
    ],
'a1087d61': [
        (log,                           ('2.8: Koleda Body LightMap Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
    ],
'6f34885f': [
        (log,                           ('2.8: Koleda BodyA MaterialMap 2048p Hash [Legacy]',)),
        (update_hash,                   ('b60ace0c',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('02e6cb95', 'Koleda.BodyA.MaterialMap.1024')),
    ],
'b60ace0c': [
        (log,                           ('2.8: Koleda BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('02e6cb95', 'Koleda.BodyA.MaterialMap.1024')),
    ],
'02e6cb95': [
        (log,                           ('2.8: Koleda BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b60ace0c', 'Koleda.BodyA.MaterialMap.2048')),
    ],
'1c162e9c': [
        (log,                           ('2.8: Koleda Body MaterialMap Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'9ccded50': [
        (log,                           ('2.8: Koleda Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n')),
    ],
'0c993237': [
        (log,                           ('2.8: Koleda Weapon LightMap Hash',)),
        (add_section_if_missing,        ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n')),
    ],
'af1fbaa3': [
        (log,                           ('2.8: Koleda Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Koleda Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2f2167a0', 'Koleda.Weapon.IB', 'match_priority = 0\n')),
    ],
'd1aac666': [
        (log,                           ('2.8: Koleda HairA NormalMap 2048p Hash [Legacy]',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7a46b52a', 'Koleda.HairA.NormalMap.1024')),
    ],
'ebac056e': [
        (log,                           ('2.8: Koleda Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7a46b52a', 'Koleda.HairA.NormalMap.1024')),
    ],
'7a46b52a': [
        (log,                           ('2.8: Koleda HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Koleda.HairA.NormalMap.2048')),
    ],
'e71d134f': [
        (log,                           ('2.8: Koleda BodyA NormalMap 2048p Hash [Legacy]',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0914d3d3', 'Koleda.BodyA.NormalMap.1024')),
    ],
'0914d3d3': [
        (log,                           ('2.8: Koleda BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Koleda.BodyA.NormalMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Koleda',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}