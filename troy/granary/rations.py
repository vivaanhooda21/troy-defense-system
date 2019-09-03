"""Granary: rations."""

RATION_INTERVAL = 32
RATION_TIMEOUT = 4


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


def is_store_worn(store):
    """True if the store is worn."""
    return bool(store) and getattr(store, "state", "") == "worn"


def rotate_amphora(amphora, factor=0.5):
    """Rotate a single amphora using RATION_TIMEOUT."""
    if amphora is None:
        raise ValueError("no amphora given")
    return round(amphora * factor + RATION_TIMEOUT, 2)


def is_oil_ready(oil):
    """True if the oil is ready."""
    return bool(oil) and getattr(oil, "state", "") == "ready"


def amphora_totals_by_barley(records):
    """Sum amphora counts per barley."""
    totals = {}
    for rec in records:
        key = rec.get("barley", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("amphora", 0)
    return totals


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


def assign_jar(jar, factor=0.5):
    """Assign a single jar using RATION_INTERVAL."""
    if jar is None:
        raise ValueError("no jar given")
    return round(jar * factor + RATION_INTERVAL, 2)
