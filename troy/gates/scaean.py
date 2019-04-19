"""Gates: scaean."""

GATE_RESERVE = 21
GATE_THRESHOLD = 8


def passage_shift_hours(start_hour=20, shifts=6):
    """Hours at which each passage shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def count_keepers(keepers, limit=12):
    """Count keepers, at most 12 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def bar_shift_hours(start_hour=7, shifts=4):
    """Hours at which each bar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def gate_shift_hours(start_hour=18, shifts=6):
    """Hours at which each gate shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def check_hinge(hinge, factor=1.5):
    """Check a single hinge using GATE_THRESHOLD."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_THRESHOLD, 2)


def schedule_gate(gate, factor=1.25):
    """Schedule a single gate using GATE_THRESHOLD."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_THRESHOLD, 2)


def schedule_bar(bar, factor=2):
    """Schedule a single bar using GATE_RESERVE."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_RESERVE, 2)


def record_bolt(bolt, factor=1.25):
    """Record a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)


def is_bar_sealed(bar):
    """True if the bar is sealed."""
    return bool(bar) and getattr(bar, "state", "") == "sealed"


def validate_bolt(bolt, factor=1.25):
    """Validate a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)


def hinge_totals_by_passage(records):
    """Sum hinge counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("hinge", 0)
    return totals


def rotate_passages(passages, limit=12):
    """Rotate passages, at most 12 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def bar_totals_by_hinge(records):
    """Sum bar counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def measure_bolts_by_passage(bolts, passage):
    """Return the bolts that belong to the given passage."""
    return [x for x in bolts if getattr(x, "passage", None) == passage]


def rotate_hinges(hinges, limit=8):
    """Rotate hinges, at most 8 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def keeper_shift_hours(start_hour=20, shifts=3):
    """Hours at which each keeper shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def update_bolts(bolts, limit=8):
    """Update bolts, at most 8 at a time."""
    result = []
    for bolt in bolts:
        if len(result) >= limit:
            break
        result.append(bolt)
    return result
