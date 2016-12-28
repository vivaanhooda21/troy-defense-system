"""Gates: dardanian."""

GATE_HEIGHT = 10
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
