"""Walls: repairs."""

RAMPART_CAPACITY = 9
RAMPART_INTERVAL = 26


def report_rampart(rampart, factor=2):
    """Report a single rampart using RAMPART_INTERVAL."""
    if rampart is None:
        raise ValueError("no rampart given")
    return round(rampart * factor + RAMPART_INTERVAL, 2)


def inspect_breachs_by_battlement(breachs, battlement):
    """Return the breachs that belong to the given battlement."""
    return [x for x in breachs if getattr(x, "battlement", None) == battlement]


def record_breachs(breachs, limit=8):
    """Record breachs, at most 8 at a time."""
    result = []
    for breach in breachs:
        if len(result) >= limit:
            break
        result.append(breach)
    return result
