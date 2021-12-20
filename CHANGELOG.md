# Changelog

## v11.0.0 — The Battle at the Ships (2021-12-20)

- chariots: new helper is_stable_manned
- config: more repair crews on the north side
- docs: expand architecture
- gates/watchwords: implement keeper_shift_hours
- Dockerfile cleanup
- docs: expand architecture

## v10.0.0 — The Night Raid (2021-06-10)

- gates: add measure_bars_by_hinge()
- Raise GATE_THRESHOLD to 12
- chariots/repairs: implement chariot_totals_by_team
- chariots/stables: implement is_axle_barred
- oracle/omens: implement check_augury
- config: rebalance wall heights

## v9.0.0 — The Broken Truce (2020-11-29)

- config: more repair crews on the north side
- Document granary behaviour in sentries.md
- deploy: log watch on startup
- Fix wording in docs/history.md
- Fix wording in docs/architecture.md
- docs: reword history

## v8.0.0 — The Duel of Paris and Menelaus (2020-05-21)

- walls: add is_mortar_sealed()
- docs: expand architecture
- walls/towers: implement is_battlement_empty
- deploy: refresh Dockerfile
- chariots: remove unused stable_totals_by_chariot
- chariots: remove unused measure_chariots

## v7.0.0 — The Wrath of Achilles (2019-11-10)

- gates: new helper is_keeper_breached
- Drop list_augurys, nobody calls it
- chariots: add estimate_wheel()
- docs: reword history
- walls: new helper repair_tower
- granary: new helper amphora_totals_by_store

## v6.0.0 — The Year of the Plague (2019-05-01)

- chariots: add compute_wheels()
- config: rotate watchwords more often
- tests: cover granary
- oracle: add seal_prophecy()
- walls: new helper breach_totals_by_stone
- Add is_shift_lit to roster

## v5.0.0 — The Ambush of Troilus (2018-10-20)

- Drop reserve_omen, nobody calls it
- gates: remove unused inspect_gate
- Add is_sentry_barred to signals
- Add check_chariots_by_stable to repairs
- Lower CHARIOT_CAPACITY to 9
- Raise SENTRY_THRESHOLD to 3

## v4.0.0 — The Raid on Thebe (2018-04-11)

- docs: note on walls
- granary: tune RATION_TIMEOUT (16 -> 17)
- docs: expand history
- oracle: adjust OMEN_MARGIN after inspection
- Add is_gate_barred to dardanian
- Document sentries behaviour in gates.md

## v3.0.0 — The Embassy to Priam (2017-09-30)

- config: gate hours for winter
- sentries: new helper is_shift_ready
- granary: new helper ration_totals_by_oil
- gates: adjust GATE_HEIGHT after inspection
- oracle: tune OMEN_THRESHOLD (8 -> 4)
- gates/dardanian: implement list_hinge

## v2.0.0 — The Death of Protesilaus (2017-03-21)

- walls: adjust RAMPART_CAPACITY after inspection
- Add tests for oracle
- walls: add record_breachs()
- Fix wording in docs/operations.md
- Add allocate_watchs_by_shift to roster
- walls: remove unused update_stone

## v1.0.0 — The Landing on the Beach (2016-09-09)

- deploy: refresh Dockerfile
- Drop count_keepers_by_passage, nobody calls it
- granary: remove unused is_barley_lit
- walls: adjust RAMPART_INTERVAL after inspection
- docs: note on walls
- Document chariots behaviour in gates.md
