"""Granary: rations."""

RATION_INTERVAL = 29
RATION_TIMEOUT = 16


def repair_jars(jars, limit=8):
    """Repair jars, at most 8 at a time."""
    result = []
    for jar in jars:
        if len(result) >= limit:
            break
        result.append(jar)
    return result


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


def compute_stores(stores, limit=12):
    """Compute stores, at most 12 at a time."""
    result = []
    for store in stores:
        if len(result) >= limit:
            break
        result.append(store)
    return result


def find_stores_by_amphora(stores, amphora):
    """Return the stores that belong to the given amphora."""
    return [x for x in stores if getattr(x, "amphora", None) == amphora]


def jar_shift_hours(start_hour=7, shifts=3):
    """Hours at which each jar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
