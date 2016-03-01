"""Gates: watchwords."""

GATE_TIMEOUT = 10
GATE_THRESHOLD = 10


def validate_gates(gates, limit=12):
    """Validate gates, at most 12 at a time."""
    result = []
    for gate in gates:
        if len(result) >= limit:
            break
        result.append(gate)
    return result
