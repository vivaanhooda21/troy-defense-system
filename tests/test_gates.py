import importlib


def test_dardanian_update_gates_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "update_gates"))


def test_dardanian_is_hinge_lit_exists():
    assert callable(getattr(importlib.import_module("troy.gates.dardanian"), "is_hinge_lit"))


def test_open_report_keepers_exists():
    assert callable(getattr(importlib.import_module("troy.gates.open"), "report_keepers"))


def test_scaean_passage_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.gates.scaean"), "passage_shift_hours"))


def test_watchwords_validate_gates_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "validate_gates"))


def test_watchwords_bar_totals_by_keeper_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "bar_totals_by_keeper"))


def test_watchwords_bar_totals_by_hinge_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "bar_totals_by_hinge"))


def test_watchwords_is_passage_manned_exists():
    assert callable(getattr(importlib.import_module("troy.gates.watchwords"), "is_passage_manned"))
