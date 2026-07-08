# Source-Grounded V2 Language Examples

- Readiness: `usable`
- Alignment links retained: `1686647`
- Aligned V2 row ids: `1137533`
- Selected source cards: `479625`

## Coverage

- `omega`: grounded `1137533` / checked `14523959`; tokens with examples `32` / `32`
- `xi`: grounded `1137533` / checked `14523959`; tokens with examples `18` / `18`
- `alpha`: grounded `1137533` / checked `14523959`; tokens with examples `18` / `18`
- `lambda`: grounded `45553` / checked `4265740`; tokens with examples `18` / `18`
  both-endpoint rate: `0.010678803677673744`
- `tau`: grounded `18562` / checked `250000`; tokens with examples `8` / `8`
  both-endpoint rate: `0.074248`
- `gamma`: grounded `2031` / checked `240000`; tokens with examples `12` / `12`
  both-endpoint rate: `0.0084625`

## Per-Token Cleanliness

### omega

- `Ω00`: links `491713`, cards `222840`, sources `80520`, clean `1.000`, score p50 `0.692`; status {'equation_shape_only': 299719, 'partial_constructor_frame': 190078, 'complete_constructor_frame': 1916}; routes {'unclassified': 383984, 'commutator_incompatibility': 53239, 'boundary_weak_form': 35444, 'constraint_closure': 12808, 'transport_flow': 11883, 'discrete_protocol': 3548, 'spectral_operator': 2794}; flags {'has_relation': 491713, 'has_math_token': 491089, 'logical_relation': 30566, 'chemical_formula_or_reaction': 24286}
- `Ω02`: links `136685`, cards `62511`, sources `28155`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 99863, 'equation_shape_only': 23040, 'complete_constructor_frame': 13782}; routes {'unclassified': 91598, 'commutator_incompatibility': 16895, 'constraint_closure': 14384, 'boundary_weak_form': 10603, 'transport_flow': 8697, 'discrete_protocol': 2429, 'spectral_operator': 1561}; flags {'has_relation': 136685, 'has_math_token': 136474, 'logical_relation': 9608, 'chemical_formula_or_reaction': 8772}
- `Ω01`: links `108681`, cards `45801`, sources `20737`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 67484, 'complete_constructor_frame': 22729, 'equation_shape_only': 18468}; routes {'spectral_operator': 62127, 'unclassified': 30432, 'commutator_incompatibility': 13611, 'constraint_closure': 12434, 'transport_flow': 8522, 'boundary_weak_form': 8049, 'discrete_protocol': 2149}; flags {'has_relation': 108681, 'has_math_token': 108568, 'logical_relation': 5211, 'chemical_formula_or_reaction': 4723}
- `Ω07`: links `96649`, cards `52924`, sources `25393`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 58579, 'equation_shape_only': 37199, 'complete_constructor_frame': 871}; routes {'unclassified': 59052, 'transport_flow': 13771, 'commutator_incompatibility': 13033, 'discrete_protocol': 12141, 'constraint_closure': 7879, 'boundary_weak_form': 6099, 'spectral_operator': 3229}; flags {'has_relation': 96649, 'has_math_token': 96481, 'logical_relation': 6146, 'chemical_formula_or_reaction': 5826}
- `Ω03`: links `96128`, cards `44197`, sources `21365`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 71528, 'equation_shape_only': 23378, 'complete_constructor_frame': 1222}; routes {'unclassified': 74981, 'commutator_incompatibility': 9424, 'boundary_weak_form': 6792, 'transport_flow': 3708, 'constraint_closure': 2369, 'discrete_protocol': 1956, 'spectral_operator': 527}; flags {'has_relation': 96128, 'has_math_token': 96089, 'logical_relation': 4780, 'chemical_formula_or_reaction': 3847}
- `Ω08`: links `94249`, cards `44823`, sources `20107`, clean `1.000`, score p50 `0.700`; status {'partial_constructor_frame': 69222, 'equation_shape_only': 23524, 'complete_constructor_frame': 1503}; routes {'constraint_closure': 56046, 'unclassified': 29553, 'commutator_incompatibility': 11346, 'boundary_weak_form': 6501, 'transport_flow': 3557, 'spectral_operator': 958, 'discrete_protocol': 828}; flags {'has_relation': 94249, 'has_math_token': 94084, 'logical_relation': 5289, 'chemical_formula_or_reaction': 4170}
- `Ω05`: links `90504`, cards `41897`, sources `19322`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 63102, 'equation_shape_only': 19040, 'complete_constructor_frame': 8362}; routes {'transport_flow': 50168, 'unclassified': 29996, 'constraint_closure': 9970, 'commutator_incompatibility': 8813, 'boundary_weak_form': 6579, 'discrete_protocol': 1576, 'spectral_operator': 753}; flags {'has_relation': 90504, 'has_math_token': 90440, 'chemical_formula_or_reaction': 4080, 'logical_relation': 3858}
- `Ω04`: links `90386`, cards `43078`, sources `21233`, clean `1.000`, score p50 `0.643`; status {'partial_constructor_frame': 60728, 'equation_shape_only': 18525, 'complete_constructor_frame': 11133}; routes {'transport_flow': 50564, 'unclassified': 28374, 'commutator_incompatibility': 11516, 'constraint_closure': 8981, 'boundary_weak_form': 8190, 'discrete_protocol': 1745, 'spectral_operator': 1045}; flags {'has_relation': 90386, 'has_math_token': 90332, 'chemical_formula_or_reaction': 4274, 'logical_relation': 4068}
- `Ω06`: links `66691`, cards `29359`, sources `15391`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 44418, 'equation_shape_only': 14443, 'complete_constructor_frame': 7830}; routes {'unclassified': 42826, 'transport_flow': 7872, 'commutator_incompatibility': 6980, 'boundary_weak_form': 6604, 'constraint_closure': 6093, 'discrete_protocol': 1144, 'spectral_operator': 812}; flags {'has_relation': 66691, 'has_math_token': 66626, 'logical_relation': 3026, 'chemical_formula_or_reaction': 2730}
- `Ω11`: links `50672`, cards `21794`, sources `10705`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 37160, 'equation_shape_only': 8733, 'complete_constructor_frame': 4779}; routes {'unclassified': 26919, 'commutator_incompatibility': 9639, 'constraint_closure': 8170, 'transport_flow': 6868, 'boundary_weak_form': 2944, 'spectral_operator': 2442, 'discrete_protocol': 1631}; flags {'has_relation': 50672, 'has_math_token': 50597, 'logical_relation': 3136, 'chemical_formula_or_reaction': 1529}
- `Ω12`: links `39934`, cards `18166`, sources `8959`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 26553, 'equation_shape_only': 8732, 'complete_constructor_frame': 4649}; routes {'unclassified': 27409, 'commutator_incompatibility': 5142, 'transport_flow': 4739, 'boundary_weak_form': 2613, 'constraint_closure': 1291, 'discrete_protocol': 748, 'spectral_operator': 623}; flags {'has_relation': 39934, 'has_math_token': 39873, 'logical_relation': 2911, 'chemical_formula_or_reaction': 2025}
- `Ω13`: links `37339`, cards `18102`, sources `8777`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 25233, 'complete_constructor_frame': 7487, 'equation_shape_only': 4619}; routes {'commutator_incompatibility': 23498, 'constraint_closure': 9550, 'unclassified': 9011, 'transport_flow': 5587, 'boundary_weak_form': 2505, 'discrete_protocol': 1021, 'spectral_operator': 637}; flags {'has_relation': 37339, 'has_math_token': 37286, 'logical_relation': 2599, 'chemical_formula_or_reaction': 1856}

### xi

- `Ξ00`: links `501726`, cards `222139`, sources `76553`, clean `1.000`, score p50 `0.706`; status {'equation_shape_only': 299193, 'partial_constructor_frame': 198999, 'complete_constructor_frame': 3534}; routes {'unclassified': 324610, 'commutator_incompatibility': 67819, 'constraint_closure': 55367, 'transport_flow': 52387, 'spectral_operator': 27642, 'discrete_protocol': 14468, 'boundary_weak_form': 3361}; flags {'has_relation': 501726, 'has_math_token': 501439, 'chemical_formula_or_reaction': 25371, 'logical_relation': 7648}
- `Ξ01`: links `255106`, cards `117101`, sources `50659`, clean `1.000`, score p50 `0.652`; status {'partial_constructor_frame': 176820, 'equation_shape_only': 54577, 'complete_constructor_frame': 23709}; routes {'unclassified': 160757, 'commutator_incompatibility': 35910, 'constraint_closure': 27892, 'transport_flow': 26433, 'spectral_operator': 19294, 'discrete_protocol': 5397, 'boundary_weak_form': 4767}; flags {'has_relation': 255106, 'has_math_token': 255049, 'chemical_formula_or_reaction': 13877, 'logical_relation': 6338}
- `Ξ02`: links `148153`, cards `64572`, sources `28986`, clean `1.000`, score p50 `0.652`; status {'partial_constructor_frame': 98311, 'equation_shape_only': 29305, 'complete_constructor_frame': 20537}; routes {'unclassified': 88893, 'constraint_closure': 25025, 'commutator_incompatibility': 20204, 'transport_flow': 15205, 'spectral_operator': 8111, 'discrete_protocol': 3056, 'boundary_weak_form': 2789}; flags {'has_relation': 148153, 'has_math_token': 147952, 'logical_relation': 7963, 'chemical_formula_or_reaction': 6442}
- `Ξ07`: links `128029`, cards `56925`, sources `25802`, clean `1.000`, score p50 `0.650`; status {'partial_constructor_frame': 91015, 'equation_shape_only': 24376, 'complete_constructor_frame': 12638}; routes {'unclassified': 59697, 'boundary_weak_form': 34984, 'transport_flow': 17530, 'commutator_incompatibility': 14395, 'constraint_closure': 14361, 'spectral_operator': 6824, 'discrete_protocol': 1994}; flags {'has_relation': 128029, 'has_math_token': 127955, 'chemical_formula_or_reaction': 7182, 'logical_relation': 3103}
- `Ξ03`: links `122153`, cards `54867`, sources `25295`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 84080, 'equation_shape_only': 21973, 'complete_constructor_frame': 16100}; routes {'unclassified': 75505, 'commutator_incompatibility': 15431, 'transport_flow': 14829, 'constraint_closure': 12948, 'spectral_operator': 7319, 'boundary_weak_form': 5640, 'discrete_protocol': 2207}; flags {'has_relation': 122153, 'has_math_token': 122015, 'chemical_formula_or_reaction': 6504, 'logical_relation': 6002}
- `Ξ06`: links `110982`, cards `52251`, sources `25363`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 71231, 'equation_shape_only': 22953, 'complete_constructor_frame': 16798}; routes {'transport_flow': 57370, 'unclassified': 37724, 'commutator_incompatibility': 16167, 'constraint_closure': 11722, 'spectral_operator': 6126, 'boundary_weak_form': 4862, 'discrete_protocol': 2214}; flags {'has_relation': 110982, 'has_math_token': 110924, 'chemical_formula_or_reaction': 5479, 'logical_relation': 4352}
- `Ξ04`: links `110614`, cards `51072`, sources `25904`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 74076, 'equation_shape_only': 32909, 'complete_constructor_frame': 3629}; routes {'unclassified': 68149, 'commutator_incompatibility': 20202, 'transport_flow': 10514, 'constraint_closure': 10068, 'spectral_operator': 5758, 'boundary_weak_form': 3827, 'discrete_protocol': 2512}; flags {'has_relation': 110614, 'has_math_token': 109799, 'logical_relation': 44186, 'chemical_formula_or_reaction': 4942}
- `Ξ05`: links `95213`, cards `43832`, sources `20834`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 69288, 'equation_shape_only': 17978, 'complete_constructor_frame': 7947}; routes {'boundary_weak_form': 51628, 'unclassified': 28739, 'transport_flow': 12515, 'commutator_incompatibility': 12393, 'constraint_closure': 9954, 'spectral_operator': 4908, 'discrete_protocol': 1741}; flags {'has_relation': 95213, 'has_math_token': 95123, 'logical_relation': 4452, 'chemical_formula_or_reaction': 4318}
- `Ξ09`: links `47566`, cards `20751`, sources `9043`, clean `1.000`, score p50 `0.692`; status {'partial_constructor_frame': 35884, 'equation_shape_only': 7801, 'complete_constructor_frame': 3881}; routes {'unclassified': 27162, 'commutator_incompatibility': 9954, 'transport_flow': 6287, 'constraint_closure': 5653, 'spectral_operator': 1951, 'discrete_protocol': 1394, 'boundary_weak_form': 1237}; flags {'has_relation': 47566, 'has_math_token': 47519, 'logical_relation': 3055, 'chemical_formula_or_reaction': 1238}
- `Ξ08`: links `39986`, cards `21683`, sources `11363`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 21274, 'equation_shape_only': 15669, 'complete_constructor_frame': 3043}; routes {'unclassified': 25018, 'commutator_incompatibility': 5833, 'constraint_closure': 5037, 'transport_flow': 4382, 'spectral_operator': 1754, 'discrete_protocol': 887, 'boundary_weak_form': 735}; flags {'has_relation': 39986, 'has_math_token': 39862, 'logical_relation': 2823, 'chemical_formula_or_reaction': 2699}
- `Ξ10`: links `39441`, cards `17391`, sources `7907`, clean `1.000`, score p50 `0.682`; status {'partial_constructor_frame': 30448, 'equation_shape_only': 5971, 'complete_constructor_frame': 3022}; routes {'unclassified': 21674, 'constraint_closure': 7815, 'transport_flow': 5716, 'commutator_incompatibility': 4762, 'boundary_weak_form': 2320, 'spectral_operator': 2051, 'discrete_protocol': 816}; flags {'has_relation': 39441, 'has_math_token': 39369, 'logical_relation': 2327, 'chemical_formula_or_reaction': 1395}
- `Ξ11`: links `32823`, cards `13874`, sources `6839`, clean `1.000`, score p50 `0.650`; status {'partial_constructor_frame': 23593, 'equation_shape_only': 7561, 'complete_constructor_frame': 1669}; routes {'unclassified': 19334, 'transport_flow': 4928, 'commutator_incompatibility': 4797, 'constraint_closure': 3542, 'spectral_operator': 1665, 'discrete_protocol': 1429, 'boundary_weak_form': 1336}; flags {'has_relation': 32823, 'has_math_token': 32804, 'logical_relation': 2182, 'chemical_formula_or_reaction': 1111}

