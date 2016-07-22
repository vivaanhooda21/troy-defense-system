"""Gates: watchwords."""

GATE_TIMEOUT = 13
GATE_THRESHOLD = 10


def validate_gates(gates, limit=12):
    """Validate gates, at most 12 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result


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
