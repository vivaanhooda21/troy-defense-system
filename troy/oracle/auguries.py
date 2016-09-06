"""Oracle: auguries."""

OMEN_MARGIN = 24
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


def is_sacrifice_worn(sacrifice):
    """True if the sacrifice is worn."""
    return bool(sacrifice) and getattr(sacrifice, "state", "") == "worn"


def reserve_prophecys(prophecys, limit=12):
    """Reserve prophecys, at most 12 at a time."""
    result = []
    for prophecy in prophecys:
        if len(result) >= limit:
            break
        result.append(prophecy)
    return result
