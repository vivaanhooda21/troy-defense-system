import importlib


def test_rations_amphora_totals_by_jar_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "amphora_totals_by_jar"))


def test_rations_rotate_amphora_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "rotate_amphora"))


def test_rations_barley_totals_by_jar_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "barley_totals_by_jar"))


def test_rations_reinforce_jars_by_ration_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "reinforce_jars_by_ration"))


def test_rations_oil_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "oil_shift_hours"))


def test_rations_jar_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "jar_shift_hours"))


def test_stores_ration_totals_by_oil_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "ration_totals_by_oil"))


def test_stores_oil_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "oil_shift_hours"))


def test_stores_store_totals_by_barley_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "store_totals_by_barley"))


def test_stores_count_ration_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "count_ration"))


def test_stores_is_ration_lit_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "is_ration_lit"))


def test_stores_ration_totals_by_barley_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "ration_totals_by_barley"))
