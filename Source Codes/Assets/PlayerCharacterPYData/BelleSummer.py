"""
BelleSummer Character Hash Commands
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
    Returns BelleSummer's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'43ed3c22': [(log, ('2.8 -> 3.0: BelleSummer Body IB Hash [Legacy]',)), (update_hash, ('619c5c94',))],
'69148073': [(log, ('2.8: BelleSummer Top IB Hash',)),                  (add_ib_check_if_missing,)],
'93f38bdd': [(log, ('2.8: BelleSummer Hat IB Hash',)),                  (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.8: BelleSummer Face IB Hash',)),                 (add_ib_check_if_missing,)],
'ea055cac': [(log, ('2.8 -> 3.0: BelleSummer Hair IB Hash [Legacy]',)), (update_hash, ('a7683988',))],
'fba5908c': [(log, ('2.8 -> 3.0: BelleSummer Hair Shadow IB Hash [Legacy]',)), (update_hash, ('403eace9',))],

# === IB Hashes (v3.0 Target) ===
'a7683988': [(log, ('3.0: BelleSummer Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'403eace9': [(log, ('3.0: BelleSummer Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'07920753': [(log, ('3.0: BelleSummer EarPendant IB Hash',)),           (add_ib_check_if_missing,)],
'3acf9aea': [(log, ('3.0: BelleSummer HairPin IB Hash',)),              (add_ib_check_if_missing,)],
'619c5c94': [(log, ('3.0: BelleSummer Body IB Hash',)),                 (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'ff8f2723': [(log, ('2.8 -> 3.0: BelleSummer Hair draw_vb [Legacy]',)), (update_hash, ('898f40fc',))],
'f0740488': [(log, ('2.8 -> 3.0: BelleSummer Hair position_vb [Legacy]',)), (update_hash, ('d440bcc9',))],
'af566e38': [(log, ('2.8 -> 3.0: BelleSummer Hair texcoord_vb [Legacy]',)), (update_hash, ('b536d9e6',))],
'8823a09a': [(log, ('2.8 -> 3.0: BelleSummer Hair blend_vb [Legacy]',)), (update_hash, ('4bb8fccc',))],

# Hair Shadow
'8c70a1df': [(log, ('2.8 -> 3.0: BelleSummer Hair Shadow draw_vb [Legacy]',)), (update_hash, ('d077170c',))],
'f98fb7ca': [(log, ('2.8 -> 3.0: BelleSummer Hair Shadow position_vb [Legacy]',)), (update_hash, ('f2298f2e',))],
'ddf97ec8': [(log, ('2.8 -> 3.0: BelleSummer Hair Shadow texcoord_vb [Legacy]',)), (update_hash, ('43f15315',))],
'0fba192e': [(log, ('2.8 -> 3.0: BelleSummer Hair Shadow blend_vb [Legacy]',)), (update_hash, ('288df448',))],

# Hat
'bd2cf1bc': [(log, ('2.8: BelleSummer Hat draw_vb',)),                  (add_section_if_missing, ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n'))],
'c6b1cd55': [(log, ('2.8: BelleSummer Hat position_vb',)),              (add_section_if_missing, ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n'))],
'a8b3bbab': [(log, ('2.8: BelleSummer Hat texcoord_vb',)),              (add_section_if_missing, ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n'))],
'b7061769': [(log, ('2.8: BelleSummer Hat blend_vb',)),                 (add_section_if_missing, ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n'))],

# Body
'2ceb44ef': [(log, ('2.8 -> 3.0: BelleSummer Body draw_vb [Legacy]',)), (update_hash, ('051d5424',))],
'537d9b9b': [(log, ('2.8 -> 3.0: BelleSummer Body position_vb [Legacy]',)), (update_hash, ('b95ddd01',))],
'f5e62ded': [(log, ('2.8 -> 3.0: BelleSummer Body texcoord_vb [Legacy]',)), (update_hash, ('91cdde70',))],
'4f3ddd5c': [(log, ('2.8 -> 3.0: BelleSummer Body blend_vb [Legacy]',)), (update_hash, ('b36f6834',))],

# Tshirt
'a1de68c0': [(log, ('2.8: BelleSummer Tshirt draw_vb',)),               (add_section_if_missing, ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n'))],
'324d9d21': [(log, ('2.8: BelleSummer Tshirt position_vb',)),           (add_section_if_missing, ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n'))],
'881514bf': [(log, ('2.8 -> 3.0: BelleSummer Tshirt texcoord_vb [Legacy]',)), (update_hash, ('325b4a1c',))],
'0139f7e8': [(log, ('2.8 -> 3.0: BelleSummer Tshirt blend_vb [Legacy]',)), (update_hash, ('0a00d846',))],

# Face
'04abceb5': [(log, ('2.8: BelleSummer Face draw_vb',)),                 (add_section_if_missing, ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('2.8: BelleSummer Face position_vb',)),             (add_section_if_missing, ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n'))],
'0c9a075b': [(log, ('2.8 -> 3.0: BelleSummer Face blend_vb [Legacy]',)), (update_hash, ('359e4502',))],

# === 3.0 Database Updates (Strict Sync) ===
# Hair VBs
'898f40fc': [(log, ('3.0: BelleSummer Hair draw_vb',)),                 (add_section_if_missing, ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],
'd440bcc9': [(log, ('3.0: BelleSummer Hair position_vb',)),             (add_section_if_missing, ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],
'b536d9e6': [(log, ('3.0: BelleSummer Hair texcoord_vb',)),             (add_section_if_missing, ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],
'4bb8fccc': [(log, ('3.0: BelleSummer Hair blend_vb',)),                (add_section_if_missing, ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow VBs
'd077170c': [(log, ('3.0: BelleSummer Hair Shadow draw_vb',)),          (add_section_if_missing, ('403eace9', 'BelleSummer.HairShadow.IB', 'match_priority = 0\n'))],
'f2298f2e': [(log, ('3.0: BelleSummer Hair Shadow position_vb',)),      (add_section_if_missing, ('403eace9', 'BelleSummer.HairShadow.IB', 'match_priority = 0\n'))],
'43f15315': [(log, ('3.0: BelleSummer Hair Shadow texcoord_vb',)),      (add_section_if_missing, ('403eace9', 'BelleSummer.HairShadow.IB', 'match_priority = 0\n'))],
'288df448': [(log, ('3.0: BelleSummer Hair Shadow blend_vb',)),         (add_section_if_missing, ('403eace9', 'BelleSummer.HairShadow.IB', 'match_priority = 0\n'))],

# EarPendant VBs
'c4e3b1e8': [(log, ('3.0: BelleSummer EarPendant draw_vb',)),           (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
'66a4bab6': [(log, ('3.0: BelleSummer EarPendant position_vb',)),       (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
'a2ee3518': [(log, ('3.0: BelleSummer EarPendant texcoord_vb',)),       (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
'28720ee7': [(log, ('3.0: BelleSummer EarPendant blend_vb',)),          (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],

# HairPin VBs
'84a9dfca': [(log, ('3.0: BelleSummer HairPin draw_vb',)),              (add_section_if_missing, ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n'))],
'a678dff4': [(log, ('3.0: BelleSummer HairPin position_vb',)),          (add_section_if_missing, ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n'))],
'1196668a': [(log, ('3.0: BelleSummer HairPin texcoord_vb',)),          (add_section_if_missing, ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n'))],
'6e583c52': [(log, ('3.0: BelleSummer HairPin blend_vb',)),             (add_section_if_missing, ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n'))],

# Body VBs
'051d5424': [(log, ('3.0: BelleSummer Body draw_vb',)),                 (add_section_if_missing, ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n'))],
'b95ddd01': [(log, ('3.0: BelleSummer Body position_vb',)),             (add_section_if_missing, ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n'))],
'91cdde70': [(log, ('3.0: BelleSummer Body texcoord_vb',)),             (add_section_if_missing, ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n'))],
'b36f6834': [(log, ('3.0: BelleSummer Body blend_vb',)),                (add_section_if_missing, ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n'))],

# Tshirt VBs
'325b4a1c': [(log, ('3.0: BelleSummer Tshirt texcoord_vb',)),           (add_section_if_missing, ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n'))],
'0a00d846': [(log, ('3.0: BelleSummer Tshirt blend_vb',)),              (add_section_if_missing, ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n'))],

# Face VBs
'359e4502': [(log, ('3.0: BelleSummer Face blend_vb',)),                (add_section_if_missing, ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'75ec3614': [
        (log,                           ('2.8: BelleSummer FaceA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],
'77eef7e8': [
        (log,                           ('2.8: BelleSummer Face Diffuse Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8 -> 3.0: BelleSummer Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],

# === Hair, Top, Hat Shared Textures ===
'afe23695': [
        (log,                           ('2.8: BelleSummer Hair, Top, Hat Diffuse Hash',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
    ],
'20954729': [
        (log,                           ('2.8 -> 3.0: BelleSummer HairA, TopA, HatA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8 -> 3.0: BelleSummer HairA, TopA, HatA NormalMap Hash (Shared) [Legacy]',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
'60250d24': [
        (log,                           ('3.0: BelleSummer Hair, Top, Hat, Body LightMap Hash',)),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'e0a86379': [
        (log,                           ('2.8 -> 3.0: BelleSummer HairA, TopA, HatA LightMap Hash (Shared) [Legacy]',)),
        (update_hash,                   ('60250d24',)),
    ],
'a189eccd': [
        (log,                           ('2.8 -> 3.0: BelleSummer Hair, Top, Hat LightMap Hash [Legacy]',)),
        (update_hash,                   ('60250d24',)),
    ],
'fbaaeb92': [
        (log,                           ('2.8: BelleSummer Hair, Top, Hat MaterialMap Hash',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
    ],
'0298fba2': [
        (log,                           ('2.8: BelleSummer HairA, TopA, HatA, FaceA MaterialMap Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification C) ===
'b9c7f71b': [
        (log,                           ('2.8: BelleSummer BodyC Diffuse Hash 2048p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'24639b77': [
        (log,                           ('2.8: BelleSummer BodyC Diffuse Hash 1024p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'a4d3687d': [
        (log,                           ('2.8: BelleSummer BodyC LightMap Hash 2048p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'7947679c': [
        (log,                           ('2.8: BelleSummer BodyC LightMap Hash 1024p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'b1abe877': [
        (log,                           ('2.8: BelleSummer BodyC MaterialMap Hash 2048p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'33f28c6d': [
        (log,                           ('2.8: BelleSummer BodyC MaterialMap Hash 1024p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification D) ===
'08f04d95': [
        (log,                           ('2.8: BelleSummer BodyD Diffuse Hash 2048p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'1ce58567': [
        (log,                           ('2.8 -> 3.0: BelleSummer BodyD / Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
'f44f330b': [
        (log,                           ('2.8: BelleSummer BodyD LightMap Hash 2048p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log,                           ('2.8 -> 3.0: BelleSummer BodyD / Accessories LightMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
'7542ef4b': [
        (log,                           ('2.8: BelleSummer BodyD MaterialMap Hash 2048p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log,                           ('2.8 -> 3.0: BelleSummer BodyD / Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleSummer',
    'game_versions': ['2.8', '3.0'],
}