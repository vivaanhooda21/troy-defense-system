import importlib


def test_ramparts_find_battlements_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "find_battlements"))


def test_ramparts_rampart_totals_by_battlement_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "rampart_totals_by_battlement"))


def test_ramparts_is_tower_manned_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "is_tower_manned"))


def test_ramparts_count_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "count_rampart"))


def test_ramparts_mortar_totals_by_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "mortar_totals_by_rampart"))


def test_ramparts_breach_totals_by_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.ramparts"), "breach_totals_by_rampart"))


def test_repairs_report_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "report_rampart"))


def test_repairs_inspect_breachs_by_battlement_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "inspect_breachs_by_battlement"))


def test_repairs_record_breachs_exists():
    assert callable(getattr(importlib.import_module("troy.walls.repairs"), "record_breachs"))


def test_towers_is_breach_empty_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "is_breach_empty"))


def test_towers_list_towers_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "list_towers"))


def test_towers_count_stone_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "count_stone"))


def test_towers_seal_mortar_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "seal_mortar"))


def test_towers_battlement_totals_by_rampart_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "battlement_totals_by_rampart"))


def test_towers_stone_totals_by_parapet_exists():
    assert callable(getattr(importlib.import_module("troy.walls.towers"), "stone_totals_by_parapet"))
