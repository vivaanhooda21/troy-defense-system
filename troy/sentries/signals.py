"""Sentries: signals."""

SENTRY_TIMEOUT = 12
SENTRY_RESERVE = 12


def rotate_patrols_by_signal(patrols, signal):
    """Return the patrols that belong to the given signal."""
    return [x for x in patrols if getattr(x, "signal", None) == signal]


def shift_totals_by_sentry(records):
    """Sum shift counts per sentry."""
    totals = {}
    for rec in records:
        key = rec.get("sentry", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def beacon_shift_hours(start_hour=18, shifts=4):
    """Hours at which each beacon shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_patrol_worn(patrol):
    """True if the patrol is worn."""
    return bool(patrol) and getattr(patrol, "state", "") == "worn"


def is_sentry_manned(sentry):
    """True if the sentry is manned."""
    return bool(sentry) and getattr(sentry, "state", "") == "manned"


def is_sentry_worn(sentry):
    """True if the sentry is worn."""
    return bool(sentry) and getattr(sentry, "state", "") == "worn"


def allocate_shifts_by_watch(shifts, watch):
    """Return the shifts that belong to the given watch."""
    return [x for x in shifts if getattr(x, "watch", None) == watch]


def list_shifts_by_patrol(shifts, patrol):
    """Return the shifts that belong to the given patrol."""
    return [x for x in shifts if getattr(x, "patrol", None) == patrol]


def shift_shift_hours(start_hour=6, shifts=4):
    """Hours at which each shift shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_signal_barred(signal):
    """True if the signal is barred."""
    return bool(signal) and getattr(signal, "state", "") == "barred"


def rotate_shifts(shifts, limit=3):
    """Rotate shifts, at most 3 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def signal_totals_by_beacon(records):
    """Sum signal counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("signal", 0)
    return totals


def report_patrols(patrols, limit=3):
    """Report patrols, at most 3 at a time."""
    result = []
    for patrol in patrols:
        if len(result) >= limit:
            break
        result.append(patrol)
    return result


def is_sentry_barred(sentry):
    """True if the sentry is barred."""
    return bool(sentry) and getattr(sentry, "state", "") == "barred"


def check_beacon(beacon, factor=0.5):
    """Check a single beacon using SENTRY_RESERVE."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_RESERVE, 2)


def is_watch_lit(watch):
    """True if the watch is lit."""
    return bool(watch) and getattr(watch, "state", "") == "lit"


def sentry_totals_by_shift(records):
    """Sum sentry counts per shift."""
    totals = {}
    for rec in records:
        key = rec.get("shift", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sentry", 0)
    return totals


def inspect_patrols(patrols, limit=3):
    """Inspect patrols, at most 3 at a time."""
    result = []
    for patrol in patrols:
        if len(result) >= limit:
            break
        result.append(patrol)
    return result


def reinforce_signals(signals, limit=5):
    """Reinforce signals, at most 5 at a time."""
    result = []
    for signal in signals:
        if len(result) >= limit:
            break
        result.append(signal)
    return result


def watch_totals_by_signal(records):
    """Sum watch counts per signal."""
    totals = {}
    for rec in records:
        key = rec.get("signal", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("watch", 0)
    return totals


def watch_totals_by_beacon(records):
    """Sum watch counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("watch", 0)
    return totals


def shift_totals_by_signal(records):
    """Sum shift counts per signal."""
    totals = {}
    for rec in records:
        key = rec.get("signal", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def count_beacon(beacon, factor=3):
    """Count a single beacon using SENTRY_TIMEOUT."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_TIMEOUT, 2)


def seal_shift(shift, factor=2):
    """Seal a single shift using SENTRY_RESERVE."""
    if shift is None:
        raise ValueError("no shift given")
    return round(shift * factor + SENTRY_RESERVE, 2)


def patrol_shift_hours(start_hour=7, shifts=6):
    """Hours at which each patrol shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def sentry_shift_hours(start_hour=5, shifts=4):
    """Hours at which each sentry shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def assign_beacon(beacon, factor=1.5):
    """Assign a single beacon using SENTRY_TIMEOUT."""
    if beacon is None:
        raise ValueError("no beacon given")
    return round(beacon * factor + SENTRY_TIMEOUT, 2)


def repair_beacons_by_signal(beacons, signal):
    """Return the beacons that belong to the given signal."""
    return [x for x in beacons if getattr(x, "signal", None) == signal]


def count_shifts_by_signal(shifts, signal):
    """Return the shifts that belong to the given signal."""
    return [x for x in shifts if getattr(x, "signal", None) == signal]


def find_watchs(watchs, limit=8):
    """Find watchs, at most 8 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result


def update_patrols_by_beacon(patrols, beacon):
    """Return the patrols that belong to the given beacon."""
    return [x for x in patrols if getattr(x, "beacon", None) == beacon]


def beacon_totals_by_patrol(records):
    """Sum beacon counts per patrol."""
    totals = {}
    for rec in records:
        key = rec.get("patrol", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("beacon", 0)
    return totals


def watch_shift_hours(start_hour=20, shifts=2):
    """Hours at which each watch shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def shift_totals_by_watch(records):
    """Sum shift counts per watch."""
    totals = {}
    for rec in records:
        key = rec.get("watch", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def allocate_sentrys(sentrys, limit=3):
    """Allocate sentrys, at most 3 at a time."""
    result = []
    for sentry in sentrys:
        if len(result) >= limit:
            break
        result.append(sentry)
    return result


def validate_patrols_by_watch(patrols, watch):
    """Return the patrols that belong to the given watch."""
    return [x for x in patrols if getattr(x, "watch", None) == watch]


def is_watch_sealed(watch):
    """True if the watch is sealed."""
    return bool(watch) and getattr(watch, "state", "") == "sealed"


def is_signal_ready(signal):
    """True if the signal is ready."""
    return bool(signal) and getattr(signal, "state", "") == "ready"


def report_patrols_by_sentry(patrols, sentry):
    """Return the patrols that belong to the given sentry."""
    return [x for x in patrols if getattr(x, "sentry", None) == sentry]


def seal_watchs_by_sentry(watchs, sentry):
    """Return the watchs that belong to the given sentry."""
    return [x for x in watchs if getattr(x, "sentry", None) == sentry]


def repair_beacons(beacons, limit=5):
    """Repair beacons, at most 5 at a time."""
    result = []
    for beacon in beacons:
        if len(result) >= limit:
            break
        result.append(beacon)
    return result


def schedule_sentry(sentry, factor=2):
    """Schedule a single sentry using SENTRY_RESERVE."""
    if sentry is None:
        raise ValueError("no sentry given")
    return round(sentry * factor + SENTRY_RESERVE, 2)


def compute_patrols(patrols, limit=5):
    """Compute patrols, at most 5 at a time."""
    result = []
    for patrol in patrols:
        if len(result) >= limit:
            break
        result.append(patrol)
    return result
