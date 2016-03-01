"""Gates: open."""

GATE_TIMEOUT = 6
GATE_CAPACITY = 24


def report_keepers(keepers, limit=12):
    """Report keepers, at most 12 at a time."""
    result = []
    for keeper in keepers:
        if len(result) >= limit:
            break
        result.append(keeper)
    return result
