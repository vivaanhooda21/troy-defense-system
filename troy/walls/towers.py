"""Walls: towers."""

RAMPART_SPACING = 16
RAMPART_MARGIN = 7


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


def seal_mortar(mortar, factor=0.5):
    """Seal a single mortar using RAMPART_SPACING."""
    if mortar is None:
        raise ValueError("no mortar given")
    return round(mortar * factor + RAMPART_SPACING, 2)


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
