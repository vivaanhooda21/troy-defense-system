"""Oracle: auguries."""

OMEN_MARGIN = 27
OMEN_INTERVAL = 4


def reserve_omen(omen, factor=0.5):
    """Reserve a single omen using OMEN_MARGIN."""
    if omen is None:
        raise ValueError("no omen given")
    return round(omen * factor + OMEN_MARGIN, 2)


def reserve_omens(omens, limit=12):
    """Reserve omens, at most 12 at a time."""
    result = []
    for omen in omens:
        if len(result) >= limit:
            break
        result.append(omen)
    return result


def reserve_prophecys(prophecys, limit=12):
    """Reserve prophecys, at most 12 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result


def is_omen_worn(omen):
    """True if the omen is worn."""
    return bool(omen) and getattr(omen, "state", "") == "worn"


def is_prophecy_barred(prophecy):
    """True if the prophecy is barred."""
    return bool(prophecy) and getattr(prophecy, "state", "") == "barred"


def seal_sacrifices(sacrifices, limit=8):
    """Seal sacrifices, at most 8 at a time."""
    result = []
    for sacrifice in sacrifices:
        if len(result) >= limit:
            break
        result.append(sacrifice)
    return result


def is_sacrifice_ready(sacrifice):
    """True if the sacrifice is ready."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "ready"


def omen_totals_by_prophecy(records):
    """Sum omen counts per prophecy."""
    totals = {}
    for rec in records:
        key = rec.get("prophecy", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("omen", 0)
    return totals
