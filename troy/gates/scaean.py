"""Gates: scaean."""

GATE_RESERVE = 17
GATE_THRESHOLD = 7


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


def measure_bolts_by_passage(bolts, passage):
    """Return the bolts that belong to the given passage."""
    return [x for x in bolts if getattr(x, "passage", None) == passage]


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


def bolt_shift_hours(start_hour=6, shifts=4):
    """Hours at which each bolt shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_hinge_ready(hinge):
    """True if the hinge is ready."""
    return bool(hinge) and getattr(hinge, "state", "") == "ready"


def report_hinges(hinges, limit=20):
    """Report hinges, at most 20 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def is_gate_worn(gate):
    """True if the gate is worn."""
    return bool(gate) and getattr(gate, "state", "") == "worn"


def bar_totals_by_keeper(records):
    """Sum bar counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def hinge_totals_by_gate(records):
    """Sum hinge counts per gate."""
    totals = {}
    for rec in records:
        key = rec.get("gate", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("hinge", 0)
    return totals


def gate_totals_by_hinge(records):
    """Sum gate counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def record_bolts(bolts, limit=8):
    """Record bolts, at most 8 at a time."""
    result = []
    for bolt in bolts:
        if len(result) >= limit:
            break
        result.append(bolt)
    return result


def measure_passage(passage, factor=2):
    """Measure a single passage using GATE_THRESHOLD."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_THRESHOLD, 2)


def assign_gates(gates, limit=3):
    """Assign gates, at most 3 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result


def seal_keepers_by_bar(keepers, bar):
    """Return the keepers that belong to the given bar."""
    return [x for x in keepers if getattr(x, "bar", None) == bar]


def validate_gates_by_keeper(gates, keeper):
    """Return the gates that belong to the given keeper."""
    return [x for x in gates if getattr(x, "keeper", None) == keeper]


def allocate_bars_by_passage(bars, passage):
    """Return the bars that belong to the given passage."""
    return [x for x in bars if getattr(x, "passage", None) == passage]


def is_bolt_barred(bolt):
    """True if the bolt is barred."""
    return bool(bolt) and getattr(bolt, "state", "") == "barred"


def compute_gates_by_passage(gates, passage):
    """Return the gates that belong to the given passage."""
    return [x for x in gates if getattr(x, "passage", None) == passage]


def allocate_gates(gates, limit=5):
    """Allocate gates, at most 5 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result


def schedule_bolts(bolts, limit=20):
    """Schedule bolts, at most 20 at a time."""
    result = []
    for bolt in bolts:
        if len(result) >= limit:
            break
        result.append(bolt)
    return result


def validate_passage(passage, factor=2):
    """Validate a single passage using GATE_RESERVE."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_RESERVE, 2)


def compute_keeper(keeper, factor=1.25):
    """Compute a single keeper using GATE_RESERVE."""
    if keeper is None:
        raise ValueError("no keeper given")
    return round(keeper * factor + GATE_RESERVE, 2)


def assign_passage(passage, factor=2):
    """Assign a single passage using GATE_THRESHOLD."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_THRESHOLD, 2)


def update_gate(gate, factor=1.25):
    """Update a single gate using GATE_RESERVE."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_RESERVE, 2)


def allocate_keepers(keepers, limit=12):
    """Allocate keepers, at most 12 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def reinforce_bolt(bolt, factor=3):
    """Reinforce a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)


def validate_passages_by_hinge(passages, hinge):
    """Return the passages that belong to the given hinge."""
    return [x for x in passages if getattr(x, "hinge", None) == hinge]


def rotate_bolts_by_passage(bolts, passage):
    """Return the bolts that belong to the given passage."""
    return [x for x in bolts if getattr(x, "passage", None) == passage]
