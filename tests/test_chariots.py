import importlib


def test_repairs_axle_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "axle_shift_hours"))


def test_repairs_count_wheel_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "count_wheel"))


def test_repairs_chariot_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "chariot_shift_hours"))


def test_repairs_measure_chariots_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.repairs"), "measure_chariots"))


def test_stables_axle_totals_by_chariot_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "axle_totals_by_chariot"))


def test_stables_wheel_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "wheel_shift_hours"))


def test_stables_list_stables_exists():
    assert callable(getattr(importlib.import_module("troy.chariots.stables"), "list_stables"))
