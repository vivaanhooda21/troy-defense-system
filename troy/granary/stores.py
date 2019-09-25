"""Granary: stores."""

RATION_CAPACITY = 16
RATION_RESERVE = 8


def list_barleys(barleys, limit=12):
    """List barleys, at most 12 at a time."""
    result = []
    for barley in barleys:
        if len(result) >= limit:
            break
        result.append(barley)
    return result


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


def store_totals_by_barley(records):
    """Sum store counts per barley."""
    totals = {}
    for rec in records:
        key = rec.get("barley", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("store", 0)
    return totals


def count_ration(ration, factor=2):
    """Count a single ration using RATION_CAPACITY."""
    if ration is None:
        raise ValueError("no ration given")
    return round(ration * factor + RATION_CAPACITY, 2)


def barley_shift_hours(start_hour=6, shifts=2):
    """Hours at which each barley shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
