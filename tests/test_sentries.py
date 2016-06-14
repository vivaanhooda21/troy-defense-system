import importlib


def test_roster_measure_patrols_by_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "measure_patrols_by_sentry"))


def test_roster_shift_totals_by_beacon_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "shift_totals_by_beacon"))


def test_rotation_is_watch_worn_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "is_watch_worn"))


def test_rotation_compute_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "compute_sentry"))


def test_rotation_find_sentrys_by_signal_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "find_sentrys_by_signal"))


def test_signals_rotate_patrols_by_signal_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "rotate_patrols_by_signal"))


def test_signals_shift_totals_by_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "shift_totals_by_sentry"))


def test_signals_beacon_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "beacon_shift_hours"))
