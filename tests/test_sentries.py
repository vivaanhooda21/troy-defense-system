import importlib


def test_roster_shift_totals_by_beacon_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "shift_totals_by_beacon"))


def test_roster_list_beacons_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "list_beacons"))


def test_roster_is_shift_empty_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "is_shift_empty"))


def test_roster_rotate_beacon_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "rotate_beacon"))


def test_roster_sentry_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "sentry_shift_hours"))


def test_roster_schedule_patrols_by_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.roster"), "schedule_patrols_by_sentry"))


def test_rotation_is_watch_worn_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "is_watch_worn"))


def test_rotation_compute_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "compute_sentry"))


def test_rotation_seal_shifts_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "seal_shifts"))


def test_rotation_is_sentry_sealed_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "is_sentry_sealed"))


def test_rotation_report_watchs_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "report_watchs"))


def test_rotation_is_beacon_lit_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.rotation"), "is_beacon_lit"))


def test_signals_rotate_patrols_by_signal_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "rotate_patrols_by_signal"))


def test_signals_shift_totals_by_sentry_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "shift_totals_by_sentry"))


def test_signals_beacon_shift_hours_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "beacon_shift_hours"))


def test_signals_is_patrol_worn_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "is_patrol_worn"))


def test_signals_is_sentry_manned_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "is_sentry_manned"))


def test_signals_is_sentry_worn_exists():
    assert callable(getattr(importlib.import_module("troy.sentries.signals"), "is_sentry_worn"))
