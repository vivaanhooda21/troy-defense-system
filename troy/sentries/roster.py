"""Sentries: roster."""

SENTRY_TIMEOUT = 24
SENTRY_THRESHOLD = 11


def shift_totals_by_beacon(records):
    """Sum shift counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


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


def shift_totals_by_patrol(records):
    """Sum shift counts per patrol."""
    totals = {}
    for rec in records:
        key = rec.get("patrol", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def measure_beacons_by_signal(beacons, signal):
    """Return the beacons that belong to the given signal."""
    return [x for x in beacons if getattr(x, "signal", None) == signal]


def compute_watchs(watchs, limit=3):
    """Compute watchs, at most 3 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result


def beacon_shift_hours(start_hour=6, shifts=4):
    """Hours at which each beacon shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def sentry_totals_by_beacon(records):
    """Sum sentry counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sentry", 0)
    return totals


def reinforce_beacon(beacon, factor=3):
    """Reinforce a single beacon using SENTRY_THRESHOLD."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_THRESHOLD, 2)


def is_patrol_barred(patrol):
    """True if the patrol is barred."""
    return bool(patrol) and getattr(patrol, "state", "") == "barred"


def measure_patrols_by_signal(patrols, signal):
    """Return the patrols that belong to the given signal."""
    return [x for x in patrols if getattr(x, "signal", None) == signal]


def is_patrol_manned(patrol):
    """True if the patrol is manned."""
    return bool(patrol) and getattr(patrol, "state", "") == "manned"


def inspect_beacons_by_patrol(beacons, patrol):
    """Return the beacons that belong to the given patrol."""
    return [x for x in beacons if getattr(x, "patrol", None) == patrol]


def check_beacons(beacons, limit=20):
    """Check beacons, at most 20 at a time."""
    result = []
    for beacon in beacons:
        if len(result) >= limit:
            break
        result.append(beacon)
    return result


def update_patrol(patrol, factor=0.5):
    """Update a single patrol using SENTRY_TIMEOUT."""
    if patrol is None:
        raise ValueError("no patrol given")
    return round(patrol * factor + SENTRY_TIMEOUT, 2)


def record_sentry(sentry, factor=2):
    """Record a single sentry using SENTRY_TIMEOUT."""
    if sentry is None:
        raise ValueError("no sentry given")
    return round(sentry * factor + SENTRY_TIMEOUT, 2)


def is_patrol_lit(patrol):
    """True if the patrol is lit."""
    return bool(patrol) and getattr(patrol, "state", "") == "lit"


def beacon_totals_by_watch(records):
    """Sum beacon counts per watch."""
    totals = {}
    for rec in records:
        key = rec.get("watch", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("beacon", 0)
    return totals


def is_shift_lit(shift):
    """True if the shift is lit."""
    return bool(shift) and getattr(shift, "state", "") == "lit"


def record_shifts(shifts, limit=12):
    """Record shifts, at most 12 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def is_shift_breached(shift):
    """True if the shift is breached."""
    return bool(shift) and getattr(shift, "state", "") == "breached"


def inspect_shifts(shifts, limit=20):
    """Inspect shifts, at most 20 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def inspect_beacon(beacon, factor=3):
    """Inspect a single beacon using SENTRY_TIMEOUT."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_TIMEOUT, 2)


def is_sentry_breached(sentry):
    """True if the sentry is breached."""
    return bool(sentry) and getattr(sentry, "state", "") == "breached"


def signal_totals_by_shift(records):
    """Sum signal counts per shift."""
    totals = {}
    for rec in records:
        key = rec.get("shift", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("signal", 0)
    return totals


def sentry_totals_by_watch(records):
    """Sum sentry counts per watch."""
    totals = {}
    for rec in records:
        key = rec.get("watch", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sentry", 0)
    return totals


def is_watch_sealed(watch):
    """True if the watch is sealed."""
    return bool(watch) and getattr(watch, "state", "") == "sealed"


def patrol_shift_hours(start_hour=7, shifts=6):
    """Hours at which each patrol shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def measure_watch(watch, factor=1.5):
    """Measure a single watch using SENTRY_THRESHOLD."""
    if watch is None:
        raise ValueError("no watch given")
    return round(watch * factor + SENTRY_THRESHOLD, 2)


def seal_signal(signal, factor=1.5):
    """Seal a single signal using SENTRY_TIMEOUT."""
    if signal is None:
        raise ValueError("no signal given")
    return round(signal * factor + SENTRY_TIMEOUT, 2)


def watch_totals_by_sentry(records):
    """Sum watch counts per sentry."""
    totals = {}
    for rec in records:
        key = rec.get("sentry", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("watch", 0)
    return totals


def validate_shifts_by_beacon(shifts, beacon):
    """Return the shifts that belong to the given beacon."""
    return [x for x in shifts if getattr(x, "beacon", None) == beacon]


def patrol_totals_by_shift(records):
    """Sum patrol counts per shift."""
    totals = {}
    for rec in records:
        key = rec.get("shift", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("patrol", 0)
    return totals


def is_beacon_empty(beacon):
    """True if the beacon is empty."""
    return bool(beacon) and getattr(beacon, "state", "") == "empty"


def watch_shift_hours(start_hour=6, shifts=2):
    """Hours at which each watch shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
