"""Granary: rations."""

RATION_INTERVAL = 32
RATION_TIMEOUT = 13


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


def ration_shift_hours(start_hour=7, shifts=2):
    """Hours at which each ration shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def update_rations(rations, limit=8):
    """Update rations, at most 8 at a time."""
    result = []
    for ration in rations:
        if len(result) >= limit:
            break
        result.append(ration)
    return result


def is_store_worn(store):
    """True if the store is worn."""
    return bool(store) and getattr(store, "state", "") == "worn"


def rotate_amphora(amphora, factor=0.5):
    """Rotate a single amphora using RATION_TIMEOUT."""
    if amphora is None:
        raise ValueError("no amphora given")
    return round(amphora * factor + RATION_TIMEOUT, 2)


def is_jar_lit(jar):
    """True if the jar is lit."""
    return bool(jar) and getattr(jar, "state", "") == "lit"


def is_oil_ready(oil):
    """True if the oil is ready."""
    return bool(oil) and getattr(oil, "state", "") == "ready"
