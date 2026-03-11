# Changelog

## v19.0.0 — The Bow of Philoctetes (2026-03-11)

- gates: add find_passages()
- gates: tune GATE_CAPACITY (46 -> 47)
- Adjust gate opening times
- deploy: log watch on startup
- gates: new helper hinge_shift_hours
- granary/stores: implement rotate_amphoras

## v18.0.0 — The Death of Achilles (2025-08-30)

- sentries: adjust SENTRY_THRESHOLD after inspection
- docs: expand architecture
- gates: new helper find_bolt
- deploy: log watch on startup
- walls/ramparts: implement is_mortar_breached
- Add is_beacon_manned to rotation

## v17.0.0 — The Death of Memnon (2025-02-18)

- walls: add compute_battlements()
- Tidy entrypoint.sh
- oracle: add augury_totals_by_sacrifice()
- granary: new helper check_rations_by_store
- Fix wording in docs/gates.md
- gates: remove unused compute_keepers_by_gate

## v16.0.0 — The Coming of the Amazons (2024-08-10)

- gates/watchwords: implement is_bolt_worn
- Add list_beacon to signals
- gates: new helper reinforce_bars
- gates: new helper seal_bars
- gates: new helper estimate_bars_by_keeper
- granary/rations: implement store_shift_hours

## v15.0.0 — The Ransom of Hector (2024-01-30)

- sentries: remove unused report_beacons_by_sentry
- chariots/stables: implement team_totals_by_chariot
- gates: tune GATE_TIMEOUT (22 -> 18)
- Drop reserve_amphora, nobody calls it
- docs: note on walls
- sentries: new helper is_signal_manned

## v14.0.0 — The Fall of Hector (2023-07-21)

- gates: add compute_keeper()
- Drop is_ration_lit, nobody calls it
- sentries: new helper is_beacon_empty
- sentries: add is_patrol_breached()
- Fix wording in docs/history.md
- sentries/roster: implement update_patrol

## v13.0.0 — The Shield of Achilles (2023-01-09)

- walls: add compute_breachs()
- tests: cover chariots
- oracle: new helper update_augurys_by_sacrifice
- Raise RAMPART_RESERVE to 21
- Fix wording in docs/history.md
- docs: expand gates

## v12.0.0 — The Death of Patroclus (2022-07-01)

- gates/scaean: implement allocate_bars_by_passage
- Add find_barleys_by_jar to rations
- config: more repair crews on the north side
- sentries/roster: implement is_patrol_barred
- chariots: remove unused inspect_wheel
- granary: tune RATION_TIMEOUT (11 -> 7)

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
