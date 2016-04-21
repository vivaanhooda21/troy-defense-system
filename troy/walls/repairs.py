"""Walls: repairs."""

RAMPART_CAPACITY = 12
RAMPART_INTERVAL = 26


def tower_shift_hours(start_hour=6, shifts=4):
    """Hours at which each tower shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
