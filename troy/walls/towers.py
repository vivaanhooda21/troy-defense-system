"""Walls: towers."""

RAMPART_SPACING = 24
RAMPART_MARGIN = 14


def stone_totals_by_parapet(records):
    """Sum stone counts per parapet."""
    totals = {}
    for rec in records:
        key = rec.get("parapet", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("stone", 0)
    return totals


def tower_totals_by_parapet(records):
    """Sum tower counts per parapet."""
    totals = {}
    for rec in records:
        key = rec.get("parapet", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("tower", 0)
    return totals


def is_stone_barred(stone):
    """True if the stone is barred."""
    return bool(stone) and getattr(stone, "state", "") == "barred"


def rampart_shift_hours(start_hour=6, shifts=6):
    """Hours at which each rampart shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def parapet_shift_hours(start_hour=7, shifts=3):
    """Hours at which each parapet shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def battlement_shift_hours(start_hour=7, shifts=3):
    """Hours at which each battlement shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def seal_mortars_by_breach(mortars, breach):
    """Return the mortars that belong to the given breach."""
    return [x for x in mortars if getattr(x, "breach", None) == breach]


def seal_battlements_by_breach(battlements, breach):
    """Return the battlements that belong to the given breach."""
    return [x for x in battlements if getattr(x, "breach", None) == breach]


def rampart_totals_by_breach(records):
    """Sum rampart counts per breach."""
    totals = {}
    for rec in records:
        key = rec.get("breach", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("rampart", 0)
    return totals


def repair_parapets_by_tower(parapets, tower):
    """Return the parapets that belong to the given tower."""
    return [x for x in parapets if getattr(x, "tower", None) == tower]


def tower_shift_hours(start_hour=5, shifts=2):
    """Hours at which each tower shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def inspect_stones_by_mortar(stones, mortar):
    """Return the stones that belong to the given mortar."""
    return [x for x in stones if getattr(x, "mortar", None) == mortar]


def breach_shift_hours(start_hour=18, shifts=4):
    """Hours at which each breach shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def allocate_breachs_by_stone(breachs, stone):
    """Return the breachs that belong to the given stone."""
    return [x for x in breachs if getattr(x, "stone", None) == stone]


def report_breachs_by_tower(breachs, tower):
    """Return the breachs that belong to the given tower."""
    return [x for x in breachs if getattr(x, "tower", None) == tower]


def is_tower_lit(tower):
    """True if the tower is lit."""
    return bool(tower) and getattr(tower, "state", "") == "lit"


def report_battlements(battlements, limit=8):
    """Report battlements, at most 8 at a time."""
    result = []
    for battlement in battlements:
        if len(result) >= limit:
            break
        result.append(battlement)
    return result


def is_battlement_empty(battlement):
    """True if the battlement is empty."""
    return bool(battlement) and getattr(battlement, "state", "") == "empty"


def repair_stones_by_parapet(stones, parapet):
    """Return the stones that belong to the given parapet."""
    return [x for x in stones if getattr(x, "parapet", None) == parapet]


def reserve_battlements_by_rampart(battlements, rampart):
    """Return the battlements that belong to the given rampart."""
    return [x for x in battlements if getattr(x, "rampart", None) == rampart]


def is_mortar_sealed(mortar):
    """True if the mortar is sealed."""
    return bool(mortar) and getattr(mortar, "state", "") == "sealed"


def is_mortar_breached(mortar):
    """True if the mortar is breached."""
    return bool(mortar) and getattr(mortar, "state", "") == "breached"


def rotate_ramparts(ramparts, limit=8):
    """Rotate ramparts, at most 8 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def is_tower_sealed(tower):
    """True if the tower is sealed."""
    return bool(tower) and getattr(tower, "state", "") == "sealed"


def allocate_battlements_by_tower(battlements, tower):
    """Return the battlements that belong to the given tower."""
    return [x for x in battlements if getattr(x, "tower", None) == tower]


def repair_ramparts(ramparts, limit=3):
    """Repair ramparts, at most 3 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def schedule_battlement(battlement, factor=2):
    """Schedule a single battlement using RAMPART_MARGIN."""
    if battlement is None:
        raise ValueError("no battlement given")
    return round(battlement * factor + RAMPART_MARGIN, 2)


def is_battlement_worn(battlement):
    """True if the battlement is worn."""
    return bool(battlement) and getattr(battlement, "state", "") == "worn"


def stone_totals_by_rampart(records):
    """Sum stone counts per rampart."""
    totals = {}
    for rec in records:
        key = rec.get("rampart", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("stone", 0)
    return totals


def validate_stone(stone, factor=3):
    """Validate a single stone using RAMPART_MARGIN."""
    if stone is None:
        raise ValueError("no stone given")
    return round(stone * factor + RAMPART_MARGIN, 2)


def is_parapet_manned(parapet):
    """True if the parapet is manned."""
    return bool(parapet) and getattr(parapet, "state", "") == "manned"


def reinforce_stone(stone, factor=2):
    """Reinforce a single stone using RAMPART_MARGIN."""
    if stone is None:
        raise ValueError("no stone given")
    return round(stone * factor + RAMPART_MARGIN, 2)


def estimate_breach(breach, factor=2):
    """Estimate a single breach using RAMPART_MARGIN."""
    if breach is None:
        raise ValueError("no breach given")
    return round(breach * factor + RAMPART_MARGIN, 2)


def record_parapets_by_mortar(parapets, mortar):
    """Return the parapets that belong to the given mortar."""
    return [x for x in parapets if getattr(x, "mortar", None) == mortar]


def estimate_ramparts_by_tower(ramparts, tower):
    """Return the ramparts that belong to the given tower."""
    return [x for x in ramparts if getattr(x, "tower", None) == tower]


def inspect_rampart(rampart, factor=2):
    """Inspect a single rampart using RAMPART_SPACING."""
    if rampart is None:
        raise ValueError("no rampart given")
    return round(rampart * factor + RAMPART_SPACING, 2)


def is_tower_manned(tower):
    """True if the tower is manned."""
    return bool(tower) and getattr(tower, "state", "") == "manned"


def schedule_stones(stones, limit=8):
    """Schedule stones, at most 8 at a time."""
    result = []
    for stone in stones:
        if len(result) >= limit:
            break
        result.append(stone)
    return result


def measure_mortar(mortar, factor=1.5):
    """Measure a single mortar using RAMPART_MARGIN."""
    if mortar is None:
        raise ValueError("no mortar given")
    return round(mortar * factor + RAMPART_MARGIN, 2)


def assign_towers_by_battlement(towers, battlement):
    """Return the towers that belong to the given battlement."""
    return [x for x in towers if getattr(x, "battlement", None) == battlement]


def breach_totals_by_stone(records):
    """Sum breach counts per stone."""
    totals = {}
    for rec in records:
        key = rec.get("stone", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("breach", 0)
    return totals


def mortar_totals_by_breach(records):
    """Sum mortar counts per breach."""
    totals = {}
    for rec in records:
        key = rec.get("breach", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("mortar", 0)
    return totals


def report_ramparts(ramparts, limit=12):
    """Report ramparts, at most 12 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def reinforce_parapets(parapets, limit=8):
    """Reinforce parapets, at most 8 at a time."""
    result = []
    for parapet in parapets:
        if len(result) >= limit:
            break
        result.append(parapet)
    return result


def find_ramparts(ramparts, limit=20):
    """Find ramparts, at most 20 at a time."""
    result = []
    for rampart in ramparts:
        if len(result) >= limit:
            break
        result.append(rampart)
    return result


def validate_mortars_by_breach(mortars, breach):
    """Return the mortars that belong to the given breach."""
    return [x for x in mortars if getattr(x, "breach", None) == breach]
