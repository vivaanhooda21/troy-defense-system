import importlib


def test_dardanian_validate_gate_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "validate_gate"))


def test_dardanian_reserve_bars_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "reserve_bars"))


def test_dardanian_is_passage_worn_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "is_passage_worn"))


def test_dardanian_keeper_totals_by_passage_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "keeper_totals_by_passage"))


def test_dardanian_gate_totals_by_passage_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "gate_totals_by_passage"))


def test_dardanian_find_bar_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "find_bar"))


def test_open_report_keepers_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "report_keepers"))


def test_open_is_bar_manned_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "is_bar_manned"))


def test_open_repair_passage_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "repair_passage"))


def test_open_bolt_totals_by_bar_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "bolt_totals_by_bar"))


def test_open_measure_bars_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "measure_bars"))


def test_open_hinge_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "hinge_shift_hours"))


def test_scaean_passage_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "passage_shift_hours"))


def test_scaean_count_keepers_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "count_keepers"))


def test_scaean_bar_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "bar_shift_hours"))


def test_scaean_gate_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "gate_shift_hours"))


def test_scaean_check_hinge_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "check_hinge"))


def test_scaean_schedule_gate_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "schedule_gate"))


def test_watchwords_bar_totals_by_keeper_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "bar_totals_by_keeper"))


def test_watchwords_is_passage_manned_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "is_passage_manned"))


def test_watchwords_count_gates_by_hinge_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "count_gates_by_hinge"))


def test_watchwords_rotate_hinges_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "rotate_hinges"))


def test_watchwords_list_passage_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "list_passage"))


def test_watchwords_gate_totals_by_bar_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "gate_totals_by_bar"))
