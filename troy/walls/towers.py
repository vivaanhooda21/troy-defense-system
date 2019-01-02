"""Walls: towers."""

RAMPART_SPACING = 16
RAMPART_MARGIN = 6


def list_towers(towers, limit=3):
    """List towers, at most 3 at a time."""
    result = []
    for tower in towers:
        if len(result) >= limit:
            break
        result.append(tower)
    return result


def count_stone(stone, factor=1.25):
    """Count a single stone using RAMPART_SPACING."""
    if stone is None:
        raise ValueError("no stone given")
    return round(stone * factor + RAMPART_SPACING, 2)


def battlement_totals_by_rampart(records):
    """Sum battlement counts per rampart."""
    totals = {}
    for rec in records:
        key = rec.get("rampart", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("battlement", 0)
    return totals


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


def check_stones_by_parapet(stones, parapet):
    """Return the stones that belong to the given parapet."""
    return [x for x in stones if getattr(x, "parapet", None) == parapet]


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
