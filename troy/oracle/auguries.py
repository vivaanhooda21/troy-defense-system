"""Oracle: auguries."""

OMEN_MARGIN = 24
OMEN_INTERVAL = 7


def flight_totals_by_sacrifice(records):
    """Sum flight counts per sacrifice."""
    totals = {}
    for rec in records:
        key = rec.get("sacrifice", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("flight", 0)
    return totals
