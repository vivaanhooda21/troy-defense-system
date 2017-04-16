import importlib


def test_rations_repair_jars_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "repair_jars"))


def test_rations_amphora_totals_by_jar_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "amphora_totals_by_jar"))


def test_rations_check_barleys_by_ration_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "check_barleys_by_ration"))


def test_rations_compute_stores_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "compute_stores"))


def test_rations_find_stores_by_amphora_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "find_stores_by_amphora"))


def test_rations_jar_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "jar_shift_hours"))


def test_stores_jar_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "jar_shift_hours"))


def test_stores_is_barley_breached_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "is_barley_breached"))


def test_stores_list_stores_by_amphora_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "list_stores_by_amphora"))


def test_stores_list_barleys_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "list_barleys"))


def test_stores_is_store_ready_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "is_store_ready"))


def test_stores_reinforce_store_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "reinforce_store"))
