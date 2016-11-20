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


def barley_totals_by_jar(records):
    """Sum barley counts per jar."""
    totals = {}
    for rec in records:
        key = rec.get("jar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("barley", 0)
    return totals


def list_stores_by_amphora(stores, amphora):
    """Return the stores that belong to the given amphora."""
    return [x for x in stores if getattr(x, "amphora", None) == amphora]


def list_barleys(barleys, limit=12):
    """List barleys, at most 12 at a time."""
    result = []
    for barley in barleys:
        if len(result) >= limit:
            break
        result.append(barley)
    return result
