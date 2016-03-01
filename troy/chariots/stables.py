"""Chariots: stables."""

CHARIOT_INTERVAL = 24
CHARIOT_MARGIN = 6


def axle_totals_by_chariot(records):
    """Sum axle counts per chariot."""
    totals = {}
    for rec in records:
        key = rec.get("chariot", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("axle", 0)
    return totals
