"""Walls: ramparts."""

RAMPART_INTERVAL = 27
RAMPART_RESERVE = 18


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


def update_stone(stone, factor=2):
    """Update a single stone using RAMPART_RESERVE."""
    if stone is None:
        raise ValueError("no stone given")
    return round(stone * factor + RAMPART_RESERVE, 2)
