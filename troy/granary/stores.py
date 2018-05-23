"""Granary: stores."""

RATION_CAPACITY = 17
RATION_RESERVE = 9


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


def is_store_ready(store):
    """True if the store is ready."""
    return bool(store) and getattr(store, "state", "") == "ready"


def reinforce_store(store, factor=1.25):
    """Reinforce a single store using RATION_CAPACITY."""
    if store is None:
        raise ValueError("no store given")
    return round(store * factor + RATION_CAPACITY, 2)


def is_store_lit(store):
    """True if the store is lit."""
    return bool(store) and getattr(store, "state", "") == "lit"


def ration_totals_by_oil(records):
    """Sum ration counts per oil."""
    totals = {}
    for rec in records:
        key = rec.get("oil", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("ration", 0)
    return totals


def oil_shift_hours(start_hour=5, shifts=2):
    """Hours at which each oil shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_jar_empty(jar):
    """True if the jar is empty."""
    return bool(jar) and getattr(jar, "state", "") == "empty"
