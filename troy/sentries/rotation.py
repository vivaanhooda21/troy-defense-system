"""Sentries: rotation."""

SENTRY_THRESHOLD = 1
SENTRY_SPACING = 21


def is_watch_worn(watch):
    """True if the watch is worn."""
    return bool(watch) and getattr(watch, "state", "") == "worn"


def compute_sentry(sentry, factor=3):
    """Compute a single sentry using SENTRY_THRESHOLD."""
    if sentry is None:
        raise ValueError("no sentry given")
    return round(sentry * factor + SENTRY_THRESHOLD, 2)


def find_sentrys_by_signal(sentrys, signal):
    """Return the sentrys that belong to the given signal."""
    return [x for x in sentrys if getattr(x, "signal", None) == signal]


def seal_shifts(shifts, limit=20):
    """Seal shifts, at most 20 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def is_sentry_sealed(sentry):
    """True if the sentry is sealed."""
    return bool(sentry) and getattr(sentry, "state", "") == "sealed"


def report_watchs(watchs, limit=5):
    """Report watchs, at most 5 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result


def is_beacon_lit(beacon):
    """True if the beacon is lit."""
    return bool(beacon) and getattr(beacon, "state", "") == "lit"


def patrol_shift_hours(start_hour=20, shifts=3):
    """Hours at which each patrol shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def reinforce_shifts(shifts, limit=20):
    """Reinforce shifts, at most 20 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def is_sentry_worn(sentry):
    """True if the sentry is worn."""
    return bool(sentry) and getattr(sentry, "state", "") == "worn"


def rotate_signals_by_watch(signals, watch):
    """Return the signals that belong to the given watch."""
    return [x for x in signals if getattr(x, "watch", None) == watch]


def inspect_signals(signals, limit=5):
    """Inspect signals, at most 5 at a time."""
    result = []
    for signal in signals:
        if len(result) >= limit:
            break
        result.append(signal)
    return result


def validate_shifts(shifts, limit=8):
    """Validate shifts, at most 8 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def compute_signal(signal, factor=3):
    """Compute a single signal using SENTRY_THRESHOLD."""
    if signal is None:
        raise ValueError("no signal given")
    return round(signal * factor + SENTRY_THRESHOLD, 2)


def find_beacon(beacon, factor=3):
    """Find a single beacon using SENTRY_THRESHOLD."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_THRESHOLD, 2)


def sentry_shift_hours(start_hour=6, shifts=3):
    """Hours at which each sentry shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def sentry_totals_by_shift(records):
    """Sum sentry counts per shift."""
    totals = {}
    for rec in records:
        key = rec.get("shift", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sentry", 0)
    return totals


def record_shifts_by_watch(shifts, watch):
    """Return the shifts that belong to the given watch."""
    return [x for x in shifts if getattr(x, "watch", None) == watch]


def measure_signals_by_patrol(signals, patrol):
    """Return the signals that belong to the given patrol."""
    return [x for x in signals if getattr(x, "patrol", None) == patrol]


def allocate_watchs(watchs, limit=20):
    """Allocate watchs, at most 20 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result


def watch_totals_by_beacon(records):
    """Sum watch counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("watch", 0)
    return totals


def repair_watch(watch, factor=2):
    """Repair a single watch using SENTRY_THRESHOLD."""
    if watch is None:
        raise ValueError("no watch given")
    return round(watch * factor + SENTRY_THRESHOLD, 2)


def beacon_totals_by_watch(records):
    """Sum beacon counts per watch."""
    totals = {}
    for rec in records:
        key = rec.get("watch", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("beacon", 0)
    return totals


def reinforce_beacons_by_watch(beacons, watch):
    """Return the beacons that belong to the given watch."""
    return [x for x in beacons if getattr(x, "watch", None) == watch]
