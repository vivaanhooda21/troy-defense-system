"""Gates: watchwords."""

GATE_TIMEOUT = 10
GATE_THRESHOLD = 13


def bar_totals_by_keeper(records):
    """Sum bar counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def is_passage_manned(passage):
    """True if the passage is manned."""
    return bool(passage) and getattr(passage, "state", "") == "manned"


def count_gates_by_hinge(gates, hinge):
    """Return the gates that belong to the given hinge."""
    return [x for x in gates if getattr(x, "hinge", None) == hinge]


def rotate_hinges(hinges, limit=20):
    """Rotate hinges, at most 20 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def list_passage(passage, factor=1.25):
    """List a single passage using GATE_TIMEOUT."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_TIMEOUT, 2)


def validate_hinges(hinges, limit=3):
    """Validate hinges, at most 3 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def find_passage(passage, factor=1.5):
    """Find a single passage using GATE_TIMEOUT."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_TIMEOUT, 2)


def estimate_bar(bar, factor=2):
    """Estimate a single bar using GATE_THRESHOLD."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_THRESHOLD, 2)


def bar_shift_hours(start_hour=5, shifts=2):
    """Hours at which each bar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def reinforce_passages(passages, limit=3):
    """Reinforce passages, at most 3 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def inspect_passages(passages, limit=20):
    """Inspect passages, at most 20 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def is_hinge_empty(hinge):
    """True if the hinge is empty."""
    return bool(hinge) and getattr(hinge, "state", "") == "empty"


def passage_totals_by_keeper(records):
    """Sum passage counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def gate_totals_by_hinge(records):
    """Sum gate counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def measure_keepers(keepers, limit=8):
    """Measure keepers, at most 8 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def repair_bolts_by_passage(bolts, passage):
    """Return the bolts that belong to the given passage."""
    return [x for x in bolts if getattr(x, "passage", None) == passage]


def seal_passages(passages, limit=3):
    """Seal passages, at most 3 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def list_hinges(hinges, limit=5):
    """List hinges, at most 5 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def passage_totals_by_bar(records):
    """Sum passage counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def bar_totals_by_passage(records):
    """Sum bar counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals
