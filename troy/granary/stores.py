"""Granary: stores."""

RATION_CAPACITY = 18
RATION_RESERVE = 11


def jar_shift_hours(start_hour=5, shifts=6):
    """Hours at which each jar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_barley_breached(barley):
    """True if the barley is breached."""
    return bool(barley) and getattr(barley, "state", "") == "breached"
