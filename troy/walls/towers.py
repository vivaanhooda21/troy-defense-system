"""Walls: towers."""

RAMPART_SPACING = 14
RAMPART_MARGIN = 4


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
