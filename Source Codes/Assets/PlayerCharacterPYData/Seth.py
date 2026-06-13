"""
Seth Character Hash Commands
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
    Returns Seth's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'35cf83ad': [(log, ('2.8: Seth Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'00172ec3': [(log, ('2.8: Seth Body IB Hash',)),                        (add_ib_check_if_missing,)],
'52f5aa74': [(log, ('2.8: Seth Head IB Hash',)),                        (add_ib_check_if_missing,)],
'52930334': [(log, ('2.8: Seth Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'd15922eb': [(log, ('2.8: Seth Shield IB Hash',)),                      (add_ib_check_if_missing,)],
'713b2a30': [(log, ('2.8: Seth Stick IB Hash',)),                       (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'd18b1600': [(log, ('2.8: Seth Hair draw_vb',)),                        (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n'))],
'9b358a6b': [(log, ('2.8: Seth Hair position_vb',)),                    (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n'))],
'a91eeef2': [(log, ('2.8: Seth Hair texcoord_vb',)),                    (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n'))],
'df779976': [(log, ('2.8: Seth Hair blend_vb',)),                       (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow
'2719bad1': [(log, ('2.8: Seth Hair Shadow draw_vb',)),                 (add_section_if_missing, ('52930334', 'Seth.HairShadow.IB', 'match_priority = 0\n'))],
'ab8a95a3': [(log, ('2.8: Seth Hair Shadow position_vb',)),             (add_section_if_missing, ('52930334', 'Seth.HairShadow.IB', 'match_priority = 0\n'))],
'ca884fde': [(log, ('2.8: Seth Hair Shadow texcoord_vb',)),             (add_section_if_missing, ('52930334', 'Seth.HairShadow.IB', 'match_priority = 0\n'))],
'85cb63a9': [(log, ('2.8: Seth Hair Shadow blend_vb',)),                (add_section_if_missing, ('52930334', 'Seth.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'2e990d11': [(log, ('2.8: Seth Body draw_vb',)),                        (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n'))],
'c5e25439': [(log, ('2.8: Seth Body position_vb',)),                    (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n'))],
'd4837e60': [(log, ('2.8: Seth Body texcoord_vb',)),                    (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n'))],
'b758d72f': [(log, ('2.8: Seth Body blend_vb',)),                       (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n'))],

# Face
'3b7803dd': [(log, ('2.8: Seth Face VertexLimit',)),                    (add_section_if_missing, ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n'))],
'016a909a': [(log, ('2.8: Seth Face position_vb',)),                    (add_section_if_missing, ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n'))],
'bff3e0b3': [(log, ('2.8: Seth Face texcoord_vb',)),                    (add_section_if_missing, ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n'))],
'9dad4eb7': [(log, ('2.8: Seth Face blend_vb',)),                       (add_section_if_missing, ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n'))],

# Shield Weapon
'4b92cd34': [(log, ('2.8: Seth Shield VertexLimit',)),                  (add_section_if_missing, ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n'))],
'c17c87ba': [(log, ('2.8: Seth Shield position_vb',)),                  (add_section_if_missing, ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n'))],
'bb5022ce': [(log, ('2.8: Seth Shield texcoord_vb',)),                  (add_section_if_missing, ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n'))],
'08a86fef': [(log, ('2.8: Seth Shield blend_vb',)),                     (add_section_if_missing, ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n'))],

# Stick Weapon
'eeea5739': [(log, ('2.8: Seth Stick VertexLimit',)),                    (add_section_if_missing, ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n'))],
'2c38f2c4': [(log, ('2.8: Seth Stick position_vb',)),                    (add_section_if_missing, ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n'))],
'0acdbd8c': [(log, ('2.8: Seth Stick texcoord_vb',)),                    (add_section_if_missing, ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n'))],
'd537bc36': [(log, ('2.8: Seth Stick blend_vb',)),                       (add_section_if_missing, ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n'))],

# === Texcoord Remap ===
'a72f760f': [
        (log,            ('2.8: Seth Hair Texcoord Hash (Old)',)),
        (update_hash,    ('a91eeef2',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '14_Seth_Hair',
            ('4f','2e','2f','2e'),
            ('4B','2e','2f','2e')
        )),
    ],

# === Legacy Hash Updates ===
'c6131117': [(log, ('2.0 -> 2.8: Seth Shield & Stick Diffuse [Legacy]',)), (update_hash, ('c5f5e59c',))],
'2f2525f7': [(log, ('2.0 -> 2.8: Seth Shield & Stick LightMap [Legacy]',)), (update_hash, ('47016fd0',))],
'36d4290d': [(log, ('2.0 -> 2.8: Seth Shield & Stick MaterialMap [Legacy]',)), (update_hash, ('4e10eb19',))],

# === Face Textures ===
'fe5b7534': [
        (log,                           ('2.8: Seth HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('09981aff', 'Seth.HeadA.Diffuse.2048')),
    ],
'09981aff': [
        (log,                           ('2.8: Seth HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fe5b7534', 'Seth.HeadA.Diffuse.1024')),
    ],

# === Hair Textures ===
'dc8e244d': [
        (log,                           ('2.8: Seth HairA Diffuse 2048p Hash (Old)',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d3756c37', 'Seth.HairA.Diffuse.1024')),
    ],
'd3756c37': [
        (log,                           ('2.8: Seth HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc8e244d', 'Seth.HairA.Diffuse.2048')),
    ],
'd4de9ec1': [
        (log,                           ('2.8: Seth HairA LightMap 2048p Hash (Old)',)),
        (update_hash,                   ('a855884d',)),
    ],
'c01dbf6c': [
        (log,                           ('2.8: Seth HairA LightMap 1024p Hash (Old)',)),
        (update_hash,                   ('a855884d',)),
    ],
'3c256565': [
        (log,                           ('2.8: Seth HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('833e9405', 'Seth.HairA.MaterialMap.1024')),
    ],
'833e9405': [
        (log,                           ('2.8: Seth HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3c256565', 'Seth.HairA.MaterialMap.2048')),
    ],
'3376b58c': [
        (log,                           ('2.8: Seth HairA NormalMap 2048p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'24d52dd8': [
        (log,                           ('2.8: Seth HairA NormalMap 1024p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],

# === Body Textures ===
'7f8416ab': [
        (log,                           ('2.8: Seth BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dbc90150', 'Seth.BodyA.Diffuse.1024')),
    ],
'dbc90150': [
        (log,                           ('2.8: Seth BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7f8416ab', 'Seth.BodyA.Diffuse.2048')),
    ],
'3d97c2ef': [
        (log,                           ('2.8: Seth BodyA LightMap 2048p Hash (Old)',)),
        (update_hash,                   ('5b205468',)),
    ],
'9436aa83': [
        (log,                           ('2.8: Seth BodyA LightMap 1024p Hash (Old)',)),
        (update_hash,                   ('5b205468',)),
    ],
'732d3f81': [
        (log,                           ('2.8: Seth BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('56775fcb', 'Seth.BodyA.MaterialMap.1024')),
    ],
'56775fcb': [
        (log,                           ('2.8: Seth BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('732d3f81', 'Seth.BodyA.MaterialMap.2048')),
    ],
'dde45d3d': [
        (log,                           ('2.8: Seth BodyA NormalMap 2048p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'62b047c5': [
        (log,                           ('2.8: Seth BodyA NormalMap 1024p Hash (Old)',)),
        (update_hash,                   ('ebac056e',)),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Seth Shared NormalMap Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: Seth Shared NormalMap Hash (Hair & Body) [Legacy]',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],

# === Light Map ===
'ca070fa7': [
        (log,                           ('2.8: Seth Hair LightMap Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'a855884d': [
        (log,                           ('2.8: Seth HairA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'57cf813c': [
        (log,                           ('2.8: Seth Body LightMap Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'5b205468': [
        (log,                           ('2.8: Seth BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon Textures (v2.8 Target) ===
'c5f5e59c': [
        (log,                           ('2.8: Seth Shield & Stick Diffuse Hash',)),
        (add_section_if_missing,        ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n')),
    ],
'47016fd0': [
        (log,                           ('2.8: Seth Shield & Stick LightMap Hash',)),
        (add_section_if_missing,        ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n')),
    ],
'4e10eb19': [
        (log,                           ('2.8: Seth Shield & Stick MaterialMap Hash',)),
        (add_section_if_missing,        ('d15922eb', 'Seth.Shield.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('713b2a30', 'Seth.Stick.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seth',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8'],
}