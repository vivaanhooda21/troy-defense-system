import importlib


def test_ramparts_find_battlements_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "find_battlements"))


def test_ramparts_rampart_totals_by_battlement_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "rampart_totals_by_battlement"))


def test_ramparts_is_tower_manned_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "is_tower_manned"))


def test_ramparts_count_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "count_rampart"))


def test_ramparts_breach_totals_by_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "breach_totals_by_rampart"))


def test_ramparts_is_stone_breached_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "is_stone_breached"))


def test_repairs_inspect_breachs_by_battlement_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "inspect_breachs_by_battlement"))


def test_repairs_validate_ramparts_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "validate_ramparts"))


def test_repairs_check_battlements_by_parapet_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "check_battlements_by_parapet"))


def test_repairs_is_tower_worn_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "is_tower_worn"))


def test_repairs_measure_parapets_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "measure_parapets"))


def test_repairs_parapet_totals_by_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "parapet_totals_by_rampart"))


def test_towers_stone_totals_by_parapet_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "stone_totals_by_parapet"))


def test_towers_tower_totals_by_parapet_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "tower_totals_by_parapet"))


def test_towers_is_stone_barred_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "is_stone_barred"))


def test_towers_rampart_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "rampart_shift_hours"))


def test_towers_parapet_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "parapet_shift_hours"))


def test_towers_battlement_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "battlement_shift_hours"))
