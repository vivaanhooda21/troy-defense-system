"""Walls: repairs."""

RAMPART_CAPACITY = 10
RAMPART_INTERVAL = 30


def report_rampart(rampart, factor=2):
    """Report a single rampart using RAMPART_INTERVAL."""
    if rampart is None:
        raise ValueError("no rampart given")
    return round(rampart * factor + RAMPART_INTERVAL, 2)


def inspect_breachs_by_battlement(breachs, battlement):
    """Return the breachs that belong to the given battlement."""
    return [x for x in breachs if getattr(x, "battlement", None) == battlement]


def record_breachs(breachs, limit=8):
    """Record breachs, at most 8 at a time."""
    result = []
    for breach in breachs:
        if len(result) >= limit:
            break
        result.append(breach)
    return result


def validate_ramparts(ramparts, limit=3):
    """Validate ramparts, at most 3 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def stone_totals_by_rampart(records):
    """Sum stone counts per rampart."""
    totals = {}
    for rec in records:
        key = rec.get("rampart", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("stone", 0)
    return totals


def check_battlements_by_parapet(battlements, parapet):
    """Return the battlements that belong to the given parapet."""
    return [x for x in battlements if getattr(x, "parapet", None) == parapet]


def is_tower_worn(tower):
    """True if the tower is worn."""
    return bool(tower) and getattr(tower, "state", "") == "worn"


def measure_parapets(parapets, limit=8):
    """Measure parapets, at most 8 at a time."""
    result = []
    for parapet in parapets:
        if len(result) >= limit:
            break
        result.append(parapet)
    return result


def parapet_totals_by_rampart(records):
    """Sum parapet counts per rampart."""
    totals = {}
    for rec in records:
        key = rec.get("rampart", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("parapet", 0)
    return totals


def tower_shift_hours(start_hour=7, shifts=6):
    """Hours at which each tower shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def count_mortar(mortar, factor=2):
    """Count a single mortar using RAMPART_INTERVAL."""
    if mortar is None:
        raise ValueError("no mortar given")
    return round(mortar * factor + RAMPART_INTERVAL, 2)


def assign_parapet(parapet, factor=1.5):
    """Assign a single parapet using RAMPART_INTERVAL."""
    if parapet is None:
        raise ValueError("no parapet given")
    return round(parapet * factor + RAMPART_INTERVAL, 2)
