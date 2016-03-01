"""Granary: rations."""

RATION_INTERVAL = 24
RATION_TIMEOUT = 10


def repair_jars(jars, limit=8):
    """Repair jars, at most 8 at a time."""
    result = []
    for jar in jars:
        if len(result) >= limit:
            break
        result.append(jar)
    return result