### alpha

- `A00`: links `872290`, cards `370496`, sources `115104`, clean `1.000`, score p50 `0.692`; status {'partial_constructor_frame': 462659, 'equation_shape_only': 390213, 'complete_constructor_frame': 19418}; routes {'unclassified': 604605, 'commutator_incompatibility': 125681, 'constraint_closure': 100972, 'boundary_weak_form': 37095, 'transport_flow': 36425, 'discrete_protocol': 6314, 'spectral_operator': 5148}; flags {'has_relation': 872290, 'has_math_token': 871059, 'logical_relation': 56022, 'chemical_formula_or_reaction': 44452}
- `A01`: links `109472`, cards `51649`, sources `24832`, clean `1.000`, score p50 `0.643`; status {'partial_constructor_frame': 71965, 'equation_shape_only': 20363, 'complete_constructor_frame': 17144}; routes {'transport_flow': 61563, 'unclassified': 33125, 'commutator_incompatibility': 16212, 'constraint_closure': 12268, 'boundary_weak_form': 7770, 'spectral_operator': 3558, 'discrete_protocol': 498}; flags {'has_relation': 109472, 'has_math_token': 109400, 'chemical_formula_or_reaction': 5333, 'logical_relation': 5018}
- `A02`: links `104291`, cards `44419`, sources `20259`, clean `1.000`, score p50 `0.640`; status {'partial_constructor_frame': 66839, 'complete_constructor_frame': 19717, 'equation_shape_only': 17735}; routes {'spectral_operator': 59727, 'unclassified': 29062, 'commutator_incompatibility': 13155, 'constraint_closure': 11982, 'transport_flow': 8738, 'boundary_weak_form': 7655, 'discrete_protocol': 531}; flags {'has_relation': 104291, 'has_math_token': 104177, 'logical_relation': 5250, 'chemical_formula_or_reaction': 4508}
- `A03`: links `96722`, cards `43775`, sources `21345`, clean `1.000`, score p50 `0.643`; status {'partial_constructor_frame': 65683, 'equation_shape_only': 17910, 'complete_constructor_frame': 13129}; routes {'unclassified': 65137, 'commutator_incompatibility': 13503, 'constraint_closure': 9991, 'transport_flow': 7460, 'boundary_weak_form': 4876, 'spectral_operator': 1298, 'discrete_protocol': 487}; flags {'has_relation': 96722, 'has_math_token': 96668, 'logical_relation': 4661, 'chemical_formula_or_reaction': 4391}
- `A05`: links `89234`, cards `40977`, sources `18907`, clean `1.000`, score p50 `0.654`; status {'partial_constructor_frame': 63099, 'equation_shape_only': 18552, 'complete_constructor_frame': 7583}; routes {'transport_flow': 48784, 'unclassified': 30560, 'constraint_closure': 10305, 'commutator_incompatibility': 9775, 'boundary_weak_form': 4150, 'spectral_operator': 589, 'discrete_protocol': 450}; flags {'has_relation': 89234, 'has_math_token': 89168, 'chemical_formula_or_reaction': 4094, 'logical_relation': 4016}
- `A04`: links `74958`, cards `35413`, sources `17238`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 56275, 'equation_shape_only': 14683, 'complete_constructor_frame': 4000}; routes {'boundary_weak_form': 41442, 'unclassified': 23355, 'commutator_incompatibility': 10011, 'transport_flow': 8257, 'constraint_closure': 7779, 'spectral_operator': 1112, 'discrete_protocol': 430}; flags {'has_relation': 74958, 'has_math_token': 74886, 'logical_relation': 3570, 'chemical_formula_or_reaction': 3284}
- `A06`: links `61573`, cards `28757`, sources `13783`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 45681, 'equation_shape_only': 11007, 'complete_constructor_frame': 4885}; routes {'unclassified': 39564, 'commutator_incompatibility': 7633, 'constraint_closure': 6237, 'transport_flow': 6229, 'boundary_weak_form': 3082, 'spectral_operator': 3048, 'discrete_protocol': 222}; flags {'has_relation': 61573, 'has_math_token': 61538, 'chemical_formula_or_reaction': 3359, 'logical_relation': 2146}
- `A08`: links `60095`, cards `26570`, sources `12547`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 38492, 'equation_shape_only': 10883, 'complete_constructor_frame': 10720}; routes {'unclassified': 37264, 'commutator_incompatibility': 8015, 'constraint_closure': 6715, 'transport_flow': 6670, 'boundary_weak_form': 3926, 'spectral_operator': 2232, 'discrete_protocol': 337}; flags {'has_relation': 60095, 'has_math_token': 60001, 'logical_relation': 4273, 'chemical_formula_or_reaction': 2959}
- `A13`: links `42362`, cards `18100`, sources `7280`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 33402, 'equation_shape_only': 6386, 'complete_constructor_frame': 2574}; routes {'transport_flow': 27669, 'discrete_protocol': 26313, 'unclassified': 9546, 'commutator_incompatibility': 6748, 'constraint_closure': 6153, 'boundary_weak_form': 2532, 'spectral_operator': 2150}; flags {'has_relation': 42362, 'has_math_token': 42339, 'logical_relation': 2533, 'chemical_formula_or_reaction': 1187}
- `A07`: links `33719`, cards `14405`, sources `8089`, clean `1.000`, score p50 `0.632`; status {'partial_constructor_frame': 18485, 'complete_constructor_frame': 7688, 'equation_shape_only': 7546}; routes {'unclassified': 14547, 'spectral_operator': 11340, 'commutator_incompatibility': 5012, 'constraint_closure': 4088, 'transport_flow': 4070, 'boundary_weak_form': 2056, 'discrete_protocol': 269}; flags {'has_relation': 33719, 'has_math_token': 33688, 'chemical_formula_or_reaction': 1911, 'logical_relation': 1804}
- `A12`: links `30808`, cards `13117`, sources `6487`, clean `1.000`, score p50 `0.652`; status {'partial_constructor_frame': 22133, 'equation_shape_only': 7294, 'complete_constructor_frame': 1381}; routes {'unclassified': 18674, 'commutator_incompatibility': 4445, 'transport_flow': 4137, 'constraint_closure': 3298, 'spectral_operator': 1426, 'boundary_weak_form': 1210, 'discrete_protocol': 1036}; flags {'has_relation': 30808, 'has_math_token': 30793, 'logical_relation': 2011, 'chemical_formula_or_reaction': 1059}
- `A09`: links `29853`, cards `13070`, sources `6509`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 19140, 'complete_constructor_frame': 6103, 'equation_shape_only': 4610}; routes {'unclassified': 16371, 'constraint_closure': 4992, 'transport_flow': 4947, 'commutator_incompatibility': 3601, 'boundary_weak_form': 2460, 'spectral_operator': 863, 'discrete_protocol': 115}; flags {'has_relation': 29853, 'has_math_token': 29830, 'chemical_formula_or_reaction': 1543, 'logical_relation': 1114}

### lambda

- `Λ00`: links `245354`, cards `20989`, sources `12544`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 172452, 'equation_shape_only': 41640, 'complete_constructor_frame': 31262}; routes {'unclassified': 102483, 'transport_flow': 57385, 'commutator_incompatibility': 48012, 'constraint_closure': 45675, 'boundary_weak_form': 20304, 'spectral_operator': 17976, 'discrete_protocol': 4795}; flags {'has_relation': 245354, 'has_math_token': 245163, 'logical_relation': 18564, 'chemical_formula_or_reaction': 12182}
- `Λ01`: links `156951`, cards `15325`, sources `9518`, clean `1.000`, score p50 `0.652`; status {'partial_constructor_frame': 115780, 'equation_shape_only': 28668, 'complete_constructor_frame': 12503}; routes {'unclassified': 72042, 'transport_flow': 32822, 'commutator_incompatibility': 28651, 'constraint_closure': 27336, 'boundary_weak_form': 11367, 'spectral_operator': 7089, 'discrete_protocol': 2260}; flags {'has_relation': 156951, 'has_math_token': 156854, 'logical_relation': 11754, 'chemical_formula_or_reaction': 7780}
- `Λ02`: links `126053`, cards `12281`, sources `7740`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 93053, 'equation_shape_only': 21550, 'complete_constructor_frame': 11450}; routes {'unclassified': 53567, 'transport_flow': 27797, 'constraint_closure': 25559, 'commutator_incompatibility': 23424, 'boundary_weak_form': 13012, 'spectral_operator': 4757, 'discrete_protocol': 2885}; flags {'has_relation': 126053, 'has_math_token': 125954, 'logical_relation': 12935, 'chemical_formula_or_reaction': 5196}
- `Λ03`: links `59548`, cards `10592`, sources `6673`, clean `1.000`, score p50 `0.643`; status {'partial_constructor_frame': 46801, 'equation_shape_only': 7144, 'complete_constructor_frame': 5603}; routes {'transport_flow': 20433, 'unclassified': 19354, 'commutator_incompatibility': 10260, 'constraint_closure': 9512, 'boundary_weak_form': 9145, 'spectral_operator': 4320, 'discrete_protocol': 494}; flags {'has_relation': 59548, 'has_math_token': 59508, 'logical_relation': 2638, 'chemical_formula_or_reaction': 2387}
- `Λ04`: links `51047`, cards `3298`, sources `2251`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 35433, 'equation_shape_only': 8568, 'complete_constructor_frame': 7046}; routes {'unclassified': 23205, 'transport_flow': 9332, 'constraint_closure': 8736, 'commutator_incompatibility': 7881, 'boundary_weak_form': 7679, 'spectral_operator': 2260, 'discrete_protocol': 1059}; flags {'has_relation': 51047, 'has_math_token': 51029, 'logical_relation': 5144, 'chemical_formula_or_reaction': 1910}
- `Λ06`: links `30621`, cards `1512`, sources `1057`, clean `1.000`, score p50 `0.632`; status {'partial_constructor_frame': 20295, 'complete_constructor_frame': 5280, 'equation_shape_only': 5046}; routes {'unclassified': 12383, 'spectral_operator': 6713, 'transport_flow': 4815, 'boundary_weak_form': 4361, 'commutator_incompatibility': 4240, 'constraint_closure': 4110, 'discrete_protocol': 366}; flags {'has_relation': 30621, 'has_math_token': 30605, 'logical_relation': 3761, 'chemical_formula_or_reaction': 1062}
- `Λ05`: links `30014`, cards `2611`, sources `1785`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 16022, 'equation_shape_only': 7253, 'complete_constructor_frame': 6739}; routes {'unclassified': 13112, 'spectral_operator': 7151, 'boundary_weak_form': 5919, 'transport_flow': 4630, 'commutator_incompatibility': 4438, 'constraint_closure': 3305, 'discrete_protocol': 344}; flags {'has_relation': 30014, 'has_math_token': 30000, 'chemical_formula_or_reaction': 3761, 'logical_relation': 2357}
- `Λ07`: links `26109`, cards `4034`, sources `2654`, clean `1.000`, score p50 `0.640`; status {'partial_constructor_frame': 20259, 'equation_shape_only': 3625, 'complete_constructor_frame': 2225}; routes {'unclassified': 8874, 'transport_flow': 7191, 'boundary_weak_form': 6078, 'commutator_incompatibility': 4817, 'constraint_closure': 4643, 'spectral_operator': 1866, 'discrete_protocol': 196}; flags {'has_relation': 26109, 'has_math_token': 26095, 'chemical_formula_or_reaction': 1041, 'logical_relation': 1006}
- `Λ08`: links `25437`, cards `5072`, sources `3362`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 17287, 'complete_constructor_frame': 4277, 'equation_shape_only': 3873}; routes {'unclassified': 10249, 'transport_flow': 5479, 'constraint_closure': 4744, 'commutator_incompatibility': 4553, 'spectral_operator': 2848, 'boundary_weak_form': 1329, 'discrete_protocol': 165}; flags {'has_relation': 25437, 'has_math_token': 25432, 'chemical_formula_or_reaction': 986, 'logical_relation': 796}
- `Λ09`: links `22700`, cards `3736`, sources `2444`, clean `1.000`, score p50 `0.643`; status {'partial_constructor_frame': 17505, 'equation_shape_only': 3298, 'complete_constructor_frame': 1897}; routes {'unclassified': 9285, 'transport_flow': 6317, 'commutator_incompatibility': 4483, 'constraint_closure': 3882, 'boundary_weak_form': 1752, 'spectral_operator': 1374, 'discrete_protocol': 221}; flags {'has_relation': 22700, 'has_math_token': 22692, 'chemical_formula_or_reaction': 1000, 'logical_relation': 676}
- `Λ10`: links `19443`, cards `5205`, sources `3488`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 15682, 'equation_shape_only': 2266, 'complete_constructor_frame': 1495}; routes {'unclassified': 7203, 'transport_flow': 5268, 'commutator_incompatibility': 4759, 'constraint_closure': 2926, 'spectral_operator': 1479, 'boundary_weak_form': 1281, 'discrete_protocol': 456}; flags {'has_relation': 19443, 'has_math_token': 19418, 'logical_relation': 1372, 'chemical_formula_or_reaction': 682}
- `Λ15`: links `14236`, cards `872`, sources `602`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 10192, 'equation_shape_only': 2616, 'complete_constructor_frame': 1428}; routes {'unclassified': 6273, 'commutator_incompatibility': 2916, 'transport_flow': 2811, 'constraint_closure': 2382, 'boundary_weak_form': 1708, 'spectral_operator': 720, 'discrete_protocol': 434}; flags {'has_relation': 14236, 'has_math_token': 14236, 'logical_relation': 1720, 'chemical_formula_or_reaction': 579}

