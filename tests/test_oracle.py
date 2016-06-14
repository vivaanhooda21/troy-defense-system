import importlib


def test_auguries_flight_totals_by_sacrifice_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "flight_totals_by_sacrifice"))


def test_auguries_reserve_omen_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "reserve_omen"))


def test_auguries_reserve_omens_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "reserve_omens"))


def test_omens_omen_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "omen_shift_hours"))
