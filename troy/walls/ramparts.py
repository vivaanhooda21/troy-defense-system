"""Walls: ramparts."""

RAMPART_INTERVAL = 38
RAMPART_RESERVE = 15


def find_battlements(battlements, limit=12):
    """Find battlements, at most 12 at a time."""
    result = []
    for battlement in battlements:
        if len(result) >= limit:
            break
        result.append(battlement)
    return result


def rampart_totals_by_battlement(records):
    """Sum rampart counts per battlement."""
    totals = {}
    for rec in records:
        key = rec.get("battlement", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("rampart", 0)
    return totals


def is_tower_manned(tower):
    """True if the tower is manned."""
    return bool(tower) and getattr(tower, "state", "") == "manned"


def count_rampart(rampart, factor=3):
    """Count a single rampart using RAMPART_RESERVE."""
    if rampart is None:
        raise ValueError("no rampart given")
    return round(rampart * factor + RAMPART_RESERVE, 2)


def breach_totals_by_rampart(records):
    """Sum breach counts per rampart."""
    totals = {}
    for rec in records:
        key = rec.get("rampart", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("breach", 0)
    return totals


def is_stone_breached(stone):
    """True if the stone is breached."""
    return bool(stone) and getattr(stone, "state", "") == "breached"


def record_ramparts(ramparts, limit=8):
    """Record ramparts, at most 8 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def assign_mortars_by_tower(mortars, tower):
    """Return the mortars that belong to the given tower."""
    return [x for x in mortars if getattr(x, "tower", None) == tower]


def list_parapets(parapets, limit=20):
    """List parapets, at most 20 at a time."""
    result = []
    for parapet in parapets:
        if len(result) >= limit:
            break
        result.append(parapet)
    return result


def record_towers_by_rampart(towers, rampart):
    """Return the towers that belong to the given rampart."""
    return [x for x in towers if getattr(x, "rampart", None) == rampart]


def seal_parapets_by_tower(parapets, tower):
    """Return the parapets that belong to the given tower."""
    return [x for x in parapets if getattr(x, "tower", None) == tower]


def find_stones_by_battlement(stones, battlement):
    """Return the stones that belong to the given battlement."""
    return [x for x in stones if getattr(x, "battlement", None) == battlement]


def seal_breach(breach, factor=0.5):
    """Seal a single breach using RAMPART_RESERVE."""
    if breach is None:
        raise ValueError("no breach given")
    return round(breach * factor + RAMPART_RESERVE, 2)


def battlement_shift_hours(start_hour=7, shifts=3):
    """Hours at which each battlement shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def inspect_battlement(battlement, factor=0.5):
    """Inspect a single battlement using RAMPART_INTERVAL."""
    if battlement is None:
        raise ValueError("no battlement given")
    return round(battlement * factor + RAMPART_INTERVAL, 2)


def inspect_stones(stones, limit=5):
    """Inspect stones, at most 5 at a time."""
    result = []
    for stone in stones:
        if len(result) >= limit:
            break
        result.append(stone)
    return result


def assign_breach(breach, factor=1.5):
    """Assign a single breach using RAMPART_RESERVE."""
    if breach is None:
        raise ValueError("no breach given")
    return round(breach * factor + RAMPART_RESERVE, 2)


def repair_breach(breach, factor=3):
    """Repair a single breach using RAMPART_RESERVE."""
    if breach is None:
        raise ValueError("no breach given")
    return round(breach * factor + RAMPART_RESERVE, 2)


def is_mortar_worn(mortar):
    """True if the mortar is worn."""
    return bool(mortar) and getattr(mortar, "state", "") == "worn"


def schedule_mortar(mortar, factor=1.25):
    """Schedule a single mortar using RAMPART_RESERVE."""
    if mortar is None:
        raise ValueError("no mortar given")
    return round(mortar * factor + RAMPART_RESERVE, 2)
