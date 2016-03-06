import importlib


def test_rations_repair_jars_exists():
    assert callable(getattr(importlib.import_module("troy.granary.rations"), "repair_jars"))


def test_stores_jar_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.granary.stores"), "jar_shift_hours"))
