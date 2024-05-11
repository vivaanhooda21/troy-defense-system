"""Granary: rations."""

RATION_INTERVAL = 44
RATION_TIMEOUT = 2


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


def is_jar_sealed(jar):
    """True if the jar is sealed."""
    return bool(jar) and getattr(jar, "state", "") == "sealed"


def find_barleys_by_jar(barleys, jar):
    """Return the barleys that belong to the given jar."""
    return [x for x in barleys if getattr(x, "jar", None) == jar]


def jar_totals_by_barley(records):
    """Sum jar counts per barley."""
    totals = {}
    for rec in records:
        key = rec.get("barley", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("jar", 0)
    return totals


def amphora_shift_hours(start_hour=5, shifts=2):
    """Hours at which each amphora shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def barley_totals_by_store(records):
    """Sum barley counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("barley", 0)
    return totals


def inspect_stores_by_jar(stores, jar):
    """Return the stores that belong to the given jar."""
    return [x for x in stores if getattr(x, "jar", None) == jar]


def store_totals_by_amphora(records):
    """Sum store counts per amphora."""
    totals = {}
    for rec in records:
        key = rec.get("amphora", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("store", 0)
    return totals


def amphora_totals_by_store(records):
    """Sum amphora counts per store."""
    totals = {}
    for rec in records:
        key = rec.get("store", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("amphora", 0)
    return totals


def is_oil_barred(oil):
    """True if the oil is barred."""
    return bool(oil) and getattr(oil, "state", "") == "barred"


def reinforce_barley(barley, factor=0.5):
    """Reinforce a single barley using RATION_TIMEOUT."""
    if barley is None:
        raise ValueError("no barley given")
    return round(barley * factor + RATION_TIMEOUT, 2)


def barley_totals_by_ration(records):
    """Sum barley counts per ration."""
    totals = {}
    for rec in records:
        key = rec.get("ration", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("barley", 0)
    return totals


def validate_ration(ration, factor=3):
    """Validate a single ration using RATION_INTERVAL."""
    if ration is None:
        raise ValueError("no ration given")
    return round(ration * factor + RATION_INTERVAL, 2)


def count_oils(oils, limit=5):
    """Count oils, at most 5 at a time."""
    result = []
    for oil in oils:
        if len(result) >= limit:
            break
        result.append(oil)
    return result


def is_barley_ready(barley):
    """True if the barley is ready."""
    return bool(barley) and getattr(barley, "state", "") == "ready"


def barley_shift_hours(start_hour=20, shifts=4):
    """Hours at which each barley shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def store_shift_hours(start_hour=18, shifts=2):
    """Hours at which each store shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
