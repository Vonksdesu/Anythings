"""
YeShunguangSword Character Hash Commands
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
    Returns YeShunguangSword's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'93c3c2b7': [(log, ('2.8: YeShunguangSword Sword IB Hash',)),         (add_ib_check_if_missing,)],

# === VB Hashes (v2.8 Target) ===
'f927c4bb': [(log, ('2.8: YeShunguangSword Sword draw_vb',))],
'4dc4764e': [(log, ('2.8: YeShunguangSword Sword position_vb',))],
'c8702180': [(log, ('2.8: YeShunguangSword Sword texcoord_vb',))],
'5783614d': [(log, ('2.8: YeShunguangSword Sword blend_vb',))],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.8: YeShunguangSword Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Sword Textures ===
'7eb1ca38': [
        (log,                           ('2.8: YeShunguangSword SwordA Diffuse Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
'90250152': [
        (log,                           ('2.8: YeShunguangSword SwordA LightMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
'a355e13d': [
        (log,                           ('2.8: YeShunguangSword SwordA MaterialMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
'3304ca16': [
        (log,                           ('2.8: YeShunguangSword SwordA EffectMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangSword',
    'game_versions': ['2.8'],
}   