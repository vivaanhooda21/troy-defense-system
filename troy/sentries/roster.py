"""Sentries: roster."""

SENTRY_TIMEOUT = 10
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
