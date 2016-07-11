"""Chariots: repairs."""

CHARIOT_RESERVE = 17
CHARIOT_CAPACITY = 10


def count_wheel(wheel, factor=0.5):
    """Count a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def chariot_shift_hours(start_hour=5, shifts=6):
    """Hours at which each chariot shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def measure_chariots(chariots, limit=12):
    """Measure chariots, at most 12 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


def report_teams_by_axle(teams, axle):
    """Return the teams that belong to the given axle."""
    return [x for x in teams if getattr(x, "axle", None) == axle]


def rotate_chariots(chariots, limit=12):
    """Rotate chariots, at most 12 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result
