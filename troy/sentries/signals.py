"""Sentries: signals."""

SENTRY_TIMEOUT = 8
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
