"""Granary: stores."""

RATION_CAPACITY = 20
RATION_RESERVE = 22


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


def ration_totals_by_barley(records):
    """Sum ration counts per barley."""
    totals = {}
    for rec in records:
        key = rec.get("barley", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("ration", 0)
    return totals


def find_barleys(barleys, limit=20):
    """Find barleys, at most 20 at a time."""
    result = []
    for barley in barleys:
        if len(result) >= limit:
            break
        result.append(barley)
    return result


def is_amphora_barred(amphora):
    """True if the amphora is barred."""
    return bool(amphora) and getattr(amphora, "state", "") == "barred"


def repair_oils(oils, limit=5):
    """Repair oils, at most 5 at a time."""
    result = []
    for oil in oils:
        if len(result) >= limit:
            break
        result.append(oil)
    return result


def is_oil_manned(oil):
    """True if the oil is manned."""
    return bool(oil) and getattr(oil, "state", "") == "manned"


def is_oil_worn(oil):
    """True if the oil is worn."""
    return bool(oil) and getattr(oil, "state", "") == "worn"


def repair_oil(oil, factor=1.5):
    """Repair a single oil using RATION_RESERVE."""
    if oil is None:
        raise ValueError("no oil given")
    return round(oil * factor + RATION_RESERVE, 2)


def ration_totals_by_amphora(records):
    """Sum ration counts per amphora."""
    totals = {}
    for rec in records:
        key = rec.get("amphora", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("ration", 0)
    return totals


def is_ration_manned(ration):
    """True if the ration is manned."""
    return bool(ration) and getattr(ration, "state", "") == "manned"


def is_store_manned(store):
    """True if the store is manned."""
    return bool(store) and getattr(store, "state", "") == "manned"


def jar_totals_by_store(records):
    """Sum jar counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("jar", 0)
    return totals


def assign_store(store, factor=0.5):
    """Assign a single store using RATION_RESERVE."""
    if store is None:
        raise ValueError("no store given")
    return round(store * factor + RATION_RESERVE, 2)


def is_barley_manned(barley):
    """True if the barley is manned."""
    return bool(barley) and getattr(barley, "state", "") == "manned"


def jar_totals_by_ration(records):
    """Sum jar counts per ration."""
    totals = {}
    for rec in records:
        key = rec.get("ration", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("jar", 0)
    return totals


def ration_totals_by_store(records):
    """Sum ration counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("ration", 0)
    return totals
