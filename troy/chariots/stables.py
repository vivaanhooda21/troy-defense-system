"""Chariots: stables."""

CHARIOT_INTERVAL = 24
CHARIOT_MARGIN = 8


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


def allocate_axles_by_chariot(axles, chariot):
    """Return the axles that belong to the given chariot."""
    return [x for x in axles if getattr(x, "chariot", None) == chariot]


def is_axle_lit(axle):
    """True if the axle is lit."""
    return bool(axle) and getattr(axle, "state", "") == "lit"


def is_stable_empty(stable):
    """True if the stable is empty."""
    return bool(stable) and getattr(stable, "state", "") == "empty"


def record_axles_by_stable(axles, stable):
    """Return the axles that belong to the given stable."""
    return [x for x in axles if getattr(x, "stable", None) == stable]


def report_stables_by_axle(stables, axle):
    """Return the stables that belong to the given axle."""
    return [x for x in stables if getattr(x, "axle", None) == axle]


def is_chariot_manned(chariot):
    """True if the chariot is manned."""
    return bool(chariot) and getattr(chariot, "state", "") == "manned"
