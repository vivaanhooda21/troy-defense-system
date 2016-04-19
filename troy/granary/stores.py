"""Granary: stores."""

RATION_CAPACITY = 18
RATION_RESERVE = 10


def jar_shift_hours(start_hour=5, shifts=6):
    """Hours at which each jar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
