# Changelog

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
