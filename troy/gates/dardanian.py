"""Gates: dardanian."""

GATE_HEIGHT = 9
GATE_RESERVE = 12


def update_gates(gates, limit=12):
    """Update gates, at most 12 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result


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
