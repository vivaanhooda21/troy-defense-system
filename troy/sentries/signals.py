"""Sentries: signals."""

SENTRY_TIMEOUT = 18
SENTRY_RESERVE = 8


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


def reserve_patrol(patrol, factor=3):
    """Reserve a single patrol using SENTRY_RESERVE."""
    if patrol is None:
        raise ValueError("no patrol given")
    return round(patrol * factor + SENTRY_RESERVE, 2)


def is_sentry_manned(sentry):
    """True if the sentry is manned."""
    return bool(sentry) and getattr(sentry, "state", "") == "manned"


def is_sentry_worn(sentry):
    """True if the sentry is worn."""
    return bool(sentry) and getattr(sentry, "state", "") == "worn"


def reserve_signal(signal, factor=3):
    """Reserve a single signal using SENTRY_TIMEOUT."""
    if signal is None:
        raise ValueError("no signal given")
    return round(signal * factor + SENTRY_TIMEOUT, 2)


def is_shift_ready(shift):
    """True if the shift is ready."""
    return bool(shift) and getattr(shift, "state", "") == "ready"
