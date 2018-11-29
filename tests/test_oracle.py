import importlib


def test_auguries_reserve_omen_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "reserve_omen"))


def test_auguries_reserve_omens_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "reserve_omens"))


def test_auguries_reserve_prophecys_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "reserve_prophecys"))


def test_auguries_is_omen_worn_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "is_omen_worn"))


def test_auguries_is_prophecy_barred_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "is_prophecy_barred"))


def test_auguries_seal_sacrifices_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.auguries"), "seal_sacrifices"))


def test_omens_omen_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "omen_shift_hours"))


def test_omens_check_prophecys_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "check_prophecys"))


def test_omens_augury_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "augury_shift_hours"))


def test_omens_repair_flights_by_prophecy_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "repair_flights_by_prophecy"))


def test_omens_omen_totals_by_sacrifice_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "omen_totals_by_sacrifice"))


def test_omens_prophecy_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.oracle.omens"), "prophecy_shift_hours"))