### tau

- `T00`: links `49001`, cards `12389`, sources `3221`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 29056, 'equation_shape_only': 15907, 'complete_constructor_frame': 4038}; routes {'unclassified': 28459, 'constraint_closure': 6710, 'transport_flow': 6305, 'commutator_incompatibility': 5890, 'boundary_weak_form': 4507, 'spectral_operator': 2477, 'discrete_protocol': 699}; flags {'has_relation': 49001, 'has_math_token': 48964, 'chemical_formula_or_reaction': 2793, 'logical_relation': 1953}
- `T01`: links `8646`, cards `5839`, sources `1920`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 5322, 'equation_shape_only': 2614, 'complete_constructor_frame': 710}; routes {'unclassified': 5131, 'transport_flow': 1043, 'constraint_closure': 981, 'commutator_incompatibility': 961, 'boundary_weak_form': 788, 'spectral_operator': 533, 'discrete_protocol': 114}; flags {'has_relation': 8646, 'has_math_token': 8639, 'chemical_formula_or_reaction': 529, 'logical_relation': 346}
- `T02`: links `7523`, cards `5338`, sources `1787`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 4606, 'equation_shape_only': 2182, 'complete_constructor_frame': 735}; routes {'unclassified': 4149, 'transport_flow': 1195, 'constraint_closure': 993, 'commutator_incompatibility': 814, 'boundary_weak_form': 728, 'spectral_operator': 469, 'discrete_protocol': 105}; flags {'has_relation': 7523, 'has_math_token': 7515, 'chemical_formula_or_reaction': 441, 'logical_relation': 285}
- `T03`: links `4475`, cards `3407`, sources `1263`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 2729, 'equation_shape_only': 1321, 'complete_constructor_frame': 425}; routes {'unclassified': 2379, 'transport_flow': 992, 'commutator_incompatibility': 545, 'constraint_closure': 535, 'boundary_weak_form': 405, 'spectral_operator': 223, 'discrete_protocol': 156}; flags {'has_relation': 4475, 'has_math_token': 4464, 'chemical_formula_or_reaction': 279, 'logical_relation': 192}
- `T04`: links `2014`, cards `1585`, sources `641`, clean `1.000`, score p50 `0.667`; status {'partial_constructor_frame': 1286, 'equation_shape_only': 528, 'complete_constructor_frame': 200}; routes {'unclassified': 1210, 'transport_flow': 280, 'constraint_closure': 222, 'commutator_incompatibility': 215, 'boundary_weak_form': 149, 'spectral_operator': 141, 'discrete_protocol': 25}; flags {'has_relation': 2014, 'has_math_token': 2013, 'chemical_formula_or_reaction': 104, 'logical_relation': 79}
- `T05`: links `882`, cards `686`, sources `335`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 557, 'equation_shape_only': 234, 'complete_constructor_frame': 91}; routes {'unclassified': 538, 'constraint_closure': 116, 'transport_flow': 98, 'commutator_incompatibility': 92, 'boundary_weak_form': 80, 'spectral_operator': 25, 'discrete_protocol': 15}; flags {'has_relation': 882, 'has_math_token': 880, 'chemical_formula_or_reaction': 60, 'logical_relation': 33}
- `T06`: links `560`, cards `432`, sources `200`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 358, 'equation_shape_only': 140, 'complete_constructor_frame': 62}; routes {'unclassified': 286, 'commutator_incompatibility': 96, 'spectral_operator': 84, 'transport_flow': 83, 'constraint_closure': 60, 'boundary_weak_form': 42, 'discrete_protocol': 7}; flags {'has_relation': 560, 'has_math_token': 560, 'chemical_formula_or_reaction': 37, 'logical_relation': 14}
- `T07`: links `486`, cards `357`, sources `163`, clean `1.000`, score p50 `0.652`; status {'partial_constructor_frame': 328, 'equation_shape_only': 107, 'complete_constructor_frame': 51}; routes {'unclassified': 210, 'boundary_weak_form': 100, 'commutator_incompatibility': 88, 'transport_flow': 82, 'constraint_closure': 65, 'spectral_operator': 17, 'discrete_protocol': 5}; flags {'has_relation': 486, 'has_math_token': 486, 'chemical_formula_or_reaction': 26, 'logical_relation': 21}

### gamma

- `Γ02`: links `10185`, cards `3331`, sources `2097`, clean `1.000`, score p50 `0.680`; status {'partial_constructor_frame': 7753, 'equation_shape_only': 1912, 'complete_constructor_frame': 520}; routes {'constraint_closure': 4801, 'unclassified': 3761, 'commutator_incompatibility': 2241, 'transport_flow': 803, 'boundary_weak_form': 384, 'discrete_protocol': 159, 'spectral_operator': 73}; flags {'has_relation': 10185, 'has_math_token': 10181, 'logical_relation': 574, 'chemical_formula_or_reaction': 514}
- `Γ00`: links `7616`, cards `2798`, sources `1915`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 5507, 'equation_shape_only': 1122, 'complete_constructor_frame': 987}; routes {'transport_flow': 3520, 'unclassified': 2820, 'commutator_incompatibility': 1248, 'constraint_closure': 749, 'boundary_weak_form': 518, 'discrete_protocol': 161, 'spectral_operator': 64}; flags {'has_relation': 7616, 'has_math_token': 7616, 'logical_relation': 504, 'chemical_formula_or_reaction': 309}
- `Γ01`: links `5912`, cards `2661`, sources `1866`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 3700, 'complete_constructor_frame': 1506, 'equation_shape_only': 706}; routes {'unclassified': 2428, 'spectral_operator': 1833, 'commutator_incompatibility': 1107, 'transport_flow': 1041, 'constraint_closure': 452, 'boundary_weak_form': 331, 'discrete_protocol': 102}; flags {'has_relation': 5912, 'has_math_token': 5896, 'logical_relation': 376, 'chemical_formula_or_reaction': 328}
- `Γ03`: links `5030`, cards `1313`, sources `911`, clean `1.000`, score p50 `0.643`; status {'partial_constructor_frame': 3535, 'equation_shape_only': 1189, 'complete_constructor_frame': 306}; routes {'unclassified': 2538, 'boundary_weak_form': 1558, 'commutator_incompatibility': 574, 'transport_flow': 461, 'constraint_closure': 406, 'discrete_protocol': 44, 'spectral_operator': 11}; flags {'has_relation': 5030, 'has_math_token': 5028, 'logical_relation': 351, 'chemical_formula_or_reaction': 127}
- `Γ04`: links `4305`, cards `1110`, sources `758`, clean `1.000`, score p50 `0.632`; status {'partial_constructor_frame': 3252, 'equation_shape_only': 913, 'complete_constructor_frame': 140}; routes {'unclassified': 2841, 'commutator_incompatibility': 824, 'constraint_closure': 468, 'transport_flow': 248, 'discrete_protocol': 144, 'boundary_weak_form': 55, 'spectral_operator': 10}; flags {'has_relation': 4305, 'has_math_token': 4304, 'logical_relation': 999, 'chemical_formula_or_reaction': 217}
- `Γ05`: links `3404`, cards `1825`, sources `1255`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 2634, 'equation_shape_only': 456, 'complete_constructor_frame': 314}; routes {'unclassified': 1418, 'transport_flow': 1397, 'commutator_incompatibility': 716, 'boundary_weak_form': 179, 'constraint_closure': 156, 'spectral_operator': 145, 'discrete_protocol': 15}; flags {'has_relation': 3404, 'has_math_token': 3401, 'logical_relation': 168, 'chemical_formula_or_reaction': 132}
- `Γ06`: links `2913`, cards `1559`, sources `1063`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 2388, 'equation_shape_only': 377, 'complete_constructor_frame': 148}; routes {'transport_flow': 1426, 'unclassified': 956, 'commutator_incompatibility': 573, 'boundary_weak_form': 412, 'constraint_closure': 197, 'spectral_operator': 46, 'discrete_protocol': 24}; flags {'has_relation': 2913, 'has_math_token': 2913, 'logical_relation': 200, 'chemical_formula_or_reaction': 94}
- `Γ07`: links `2842`, cards `1624`, sources `1137`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 2212, 'equation_shape_only': 387, 'complete_constructor_frame': 243}; routes {'unclassified': 1180, 'transport_flow': 746, 'commutator_incompatibility': 525, 'boundary_weak_form': 485, 'constraint_closure': 351, 'spectral_operator': 160, 'discrete_protocol': 16}; flags {'has_relation': 2842, 'has_math_token': 2841, 'logical_relation': 133, 'chemical_formula_or_reaction': 130}
- `Γ09`: links `2078`, cards `844`, sources `608`, clean `1.000`, score p50 `0.632`; status {'partial_constructor_frame': 1389, 'complete_constructor_frame': 377, 'equation_shape_only': 312}; routes {'unclassified': 804, 'spectral_operator': 483, 'transport_flow': 342, 'boundary_weak_form': 298, 'constraint_closure': 281, 'commutator_incompatibility': 281, 'discrete_protocol': 31}; flags {'has_relation': 2078, 'has_math_token': 2078, 'logical_relation': 263, 'chemical_formula_or_reaction': 76}
- `Γ08`: links `2046`, cards `896`, sources `640`, clean `1.000`, score p50 `0.647`; status {'partial_constructor_frame': 1058, 'equation_shape_only': 495, 'complete_constructor_frame': 493}; routes {'unclassified': 870, 'spectral_operator': 528, 'boundary_weak_form': 374, 'transport_flow': 353, 'commutator_incompatibility': 299, 'constraint_closure': 272, 'discrete_protocol': 21}; flags {'has_relation': 2046, 'has_math_token': 2045, 'chemical_formula_or_reaction': 234, 'logical_relation': 140}
- `Γ10`: links `2007`, cards `997`, sources `692`, clean `1.000`, score p50 `0.636`; status {'partial_constructor_frame': 1505, 'equation_shape_only': 384, 'complete_constructor_frame': 118}; routes {'unclassified': 1016, 'commutator_incompatibility': 512, 'transport_flow': 387, 'boundary_weak_form': 319, 'constraint_closure': 123, 'spectral_operator': 29, 'discrete_protocol': 10}; flags {'has_relation': 2007, 'has_math_token': 2004, 'logical_relation': 137, 'chemical_formula_or_reaction': 135}
- `Γ11`: links `288`, cards `162`, sources `117`, clean `1.000`, score p50 `0.652`; status {'partial_constructor_frame': 213, 'equation_shape_only': 43, 'complete_constructor_frame': 32}; routes {'unclassified': 128, 'commutator_incompatibility': 83, 'transport_flow': 53, 'constraint_closure': 36, 'boundary_weak_form': 34, 'spectral_operator': 10, 'discrete_protocol': 7}; flags {'has_relation': 288, 'has_math_token': 288, 'logical_relation': 49, 'chemical_formula_or_reaction': 16}


## Examples

### omega

