"""Sentries: roster."""

SENTRY_TIMEOUT = 8
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
