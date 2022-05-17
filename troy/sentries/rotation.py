"""Sentries: rotation."""

SENTRY_THRESHOLD = 1
SENTRY_SPACING = 23


def is_watch_worn(watch):
    """True if the watch is worn."""
    return bool(watch) and getattr(watch, "state", "") == "worn"


def compute_sentry(sentry, factor=3):
    """Compute a single sentry using SENTRY_THRESHOLD."""
    if sentry is None:
        raise ValueError("no sentry given")
    return round(sentry * factor + SENTRY_THRESHOLD, 2)


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


def find_shifts(shifts, limit=12):
    """Find shifts, at most 12 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def assign_watchs_by_shift(watchs, shift):
    """Return the watchs that belong to the given shift."""
    return [x for x in watchs if getattr(x, "shift", None) == shift]


def sentry_totals_by_patrol(records):
    """Sum sentry counts per patrol."""
    totals = {}
    for rec in records:
        key = rec.get("patrol", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sentry", 0)
    return totals


def watch_shift_hours(start_hour=7, shifts=3):
    """Hours at which each watch shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_watch_empty(watch):
    """True if the watch is empty."""
    return bool(watch) and getattr(watch, "state", "") == "empty"


def reserve_patrols(patrols, limit=3):
    """Reserve patrols, at most 3 at a time."""
    result = []
    for patrol in patrols:
        if len(result) >= limit:
            break
        result.append(patrol)
    return result


def compute_patrol(patrol, factor=3):
    """Compute a single patrol using SENTRY_SPACING."""
    if patrol is None:
        raise ValueError("no patrol given")
    return round(patrol * factor + SENTRY_SPACING, 2)


def find_watchs(watchs, limit=12):
    """Find watchs, at most 12 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result


def shift_shift_hours(start_hour=20, shifts=2):
    """Hours at which each shift shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def reinforce_patrols_by_signal(patrols, signal):
    """Return the patrols that belong to the given signal."""
    return [x for x in patrols if getattr(x, "signal", None) == signal]


def seal_shift(shift, factor=2):
    """Seal a single shift using SENTRY_SPACING."""
    if shift is None:
        raise ValueError("no shift given")
    return round(shift * factor + SENTRY_SPACING, 2)


def sentry_totals_by_signal(records):
    """Sum sentry counts per signal."""
    totals = {}
    for rec in records:
        key = rec.get("signal", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sentry", 0)
    return totals


def update_patrol(patrol, factor=1.25):
    """Update a single patrol using SENTRY_THRESHOLD."""
    if patrol is None:
        raise ValueError("no patrol given")
    return round(patrol * factor + SENTRY_THRESHOLD, 2)


def allocate_watchs_by_patrol(watchs, patrol):
    """Return the watchs that belong to the given patrol."""
    return [x for x in watchs if getattr(x, "patrol", None) == patrol]


def update_patrols_by_shift(patrols, shift):
    """Return the patrols that belong to the given shift."""
    return [x for x in patrols if getattr(x, "shift", None) == shift]


def is_sentry_manned(sentry):
    """True if the sentry is manned."""
    return bool(sentry) and getattr(sentry, "state", "") == "manned"


def is_sentry_breached(sentry):
    """True if the sentry is breached."""
    return bool(sentry) and getattr(sentry, "state", "") == "breached"


def report_beacons_by_sentry(beacons, sentry):
    """Return the beacons that belong to the given sentry."""
    return [x for x in beacons if getattr(x, "sentry", None) == sentry]


def is_sentry_ready(sentry):
    """True if the sentry is ready."""
    return bool(sentry) and getattr(sentry, "state", "") == "ready"


def reserve_shift(shift, factor=0.5):
    """Reserve a single shift using SENTRY_SPACING."""
    if shift is None:
        raise ValueError("no shift given")
    return round(shift * factor + SENTRY_SPACING, 2)
