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


def reserve_omen(omen, factor=0.5):
    """Reserve a single omen using OMEN_MARGIN."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_MARGIN, 2)
