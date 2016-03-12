import importlib


def test_roster_inspect_shifts_by_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "inspect_shifts_by_sentry"))


def test_rotation_is_watch_worn_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "is_watch_worn"))


def test_signals_rotate_patrols_by_signal_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "rotate_patrols_by_signal"))
