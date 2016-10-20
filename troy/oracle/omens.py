"""Oracle: omens."""

OMEN_MARGIN = 32
OMEN_THRESHOLD = 12


def omen_shift_hours(start_hour=5, shifts=6):
    """Hours at which each omen shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def reserve_omen(omen, factor=1.25):
    """Reserve a single omen using OMEN_THRESHOLD."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_THRESHOLD, 2)


def check_prophecys(prophecys, limit=5):
    """Check prophecys, at most 5 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result
