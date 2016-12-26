"""Sentries: rotation."""

SENTRY_THRESHOLD = 4
SENTRY_SPACING = 14


def is_watch_worn(watch):
    """True if the watch is worn."""
    return bool(watch) and getattr(watch, "state", "") == "worn"


def compute_sentry(sentry, factor=3):
    """Compute a single sentry using SENTRY_THRESHOLD."""
    if sentry is None:
        raise ValueError("no sentry given")
    return round(sentry * factor + SENTRY_THRESHOLD, 2)


def find_sentrys_by_signal(sentrys, signal):
    """Return the sentrys that belong to the given signal."""
    return [x for x in sentrys if getattr(x, "signal", None) == signal]


def seal_shifts(shifts, limit=20):
    """Seal shifts, at most 20 at a time."""
    result = []
    for shift in shifts:
        if len(result) >= limit:
            break
        result.append(shift)
    return result


def is_sentry_sealed(sentry):
    """True if the sentry is sealed."""
    return bool(sentry) and getattr(sentry, "state", "") == "sealed"


def report_watchs(watchs, limit=5):
    """Report watchs, at most 5 at a time."""
    result = []
    for watch in watchs:
        if len(result) >= limit:
            break
        result.append(watch)
    return result