#### `Ω00`
- `Ω:readout_closure_spectral`; row `20`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ω:readout_closure_spectral`; row `225`; score `1.0`; roles `[]`; routes `[]`.
  equation: `K >\nK_{crit}`
- `Ω:readout_closure_spectral`; row `261`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nR(z) = R(0) E_R (z)\n\`
- `Ω:readout_closure_spectral`; row `353`; score `1.0`; roles `[]`; routes `[]`.
  equation: `B_{Vega}=B_{AB}+0.077`

#### `Ω01`
- `Ω:spectral`; row `260`; score `1.0`; roles `[]`; routes `[]`.
  equation: `M_{*,s}\n= -21.1`
- `Ω:spectral`; row `280`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\lambda = J |E|^{1/2} G^{-1} M^{-5/2}\n\`
- `Ω:spectral`; row `16842`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nH_{1} = A(C/\\Delta)\\Delta_{\\lambda} -(EA(1/\\Delta)\\Delta_{\\lambda}-1) \ \\\\\nH_{2} = B(C/\\Delta)\\Delta_{\\lambda} -EB(1/\\Delta)\\Delta_{\\lambda} \ \\\\\nH_{3} = F(C/\\Delta)\\Delta_{\\lambda} -EF(1/\\Delt...`
- `Ω:spectral`; row `16843`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nH_{1} = A(C/\\Delta)\\Delta_{\\lambda} -(EA(1/\\Delta)\\Delta_{\\lambda}-1) \ \\\\\nH_{2} = B(C/\\Delta)\\Delta_{\\lambda} -EB(1/\\Delta)\\Delta_{\\lambda} \ \\\\\nH_{3} = F(C/\\Delta)\\Delta_{\\lambda} -EF(1/\\Delt...`

#### `Ω02`
- `Ω:spectral`; row `21`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ω:spectral`; row `22`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ω:spectral`; row `23`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ω:spectral`; row `151`; score `1.0`; roles `[]`; routes `[]`.
  equation: `r > r_h`

#### `Ω03`
- `Ω:readout`; row `8803`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\ba{rclrcl}\n A_3^{-2}+B_3^{-2}&=&c^*,& K_3^{-1}&=&\\phi^*, \\nm \\\\\n A_3^{-2}&=&(B^1)^*,& \\phi_3^{-3}&=&-(K^2)^*,\\nm \\\\\n A_2^{-1}+B_2^{-1}&=&A^*,& \\phi_2^{-2}&=&-(K_1^1)^*,\\nm \\\\\n A_2^{-1}&=&(B_1)^*,&...`
- `Ω:readout`; row `10486`; score `1.0`; roles `[]`; routes `[]`.
  equation: `1-t/4 < e^{-t/4} < 1- t/8`
- `Ω:readout`; row `14069`; score `1.0`; roles `[]`; routes `[]`.
  equation: `n^{b}_{-1/2,-1/2} = n^{b}_{1/2,1/2} = {1 \\over 2} -\n {3 \\over 8} \\sin^{2}{\\psi}~`
- `Ω:readout`; row `14438`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nd|A_v|^2&=A_v^*(dA_v)+(dA_v^*)A_v+(dA_v^*)(dA_v) \\\\\n&=A_v^* e^{i\\Phi(v)}I(v)dv + e^{-i\\Phi(v)}I(v)dv A_v +dv \\\\\n&=[ |A_v| I(v) 2{\\rm Re}( e^{i\\Phi(v)}e^{-i\\varphi_v^A})\n+1] dv,\n\`

#### `Ω04`
- `Ω:derivative_graph`; row `352`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\Delta(V_{555}-I_{814})=0.33`
- `Ω:derivative_graph`; row `3571`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nT^{tt}_{em} & = & T^{zz}_{em} = \\frac{I^2}{4\\pi} \\nabla^2 \\left( \n\\ln \\frac{r}{r_0} \\right)^2 \ \\\\\nT^{ij}_{em} & = & - \\frac{I^2}{2\\pi} \\partial_i\\partial_j \\ln \\frac{r}{r_0} .\n\`
- `Ω:derivative_graph`; row `12855`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\ne_{i}e_{j} &=&-\\delta _{ij}+\\epsilon _{ijk}e_{k}, \\\\\ne_{i}e_{0} &=&e_{0}e_{i}=e_{i}, \\\\\ne_{0}e_{0} &=&e_{0},\n\`
- `Ω:derivative_graph`; row `12856`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\ne_{i}e_{j} &=&-\\delta _{ij}+\\epsilon _{ijk}e_{k}, \\\\\ne_{i}e_{0} &=&e_{0}e_{i}=e_{i}, \\\\\ne_{0}e_{0} &=&e_{0},\n\`

#### `Ω05`
- `Ω:derivative`; row `3835`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m=10^{-6}M_{p}`
- `Ω:derivative`; row `13971`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n&&{\\bf B}=B_r\\hat {\\bf r}+B_z\\hat {\\bf z},\\\\\n&&B_r=B_wF_r(r,z),\\\\\n&&B_z=B_0+B_wF_z(r,z),\n\`
- `Ω:derivative`; row `19044`; score `1.0`; roles `[]`; routes `[]`.
  equation: `U_i=H_ix_i`
- `Ω:derivative`; row `20805`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nh_{1}^{(i)} &=& 4m_{t}\\eta^{(2)}(2p_{b}\\cdot k -p^{(i)}\\cdot p_b)\n-4m_{b}\\eta^{(1)}(p^{(i)}\\cdot p_{t} +p_{t}\\cdot k),\n\\\\ h_{2}^{(i)} &=& h_{1}^{(i)}(\\eta^{(1)}\n\\leftrightarrow \\eta^{(2)}),\n\\\\ h_{3}...`

#### `Ω06`
- `Ω:integral`; row `5986`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`
- `Ω:integral`; row `5987`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`
- `Ω:integral`; row `5988`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`
- `Ω:integral`; row `5989`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`

#### `Ω07`
- `Ω:closure_protocol_derivative`; row `350`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m_{410}-V_{555}< -0.2`
- `Ω:closure_protocol_derivative`; row `351`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m_{410}-V_{555}< -0.2`
- `Ω:closure_protocol_derivative`; row `6573`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nG^{0}&=&-F_{1},\ \\\\\nG^{1}&=&-F_{0}+2F_{1}-2e(A_{0}-A_{1}).\n\`
- `Ω:closure_protocol_derivative`; row `16543`; score `1.0`; roles `[]`; routes `[]`.
  equation: `c_f=[2 A(n_f^{eq})^{2/3}/3m_f]^{1/2}`

#### `Ω08`
- `Ω:closure_markov`; row `504`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`
- `Ω:closure_markov`; row `505`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`
- `Ω:closure_markov`; row `506`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`
- `Ω:closure_markov`; row `507`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`

#### `Ω09`
- `Ω:readout_derivative_closure`; row `14440`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nd|A_v|^2&=A_v^*(dA_v)+(dA_v^*)A_v+(dA_v^*)(dA_v) \\\\\n&=A_v^* e^{i\\Phi(v)}I(v)dv + e^{-i\\Phi(v)}I(v)dv A_v +dv \\\\\n&=[ |A_v| I(v) 2{\\rm Re}( e^{i\\Phi(v)}e^{-i\\varphi_v^A})\n+1] dv,\n\`
- `Ω:readout_derivative_closure`; row `24811`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m^2=3D0`
- `Ω:readout_derivative_closure`; row `24812`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m^2=3D0`
- `Ω:readout_derivative_closure`; row `28850`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\widetilde L=-\\partial_x^2+\\widetilde u(x),\\qquad\n\\widetilde u(x)=-v_x+v^2.\n`

#### `Ω10`
- `Ω:spectral_readout_closure`; row `16552`; score `1.0`; roles `[]`; routes `[]`.
  equation: `X_{b,f}=R_{b,f}/a_{ho}`
- `Ω:spectral_readout_closure`; row `16553`; score `1.0`; roles `[]`; routes `[]`.
  equation: `X_{b,f}=R_{b,f}/a_{ho}`
- `Ω:spectral_readout_closure`; row `16554`; score `1.0`; roles `[]`; routes `[]`.
  equation: `X_{b,f}=R_{b,f}/a_{ho}`
- `Ω:spectral_readout_closure`; row `20670`; score `1.0`; roles `[]`; routes `[]`.
  equation: `t=-(p_1-k_1)^2`

#### `Ω11`
- `Ω:closure`; row `11083`; score `1.0`; roles `[]`; routes `[]`.
  equation: `[h_i,e_j]=a_{ij}e_i`
- `Ω:closure`; row `25215`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n ~~~ Z^j &=& A_j r^j + B_j,\\\\\n \\mbox{For} ~ \\lambda = 0, ~~~ \\mbox{and}~~~~ && \ \\\\\n ~~~ Z^j &=& C_j -\\frac{1}{\\lambda_j}\\log \\mid r^j - R^j \\mid,\\\\\n \\mbox{For} ~ \\lambda \\neq 0,~~~~~~~~~~~~ && \...`
- `Ω:closure`; row `25216`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n ~~~ Z^j &=& A_j r^j + B_j,\\\\\n \\mbox{For} ~ \\lambda = 0, ~~~ \\mbox{and}~~~~ && \ \\\\\n ~~~ Z^j &=& C_j -\\frac{1}{\\lambda_j}\\log \\mid r^j - R^j \\mid,\\\\\n \\mbox{For} ~ \\lambda \\neq 0,~~~~~~~~~~~~ && \...`
- `Ω:closure`; row `25218`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n ~~~ Z^j &=& A_j r^j + B_j,\\\\\n \\mbox{For} ~ \\lambda = 0, ~~~ \\mbox{and}~~~~ && \ \\\\\n ~~~ Z^j &=& C_j -\\frac{1}{\\lambda_j}\\log \\mid r^j - R^j \\mid,\\\\\n \\mbox{For} ~ \\lambda \\neq 0,~~~~~~~~~~~~ && \...`

### xi

#### `Ξ00`
- `Ξ:coordinate_field_carrier_selector`; row `20`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ξ:coordinate_field_carrier_selector`; row `21`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ξ:coordinate_field_carrier_selector`; row `22`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `Ξ:coordinate_field_carrier_selector`; row `23`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`

#### `Ξ01`
- `Ξ:selector_hilbert_field_carrier`; row `350`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m_{410}-V_{555}< -0.2`
- `Ξ:selector_hilbert_field_carrier`; row `351`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m_{410}-V_{555}< -0.2`
- `Ξ:selector_hilbert_field_carrier`; row `532`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nQ=(A-B C^{-1} B^T)^{-1}\n\`
- `Ξ:selector_hilbert_field_carrier`; row `533`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nQ=(A-B C^{-1} B^T)^{-1}\n\`

#### `Ξ02`
- `Ξ:field_carrier`; row `3835`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m=10^{-6}M_{p}`
- `Ξ:field_carrier`; row `8803`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\ba{rclrcl}\n A_3^{-2}+B_3^{-2}&=&c^*,& K_3^{-1}&=&\\phi^*, \\nm \\\\\n A_3^{-2}&=&(B^1)^*,& \\phi_3^{-3}&=&-(K^2)^*,\\nm \\\\\n A_2^{-1}+B_2^{-1}&=&A^*,& \\phi_2^{-2}&=&-(K_1^1)^*,\\nm \\\\\n A_2^{-1}&=&(B_1)^*,&...`
- `Ξ:field_carrier`; row `10231`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\widetilde{A}_q (x) = A_p c^p_{qi} x^i`
- `Ξ:field_carrier`; row `10279`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\varphi(X_1,X_2,X_3)=0`

#### `Ξ03`
- `Ξ:markov`; row `151`; score `1.0`; roles `[]`; routes `[]`.
  equation: `r > r_h`
- `Ξ:markov`; row `260`; score `1.0`; roles `[]`; routes `[]`.
  equation: `M_{*,s}\n= -21.1`
- `Ξ:markov`; row `5078`; score `1.0`; roles `[]`; routes `[]`.
  equation: `0 <\n\\rho_0< \\rho_{-}< \\rho_1<\\rho_{+}<1`
- `Ξ:markov`; row `9224`; score `1.0`; roles `[]`; routes `[]`.
  equation: `is diffeomorphic to`

#### `Ξ04`
- `Ξ:selector`; row `544`; score `1.0`; roles `[]`; routes `[]`.
  equation: `W_{ii}=(V^i)^{-1}`
- `Ξ:selector`; row `2385`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\psi_{i} = u_{z}`
- `Ξ:selector`; row `9528`; score `1.0`; roles `[]`; routes `[]`.
  equation: `GL(2,\\mathbb{Z})=\\langle A,B,R | A^2=B^3,\nA^4=R^2={(RA)}^2={(RB)}^2=1 \\rangle,\`
- `Ξ:selector`; row `9529`; score `1.0`; roles `[]`; routes `[]`.
  equation: `GL(2,\\mathbb{Z})=\\langle A,B,R | A^2=B^3,\nA^4=R^2={(RA)}^2={(RB)}^2=1 \\rangle,\`

#### `Ξ05`
- `Ξ:closure_field_carrier_coordinate`; row `225`; score `1.0`; roles `[]`; routes `[]`.
  equation: `K >\nK_{crit}`
- `Ξ:closure_field_carrier_coordinate`; row `6782`; score `1.0`; roles `[]`; routes `[]`.
  equation: `g^{\\mu \\nu},\ng^{00}=-g^{11}=1, g^{12}=g^{21}=0`
- `Ξ:closure_field_carrier_coordinate`; row `6783`; score `1.0`; roles `[]`; routes `[]`.
  equation: `g^{\\mu \\nu},\ng^{00}=-g^{11}=1, g^{12}=g^{21}=0`
- `Ξ:closure_field_carrier_coordinate`; row `6953`; score `1.0`; roles `[]`; routes `[]`.
  equation: `K_{ab}{}^i = K_{ba}{}^i`

#### `Ξ06`
- `Ξ:graph_closure`; row `352`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\Delta(V_{555}-I_{814})=0.33`
- `Ξ:graph_closure`; row `573`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F^p=0`
- `Ξ:graph_closure`; row `5618`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\delta\\mu^2&=&\\mu^2-\\mu_{0}^2,\ \\\\\n\\delta\\eta&=&\\eta-\\eta_{0},\ \\\\\n\\delta\\lambda^2&=&\\lambda^2-\\lambda_{0}^2,\ \\\\\n\\delta\\xi&=&\\xi-\\xi_{0},\ \\\\\n\\delta m&=&m-m_{0},\ \\\\\n\\delta M&=&M-M_...`
- `Ξ:graph_closure`; row `5858`; score `1.0`; roles `[]`; routes `[]`.
  equation: `[p(t), x_{1}(t)]=0`

#### `Ξ07`
- `Ξ:coordinate_field_carrier`; row `280`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\lambda = J |E|^{1/2} G^{-1} M^{-5/2}\n\`
- `Ξ:coordinate_field_carrier`; row `504`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`
- `Ξ:coordinate_field_carrier`; row `505`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`
- `Ξ:coordinate_field_carrier`; row `506`; score `1.0`; roles `[]`; routes `[]`.
  equation: `h_{00} = h_{0i} = 0`

#### `Ξ08`
- `Ξ:reaction_hilbert`; row `9729`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F=I_{Z}`
- `Ξ:reaction_hilbert`; row `9730`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F=I_{Z}`
- `Ξ:reaction_hilbert`; row `9731`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F=I_{Z}`
- `Ξ:reaction_hilbert`; row `16543`; score `1.0`; roles `[]`; routes `[]`.
  equation: `c_f=[2 A(n_f^{eq})^{2/3}/3m_f]^{1/2}`

#### `Ξ09`
- `Ξ:lattice_selector`; row `11463`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\beta _n(g_i)=g_i`
- `Ξ:lattice_selector`; row `11464`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\beta _n(g_i)=g_i`
- `Ξ:lattice_selector`; row `16684`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\widetilde K_{ij}=(q_iKq_j)`
- `Ξ:lattice_selector`; row `16685`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\widetilde\nT_{ij}=(p_iTp_j)`

#### `Ξ10`
- `Ξ:selector`; row `732`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nQ_X =q_X g_X m_X^4.\n\`
- `Ξ:selector`; row `733`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nQ_X =q_X g_X m_X^4.\n\`
- `Ξ:selector`; row `734`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nQ_X =q_X g_X m_X^4.\n\`
- `Ξ:selector`; row `735`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nQ_X =q_X g_X m_X^4.\n\`

#### `Ξ11`
- `Ξ:positivity`; row `30843`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\sigma_{x_1}^2&=&<x_1^2>=\\int\\int x_1^2 f(x_1,x_2)\\ud x_1\\ud x_2 \ \\\\\n\\sigma_{x_2}^2&=&<x_2^2>=\\int\\int x_2^2 f(x_1,x_2)\\ud x_1\\ud x_2 \\\\\n\\sigma_{x_1 x_2}^2&=&<x_1 x_2>=\\int\\int x_1 x_2 f(x_1,x_2)...`
- `Ξ:positivity`; row `30857`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\varepsilon^2_{x,rms}=<x_1^2><x_2^2>-<x_1 x_2>^2\n\`
- `Ξ:positivity`; row `30858`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\varepsilon^2_{x,rms}=<x_1^2><x_2^2>-<x_1 x_2>^2\n\`
- `Ξ:positivity`; row `30859`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\varepsilon^2_{x,rms}=<x_1^2><x_2^2>-<x_1 x_2>^2\n\`

### alpha

#### `A00`
- `A:Ω_readout_closure_spectral-Ξ_diffuse-R_mixed-Γ_lo`; row `20`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `A:Ω_readout_closure_spectral-Ξ_diffuse-R_mixed-Γ_lo`; row `21`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `A:Ω_readout_closure_spectral-Ξ_diffuse-R_mixed-Γ_lo`; row `22`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`
- `A:Ω_readout_closure_spectral-Ξ_diffuse-R_mixed-Γ_lo`; row `23`; score `1.0`; roles `[]`; routes `[]`.
  equation: `v=v_{n,i}`

#### `A01`
- `A:Ω_derivative_graph-Ξ_graph_closure-R_transport-Γ_lo`; row `352`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\Delta(V_{555}-I_{814})=0.33`
- `A:Ω_derivative_graph-Ξ_graph_closure-R_transport-Γ_lo`; row `573`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F^p=0`
- `A:Ω_derivative_graph-Ξ_graph_closure-R_transport-Γ_lo`; row `3571`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nT^{tt}_{em} & = & T^{zz}_{em} = \\frac{I^2}{4\\pi} \\nabla^2 \\left( \n\\ln \\frac{r}{r_0} \\right)^2 \ \\\\\nT^{ij}_{em} & = & - \\frac{I^2}{2\\pi} \\partial_i\\partial_j \\ln \\frac{r}{r_0} .\n\`
- `A:Ω_derivative_graph-Ξ_graph_closure-R_transport-Γ_lo`; row `5618`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\delta\\mu^2&=&\\mu^2-\\mu_{0}^2,\ \\\\\n\\delta\\eta&=&\\eta-\\eta_{0},\ \\\\\n\\delta\\lambda^2&=&\\lambda^2-\\lambda_{0}^2,\ \\\\\n\\delta\\xi&=&\\xi-\\xi_{0},\ \\\\\n\\delta m&=&m-m_{0},\ \\\\\n\\delta M&=&M-M_...`

#### `A02`
- `A:Ω_spectral-Ξ_diffuse-R_spectral-Γ_lo`; row `280`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\lambda = J |E|^{1/2} G^{-1} M^{-5/2}\n\`
- `A:Ω_spectral-Ξ_diffuse-R_spectral-Γ_lo`; row `18575`; score `1.0`; roles `[]`; routes `[]`.
  equation: `R^0_0 = R^1_1`
- `A:Ω_spectral-Ξ_diffuse-R_spectral-Γ_lo`; row `18576`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n- \\rho_t = R^0_0 = R^1_1 =\\frac{1}{c^2}(\\frac{\\ddot a}{a} - \n\\frac{\\dot a\\dot c}{ac}) - \\frac{1}{a^2}(\\frac{c^{\\prime\\prime}}{c} - \n\\frac{a^{\\prime}c^{\\prime}}{ac}), \\hspace{0.3cm}\n\\rho = R^2_2 =...`
- `A:Ω_spectral-Ξ_diffuse-R_spectral-Γ_lo`; row `23402`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\lambda_{C_4}^B = \n0`

#### `A03`
- `A:Ω_readout-Ξ_selector_hilbert_field_carrier-R_mixed-Γ_lo`; row `2385`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\\psi_{i} = u_{z}`
- `A:Ω_readout-Ξ_selector_hilbert_field_carrier-R_mixed-Γ_lo`; row `5986`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`
- `A:Ω_readout-Ξ_selector_hilbert_field_carrier-R_mixed-Γ_lo`; row `5987`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`
- `A:Ω_readout-Ξ_selector_hilbert_field_carrier-R_mixed-Γ_lo`; row `5988`; score `1.0`; roles `[]`; routes `[]`.
  equation: `b_{1}=b_{2}`

#### `A04`
- `A:Ω_readout_closure_spectral-Ξ_closure_field_carrier_coordinate-R_boundary-Γ_lo`; row `225`; score `1.0`; roles `[]`; routes `[]`.
  equation: `K >\nK_{crit}`
- `A:Ω_readout_closure_spectral-Ξ_closure_field_carrier_coordinate-R_boundary-Γ_lo`; row `6782`; score `1.0`; roles `[]`; routes `[]`.
  equation: `g^{\\mu \\nu},\ng^{00}=-g^{11}=1, g^{12}=g^{21}=0`
- `A:Ω_readout_closure_spectral-Ξ_closure_field_carrier_coordinate-R_boundary-Γ_lo`; row `6783`; score `1.0`; roles `[]`; routes `[]`.
  equation: `g^{\\mu \\nu},\ng^{00}=-g^{11}=1, g^{12}=g^{21}=0`
- `A:Ω_readout_closure_spectral-Ξ_closure_field_carrier_coordinate-R_boundary-Γ_lo`; row `6953`; score `1.0`; roles `[]`; routes `[]`.
  equation: `K_{ab}{}^i = K_{ba}{}^i`

#### `A05`
- `A:Ω_derivative-Ξ_diffuse-R_transport-Γ_lo`; row `752`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nR= 4.5 m_X^{-8/3} M^{-1/3} m_{Planck}^{2}\n=0.98{\\rm kpc}\\left({m_X\\over 100{\\rm eV}}\\right)^{-8/3}\n\\left({M\\over 10^{10}M_\\odot}\\right)^{-1/3},\n\`
- `A:Ω_derivative-Ξ_diffuse-R_transport-Γ_lo`; row `753`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nR= 4.5 m_X^{-8/3} M^{-1/3} m_{Planck}^{2}\n=0.98{\\rm kpc}\\left({m_X\\over 100{\\rm eV}}\\right)^{-8/3}\n\\left({M\\over 10^{10}M_\\odot}\\right)^{-1/3},\n\`
- `A:Ω_derivative-Ξ_diffuse-R_transport-Γ_lo`; row `754`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\nR= 4.5 m_X^{-8/3} M^{-1/3} m_{Planck}^{2}\n=0.98{\\rm kpc}\\left({m_X\\over 100{\\rm eV}}\\right)^{-8/3}\n\\left({M\\over 10^{10}M_\\odot}\\right)^{-1/3},\n\`
- `A:Ω_derivative-Ξ_diffuse-R_transport-Γ_lo`; row `3835`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m=10^{-6}M_{p}`

#### `A06`
- `A:Ω_readout_closure_spectral-Ξ_markov-R_mixed-Γ_lo`; row `151`; score `1.0`; roles `[]`; routes `[]`.
  equation: `r > r_h`
- `A:Ω_readout_closure_spectral-Ξ_markov-R_mixed-Γ_lo`; row `5078`; score `1.0`; roles `[]`; routes `[]`.
  equation: `0 <\n\\rho_0< \\rho_{-}< \\rho_1<\\rho_{+}<1`
- `A:Ω_readout_closure_spectral-Ξ_markov-R_mixed-Γ_lo`; row `11007`; score `1.0`; roles `[]`; routes `[]`.
  equation: `S(X_n)=0`
- `A:Ω_readout_closure_spectral-Ξ_markov-R_mixed-Γ_lo`; row `11008`; score `1.0`; roles `[]`; routes `[]`.
  equation: `S(X_n)=0`

#### `A07`
- `A:Ω_spectral_readout_closure-Ξ_selector_hilbert_field_carrier-R_spectral-Γ_lo`; row `9226`; score `1.0`; roles `[]`; routes `[]`.
  equation: `into`
- `A:Ω_spectral_readout_closure-Ξ_selector_hilbert_field_carrier-R_spectral-Γ_lo`; row `9227`; score `1.0`; roles `[]`; routes `[]`.
  equation: `into`
- `A:Ω_spectral_readout_closure-Ξ_selector_hilbert_field_carrier-R_spectral-Γ_lo`; row `9228`; score `1.0`; roles `[]`; routes `[]`.
  equation: `into`
- `A:Ω_spectral_readout_closure-Ξ_selector_hilbert_field_carrier-R_spectral-Γ_lo`; row `9229`; score `1.0`; roles `[]`; routes `[]`.
  equation: `into`

#### `A08`
- `A:Ω_markov_integral-Ξ_markov-R_mixed-Γ_lo`; row `260`; score `1.0`; roles `[]`; routes `[]`.
  equation: `M_{*,s}\n= -21.1`
- `A:Ω_markov_integral-Ξ_markov-R_mixed-Γ_lo`; row `2004`; score `1.0`; roles `[]`; routes `[]`.
  equation: `U_0>E_R/4`
- `A:Ω_markov_integral-Ξ_markov-R_mixed-Γ_lo`; row `5858`; score `1.0`; roles `[]`; routes `[]`.
  equation: `[p(t), x_{1}(t)]=0`
- `A:Ω_markov_integral-Ξ_markov-R_mixed-Γ_lo`; row `5859`; score `1.0`; roles `[]`; routes `[]`.
  equation: `[p(t), x_{1}(t)]=0`

#### `A09`
- `A:Ω_readout_derivative_closure-Ξ_diffuse-R_transport-Γ_lo`; row `24811`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m^2=3D0`
- `A:Ω_readout_derivative_closure-Ξ_diffuse-R_transport-Γ_lo`; row `24812`; score `1.0`; roles `[]`; routes `[]`.
  equation: `m^2=3D0`
- `A:Ω_readout_derivative_closure-Ξ_diffuse-R_transport-Γ_lo`; row `28850`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\widetilde L=-\\partial_x^2+\\widetilde u(x),\\qquad\n\\widetilde u(x)=-v_x+v^2.\n`
- `A:Ω_readout_derivative_closure-Ξ_diffuse-R_transport-Γ_lo`; row `28851`; score `1.0`; roles `[]`; routes `[]`.
  equation: `\n\\widetilde L=-\\partial_x^2+\\widetilde u(x),\\qquad\n\\widetilde u(x)=-v_x+v^2.\n`

#### `A10`
- `A:Ω_closure_protocol_derivative-Ξ_diffuse-R_spectral-Γ_lo`; row `9729`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F=I_{Z}`
- `A:Ω_closure_protocol_derivative-Ξ_diffuse-R_spectral-Γ_lo`; row `9730`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F=I_{Z}`
- `A:Ω_closure_protocol_derivative-Ξ_diffuse-R_spectral-Γ_lo`; row `9731`; score `1.0`; roles `[]`; routes `[]`.
  equation: `F=I_{Z}`
- `A:Ω_closure_protocol_derivative-Ξ_diffuse-R_spectral-Γ_lo`; row `16543`; score `1.0`; roles `[]`; routes `[]`.
  equation: `c_f=[2 A(n_f^{eq})^{2/3}/3m_f]^{1/2}`

#### `A11`
- `A:Ω_closure_protocol_derivative-Ξ_reaction_hilbert-R_mixed-Γ_lo`; row `17128`; score `1.0`; roles `[]`; routes `[]`.
  equation: `c_{na}(k,x)=1`
- `A:Ω_closure_protocol_derivative-Ξ_reaction_hilbert-R_mixed-Γ_lo`; row `17129`; score `1.0`; roles `[]`; routes `[]`.
  equation: `c_{na}(k,x)=1`
- `A:Ω_closure_protocol_derivative-Ξ_reaction_hilbert-R_mixed-Γ_lo`; row `17131`; score `1.0`; roles `[]`; routes `[]`.
  equation: `c_{na}(k,x)=1`
- `A:Ω_closure_protocol_derivative-Ξ_reaction_hilbert-R_mixed-Γ_lo`; row `41079`; score `1.0`; roles `[]`; routes `[]`.
  equation: `n_S^i=n_C^i=n_F^i/2`

### lambda

#### `Λ00`
- `Λ00`; rows `29703` -> `295161`; endpoint alignment `both`; same source `False`.
  source: `\\alpha=k_{f}=k_{r}=0`
  target: `m_u=m_d=0`
- `Λ00`; rows `80308` -> `80309`; endpoint alignment `both`; same source `True`.
  source: `\nK_r^{-1}=K^{-1}+\n\\frac{4\\pi^3 y_0}{r_c^4}\n\\int_{r_c}^{R}dr(R-r)^2\\,r \n\\exp \\left[-2\\pi K\\ln\n\\frac{R^2-r^2}{rr_c}\\right],\n\`
  target: `\nK_r^{-1}=K^{-1}+\n\\frac{4\\pi^3 y_0}{r_c^4}\n\\int_{r_c}^{R}dr(R-r)^2\\,r \n\\exp \\left[-2\\pi K\\ln\n\\frac{R^2-r^2}{rr_c}\\right],\n\`
- `Λ00`; rows `80309` -> `80308`; endpoint alignment `both`; same source `True`.
  source: `\nK_r^{-1}=K^{-1}+\n\\frac{4\\pi^3 y_0}{r_c^4}\n\\int_{r_c}^{R}dr(R-r)^2\\,r \n\\exp \\left[-2\\pi K\\ln\n\\frac{R^2-r^2}{rr_c}\\right],\n\`
  target: `\nK_r^{-1}=K^{-1}+\n\\frac{4\\pi^3 y_0}{r_c^4}\n\\int_{r_c}^{R}dr(R-r)^2\\,r \n\\exp \\left[-2\\pi K\\ln\n\\frac{R^2-r^2}{rr_c}\\right],\n\`
- `Λ00`; rows `295161` -> `29703`; endpoint alignment `both`; same source `False`.
  source: `m_u=m_d=0`
  target: `\\alpha=k_{f}=k_{r}=0`

#### `Λ01`
- `Λ01`; rows `645418` -> `29701`; endpoint alignment `both`; same source `False`.
  source: `\n(T_i+1)(T_i-q)&=0 \\\\\nT_iT_j & =T_jT_i\\quad (\\textrm{when } \\left\\vert i-j\\right\\vert >1) \\\\\nT_iT_{i+1}T_i & =T_{i+1}T_iT_{i+1}\\\\\nX_iX_j & =X_jX_i\\\\\nX_iX_i^{-1}&=X_i^{-1}X_i=1\\\\\nX_iT_j & =T_jX_i\...`
  target: `\\alpha=k_{f}=k_{r}=0`
- `Λ01`; rows `645419` -> `29703`; endpoint alignment `both`; same source `False`.
  source: `\n(T_i+1)(T_i-q)&=0 \\\\\nT_iT_j & =T_jT_i\\quad (\\textrm{when } \\left\\vert i-j\\right\\vert >1) \\\\\nT_iT_{i+1}T_i & =T_{i+1}T_iT_{i+1}\\\\\nX_iX_j & =X_jX_i\\\\\nX_iX_i^{-1}&=X_i^{-1}X_i=1\\\\\nX_iT_j & =T_jX_i\...`
  target: `\\alpha=k_{f}=k_{r}=0`
- `Λ01`; rows `645419` -> `295161`; endpoint alignment `both`; same source `False`.
  source: `\n(T_i+1)(T_i-q)&=0 \\\\\nT_iT_j & =T_jT_i\\quad (\\textrm{when } \\left\\vert i-j\\right\\vert >1) \\\\\nT_iT_{i+1}T_i & =T_{i+1}T_iT_{i+1}\\\\\nX_iX_j & =X_jX_i\\\\\nX_iX_i^{-1}&=X_i^{-1}X_i=1\\\\\nX_iT_j & =T_jX_i\...`
  target: `m_u=m_d=0`
- `Λ01`; rows `9213278` -> `498436`; endpoint alignment `both`; same source `False`.
  source: `c_{-1}=0`
  target: `c_1(E) = aC_0 + bF`

#### `Λ02`
- `Λ02`; rows `29701` -> `645418`; endpoint alignment `both`; same source `False`.
  source: `\\alpha=k_{f}=k_{r}=0`
  target: `\n(T_i+1)(T_i-q)&=0 \\\\\nT_iT_j & =T_jT_i\\quad (\\textrm{when } \\left\\vert i-j\\right\\vert >1) \\\\\nT_iT_{i+1}T_i & =T_{i+1}T_iT_{i+1}\\\\\nX_iX_j & =X_jX_i\\\\\nX_iX_i^{-1}&=X_i^{-1}X_i=1\\\\\nX_iT_j & =T_jX_i\...`
- `Λ02`; rows `1002884` -> `170857`; endpoint alignment `both`; same source `False`.
  source: `\nM_{ab} = d_{acb} m^c\n~~~~~~~~~~~~~~~~~~\n\\Phi_{ab} = d_{abc} \\langle \\phi^c\\rangle \n`
  target: `\nh_0v_{l}=lv_{l},\\quad f_0^{l+1}v_{l}=e_1^{k-l+1}v_{l}=f_{i}v_{l}=e_{i+1}v_{l}=h_iv_{l}=0,\n\\qquad i\\in \\Z_{<0},\n\`
- `Λ02`; rows `3536429` -> `645418`; endpoint alignment `both`; same source `False`.
  source: `\n\tx_{u} - x_{u-1} < x_{u+1} - x_u < y_{v+1} - x_u.\n\t`
  target: `\n(T_i+1)(T_i-q)&=0 \\\\\nT_iT_j & =T_jT_i\\quad (\\textrm{when } \\left\\vert i-j\\right\\vert >1) \\\\\nT_iT_{i+1}T_i & =T_{i+1}T_iT_{i+1}\\\\\nX_iX_j & =X_jX_i\\\\\nX_iX_i^{-1}&=X_i^{-1}X_i=1\\\\\nX_iT_j & =T_jX_i\...`
- `Λ02`; rows `7576017` -> `458556`; endpoint alignment `both`; same source `False`.
  source: `tX_{t}=tU_{x}\`
  target: `N_{z}=1`

#### `Λ03`
- `Λ03`; rows `1757626` -> `696113`; endpoint alignment `both`; same source `False`.
  source: `H(t,y)=E[h_{ij}(t,y)]`
  target: `pr_a(b) := q[a,b](t)`
- `Λ03`; rows `3121794` -> `170857`; endpoint alignment `both`; same source `False`.
  source: `c_{n/2}=0`
  target: `\nh_0v_{l}=lv_{l},\\quad f_0^{l+1}v_{l}=e_1^{k-l+1}v_{l}=f_{i}v_{l}=e_{i+1}v_{l}=h_iv_{l}=0,\n\\qquad i\\in \\Z_{<0},\n\`
- `Λ03`; rows `3681851` -> `170857`; endpoint alignment `both`; same source `False`.
  source: `r_{+}=r_{m}`
  target: `\nh_0v_{l}=lv_{l},\\quad f_0^{l+1}v_{l}=e_1^{k-l+1}v_{l}=f_{i}v_{l}=e_{i+1}v_{l}=h_iv_{l}=0,\n\\qquad i\\in \\Z_{<0},\n\`
- `Λ03`; rows `6111909` -> `170857`; endpoint alignment `both`; same source `False`.
  source: `C(z)=x_1zL(u,v)x_2x_3y_1x_1`
  target: `\nh_0v_{l}=lv_{l},\\quad f_0^{l+1}v_{l}=e_1^{k-l+1}v_{l}=f_{i}v_{l}=e_{i+1}v_{l}=h_iv_{l}=0,\n\\qquad i\\in \\Z_{<0},\n\`

#### `Λ04`
- `Λ04`; rows `344585` -> `344584`; endpoint alignment `both`; same source `True`.
  source: `\\gamma m_e c^2 >> q_e U`
  target: `\\gamma m_e c^2 >> q_e U`
- `Λ04`; rows `3417276` -> `1011782`; endpoint alignment `both`; same source `False`.
  source: `c(t)=(q_1(t),p_1(t),q_2(t),p_2(t))`
  target: `[Q_i,P_j]=0`
- `Λ04`; rows `3417276` -> `1011783`; endpoint alignment `both`; same source `False`.
  source: `c(t)=(q_1(t),p_1(t),q_2(t),p_2(t))`
  target: `[Q_i,P_j]=0`
- `Λ04`; rows `3417278` -> `1011782`; endpoint alignment `both`; same source `False`.
  source: `c(t)=(q_1(t),p_1(t),q_2(t),p_2(t))`
  target: `[Q_i,P_j]=0`

#### `Λ05`
- `Λ05`; rows `9471935` -> `888608`; endpoint alignment `both`; same source `False`.
  source: `X_3^e=GM/r_e`
  target: `f_T(x)=C_ji_{x_j}`
- `Λ05`; rows `387533` -> `31292`; endpoint alignment `both`; same source `False`.
  source: `\n U=e^{-tH}+G_+dte^{-tH}\n \`
  target: `\n\\sum_{k=1}^M \\sum_{s=1}^{L_U } \\sum_{q=1}^{L_V }l_{ksq}^{UV} =N.\n`
- `Λ05`; rows `387534` -> `31292`; endpoint alignment `both`; same source `False`.
  source: `\n U=e^{-tH}+G_+dte^{-tH}\n \`
  target: `\n\\sum_{k=1}^M \\sum_{s=1}^{L_U } \\sum_{q=1}^{L_V }l_{ksq}^{UV} =N.\n`
- `Λ05`; rows `387534` -> `31293`; endpoint alignment `both`; same source `False`.
  source: `\n U=e^{-tH}+G_+dte^{-tH}\n \`
  target: `\n\\sum_{k=1}^M \\sum_{s=1}^{L_U } \\sum_{q=1}^{L_V }l_{ksq}^{UV} =N.\n`

#### `Λ06`
- `Λ06`; rows `2821893` -> `2249`; endpoint alignment `both`; same source `False`.
  source: `G(x)(G^\\bot(x))^* = f_{1}(x)^m . . . . f_{s}(x)^mh_{1}(x)^mh_{1}^*(x)^m . . . . h_{t}(x)^mh_{t}^*(x)^m = ({x^n}+1)^m = 0`
  target: `\nN_1^{\\pm}|_{1D} =\n\\sum\\limits_{k_z\\ne 0}^{10} f(T_c^0|_{1D}, E_{k_z}^0)=1.8\\cdot 10^4 <N|_{1D}\n`
- `Λ06`; rows `2821893` -> `2250`; endpoint alignment `both`; same source `False`.
  source: `G(x)(G^\\bot(x))^* = f_{1}(x)^m . . . . f_{s}(x)^mh_{1}(x)^mh_{1}^*(x)^m . . . . h_{t}(x)^mh_{t}^*(x)^m = ({x^n}+1)^m = 0`
  target: `\nN_1^{\\pm}|_{1D} =\n\\sum\\limits_{k_z\\ne 0}^{10} f(T_c^0|_{1D}, E_{k_z}^0)=1.8\\cdot 10^4 <N|_{1D}\n`
- `Λ06`; rows `2821894` -> `2249`; endpoint alignment `both`; same source `False`.
  source: `G(x)(G^\\bot(x))^* = f_{1}(x)^m . . . . f_{s}(x)^mh_{1}(x)^mh_{1}^*(x)^m . . . . h_{t}(x)^mh_{t}^*(x)^m = ({x^n}+1)^m = 0`
  target: `\nN_1^{\\pm}|_{1D} =\n\\sum\\limits_{k_z\\ne 0}^{10} f(T_c^0|_{1D}, E_{k_z}^0)=1.8\\cdot 10^4 <N|_{1D}\n`
- `Λ06`; rows `2821894` -> `2250`; endpoint alignment `both`; same source `False`.
  source: `G(x)(G^\\bot(x))^* = f_{1}(x)^m . . . . f_{s}(x)^mh_{1}(x)^mh_{1}^*(x)^m . . . . h_{t}(x)^mh_{t}^*(x)^m = ({x^n}+1)^m = 0`
  target: `\nN_1^{\\pm}|_{1D} =\n\\sum\\limits_{k_z\\ne 0}^{10} f(T_c^0|_{1D}, E_{k_z}^0)=1.8\\cdot 10^4 <N|_{1D}\n`

#### `Λ07`
- `Λ07`; rows `6926502` -> `498436`; endpoint alignment `both`; same source `False`.
  source: `{z}_{2}^{m}=0`
  target: `c_1(E) = aC_0 + bF`
- `Λ07`; rows `992124` -> `611282`; endpoint alignment `both`; same source `False`.
  source: `\n-3b_1A^2+12c_1 F A^2+dB^2+2e FB^2+4e ABG=0\\,,\n\`
  target: `d(p_1+p_2)=d(p_1)+d(p_2)`
- `Λ07`; rows `992128` -> `611282`; endpoint alignment `both`; same source `False`.
  source: `\n-3b_1A^2+12c_1 F A^2+dB^2+2e FB^2+4e ABG=0\\,,\n\`
  target: `d(p_1+p_2)=d(p_1)+d(p_2)`
- `Λ07`; rows `1840542` -> `611281`; endpoint alignment `both`; same source `False`.
  source: `g_1f=g_2f`
  target: `d(p_1+p_2)=d(p_1)+d(p_2)`

#### `Λ08`
- `Λ08`; rows `1277065` -> `181578`; endpoint alignment `both`; same source `False`.
  source: `\n=u^2wu+uwu^2+wu^3-u^3v-u^3w-u^2wu=uwu^2+wu^3-u^3v-u^3w,\n\`
  target: `u(x,Q^2)=u_v(x,Q^2)+u_s(x,Q^2)`
- `Λ08`; rows `1757030` -> `92183`; endpoint alignment `both`; same source `False`.
  source: `\n2 \\p \\a' m_q = M = U_0 - U_T\n\`
  target: `v_x(x,0)=(a (u_{-1})_x+b (u_{-1})_t)_x=-(b (u_{-1})_{xt}+\n c (u_{-1})_{tt})=-b u_x-c u_t=f(x)`
- `Λ08`; rows `11023433` -> `1149010`; endpoint alignment `both`; same source `False`.
  source: `\\cup_{j=1}^{k} S^*_j = T`
  target: `Cf_j=f_j`
- `Λ08`; rows `1298363` -> `1298364`; endpoint alignment `both`; same source `True`.
  source: `m_0[a,b]=b-a`
  target: `m_q[a,b]=\\int_{a}^{b}1_{[a,b]}d_qx=(b-a)+qa-q^lb`

#### `Λ09`
- `Λ09`; rows `1126521` -> `2203332`; endpoint alignment `both`; same source `False`.
  source: `H:=L^2_w(0,1)`
  target: `uxu^*=y`
- `Λ09`; rows `3951783` -> `2302614`; endpoint alignment `both`; same source `False`.
  source: `w_{M}=0`
  target: `b\'_k:=d(z_k, y\'_k)`
- `Λ09`; rows `13188854` -> `1435004`; endpoint alignment `both`; same source `False`.
  source: `x_1=0)`
  target: `\nH_{n} & =G_{n}C_{n}^{*},\`
- `Λ09`; rows `13188854` -> `1435005`; endpoint alignment `both`; same source `False`.
  source: `x_1=0)`
  target: `\nH_{n} & =G_{n}C_{n}^{*},\`

#### `Λ10`
- `Λ10`; rows `2203332` -> `1126521`; endpoint alignment `both`; same source `False`.
  source: `uxu^*=y`
  target: `H:=L^2_w(0,1)`
- `Λ10`; rows `234934` -> `111716`; endpoint alignment `both`; same source `False`.
  source: `c_{Y^3}=c_{Z^3}=c_{W^3}=c_{X^2 Y}=c_{XY^2}=c_{Z^2W}=c_{ZW^2}=0`
  target: `V_y=V_z=0`
- `Λ10`; rows `234947` -> `111716`; endpoint alignment `both`; same source `False`.
  source: `c_{X^3} = c_{X^2Y} = c_{XY^2} = c_{Y^3} = c_{Z^3} = c_{Z^2W} = 0`
  target: `V_y=V_z=0`
- `Λ10`; rows `370201` -> `111716`; endpoint alignment `both`; same source `False`.
  source: `\n-(g_{ij}g_{jk})^*w_i+g_{ik}^*w_i=g_{ik}^*(w_i-(g_{ij}g_{jk}g_{ki})^*w_i)=\ng_{ik}^*(w_i-c_{ijk}^*w_i)=c_{ijk}^{-1}dc_{ijk}\n`
  target: `V_y=V_z=0`

#### `Λ11`
- `Λ11`; rows `145875` -> `243251`; endpoint alignment `both`; same source `False`.
  source: `X^1_{(0)}=0={}^-V_{(0)1}`
  target: `k=(z_{-}/z_{+})^{2}=0`
- `Λ11`; rows `451255` -> `80711`; endpoint alignment `both`; same source `False`.
  source: `\\widehat{X}^{g} = (p, x_{i})`
  target: `\\tilde{J}^2=J^2`
- `Λ11`; rows `1034246` -> `243251`; endpoint alignment `both`; same source `False`.
  source: `\nx A\'_n(x) + (2 + x) A_n(x) &=& - B_{n-1}(x) , \ \\\\\n2P_n(x) + 3 M_n(x) + 2 Q_n(x) &=& 2 N_{n-1}(x),\n\`
  target: `k=(z_{-}/z_{+})^{2}=0`
