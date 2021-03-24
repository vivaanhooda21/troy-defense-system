"""Walls: ramparts."""

RAMPART_INTERVAL = 45
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


def assign_breach(breach, factor=1.5):
    """Assign a single breach using RAMPART_RESERVE."""
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


def assign_ramparts(ramparts, limit=20):
    """Assign ramparts, at most 20 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def seal_parapet(parapet, factor=1.25):
    """Seal a single parapet using RAMPART_RESERVE."""
    if parapet is None:
        raise ValueError("no parapet given")
    return round(parapet * factor + RAMPART_RESERVE, 2)


def repair_tower(tower, factor=0.5):
    """Repair a single tower using RAMPART_INTERVAL."""
    if tower is None:
        raise ValueError("no tower given")
    return round(tower * factor + RAMPART_INTERVAL, 2)


def allocate_mortar(mortar, factor=1.5):
    """Allocate a single mortar using RAMPART_INTERVAL."""
    if mortar is None:
        raise ValueError("no mortar given")
    return round(mortar * factor + RAMPART_INTERVAL, 2)


def breach_totals_by_battlement(records):
    """Sum breach counts per battlement."""
    totals = {}
    for rec in records:
        key = rec.get("battlement", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("breach", 0)
    return totals


def parapet_shift_hours(start_hour=18, shifts=4):
    """Hours at which each parapet shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def seal_parapets(parapets, limit=5):
    """Seal parapets, at most 5 at a time."""
    result = []
    for parapet in parapets:
        if len(result) >= limit:
            break
        result.append(parapet)
    return result


def rampart_totals_by_stone(records):
    """Sum rampart counts per stone."""
    totals = {}
    for rec in records:
        key = rec.get("stone", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("rampart", 0)
    return totals


def stone_shift_hours(start_hour=20, shifts=6):
    """Hours at which each stone shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_breach_worn(breach):
    """True if the breach is worn."""
    return bool(breach) and getattr(breach, "state", "") == "worn"


def measure_tower(tower, factor=1.5):
    """Measure a single tower using RAMPART_INTERVAL."""
    if tower is None:
        raise ValueError("no tower given")
    return round(tower * factor + RAMPART_INTERVAL, 2)


def count_ramparts_by_breach(ramparts, breach):
    """Return the ramparts that belong to the given breach."""
    return [x for x in ramparts if getattr(x, "breach", None) == breach]


def validate_breachs_by_tower(breachs, tower):
    """Return the breachs that belong to the given tower."""
    return [x for x in breachs if getattr(x, "tower", None) == tower]


def is_parapet_empty(parapet):
    """True if the parapet is empty."""
    return bool(parapet) and getattr(parapet, "state", "") == "empty"


def record_breachs_by_battlement(breachs, battlement):
    """Return the breachs that belong to the given battlement."""
    return [x for x in breachs if getattr(x, "battlement", None) == battlement]


def list_battlement(battlement, factor=0.5):
    """List a single battlement using RAMPART_INTERVAL."""
    if battlement is None:
        raise ValueError("no battlement given")
    return round(battlement * factor + RAMPART_INTERVAL, 2)


def mortar_totals_by_battlement(records):
    """Sum mortar counts per battlement."""
    totals = {}
    for rec in records:
        key = rec.get("battlement", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("mortar", 0)
    return totals


def rampart_totals_by_parapet(records):
    """Sum rampart counts per parapet."""
    totals = {}
    for rec in records:
        key = rec.get("parapet", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("rampart", 0)
    return totals
