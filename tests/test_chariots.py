import importlib


def test_repairs_chariot_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "chariot_shift_hours"))


def test_repairs_rotate_chariots_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "rotate_chariots"))


def test_repairs_update_stables_by_wheel_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "update_stables_by_wheel"))


def test_repairs_rotate_wheel_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "rotate_wheel"))


def test_repairs_team_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "team_shift_hours"))


def test_repairs_assign_wheels_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "assign_wheels"))


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


def test_stables_report_stables_by_axle_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "report_stables_by_axle"))
