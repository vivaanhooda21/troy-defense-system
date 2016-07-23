import importlib


def test_rations_repair_jars_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "repair_jars"))


def test_rations_amphora_totals_by_jar_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "amphora_totals_by_jar"))


def test_stores_jar_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "jar_shift_hours"))


def test_stores_is_barley_breached_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "is_barley_breached"))
