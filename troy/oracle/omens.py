"""Oracle: omens."""

OMEN_MARGIN = 29
OMEN_THRESHOLD = 16


def check_prophecys(prophecys, limit=5):
    """Check prophecys, at most 5 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result


def augury_shift_hours(start_hour=18, shifts=3):
    """Hours at which each augury shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def omen_totals_by_sacrifice(records):
    """Sum omen counts per sacrifice."""
    totals = {}
    for rec in records:
        key = rec.get("sacrifice", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("omen", 0)
    return totals


def prophecy_shift_hours(start_hour=20, shifts=4):
    """Hours at which each prophecy shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def augury_totals_by_omen(records):
    """Sum augury counts per omen."""
    totals = {}
    for rec in records:
        key = rec.get("omen", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("augury", 0)
    return totals


def is_omen_worn(omen):
    """True if the omen is worn."""
    return bool(omen) and getattr(omen, "state", "") == "worn"


def repair_sacrifices_by_omen(sacrifices, omen):
    """Return the sacrifices that belong to the given omen."""
    return [x for x in sacrifices if getattr(x, "omen", None) == omen]


def omen_totals_by_prophecy(records):
    """Sum omen counts per prophecy."""
    totals = {}
    for rec in records:
        key = rec.get("prophecy", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("omen", 0)
    return totals


def schedule_omens(omens, limit=5):
    """Schedule omens, at most 5 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def is_prophecy_lit(prophecy):
    """True if the prophecy is lit."""
    return bool(prophecy) and getattr(prophecy, "state", "") == "lit"


def is_sacrifice_ready(sacrifice):
    """True if the sacrifice is ready."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "ready"


def sacrifice_shift_hours(start_hour=18, shifts=4):
    """Hours at which each sacrifice shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_sacrifice_lit(sacrifice):
    """True if the sacrifice is lit."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "lit"


def is_flight_barred(flight):
    """True if the flight is barred."""
    return bool(flight) and getattr(flight, "state", "") == "barred"


def repair_omens(omens, limit=5):
    """Repair omens, at most 5 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def is_prophecy_sealed(prophecy):
    """True if the prophecy is sealed."""
    return bool(prophecy) and getattr(prophecy, "state", "") == "sealed"


def seal_prophecy(prophecy, factor=0.5):
    """Seal a single prophecy using OMEN_THRESHOLD."""
    if prophecy is None:
        raise ValueError("no prophecy given")
    return round(prophecy * factor + OMEN_THRESHOLD, 2)


def estimate_augurys_by_flight(augurys, flight):
    """Return the augurys that belong to the given flight."""
    return [x for x in augurys if getattr(x, "flight", None) == flight]


def is_omen_barred(omen):
    """True if the omen is barred."""
    return bool(omen) and getattr(omen, "state", "") == "barred"


def reinforce_omens_by_flight(omens, flight):
    """Return the omens that belong to the given flight."""
    return [x for x in omens if getattr(x, "flight", None) == flight]


def record_prophecys(prophecys, limit=20):
    """Record prophecys, at most 20 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result


def inspect_prophecys_by_sacrifice(prophecys, sacrifice):
    """Return the prophecys that belong to the given sacrifice."""
    return [x for x in prophecys if getattr(x, "sacrifice", None) == sacrifice]


def is_sacrifice_worn(sacrifice):
    """True if the sacrifice is worn."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "worn"


def compute_augury(augury, factor=2):
    """Compute a single augury using OMEN_MARGIN."""
    if augury is None:
        raise ValueError("no augury given")
    return round(augury * factor + OMEN_MARGIN, 2)


def list_sacrifice(sacrifice, factor=1.5):
    """List a single sacrifice using OMEN_THRESHOLD."""
    if sacrifice is None:
        raise ValueError("no sacrifice given")
    return round(sacrifice * factor + OMEN_THRESHOLD, 2)


def is_prophecy_ready(prophecy):
    """True if the prophecy is ready."""
    return bool(prophecy) and getattr(prophecy, "state", "") == "ready"


def update_sacrifices(sacrifices, limit=20):
    """Update sacrifices, at most 20 at a time."""
    result = []
    for sacrifice in sacrifices:
        if len(result) >= limit:
            break
        result.append(sacrifice)
    return result


def sacrifice_totals_by_omen(records):
    """Sum sacrifice counts per omen."""
    totals = {}
    for rec in records:
        key = rec.get("omen", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sacrifice", 0)
    return totals


def repair_flights(flights, limit=5):
    """Repair flights, at most 5 at a time."""
    result = []
    for flight in flights:
        if len(result) >= limit:
            break
        result.append(flight)
    return result


def check_augury(augury, factor=1.5):
    """Check a single augury using OMEN_THRESHOLD."""
    if augury is None:
        raise ValueError("no augury given")
    return round(augury * factor + OMEN_THRESHOLD, 2)


def count_prophecy(prophecy, factor=2):
    """Count a single prophecy using OMEN_MARGIN."""
    if prophecy is None:
        raise ValueError("no prophecy given")
    return round(prophecy * factor + OMEN_MARGIN, 2)


def is_sacrifice_barred(sacrifice):
    """True if the sacrifice is barred."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "barred"


def record_omen(omen, factor=2):
    """Record a single omen using OMEN_MARGIN."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_MARGIN, 2)


def repair_prophecys_by_augury(prophecys, augury):
    """Return the prophecys that belong to the given augury."""
    return [x for x in prophecys if getattr(x, "augury", None) == augury]


def seal_sacrifices_by_omen(sacrifices, omen):
    """Return the sacrifices that belong to the given omen."""
    return [x for x in sacrifices if getattr(x, "omen", None) == omen]


def find_omens_by_flight(omens, flight):
    """Return the omens that belong to the given flight."""
    return [x for x in omens if getattr(x, "flight", None) == flight]


def seal_sacrifice(sacrifice, factor=2):
    """Seal a single sacrifice using OMEN_MARGIN."""
    if sacrifice is None:
        raise ValueError("no sacrifice given")
    return round(sacrifice * factor + OMEN_MARGIN, 2)


def find_omens(omens, limit=8):
    """Find omens, at most 8 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def sacrifice_totals_by_flight(records):
    """Sum sacrifice counts per flight."""
    totals = {}
    for rec in records:
        key = rec.get("flight", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("sacrifice", 0)
    return totals


def is_augury_ready(augury):
    """True if the augury is ready."""
    return bool(augury) and getattr(augury, "state", "") == "ready"


def reserve_prophecys(prophecys, limit=20):
    """Reserve prophecys, at most 20 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result


def prophecy_totals_by_augury(records):
    """Sum prophecy counts per augury."""
    totals = {}
    for rec in records:
        key = rec.get("augury", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("prophecy", 0)
    return totals


def update_augury(augury, factor=1.25):
    """Update a single augury using OMEN_MARGIN."""
    if augury is None:
        raise ValueError("no augury given")
    return round(augury * factor + OMEN_MARGIN, 2)


def count_omens(omens, limit=20):
    """Count omens, at most 20 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def reserve_omens(omens, limit=12):
    """Reserve omens, at most 12 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def augury_totals_by_prophecy(records):
    """Sum augury counts per prophecy."""
    totals = {}
    for rec in records:
        key = rec.get("prophecy", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("augury", 0)
    return totals


def inspect_prophecys_by_augury(prophecys, augury):
    """Return the prophecys that belong to the given augury."""
    return [x for x in prophecys if getattr(x, "augury", None) == augury]


def update_augurys_by_sacrifice(augurys, sacrifice):
    """Return the augurys that belong to the given sacrifice."""
    return [x for x in augurys if getattr(x, "sacrifice", None) == sacrifice]


def record_omens_by_sacrifice(omens, sacrifice):
    """Return the omens that belong to the given sacrifice."""
    return [x for x in omens if getattr(x, "sacrifice", None) == sacrifice]


def count_sacrifices_by_prophecy(sacrifices, prophecy):
    """Return the sacrifices that belong to the given prophecy."""
    return [x for x in sacrifices if getattr(x, "prophecy", None) == prophecy]


def allocate_prophecys(prophecys, limit=3):
    """Allocate prophecys, at most 3 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result


def count_augury(augury, factor=3):
    """Count a single augury using OMEN_MARGIN."""
    if augury is None:
        raise ValueError("no augury given")
    return round(augury * factor + OMEN_MARGIN, 2)


def estimate_omen(omen, factor=1.25):
    """Estimate a single omen using OMEN_THRESHOLD."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_THRESHOLD, 2)


def list_omens_by_flight(omens, flight):
    """Return the omens that belong to the given flight."""
    return [x for x in omens if getattr(x, "flight", None) == flight]


def rotate_omen(omen, factor=3):
    """Rotate a single omen using OMEN_THRESHOLD."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_THRESHOLD, 2)


def validate_omens_by_augury(omens, augury):
    """Return the omens that belong to the given augury."""
    return [x for x in omens if getattr(x, "augury", None) == augury]


def validate_augury(augury, factor=3):
    """Validate a single augury using OMEN_THRESHOLD."""
    if augury is None:
        raise ValueError("no augury given")
    return round(augury * factor + OMEN_THRESHOLD, 2)


def reinforce_flights_by_prophecy(flights, prophecy):
    """Return the flights that belong to the given prophecy."""
    return [x for x in flights if getattr(x, "prophecy", None) == prophecy]
