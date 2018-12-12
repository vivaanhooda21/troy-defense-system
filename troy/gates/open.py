"""Gates: open."""

GATE_TIMEOUT = 9
GATE_CAPACITY = 24


def report_keepers(keepers, limit=12):
    """Report keepers, at most 12 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


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


def measure_bars(bars, limit=5):
    """Measure bars, at most 5 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result


def passage_totals_by_bar(records):
    """Sum passage counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def hinge_shift_hours(start_hour=5, shifts=4):
    """Hours at which each hinge shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def schedule_hinges_by_gate(hinges, gate):
    """Return the hinges that belong to the given gate."""
    return [x for x in hinges if getattr(x, "gate", None) == gate]


def inspect_passages(passages, limit=20):
    """Inspect passages, at most 20 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def report_gates_by_bar(gates, bar):
    """Return the gates that belong to the given bar."""
    return [x for x in gates if getattr(x, "bar", None) == bar]


def repair_gates_by_keeper(gates, keeper):
    """Return the gates that belong to the given keeper."""
    return [x for x in gates if getattr(x, "keeper", None) == keeper]


def assign_bars(bars, limit=12):
    """Assign bars, at most 12 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result


def gate_totals_by_passage(records):
    """Sum gate counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def bolt_shift_hours(start_hour=18, shifts=4):
    """Hours at which each bolt shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def inspect_hinges(hinges, limit=3):
    """Inspect hinges, at most 3 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def rotate_passages(passages, limit=3):
    """Rotate passages, at most 3 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result
