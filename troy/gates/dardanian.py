"""Gates: dardanian."""

GATE_HEIGHT = 5
GATE_RESERVE = 11


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


def list_hinge(hinge, factor=3):
    """List a single hinge using GATE_HEIGHT."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_HEIGHT, 2)


def hinge_shift_hours(start_hour=18, shifts=3):
    """Hours at which each hinge shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]
