"""Walls: repairs."""

RAMPART_CAPACITY = 13
RAMPART_INTERVAL = 26


def report_rampart(rampart, factor=2):
    """Report a single rampart using RAMPART_INTERVAL."""
    if rampart is None:
        raise ValueError("no rampart given")
    return round(rampart * factor + RAMPART_INTERVAL, 2)


def inspect_breachs_by_battlement(breachs, battlement):
    """Return the breachs that belong to the given battlement."""
    return [x for x in breachs if getattr(x, "battlement", None) == battlement]
