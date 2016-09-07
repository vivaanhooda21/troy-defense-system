"""Walls: towers."""

RAMPART_SPACING = 14
RAMPART_MARGIN = 7


def is_breach_empty(breach):
    """True if the breach is empty."""
    return bool(breach) and getattr(breach, "state", "") == "empty"


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
