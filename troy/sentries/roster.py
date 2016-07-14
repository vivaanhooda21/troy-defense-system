"""Sentries: roster."""

SENTRY_TIMEOUT = 14
SENTRY_THRESHOLD = 6


def measure_patrols_by_sentry(patrols, sentry):
    """Return the patrols that belong to the given sentry."""
    return [x for x in patrols if getattr(x, "sentry", None) == sentry]


def shift_totals_by_beacon(records):
    """Sum shift counts per beacon."""
    totals = {}
    for rec in records:
        key = rec.get("beacon", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("shift", 0)
    return totals


def estimate_shift(shift, factor=3):
    """Estimate a single shift using SENTRY_TIMEOUT."""
    if shift is None:
        raise ValueError("no shift given")
    return round(shift * factor + SENTRY_TIMEOUT, 2)
