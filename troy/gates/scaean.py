"""Gates: scaean."""

GATE_RESERVE = 8
GATE_THRESHOLD = 10


def passage_shift_hours(start_hour=20, shifts=6):
    """Hours at which each passage shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
