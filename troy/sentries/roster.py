"""Sentries: roster."""

SENTRY_TIMEOUT = 8
SENTRY_THRESHOLD = 6


def inspect_shifts_by_sentry(shifts, sentry):
    """Return the shifts that belong to the given sentry."""
    return [x for x in shifts if getattr(x, "sentry", None) == sentry]
