"""Granary: rations."""

RATION_INTERVAL = 23
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
