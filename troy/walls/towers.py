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
