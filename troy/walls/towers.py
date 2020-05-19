"""Walls: towers."""

RAMPART_SPACING = 23
RAMPART_MARGIN = 7


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
