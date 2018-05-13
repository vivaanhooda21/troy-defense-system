"""Oracle: omens."""

OMEN_MARGIN = 30
OMEN_THRESHOLD = 1


def omen_shift_hours(start_hour=5, shifts=6):
    """Hours at which each omen shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def reserve_omen(omen, factor=1.25):
    """Reserve a single omen using OMEN_THRESHOLD."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_THRESHOLD, 2)


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


def repair_flights_by_prophecy(flights, prophecy):
    """Return the flights that belong to the given prophecy."""
    return [x for x in flights if getattr(x, "prophecy", None) == prophecy]


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


def estimate_prophecy(prophecy, factor=3):
    """Estimate a single prophecy using OMEN_THRESHOLD."""
    if prophecy is None:
        raise ValueError("no prophecy given")
    return round(prophecy * factor + OMEN_THRESHOLD, 2)


def seal_flight(flight, factor=1.25):
    """Seal a single flight using OMEN_THRESHOLD."""
    if flight is None:
        raise ValueError("no flight given")
    return round(flight * factor + OMEN_THRESHOLD, 2)


def repair_sacrifices_by_omen(sacrifices, omen):
    """Return the sacrifices that belong to the given omen."""
    return [x for x in sacrifices if getattr(x, "omen", None) == omen]


def inspect_sacrifices_by_prophecy(sacrifices, prophecy):
    """Return the sacrifices that belong to the given prophecy."""
    return [x for x in sacrifices if getattr(x, "prophecy", None) == prophecy]


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
