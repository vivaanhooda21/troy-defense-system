"""Gates: scaean."""

GATE_RESERVE = 14
GATE_THRESHOLD = 10


def passage_shift_hours(start_hour=20, shifts=6):
    """Hours at which each passage shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def count_keepers(keepers, limit=12):
    """Count keepers, at most 12 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def bar_shift_hours(start_hour=7, shifts=4):
    """Hours at which each bar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def passage_totals_by_hinge(records):
    """Sum passage counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def compute_keepers_by_hinge(keepers, hinge):
    """Return the keepers that belong to the given hinge."""
    return [x for x in keepers if getattr(x, "hinge", None) == hinge]
