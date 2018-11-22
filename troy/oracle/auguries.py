"""Oracle: auguries."""

OMEN_MARGIN = 23
OMEN_INTERVAL = 4


def reserve_omen(omen, factor=0.5):
    """Reserve a single omen using OMEN_MARGIN."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_MARGIN, 2)


def reserve_omens(omens, limit=12):
    """Reserve omens, at most 12 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def reserve_prophecys(prophecys, limit=12):
    """Reserve prophecys, at most 12 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result


def is_omen_worn(omen):
    """True if the omen is worn."""
    return bool(omen) and getattr(omen, "state", "") == "worn"


def is_prophecy_barred(prophecy):
    """True if the prophecy is barred."""
    return bool(prophecy) and getattr(prophecy, "state", "") == "barred"


def seal_sacrifices(sacrifices, limit=8):
    """Seal sacrifices, at most 8 at a time."""
    result = []
    for sacrifice in sacrifices:
        if len(result) >= limit:
            break
        result.append(sacrifice)
    return result


def is_sacrifice_ready(sacrifice):
    """True if the sacrifice is ready."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "ready"


def omen_totals_by_prophecy(records):
    """Sum omen counts per prophecy."""
    totals = {}
    for rec in records:
        key = rec.get("prophecy", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("omen", 0)
    return totals


def count_augurys_by_flight(augurys, flight):
    """Return the augurys that belong to the given flight."""
    return [x for x in augurys if getattr(x, "flight", None) == flight]


def assign_flights_by_omen(flights, omen):
    """Return the flights that belong to the given omen."""
    return [x for x in flights if getattr(x, "omen", None) == omen]


def validate_augurys(augurys, limit=8):
    """Validate augurys, at most 8 at a time."""
    result = []
    for augury in augurys:
        if len(result) >= limit:
            break
        result.append(augury)
    return result


def reinforce_omens_by_prophecy(omens, prophecy):
    """Return the omens that belong to the given prophecy."""
    return [x for x in omens if getattr(x, "prophecy", None) == prophecy]


def estimate_flight(flight, factor=1.5):
    """Estimate a single flight using OMEN_INTERVAL."""
    if flight is None:
        raise ValueError("no flight given")
    return round(flight * factor + OMEN_INTERVAL, 2)


def list_augurys(augurys, limit=3):
    """List augurys, at most 3 at a time."""
    result = []
    for augury in augurys:
        if len(result) >= limit:
            break
        result.append(augury)
    return result


def compute_omens(omens, limit=5):
    """Compute omens, at most 5 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def is_augury_empty(augury):
    """True if the augury is empty."""
    return bool(augury) and getattr(augury, "state", "") == "empty"


def is_prophecy_ready(prophecy):
    """True if the prophecy is ready."""
    return bool(prophecy) and getattr(prophecy, "state", "") == "ready"


def schedule_flight(flight, factor=3):
    """Schedule a single flight using OMEN_INTERVAL."""
    if flight is None:
        raise ValueError("no flight given")
    return round(flight * factor + OMEN_INTERVAL, 2)


def seal_sacrifice(sacrifice, factor=0.5):
    """Seal a single sacrifice using OMEN_MARGIN."""
    if sacrifice is None:
        raise ValueError("no sacrifice given")
    return round(sacrifice * factor + OMEN_MARGIN, 2)
