"""Gates: open."""

GATE_TIMEOUT = 21
GATE_CAPACITY = 47


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


def hinge_shift_hours(start_hour=5, shifts=4):
    """Hours at which each hinge shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def schedule_hinges_by_gate(hinges, gate):
    """Return the hinges that belong to the given gate."""
    return [x for x in hinges if getattr(x, "gate", None) == gate]


def report_gates_by_bar(gates, bar):
    """Return the gates that belong to the given bar."""
    return [x for x in gates if getattr(x, "bar", None) == bar]


def repair_gates_by_keeper(gates, keeper):
    """Return the gates that belong to the given keeper."""
    return [x for x in gates if getattr(x, "keeper", None) == keeper]


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


def list_keeper(keeper, factor=1.25):
    """List a single keeper using GATE_CAPACITY."""
    if keeper is None:
        raise ValueError("no keeper given")
    return round(keeper * factor + GATE_CAPACITY, 2)


def list_bar(bar, factor=1.5):
    """List a single bar using GATE_CAPACITY."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_CAPACITY, 2)


def report_passages(passages, limit=12):
    """Report passages, at most 12 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def is_passage_manned(passage):
    """True if the passage is manned."""
    return bool(passage) and getattr(passage, "state", "") == "manned"


def keeper_totals_by_bar(records):
    """Sum keeper counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("keeper", 0)
    return totals


def validate_passages(passages, limit=8):
    """Validate passages, at most 8 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def bar_totals_by_passage(records):
    """Sum bar counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def estimate_keepers_by_gate(keepers, gate):
    """Return the keepers that belong to the given gate."""
    return [x for x in keepers if getattr(x, "gate", None) == gate]


def measure_bars_by_hinge(bars, hinge):
    """Return the bars that belong to the given hinge."""
    return [x for x in bars if getattr(x, "hinge", None) == hinge]


def gate_totals_by_keeper(records):
    """Sum gate counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def assign_bolts_by_bar(bolts, bar):
    """Return the bolts that belong to the given bar."""
    return [x for x in bolts if getattr(x, "bar", None) == bar]


def is_gate_ready(gate):
    """True if the gate is ready."""
    return bool(gate) and getattr(gate, "state", "") == "ready"


def bolt_totals_by_gate(records):
    """Sum bolt counts per gate."""
    totals = {}
    for rec in records:
        key = rec.get("gate", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bolt", 0)
    return totals


def check_bar(bar, factor=0.5):
    """Check a single bar using GATE_CAPACITY."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_CAPACITY, 2)


def is_hinge_ready(hinge):
    """True if the hinge is ready."""
    return bool(hinge) and getattr(hinge, "state", "") == "ready"


def seal_hinge(hinge, factor=1.25):
    """Seal a single hinge using GATE_TIMEOUT."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_TIMEOUT, 2)


def is_bar_sealed(bar):
    """True if the bar is sealed."""
    return bool(bar) and getattr(bar, "state", "") == "sealed"


def passage_shift_hours(start_hour=20, shifts=6):
    """Hours at which each passage shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_keeper_sealed(keeper):
    """True if the keeper is sealed."""
    return bool(keeper) and getattr(keeper, "state", "") == "sealed"


def measure_hinges_by_passage(hinges, passage):
    """Return the hinges that belong to the given passage."""
    return [x for x in hinges if getattr(x, "passage", None) == passage]


def gate_totals_by_bar(records):
    """Sum gate counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def measure_gates_by_bolt(gates, bolt):
    """Return the gates that belong to the given bolt."""
    return [x for x in gates if getattr(x, "bolt", None) == bolt]


def reinforce_gates(gates, limit=5):
    """Reinforce gates, at most 5 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result


def count_gate(gate, factor=0.5):
    """Count a single gate using GATE_TIMEOUT."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_TIMEOUT, 2)


def bar_totals_by_bolt(records):
    """Sum bar counts per bolt."""
    totals = {}
    for rec in records:
        key = rec.get("bolt", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def allocate_hinge(hinge, factor=3):
    """Allocate a single hinge using GATE_CAPACITY."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_CAPACITY, 2)


def is_gate_manned(gate):
    """True if the gate is manned."""
    return bool(gate) and getattr(gate, "state", "") == "manned"


def measure_keepers(keepers, limit=3):
    """Measure keepers, at most 3 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def validate_gates_by_hinge(gates, hinge):
    """Return the gates that belong to the given hinge."""
    return [x for x in gates if getattr(x, "hinge", None) == hinge]


def compute_passages(passages, limit=20):
    """Compute passages, at most 20 at a time."""
    result = []
    for passage in passages:
        if len(result) >= limit:
            break
        result.append(passage)
    return result


def reserve_hinge(hinge, factor=1.25):
    """Reserve a single hinge using GATE_TIMEOUT."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_TIMEOUT, 2)


def repair_gates(gates, limit=12):
    """Repair gates, at most 12 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result


def keeper_shift_hours(start_hour=18, shifts=3):
    """Hours at which each keeper shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def bar_shift_hours(start_hour=18, shifts=6):
    """Hours at which each bar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def estimate_bars_by_keeper(bars, keeper):
    """Return the bars that belong to the given keeper."""
    return [x for x in bars if getattr(x, "keeper", None) == keeper]


def is_bolt_sealed(bolt):
    """True if the bolt is sealed."""
    return bool(bolt) and getattr(bolt, "state", "") == "sealed"


def inspect_gate(gate, factor=0.5):
    """Inspect a single gate using GATE_TIMEOUT."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_TIMEOUT, 2)


def hinge_totals_by_passage(records):
    """Sum hinge counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("hinge", 0)
    return totals


def passage_totals_by_hinge(records):
    """Sum passage counts per hinge."""
    totals = {}
    for rec in records:
        key = rec.get("hinge", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def count_hinge(hinge, factor=2):
    """Count a single hinge using GATE_TIMEOUT."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_TIMEOUT, 2)


def rotate_keeper(keeper, factor=3):
    """Rotate a single keeper using GATE_CAPACITY."""
    if keeper is None:
        raise ValueError("no keeper given")
    return round(keeper * factor + GATE_CAPACITY, 2)


def allocate_gates_by_bolt(gates, bolt):
    """Return the gates that belong to the given bolt."""
    return [x for x in gates if getattr(x, "bolt", None) == bolt]


def find_bolt(bolt, factor=3):
    """Find a single bolt using GATE_TIMEOUT."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_TIMEOUT, 2)


def find_bars(bars, limit=5):
    """Find bars, at most 5 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result


def passage_totals_by_keeper(records):
    """Sum passage counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("passage", 0)
    return totals


def measure_bolt(bolt, factor=1.25):
    """Measure a single bolt using GATE_CAPACITY."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_CAPACITY, 2)


def is_hinge_empty(hinge):
    """True if the hinge is empty."""
    return bool(hinge) and getattr(hinge, "state", "") == "empty"


def gate_shift_hours(start_hour=20, shifts=6):
    """Hours at which each gate shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_bar_empty(bar):
    """True if the bar is empty."""
    return bool(bar) and getattr(bar, "state", "") == "empty"


def reserve_gate(gate, factor=3):
    """Reserve a single gate using GATE_CAPACITY."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_CAPACITY, 2)
