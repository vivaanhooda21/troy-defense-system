import importlib


def test_repairs_count_wheel_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "count_wheel"))


def test_repairs_chariot_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "chariot_shift_hours"))


def test_repairs_report_teams_by_axle_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "report_teams_by_axle"))


def test_repairs_rotate_chariots_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "rotate_chariots"))


def test_repairs_inspect_wheel_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "inspect_wheel"))


def test_repairs_update_stables_by_wheel_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "update_stables_by_wheel"))


def test_stables_axle_totals_by_chariot_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "axle_totals_by_chariot"))


def test_stables_wheel_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "wheel_shift_hours"))


def test_stables_list_stables_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "list_stables"))


def test_stables_allocate_axles_by_chariot_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "allocate_axles_by_chariot"))


def test_stables_is_axle_lit_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "is_axle_lit"))


def test_stables_record_axles_by_stable_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "record_axles_by_stable"))
