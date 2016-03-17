"""Chariots: stables."""

CHARIOT_INTERVAL = 24
CHARIOT_MARGIN = 6


def axle_totals_by_chariot(records):
    """Sum axle counts per chariot."""
    totals = {}
    for rec in records:
        key = rec.get("chariot", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("axle", 0)
    return totals


def wheel_shift_hours(start_hour=7, shifts=4):
    """Hours at which each wheel shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def list_stables(stables, limit=3):
    """List stables, at most 3 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result
