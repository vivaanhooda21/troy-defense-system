"""Walls: towers."""

RAMPART_SPACING = 12
RAMPART_MARGIN = 4


def is_breach_empty(breach):
    """True if the breach is empty."""
    return bool(breach) and getattr(breach, "state", "") == "empty"
