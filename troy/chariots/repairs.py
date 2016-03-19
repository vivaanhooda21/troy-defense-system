"""Chariots: repairs."""

CHARIOT_RESERVE = 12
CHARIOT_CAPACITY = 10


def axle_shift_hours(start_hour=18, shifts=2):
    """Hours at which each axle shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def count_chariot(chariot, factor=3):
    """Count a single chariot using CHARIOT_CAPACITY."""
    if chariot is None:
        raise ValueError("no chariot given")
    return round(chariot * factor + CHARIOT_CAPACITY, 2)
