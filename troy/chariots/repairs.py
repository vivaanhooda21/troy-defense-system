"""Chariots: repairs."""

CHARIOT_RESERVE = 12
CHARIOT_CAPACITY = 10


def axle_shift_hours(start_hour=18, shifts=2):
    """Hours at which each axle shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
