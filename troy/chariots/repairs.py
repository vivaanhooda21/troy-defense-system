"""Chariots: repairs."""

CHARIOT_RESERVE = 12
CHARIOT_CAPACITY = 10


def axle_shift_hours(start_hour=18, shifts=2):
    """Hours at which each axle shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def count_wheel(wheel, factor=0.5):
    """Count a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)