- `Λ11`; rows `1099418` -> `243251`; endpoint alignment `both`; same source `False`.
  source: `m_2(a,b) + (-1)^{|a|'|b|'}m_2(b,a)=0`
  target: `k=(z_{-}/z_{+})^{2}=0`

### tau

#### `T00`
- `T00`; rows `20` -> `21`; endpoint alignment `both`; same source `True`.
  source: `v=v_{n,i}`
  target: `v=v_{n,i}`
- `T00`; rows `21` -> `22`; endpoint alignment `both`; same source `True`.
  source: `v=v_{n,i}`
  target: `v=v_{n,i}`
- `T00`; rows `22` -> `23`; endpoint alignment `both`; same source `True`.
  source: `v=v_{n,i}`
  target: `v=v_{n,i}`
- `T00`; rows `133` -> `134`; endpoint alignment `both`; same source `True`.
  source: `r=r_{0}`
  target: `r=r_{0}`

#### `T01`
- `T01`; rows `9529` -> `9530`; endpoint alignment `both`; same source `True`.
  source: `GL(2,\\mathbb{Z})=\\langle A,B,R | A^2=B^3,\nA^4=R^2={(RA)}^2={(RB)}^2=1 \\rangle,\`
  target: `SL(2,\\mathbb{Z})=\\langle\nA,B | A^2=B^3, A^4=1 \\rangle.\`
- `T01`; rows `11462` -> `11464`; endpoint alignment `both`; same source `True`.
  source: `\\alpha _n(g_i)=g_{n-i}`
  target: `\\beta _n(g_i)=g_i`
- `T01`; rows `17130` -> `17128`; endpoint alignment `both`; same source `True`.
  source: `c_{na}(k,x)=1`
  target: `c_{na}(k,x)=1`
- `T01`; rows `25219` -> `25217`; endpoint alignment `both`; same source `True`.
  source: `\n ~~~ Z^j &=& A_j r^j + B_j,\\\\\n \\mbox{For} ~ \\lambda = 0, ~~~ \\mbox{and}~~~~ && \ \\\\\n ~~~ Z^j &=& C_j -\\frac{1}{\\lambda_j}\\log \\mid r^j - R^j \\mid,\\\\\n \\mbox{For} ~ \\lambda \\neq 0,~~~~~~~~~~~~ && \...`
  target: `\n ~~~ Z^j &=& A_j r^j + B_j,\\\\\n \\mbox{For} ~ \\lambda = 0, ~~~ \\mbox{and}~~~~ && \ \\\\\n ~~~ Z^j &=& C_j -\\frac{1}{\\lambda_j}\\log \\mid r^j - R^j \\mid,\\\\\n \\mbox{For} ~ \\lambda \\neq 0,~~~~~~~~~~~~ && \...`

#### `T02`
- `T02`; rows `352` -> `353`; endpoint alignment `both`; same source `True`.
  source: `\\Delta(V_{555}-I_{814})=0.33`
  target: `B_{Vega}=B_{AB}+0.077`
- `T02`; rows `8665` -> `8662`; endpoint alignment `both`; same source `True`.
  source: `\nG_{r}^{gh^{2}} = L^{G}_{2r}\n\`
  target: `\n[L_m^G,G_r^{gh}]=(m/2-r)G^{gh}_{m+r}\n\`
- `T02`; rows `11461` -> `11462`; endpoint alignment `both`; same source `True`.
  source: `\\beta _n(e_i)=e_i`
  target: `\\alpha _n(g_i)=g_{n-i}`
- `T02`; rows `17129` -> `17130`; endpoint alignment `both`; same source `True`.
  source: `c_{na}(k,x)=1`
  target: `c_{na}(k,x)=1`

#### `T03`
- `T03`; rows `351` -> `352`; endpoint alignment `both`; same source `True`.
  source: `m_{410}-V_{555}< -0.2`
  target: `\\Delta(V_{555}-I_{814})=0.33`
- `T03`; rows `532` -> `535`; endpoint alignment `both`; same source `True`.
  source: `\nQ=(A-B C^{-1} B^T)^{-1}\n\`
  target: `\n\\Psi= C^{-1} +C^{-1}B^TQBC^{-1}.\n\`
- `T03`; rows `8659` -> `8665`; endpoint alignment `both`; same source `True`.
  source: `\n[L^G_m, c_n]=-(2m+n)c_{n+m}\n\`
  target: `\nG_{r}^{gh^{2}} = L^{G}_{2r}\n\`
- `T03`; rows `16685` -> `16686`; endpoint alignment `both`; same source `True`.
  source: `\\widetilde\nT_{ij}=(p_iTp_j)`
  target: `\\widetilde\nT_{ij}=(p_iTp_j)`

#### `T04`
- `T04`; rows `11009` -> `11020`; endpoint alignment `both`; same source `True`.
  source: `S(X_n)=0`
  target: `E_i=-E_i`
- `T04`; rows `31403` -> `31404`; endpoint alignment `both`; same source `True`.
  source: `r=r^{'}`
  target: `\\int[x_j(r)x^*_j(r)-y_j(r)y^*_j(r)]dr=1`
- `T04`; rows `57806` -> `57802`; endpoint alignment `both`; same source `True`.
  source: `H=H(A, R)=R_{(r)}`
  target: `H=H(A, R)=R_{(r)}`
- `T04`; rows `57813` -> `57812`; endpoint alignment `both`; same source `True`.
  source: `\nP=P(A,R):=R_{(l)}, \\quad H=H(A,R):=R_{(r)}.\n`
  target: `\nP=P(A,R):=R_{(l)}, \\quad H=H(A,R):=R_{(r)}.\n`

#### `T05`
- `T05`; rows `39899` -> `39900`; endpoint alignment `both`; same source `True`.
  source: `\n\\frac1{2\\pi} \\int dx_1dx_2 F_{12} &=& n_1 \\\\\n\\frac1{2\\pi} \\int dx_3dx_4 F_{34} &=& n_2.\n\`
  target: `\n&& D_1T-isD_2T = 0 \ \\\\\n&& D_3T-iss'D_4T = 0 \ \\\\\n&& D_5T-iss''D_6T = 0 \ \\\\\n&& F_{12}+s'F_{34}+s''F_{56}+s(|T|^2-\\zeta) = 0 \ \\\\\n&& F_{13}-s'F_{24} = 0 \ \\\\\n&& F_{14}+s'F_{23} = 0 \ \\\\\n&& F_{15}-...`
- `T05`; rows `62500` -> `62502`; endpoint alignment `both`; same source `True`.
  source: `\n N_{obs}(D_s) = N_n a_c^{-D_s/d_c}\n\`
  target: `\n N_{obs}(x_c) = N_n a_c^{-x_c/d_c}\n\`
- `T05`; rows `69075` -> `69081`; endpoint alignment `both`; same source `True`.
  source: `\n\\tau (n_1,n_2,n_3) = M_{n_1}M_{n_2}M_{n_3}a^{2n_1}b^{2n_2}c^{2n_3}.\n\`
  target: `\n u_w(z_{1,2}) = 1,\n \`
- `T05`; rows `114582` -> `114583`; endpoint alignment `both`; same source `True`.
  source: `c_{2} = 1`
  target: `c_{1} = - r_{s}`

#### `T06`
- `T06`; rows `9225` -> `9226`; endpoint alignment `both`; same source `True`.
  source: `is diffeomorphic to`
  target: `into`
- `T06`; rows `16545` -> `16552`; endpoint alignment `both`; same source `True`.
  source: `c_f=[2 A(n_f^{eq})^{2/3}/3m_f]^{1/2}`
  target: `X_{b,f}=R_{b,f}/a_{ho}`
- `T06`; rows `41637` -> `41635`; endpoint alignment `both`; same source `True`.
  source: `\n[e_{-2},e_{+1}]=-h_{1}+h_{3}\n\`
  target: `\n[e_{-2},e_{+1}]=-h_{1}+h_{3}\n\`
- `T06`; rows `141866` -> `141868`; endpoint alignment `both`; same source `True`.
  source: `G_{nm} = C_{nm0} g_{0}`
  target: `n=n_{r}+n_{l}`

#### `T07`
- `T07`; rows `32632` -> `32627`; endpoint alignment `both`; same source `True`.
  source: `z_{f}>3`
  target: `z_{f}<3`
- `T07`; rows `69606` -> `69607`; endpoint alignment `both`; same source `True`.
  source: `W(z)=P(z)/Q(z^{-1})`
  target: `W(z)=P(z)/Q(z^{-1})`
- `T07`; rows `69605` -> `69608`; endpoint alignment `both`; same source `True`.
  source: `W(z)=P(z)/Q(z^{-1})`
  target: `W(z)=P(z)/Q(z^{-1})`
- `T07`; rows `168299` -> `168300`; endpoint alignment `both`; same source `True`.
  source: `W(z)=P(z)/Q(z^{-1})`
  target: `W(z)=P(z)/Q(z^{-1})`

### gamma

#### `Γ00`
- `Γ00`; rows `5173473` -> `5173471`; endpoint alignment `both`; same source `True`.
  source: `\n\\Sing(T)=V(y_1,t_u^3+y_3,t_u)\\\\\n\\Sing(U)=V(y_2,1+u_t^3y_3,u_v).\n\`
  target: `\n\\Sing(T)=V(y_1,t_u^3+y_3,t_u)\\\\\n\\Sing(U)=V(y_2,1+u_t^3y_3,u_v).\n\`
- `Γ00`; rows `10199647` -> `10199650`; endpoint alignment `both`; same source `True`.
  source: `\\forall f = (f_{h}, f_{3})`
  target: `\\forall f = (f_{h}, f_{3})`
- `Γ00`; rows `2130464` -> `2130461`; endpoint alignment `both`; same source `True`.
  source: `u|_{t=0} = f`
  target: `u|_{t=0} = f`
- `Γ00`; rows `1818645` -> `1818649`; endpoint alignment `both`; same source `True`.
  source: `W= k_x x + k_yy + G(z)`
  target: `W= k_x x + k_yy + G(z)`

#### `Γ01`
- `Γ01`; rows `5295366` -> `5295367`; endpoint alignment `both`; same source `True`.
  source: `\n[u(x_r), P_3] = 0.\n`
  target: `\n[u(x_r), P_3] = 0.\n`
- `Γ01`; rows `2608786` -> `304358`; endpoint alignment `both`; same source `False`.
  source: `\nh(u) = u + 1 + O(1/u^2).\n`
  target: `V(q)=q^{-2}`
- `Γ01`; rows `7470155` -> `7470154`; endpoint alignment `both`; same source `True`.
  source: `\\lambda=120h^{-1}`
  target: `\\lambda=120h^{-1}`
- `Γ01`; rows `5641502` -> `5641501`; endpoint alignment `both`; same source `True`.
  source: `\\omega_2(x)=e^{-2V(x)}`
  target: `\\omega_2(x)=e^{-2V(x)}`

#### `Γ02`
- `Γ02`; rows `6111909` -> `170857`; endpoint alignment `both`; same source `False`.
  source: `C(z)=x_1zL(u,v)x_2x_3y_1x_1`
  target: `\nh_0v_{l}=lv_{l},\\quad f_0^{l+1}v_{l}=e_1^{k-l+1}v_{l}=f_{i}v_{l}=e_{i+1}v_{l}=h_iv_{l}=0,\n\\qquad i\\in \\Z_{<0},\n\`
- `Γ02`; rows `645418` -> `29701`; endpoint alignment `both`; same source `False`.
  source: `\n(T_i+1)(T_i-q)&=0 \\\\\nT_iT_j & =T_jT_i\\quad (\\textrm{when } \\left\\vert i-j\\right\\vert >1) \\\\\nT_iT_{i+1}T_i & =T_{i+1}T_iT_{i+1}\\\\\nX_iX_j & =X_jX_i\\\\\nX_iX_i^{-1}&=X_i^{-1}X_i=1\\\\\nX_iT_j & =T_jX_i\...`
  target: `\\alpha=k_{f}=k_{r}=0`
- `Γ02`; rows `2834956` -> `2834955`; endpoint alignment `both`; same source `True`.
  source: `s_{ij} Y_{i, k} = Y_{j, k} s_{ij}`
  target: `s_{ij} Y_{i, k} = Y_{j, k} s_{ij}`
- `Γ02`; rows `9978091` -> `2704782`; endpoint alignment `both`; same source `False`.
  source: `U_j(y)=V_1(y)=0`
  target: `U_j(y)=V_1(y)=0`

#### `Γ03`
- `Γ03`; rows `4619954` -> `4619960`; endpoint alignment `both`; same source `True`.
  source: `|E|=e_1,|G|=e_2`
  target: `|E|=e_1,|G|=e_2`
- `Γ03`; rows `1011568` -> `1011569`; endpoint alignment `both`; same source `True`.
  source: `y_n>0`
  target: `y_n>0`
- `Γ03`; rows `13209987` -> `13209989`; endpoint alignment `both`; same source `True`.
  source: `\\rho(z_0,x_0)>p+R`
  target: `\\rho(z_0,x_0)>p+R`
- `Γ03`; rows `10319043` -> `10319045`; endpoint alignment `both`; same source `True`.
  source: `\\pi_0(t)=t_{T}`
  target: `\\pi_0(t)=t_{T}`

#### `Γ04`
- `Γ04`; rows `2405590` -> `2405591`; endpoint alignment `both`; same source `True`.
  source: `P= (p_{ij})`
  target: `P= (p_{ij})`
- `Γ04`; rows `8884071` -> `8884070`; endpoint alignment `both`; same source `True`.
  source: `C_2(G)=N_c+1`
  target: `C_2(G)=N_c-2`
- `Γ04`; rows `10728106` -> `290659`; endpoint alignment `both`; same source `False`.
  source: `t>T_1`
  target: `{\\bf x} = x_1 {\\bf a_1} + x_2 {\\bf a_2} + x_3 {\\bf a_3}`
- `Γ04`; rows `1158573` -> `1158574`; endpoint alignment `both`; same source `True`.
  source: `\\varphi_1(fg)=\\varphi_1(f)\\varphi_1(g), \\ \\ \\ \\varphi_2(fg)=\\varphi_2(f)\\varphi_1(g)+(-1)^{p(f)}\\varphi_1(f)\\varphi_2(g)`
  target: `\\varphi_1(fg)=\\varphi_1(f)\\varphi_1(g), \\ \\ \\ \\varphi_2(fg)=\\varphi_2(f)\\varphi_1(g)+(-1)^{p(f)}\\varphi_1(f)\\varphi_2(g)`

#### `Γ05`
- `Γ05`; rows `10818634` -> `39213`; endpoint alignment `both`; same source `False`.
  source: `p_1^2=p_2^2=m_Q^2`
  target: `x_q =\nx_{bj}`
- `Γ05`; rows `1454840` -> `341194`; endpoint alignment `both`; same source `False`.
  source: `\nu_{tt}=u_{xx},\n\`
  target: `\nu_t=u_{xxx}+3uu_x\n\`
- `Γ05`; rows `13396224` -> `170714`; endpoint alignment `both`; same source `False`.
  source: `{\\cal R}_k=-1`
  target: `cv+u-a=cv+u-ec^2-fc-g`
- `Γ05`; rows `3307382` -> `419100`; endpoint alignment `both`; same source `False`.
  source: `-\\nabla^2 u = f(x)`
  target: `\nH=H_a+V_a=H_b+V_b \n`

#### `Γ06`
- `Γ06`; rows `12417007` -> `958802`; endpoint alignment `both`; same source `False`.
  source: `T_{max}<+\\infty`
  target: `\\chi = \\frac{1}{2}m|v -\nu(r,t)|^2`
- `Γ06`; rows `3077056` -> `262956`; endpoint alignment `both`; same source `False`.
  source: `w := w(\\cdot,u^*,u\')`
  target: `x=({\\bf x},x^4)`
- `Γ06`; rows `4320183` -> `375057`; endpoint alignment `both`; same source `False`.
  source: `-\\Delta_x \\int_{M}{G(x,y) f(y) dy} = f(x)`
  target: `\nx(u,\\gamma)-x(w,\\gamma)= \\int_{w}^{u}f(s,x_s(\\gamma))ds \\geq a(u-w) >\na(1+\\delta/2).\n`
- `Γ06`; rows `2578583` -> `375057`; endpoint alignment `both`; same source `False`.
  source: `\nV_{GS}= \\frac{V_{DD}}{T_R}t \n\`
  target: `\nx(u,\\gamma)-x(w,\\gamma)= \\int_{w}^{u}f(s,x_s(\\gamma))ds \\geq a(u-w) >\na(1+\\delta/2).\n`

#### `Γ07`
- `Γ07`; rows `6926502` -> `498436`; endpoint alignment `both`; same source `False`.
  source: `{z}_{2}^{m}=0`
  target: `c_1(E) = aC_0 + bF`
- `Γ07`; rows `1459732` -> `611282`; endpoint alignment `both`; same source `False`.
  source: `L_{1}=L_{T} \`
  target: `d(p_1+p_2)=d(p_1)+d(p_2)`
- `Γ07`; rows `1757647` -> `601104`; endpoint alignment `both`; same source `False`.
  source: `X=X_1+X_2`
  target: `||g'(x)||_H=s`
- `Γ07`; rows `11552620` -> `3046712`; endpoint alignment `both`; same source `False`.
  source: `\n\\Gamma^0_{i0}=N^{-1}\\partial_iN-\\frac{1}{4}N^{-2}\\partial_i\\{g(\\beta,\\beta)\\}-\\frac{1}{2}N^{-2}\\beta^l\\cdot{}^t\\nabla_l\\beta^pg_{pi}+\\frac{1}{2}N^{-2}\\beta^l\\partial_tg_{il};\n\`
  target: `p=c_{s}^{2}\\Sigma`

#### `Γ08`
- `Γ08`; rows `10289499` -> `31293`; endpoint alignment `both`; same source `False`.
  source: `v=v_0`
  target: `\n\\sum_{k=1}^M \\sum_{s=1}^{L_U } \\sum_{q=1}^{L_V }l_{ksq}^{UV} =N.\n`
- `Γ08`; rows `6906184` -> `31292`; endpoint alignment `both`; same source `False`.
  source: `\nmg_1 = g_4.\n`
  target: `\n\\sum_{k=1}^M \\sum_{s=1}^{L_U } \\sum_{q=1}^{L_V }l_{ksq}^{UV} =N.\n`
- `Γ08`; rows `10289499` -> `31292`; endpoint alignment `both`; same source `False`.
  source: `v=v_0`
  target: `\n\\sum_{k=1}^M \\sum_{s=1}^{L_U } \\sum_{q=1}^{L_V }l_{ksq}^{UV} =N.\n`
- `Γ08`; rows `4724482` -> `232320`; endpoint alignment `both`; same source `False`.
  source: `C_i=(Z_i k_BT_e/m_i)^{1/2}`
  target: `\\Hom(X_i,X_j[m])=\n \\Hom(\\Omega^{n_i}F(S_i),\\Omega^{n_j}F(S_j)[m+n_j-n_i])`

#### `Γ09`
- `Γ09`; rows `9208714` -> `4611058`; endpoint alignment `both`; same source `False`.
  source: `\\gamma=g(x_0,y_0)`
  target: `x_i=h_ix_0\\frac{r_1}{r_2}`
- `Γ09`; rows `537825` -> `978530`; endpoint alignment `both`; same source `False`.
  source: `P^{(1)}=\\mu^{(1)}_3 + w_2 \\mu^{(1)}_2 + w_2 w_1 \\mu^{(1)}_1`
  target: `\nB_{xu} = T_xB_u,\n\\qquad\\qquad\nB_{yu} = T_yB_u,\n\`
- `Γ09`; rows `10105310` -> `1818646`; endpoint alignment `both`; same source `False`.
  source: `\n V_2 = V_{\\rm elastic} + V_{\\rm curvature} + V_{\\rm interaction} + V_{\\rm coupling},\n\`
  target: `W= k_x x + k_yy + G(z)`
- `Γ09`; rows `6132832` -> `351959`; endpoint alignment `both`; same source `False`.
  source: `\\mathcal{L}_\\mathrm{m}=-P=- \\frac{p_r +2 p_t}{3}`
  target: `\nds^2=\\frac{b^2-c^2+(bR-cS)}{(1+b R+c S)^2}(\\frac{dR^2}{R^2-1}+\\frac{dS^2}{1-S^2})\n`

#### `Γ10`
- `Γ10`; rows `10784547` -> `1459734`; endpoint alignment `both`; same source `False`.
  source: `\\text{det}(M(z)) = (a+b+c)(a^2+b^2+c^2-ab-ac-bc)`
  target: `L_{1}=L_{T} \`
- `Γ10`; rows `10778012` -> `748616`; endpoint alignment `both`; same source `False`.
  source: `\\chi (A)=det(tI_n-A)`
  target: `a_*b_*c_*=Z`
- `Γ10`; rows `748679` -> `748603`; endpoint alignment `both`; same source `True`.
  source: `a=a_*Z^{-5},b=b_*,c=c_*Z^4`
  target: `a_*b_*c_*=Z`
- `Γ10`; rows `748603` -> `748617`; endpoint alignment `both`; same source `True`.
  source: `a_*b_*c_*=Z`
  target: `a_*b_*c_*=Z`

#### `Γ11`
- `Γ11`; rows `10018951` -> `648872`; endpoint alignment `both`; same source `False`.
  source: `\\rho_{s} = \\rho_{l}(1+\\Delta\\rho^{*})`
  target: `L = \\log\\det(u_{ij})= -\\log \\xi + \\log(-\\log \\xi) + \\log(-B') +\n \\log \\rho^{2} + \\log \\Delta`

## Scope

Examples attach original source equation cards to V2 symbolic-language assignments through conservative source-card/V2-row alignment. They support inspection and decoder conditioning; they do not prove physical equivalence or exact mechanism reconstruction.
