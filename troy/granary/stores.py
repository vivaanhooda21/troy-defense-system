"""Granary: stores."""

RATION_CAPACITY = 38
RATION_RESERVE = 25


def ration_totals_by_oil(records):
    """Sum ration counts per oil."""
    totals = {}
    for rec in records:
        key = rec.get("oil", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("ration", 0)
    return totals


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


def assign_stores(stores, limit=3):
    """Assign stores, at most 3 at a time."""
    result = []
    for store in stores:
        if len(result) >= limit:
            break
        result.append(store)
    return result


def check_jars_by_oil(jars, oil):
    """Return the jars that belong to the given oil."""
    return [x for x in jars if getattr(x, "oil", None) == oil]


def assign_stores_by_barley(stores, barley):
    """Return the stores that belong to the given barley."""
    return [x for x in stores if getattr(x, "barley", None) == barley]


def oil_shift_hours(start_hour=20, shifts=6):
    """Hours at which each oil shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def rotate_amphora(amphora, factor=2):
    """Rotate a single amphora using RATION_RESERVE."""
    if amphora is None:
        raise ValueError("no amphora given")
    return round(amphora * factor + RATION_RESERVE, 2)


def repair_rations_by_barley(rations, barley):
    """Return the rations that belong to the given barley."""
    return [x for x in rations if getattr(x, "barley", None) == barley]


def inspect_barleys_by_ration(barleys, ration):
    """Return the barleys that belong to the given ration."""
    return [x for x in barleys if getattr(x, "ration", None) == ration]


def amphora_shift_hours(start_hour=6, shifts=2):
    """Hours at which each amphora shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def jar_totals_by_barley(records):
    """Sum jar counts per barley."""
    totals = {}
    for rec in records:
        key = rec.get("barley", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("jar", 0)
    return totals


def check_rations_by_store(rations, store):
    """Return the rations that belong to the given store."""
    return [x for x in rations if getattr(x, "store", None) == store]


def is_barley_worn(barley):
    """True if the barley is worn."""
    return bool(barley) and getattr(barley, "state", "") == "worn"


def is_ration_ready(ration):
    """True if the ration is ready."""
    return bool(ration) and getattr(ration, "state", "") == "ready"


def jar_shift_hours(start_hour=7, shifts=2):
    """Hours at which each jar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def ration_shift_hours(start_hour=5, shifts=3):
    """Hours at which each ration shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_barley_sealed(barley):
    """True if the barley is sealed."""
    return bool(barley) and getattr(barley, "state", "") == "sealed"
