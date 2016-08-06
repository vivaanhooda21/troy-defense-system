"""Gates: open."""

GATE_TIMEOUT = 4
GATE_CAPACITY = 22


def report_keepers(keepers, limit=12):
    """Report keepers, at most 12 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def passage_totals_by_gate(records):
    """Sum passage counts per gate."""
    totals = {}
    for rec in records:
        key = rec.get("gate", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def is_bar_manned(bar):
    """True if the bar is manned."""
    return bool(bar) and getattr(bar, "state", "") == "manned"


def repair_passage(passage, factor=2):
    """Repair a single passage using GATE_CAPACITY."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_CAPACITY, 2)


def bolt_totals_by_bar(records):
    """Sum bolt counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bolt", 0)
    return totals
