"""Sentries: signals."""

SENTRY_TIMEOUT = 8
SENTRY_RESERVE = 6


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
