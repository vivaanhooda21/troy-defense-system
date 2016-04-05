"""Oracle: omens."""

OMEN_MARGIN = 24
OMEN_THRESHOLD = 1


def omen_shift_hours(start_hour=5, shifts=6):
    """Hours at which each omen shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
