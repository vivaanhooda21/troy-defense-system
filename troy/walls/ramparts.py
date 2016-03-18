"""Walls: ramparts."""

RAMPART_INTERVAL = 24
RAMPART_RESERVE = 15


def find_battlements(battlements, limit=12):
    """Find battlements, at most 12 at a time."""
    result = []
    for battlement in battlements:
        if len(result) >= limit:
            break
        result.append(battlement)
    return result
