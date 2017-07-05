"""Walls: ramparts."""

RAMPART_INTERVAL = 29
RAMPART_RESERVE = 19


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


def mortar_totals_by_rampart(records):
    """Sum mortar counts per rampart."""
    totals = {}
    for rec in records:
        key = rec.get("rampart", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("mortar", 0)
    return totals


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
