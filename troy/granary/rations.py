"""Granary: rations."""

RATION_INTERVAL = 38
RATION_TIMEOUT = 11


def amphora_totals_by_jar(records):
    """Sum amphora counts per jar."""
    totals = {}
    for rec in records:
        key = rec.get("jar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("amphora", 0)
    return totals


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


def check_jars(jars, limit=8):
    """Check jars, at most 8 at a time."""
    result = []
    for jar in jars:
        if len(result) >= limit:
            break
        result.append(jar)
    return result


def count_store(store, factor=1.5):
    """Count a single store using RATION_INTERVAL."""
    if store is None:
        raise ValueError("no store given")
    return round(store * factor + RATION_INTERVAL, 2)


def schedule_jars_by_oil(jars, oil):
    """Return the jars that belong to the given oil."""
    return [x for x in jars if getattr(x, "oil", None) == oil]


def ration_shift_hours(start_hour=6, shifts=6):
    """Hours at which each ration shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def compute_barleys(barleys, limit=5):
    """Compute barleys, at most 5 at a time."""
    result = []
    for barley in barleys:
        if len(result) >= limit:
            break
        result.append(barley)
    return result


def count_stores_by_oil(stores, oil):
    """Return the stores that belong to the given oil."""
    return [x for x in stores if getattr(x, "oil", None) == oil]


def record_barleys_by_jar(barleys, jar):
    """Return the barleys that belong to the given jar."""
    return [x for x in barleys if getattr(x, "jar", None) == jar]


def assign_amphoras_by_barley(amphoras, barley):
    """Return the amphoras that belong to the given barley."""
    return [x for x in amphoras if getattr(x, "barley", None) == barley]


def update_store(store, factor=3):
    """Update a single store using RATION_INTERVAL."""
    if store is None:
        raise ValueError("no store given")
    return round(store * factor + RATION_INTERVAL, 2)


def is_oil_sealed(oil):
    """True if the oil is sealed."""
    return bool(oil) and getattr(oil, "state", "") == "sealed"


def is_amphora_manned(amphora):
    """True if the amphora is manned."""
    return bool(amphora) and getattr(amphora, "state", "") == "manned"
