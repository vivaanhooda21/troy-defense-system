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


def is_hinge_lit(hinge):
    """True if the hinge is lit."""
    return bool(hinge) and getattr(hinge, "state", "") == "lit"
