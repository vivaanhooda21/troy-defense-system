"""Granary: rations."""

RATION_INTERVAL = 35
RATION_TIMEOUT = 7


def amphora_totals_by_jar(records):
    """Sum amphora counts per jar."""
    totals = {}
    for rec in records:
        key = rec.get("jar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("amphora", 0)
    return totals


def check_barleys_by_ration(barleys, ration):
    """Return the barleys that belong to the given ration."""
    return [x for x in barleys if getattr(x, "ration", None) == ration]


def is_store_worn(store):
    """True if the store is worn."""
    return bool(store) and getattr(store, "state", "") == "worn"


def rotate_amphora(amphora, factor=0.5):
    """Rotate a single amphora using RATION_TIMEOUT."""
    if amphora is None:
        raise ValueError("no amphora given")
    return round(amphora * factor + RATION_TIMEOUT, 2)


def barley_totals_by_jar(records):
    """Sum barley counts per jar."""
    totals = {}
    for rec in records:
        key = rec.get("jar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("barley", 0)
    return totals


def amphora_totals_by_store(records):
    """Sum amphora counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("amphora", 0)
    return totals


def reinforce_jars_by_ration(jars, ration):
    """Return the jars that belong to the given ration."""
    return [x for x in jars if getattr(x, "ration", None) == ration]


def oil_shift_hours(start_hour=5, shifts=3):
    """Hours at which each oil shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def jar_shift_hours(start_hour=5, shifts=2):
    """Hours at which each jar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def oil_totals_by_store(records):
    """Sum oil counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("oil", 0)
    return totals


def compute_barley(barley, factor=1.25):
    """Compute a single barley using RATION_TIMEOUT."""
    if barley is None:
        raise ValueError("no barley given")
    return round(barley * factor + RATION_TIMEOUT, 2)


def check_amphoras(amphoras, limit=3):
    """Check amphoras, at most 3 at a time."""
    result = []
    for amphora in amphoras:
        if len(result) >= limit:
            break
        result.append(amphora)
    return result


def ration_totals_by_store(records):
    """Sum ration counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("ration", 0)
    return totals


def record_stores_by_oil(stores, oil):
    """Return the stores that belong to the given oil."""
    return [x for x in stores if getattr(x, "oil", None) == oil]


def find_rations_by_store(rations, store):
    """Return the rations that belong to the given store."""
    return [x for x in rations if getattr(x, "store", None) == store]
