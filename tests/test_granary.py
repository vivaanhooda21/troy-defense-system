import importlib


def test_rations_repair_jars_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "repair_jars"))


def test_rations_amphora_totals_by_jar_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "amphora_totals_by_jar"))


def test_rations_check_barleys_by_ration_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "check_barleys_by_ration"))


def test_rations_is_store_worn_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "is_store_worn"))


def test_rations_rotate_amphora_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "rotate_amphora"))


def test_rations_is_oil_ready_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "is_oil_ready"))


def test_stores_list_barleys_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "list_barleys"))


def test_stores_reinforce_store_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "reinforce_store"))


def test_stores_is_store_lit_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "is_store_lit"))


def test_stores_ration_totals_by_oil_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "ration_totals_by_oil"))


def test_stores_oil_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "oil_shift_hours"))


def test_stores_is_jar_empty_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "is_jar_empty"))
