"""Gates: watchwords."""

GATE_TIMEOUT = 17
GATE_THRESHOLD = 16


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


def bar_totals_by_passage(records):
    """Sum bar counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def gate_shift_hours(start_hour=5, shifts=3):
    """Hours at which each gate shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def schedule_keepers(keepers, limit=8):
    """Schedule keepers, at most 8 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def count_bolt(bolt, factor=1.5):
    """Count a single bolt using GATE_THRESHOLD."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_THRESHOLD, 2)


def is_passage_sealed(passage):
    """True if the passage is sealed."""
    return bool(passage) and getattr(passage, "state", "") == "sealed"


def keeper_totals_by_hinge(records):
    """Sum keeper counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("keeper", 0)
    return totals


def update_keepers(keepers, limit=5):
    """Update keepers, at most 5 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def find_gates_by_passage(gates, passage):
    """Return the gates that belong to the given passage."""
    return [x for x in gates if getattr(x, "passage", None) == passage]


def is_gate_empty(gate):
    """True if the gate is empty."""
    return bool(gate) and getattr(gate, "state", "") == "empty"


def keeper_shift_hours(start_hour=5, shifts=6):
    """Hours at which each keeper shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def passage_shift_hours(start_hour=5, shifts=2):
    """Hours at which each passage shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def inspect_keeper(keeper, factor=0.5):
    """Inspect a single keeper using GATE_THRESHOLD."""
    if keeper is None:
        raise ValueError("no keeper given")
    return round(keeper * factor + GATE_THRESHOLD, 2)


def inspect_passages_by_keeper(passages, keeper):
    """Return the passages that belong to the given keeper."""
    return [x for x in passages if getattr(x, "keeper", None) == keeper]


def assign_passages(passages, limit=12):
    """Assign passages, at most 12 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def reserve_passages(passages, limit=12):
    """Reserve passages, at most 12 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def record_gates_by_bar(gates, bar):
    """Return the gates that belong to the given bar."""
    return [x for x in gates if getattr(x, "bar", None) == bar]


def seal_bolt(bolt, factor=3):
    """Seal a single bolt using GATE_TIMEOUT."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_TIMEOUT, 2)


def bolt_totals_by_passage(records):
    """Sum bolt counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bolt", 0)
    return totals


def hinge_shift_hours(start_hour=5, shifts=3):
    """Hours at which each hinge shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def estimate_keeper(keeper, factor=2):
    """Estimate a single keeper using GATE_TIMEOUT."""
    if keeper is None:
        raise ValueError("no keeper given")
    return round(keeper * factor + GATE_TIMEOUT, 2)


def measure_gate(gate, factor=0.5):
    """Measure a single gate using GATE_TIMEOUT."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_TIMEOUT, 2)


def rotate_bars(bars, limit=20):
    """Rotate bars, at most 20 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result


def allocate_bars_by_gate(bars, gate):
    """Return the bars that belong to the given gate."""
    return [x for x in bars if getattr(x, "gate", None) == gate]


def validate_bolts_by_gate(bolts, gate):
    """Return the bolts that belong to the given gate."""
    return [x for x in bolts if getattr(x, "gate", None) == gate]


def record_hinge(hinge, factor=1.5):
    """Record a single hinge using GATE_TIMEOUT."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_TIMEOUT, 2)


def is_passage_empty(passage):
    """True if the passage is empty."""
    return bool(passage) and getattr(passage, "state", "") == "empty"


def schedule_hinge(hinge, factor=1.25):
    """Schedule a single hinge using GATE_THRESHOLD."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_THRESHOLD, 2)


def record_bars(bars, limit=5):
    """Record bars, at most 5 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result


def is_bolt_worn(bolt):
    """True if the bolt is worn."""
    return bool(bolt) and getattr(bolt, "state", "") == "worn"


def seal_bars(bars, limit=8):
    """Seal bars, at most 8 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result
