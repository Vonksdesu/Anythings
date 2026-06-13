"""
YeShunguangSwordUlt Character Hash Commands
ZZZ Mod Fixer v2.5 / v2.8
Pembaruan Database 2.8 oleh AI & Komunitas
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YeShunguangSwordUlt's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'dd46b065': [(log, ('2.5: YeShunguangSwordUlt Sword IB Hash',)),         (add_ib_check_if_missing,)],

# === NormalMap ===
'8842671b': [
        (log,                           ('2.5: YeShunguangSwordUlt Sword NormalMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.NormalMap', 'match_priority = 0\n')),
    ],

# === Sword Textures ===
'512d9f71': [
        (log,                           ('2.5: YeShunguangSwordUlt SwordA Diffuse Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'd87a1e13': [
        (log,                           ('2.5: YeShunguangSwordUlt SwordA LightMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'ce96ea2f': [
        (log,                           ('2.5: YeShunguangSwordUlt SwordA MaterialMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'694ac591': [
        (log,                           ('2.5: YeShunguangSwordUlt SwordA CoolExtra Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],
'2ed1817d': [
        (log,                           ('2.5: YeShunguangSwordUlt SwordA EffectMap Hash',)),
        (add_section_if_missing,        ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# Target Model Vertex / Position / TexCoord / Blend Hashes (v2.8)
'3a44ca69': [(log, ('2.8: YeShunguangSwordUlt Sword draw_vb',)), (add_section_if_missing, ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n'))],
'724d29ad': [(log, ('2.8: YeShunguangSwordUlt Sword position_vb',)), (add_section_if_missing, ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n'))],
'2c36b1a8': [(log, ('2.8: YeShunguangSwordUlt Sword texcoord_vb',)), (add_section_if_missing, ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n'))],
'2e3a5c01': [(log, ('2.8: YeShunguangSwordUlt Sword blend_vb',)), (add_section_if_missing, ('dd46b065', 'YeShunguangSwordUlt.Sword.IB', 'match_priority = 0\n'))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangSwordUlt',
    'game_versions': ['2.5', '2.8'],
}