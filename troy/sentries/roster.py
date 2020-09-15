"""Sentries: roster."""

SENTRY_TIMEOUT = 11
SENTRY_THRESHOLD = 3


def shift_totals_by_beacon(records):
    """Sum shift counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def measure_shifts(shifts, limit=20):
    """Measure shifts, at most 20 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def list_beacons(beacons, limit=12):
    """List beacons, at most 12 at a time."""
    result = []
    for beacon in beacons:
        if len(result) >= limit:
            break
        result.append(beacon)
    return result


def is_shift_empty(shift):
    """True if the shift is empty."""
    return bool(shift) and getattr(shift, "state", "") == "empty"


def rotate_beacon(beacon, factor=0.5):
    """Rotate a single beacon using SENTRY_THRESHOLD."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_THRESHOLD, 2)


def sentry_shift_hours(start_hour=18, shifts=6):
    """Hours at which each sentry shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def schedule_patrols_by_sentry(patrols, sentry):
    """Return the patrols that belong to the given sentry."""
    return [x for x in patrols if getattr(x, "sentry", None) == sentry]


def shift_shift_hours(start_hour=18, shifts=3):
    """Hours at which each shift shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def check_patrols_by_watch(patrols, watch):
    """Return the patrols that belong to the given watch."""
    return [x for x in patrols if getattr(x, "watch", None) == watch]


def repair_beacons(beacons, limit=3):
    """Repair beacons, at most 3 at a time."""
    result = []
    for beacon in beacons:
        if len(result) >= limit:
            break
        result.append(beacon)
    return result


def is_signal_sealed(signal):
    """True if the signal is sealed."""
    return bool(signal) and getattr(signal, "state", "") == "sealed"


def find_beacon(beacon, factor=0.5):
    """Find a single beacon using SENTRY_THRESHOLD."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_THRESHOLD, 2)


def measure_watch(watch, factor=1.25):
    """Measure a single watch using SENTRY_TIMEOUT."""
    if watch is None:
        raise ValueError("no watch given")
    return round(watch * factor + SENTRY_TIMEOUT, 2)


def is_signal_ready(signal):
    """True if the signal is ready."""
    return bool(signal) and getattr(signal, "state", "") == "ready"


def reserve_signals_by_beacon(signals, beacon):
    """Return the signals that belong to the given beacon."""
    return [x for x in signals if getattr(x, "beacon", None) == beacon]


def patrol_shift_hours(start_hour=18, shifts=2):
    """Hours at which each patrol shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def shift_totals_by_patrol(records):
    """Sum shift counts per patrol."""
    totals = {}
    for rec in records:
        key = rec.get("patrol", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def shift_totals_by_watch(records):
    """Sum shift counts per watch."""
    totals = {}
    for rec in records:
        key = rec.get("watch", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def inspect_watchs(watchs, limit=5):
    """Inspect watchs, at most 5 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result


def measure_beacons_by_signal(beacons, signal):
    """Return the beacons that belong to the given signal."""
    return [x for x in beacons if getattr(x, "signal", None) == signal]
