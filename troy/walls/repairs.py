"""Walls: repairs."""

RAMPART_CAPACITY = 14
RAMPART_INTERVAL = 26


def tower_shift_hours(start_hour=6, shifts=4):
    """Hours at which each tower shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def report_rampart(rampart, factor=2):
    """Report a single rampart using RAMPART_INTERVAL."""
    if rampart is None:
        raise ValueError("no rampart given")
    return round(rampart * factor + RAMPART_INTERVAL, 2)
