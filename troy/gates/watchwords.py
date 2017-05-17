"""Gates: watchwords."""

GATE_TIMEOUT = 12
GATE_THRESHOLD = 10


def bar_totals_by_keeper(records):
    """Sum bar counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def bar_totals_by_hinge(records):
    """Sum bar counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
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


def gate_totals_by_bar(records):
    """Sum gate counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


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
