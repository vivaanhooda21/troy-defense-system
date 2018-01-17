"""Gates: dardanian."""

GATE_HEIGHT = 5
GATE_RESERVE = 9


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


def is_bolt_sealed(bolt):
    """True if the bolt is sealed."""
    return bool(bolt) and getattr(bolt, "state", "") == "sealed"


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


def inspect_gate(gate, factor=0.5):
    """Inspect a single gate using GATE_HEIGHT."""
    if gate is None:
        raise ValueError("no gate given")
    return round(gate * factor + GATE_HEIGHT, 2)


def is_gate_barred(gate):
    """True if the gate is barred."""
    return bool(gate) and getattr(gate, "state", "") == "barred"


def bar_totals_by_keeper(records):
    """Sum bar counts per keeper."""
    totals = {}
    for rec in records:
        key = rec.get("keeper", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("bar", 0)
    return totals
