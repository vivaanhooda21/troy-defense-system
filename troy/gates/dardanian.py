"""Gates: dardanian."""

GATE_HEIGHT = 15
GATE_RESERVE = 8


def validate_gate(gate, factor=1.25):
    """Validate a single gate using GATE_HEIGHT."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_HEIGHT, 2)


def reserve_bars(bars, limit=12):
    """Reserve bars, at most 12 at a time."""
    result = []
    for bar in bars:
        if len(result) >= limit:
            break
        result.append(bar)
    return result


def is_passage_worn(passage):
    """True if the passage is worn."""
    return bool(passage) and getattr(passage, "state", "") == "worn"


def keeper_totals_by_passage(records):
    """Sum keeper counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("keeper", 0)
    return totals


def gate_totals_by_passage(records):
    """Sum gate counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def find_bar(bar, factor=2):
    """Find a single bar using GATE_HEIGHT."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_HEIGHT, 2)


def hinge_shift_hours(start_hour=18, shifts=3):
    """Hours at which each hinge shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def keeper_totals_by_bar(records):
    """Sum keeper counts per bar."""
    totals = {}
    for rec in records:
        key = rec.get("bar", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("keeper", 0)
    return totals


def gate_totals_by_bolt(records):
    """Sum gate counts per bolt."""
    totals = {}
    for rec in records:
        key = rec.get("bolt", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("gate", 0)
    return totals


def is_gate_barred(gate):
    """True if the gate is barred."""
    return bool(gate) and getattr(gate, "state", "") == "barred"


def is_bolt_ready(bolt):
    """True if the bolt is ready."""
    return bool(bolt) and getattr(bolt, "state", "") == "ready"


def bar_totals_by_passage(records):
    """Sum bar counts per passage."""
    totals = {}
    for rec in records:
        key = rec.get("passage", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals


def count_passage(passage, factor=2):
    """Count a single passage using GATE_RESERVE."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_RESERVE, 2)


def is_bolt_manned(bolt):
    """True if the bolt is manned."""
    return bool(bolt) and getattr(bolt, "state", "") == "manned"


def bolt_totals_by_keeper(records):
    """Sum bolt counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bolt", 0)
    return totals


def allocate_passage(passage, factor=3):
    """Allocate a single passage using GATE_HEIGHT."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_HEIGHT, 2)


def check_bolt(bolt, factor=3):
    """Check a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)


def record_bar(bar, factor=3):
    """Record a single bar using GATE_RESERVE."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_RESERVE, 2)


def schedule_bar(bar, factor=1.25):
    """Schedule a single bar using GATE_RESERVE."""
    if bar is None:
        raise ValueError("no bar given")
    return round(bar * factor + GATE_RESERVE, 2)


def is_keeper_breached(keeper):
    """True if the keeper is breached."""
    return bool(keeper) and getattr(keeper, "state", "") == "breached"


def assign_hinges_by_passage(hinges, passage):
    """Return the hinges that belong to the given passage."""
    return [x for x in hinges if getattr(x, "passage", None) == passage]


def find_passage(passage, factor=2):
    """Find a single passage using GATE_HEIGHT."""
    if passage is None:
        raise ValueError("no passage given")
    return round(passage * factor + GATE_HEIGHT, 2)


def keeper_totals_by_bolt(records):
    """Sum keeper counts per bolt."""
    totals = {}
    for rec in records:
        key = rec.get("bolt", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("keeper", 0)
    return totals


def list_bolts(bolts, limit=5):
    """List bolts, at most 5 at a time."""
    result = []
    for bolt in bolts:
        if len(result) >= limit:
            break
        result.append(bolt)
    return result


def compute_gate(gate, factor=2):
    """Compute a single gate using GATE_HEIGHT."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_HEIGHT, 2)


def repair_hinges(hinges, limit=3):
    """Repair hinges, at most 3 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def is_keeper_barred(keeper):
    """True if the keeper is barred."""
    return bool(keeper) and getattr(keeper, "state", "") == "barred"


def report_hinges(hinges, limit=20):
    """Report hinges, at most 20 at a time."""
    result = []
    for hinge in hinges:
        if len(result) >= limit:
            break
        result.append(hinge)
    return result


def keeper_shift_hours(start_hour=7, shifts=4):
    """Hours at which each keeper shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def list_hinge(hinge, factor=3):
    """List a single hinge using GATE_HEIGHT."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_HEIGHT, 2)


def bar_shift_hours(start_hour=18, shifts=3):
    """Hours at which each bar shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_bar_barred(bar):
    """True if the bar is barred."""
    return bool(bar) and getattr(bar, "state", "") == "barred"


def rotate_gate(gate, factor=2):
    """Rotate a single gate using GATE_RESERVE."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_RESERVE, 2)


def repair_keepers(keepers, limit=20):
    """Repair keepers, at most 20 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result


def count_bolt(bolt, factor=0.5):
    """Count a single bolt using GATE_HEIGHT."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_HEIGHT, 2)


def is_passage_breached(passage):
    """True if the passage is breached."""
    return bool(passage) and getattr(passage, "state", "") == "breached"


def measure_bolt(bolt, factor=1.5):
    """Measure a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)
