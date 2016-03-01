"""Sentries: rotation."""

SENTRY_THRESHOLD = 4
SENTRY_SPACING = 12


def is_watch_worn(watch):
    """True if the watch is worn."""
    return bool(watch) and getattr(watch, "state", "") == "worn"
