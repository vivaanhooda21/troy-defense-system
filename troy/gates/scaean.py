"""Gates: scaean."""

GATE_RESERVE = 23
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


def compute_keepers_by_hinge(keepers, hinge):
    """Return the keepers that belong to the given hinge."""
    return [x for x in keepers if getattr(x, "hinge", None) == hinge]


def gate_shift_hours(start_hour=18, shifts=6):
    """Hours at which each gate shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def check_hinge(hinge, factor=1.5):
    """Check a single hinge using GATE_THRESHOLD."""
    if hinge is None:
        raise ValueError("no hinge given")
    return round(hinge * factor + GATE_THRESHOLD, 2)


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


def record_bolts_by_passage(bolts, passage):
    """Return the bolts that belong to the given passage."""
    return [x for x in bolts if getattr(x, "passage", None) == passage]


def allocate_bars_by_passage(bars, passage):
    """Return the bars that belong to the given passage."""
    return [x for x in bars if getattr(x, "passage", None) == passage]


def record_bolt(bolt, factor=1.25):
    """Record a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)


def is_bar_sealed(bar):
    """True if the bar is sealed."""
    return bool(bar) and getattr(bar, "state", "") == "sealed"


def validate_bolt(bolt, factor=1.25):
    """Validate a single bolt using GATE_RESERVE."""
    if bolt is None:
        raise ValueError("no bolt given")
    return round(bolt * factor + GATE_RESERVE, 2)
