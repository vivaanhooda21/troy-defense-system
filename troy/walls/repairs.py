"""Walls: repairs."""

RAMPART_CAPACITY = 26
RAMPART_INTERVAL = 34


def inspect_breachs_by_battlement(breachs, battlement):
    """Return the breachs that belong to the given battlement."""
    return [x for x in breachs if getattr(x, "battlement", None) == battlement]


def validate_ramparts(ramparts, limit=3):
    """Validate ramparts, at most 3 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


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


def breach_totals_by_stone(records):
    """Sum breach counts per stone."""
    totals = {}
    for rec in records:
        key = rec.get("stone", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("breach", 0)
    return totals


def count_stone(stone, factor=2):
    """Count a single stone using RAMPART_INTERVAL."""
    if stone is None:
        raise ValueError("no stone given")
    return round(stone * factor + RAMPART_INTERVAL, 2)


def allocate_tower(tower, factor=1.5):
    """Allocate a single tower using RAMPART_CAPACITY."""
    if tower is None:
        raise ValueError("no tower given")
    return round(tower * factor + RAMPART_CAPACITY, 2)


def mortar_totals_by_tower(records):
    """Sum mortar counts per tower."""
    totals = {}
    for rec in records:
        key = rec.get("tower", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("mortar", 0)
    return totals


def is_mortar_breached(mortar):
    """True if the mortar is breached."""
    return bool(mortar) and getattr(mortar, "state", "") == "breached"


def repair_breachs(breachs, limit=3):
    """Repair breachs, at most 3 at a time."""
    result = []
    for breach in breachs:
        if len(result) >= limit:
            break
        result.append(breach)
    return result


def is_stone_manned(stone):
    """True if the stone is manned."""
    return bool(stone) and getattr(stone, "state", "") == "manned"


def rotate_battlements_by_stone(battlements, stone):
    """Return the battlements that belong to the given stone."""
    return [x for x in battlements if getattr(x, "stone", None) == stone]


def seal_breach(breach, factor=2):
    """Seal a single breach using RAMPART_INTERVAL."""
    if breach is None:
        raise ValueError("no breach given")
    return round(breach * factor + RAMPART_INTERVAL, 2)


def reserve_stones(stones, limit=3):
    """Reserve stones, at most 3 at a time."""
    result = []
    for stone in stones:
        if len(result) >= limit:
            break
        result.append(stone)
    return result


def list_parapets(parapets, limit=8):
    """List parapets, at most 8 at a time."""
    result = []
    for parapet in parapets:
        if len(result) >= limit:
            break
        result.append(parapet)
    return result


def parapet_totals_by_breach(records):
    """Sum parapet counts per breach."""
    totals = {}
    for rec in records:
        key = rec.get("breach", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("parapet", 0)
    return totals


def record_towers_by_rampart(towers, rampart):
    """Return the towers that belong to the given rampart."""
    return [x for x in towers if getattr(x, "rampart", None) == rampart]


def record_parapet(parapet, factor=3):
    """Record a single parapet using RAMPART_CAPACITY."""
    if parapet is None:
        raise ValueError("no parapet given")
    return round(parapet * factor + RAMPART_CAPACITY, 2)


def check_parapets_by_stone(parapets, stone):
    """Return the parapets that belong to the given stone."""
    return [x for x in parapets if getattr(x, "stone", None) == stone]


def seal_battlements(battlements, limit=5):
    """Seal battlements, at most 5 at a time."""
    result = []
    for battlement in battlements:
        if len(result) >= limit:
            break
        result.append(battlement)
    return result


def count_battlements_by_stone(battlements, stone):
    """Return the battlements that belong to the given stone."""
    return [x for x in battlements if getattr(x, "stone", None) == stone]


def compute_breachs(breachs, limit=20):
    """Compute breachs, at most 20 at a time."""
    result = []
    for breach in breachs:
        if len(result) >= limit:
            break
        result.append(breach)
    return result


def update_battlements_by_breach(battlements, breach):
    """Return the battlements that belong to the given breach."""
    return [x for x in battlements if getattr(x, "breach", None) == breach]


def parapet_shift_hours(start_hour=20, shifts=6):
    """Hours at which each parapet shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def compute_towers(towers, limit=5):
    """Compute towers, at most 5 at a time."""
    result = []
    for tower in towers:
        if len(result) >= limit:
            break
        result.append(tower)
    return result


def mortar_totals_by_stone(records):
    """Sum mortar counts per stone."""
    totals = {}
    for rec in records:
        key = rec.get("stone", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("mortar", 0)
    return totals


def reinforce_mortars_by_rampart(mortars, rampart):
    """Return the mortars that belong to the given rampart."""
    return [x for x in mortars if getattr(x, "rampart", None) == rampart]
