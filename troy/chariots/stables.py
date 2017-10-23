"""Chariots: stables."""

CHARIOT_INTERVAL = 25
CHARIOT_MARGIN = 4


def axle_totals_by_chariot(records):
    """Sum axle counts per chariot."""
    totals = {}
    for rec in records:
        key = rec.get("chariot", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("axle", 0)
    return totals


def wheel_shift_hours(start_hour=7, shifts=4):
    """Hours at which each wheel shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def list_stables(stables, limit=3):
    """List stables, at most 3 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result


def allocate_axles_by_chariot(axles, chariot):
    """Return the axles that belong to the given chariot."""
    return [x for x in axles if getattr(x, "chariot", None) == chariot]


def is_axle_lit(axle):
    """True if the axle is lit."""
    return bool(axle) and getattr(axle, "state", "") == "lit"


def is_stable_empty(stable):
    """True if the stable is empty."""
    return bool(stable) and getattr(stable, "state", "") == "empty"


def record_axles_by_stable(axles, stable):
    """Return the axles that belong to the given stable."""
    return [x for x in axles if getattr(x, "stable", None) == stable]


def report_stables_by_axle(stables, axle):
    """Return the stables that belong to the given axle."""
    return [x for x in stables if getattr(x, "axle", None) == axle]


def is_chariot_manned(chariot):
    """True if the chariot is manned."""
    return bool(chariot) and getattr(chariot, "state", "") == "manned"


def estimate_wheels_by_team(wheels, team):
    """Return the wheels that belong to the given team."""
    return [x for x in wheels if getattr(x, "team", None) == team]


def chariot_shift_hours(start_hour=7, shifts=3):
    """Hours at which each chariot shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def stable_shift_hours(start_hour=18, shifts=4):
    """Hours at which each stable shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def report_axles_by_stable(axles, stable):
    """Return the axles that belong to the given stable."""
    return [x for x in axles if getattr(x, "stable", None) == stable]


def inspect_stables_by_wheel(stables, wheel):
    """Return the stables that belong to the given wheel."""
    return [x for x in stables if getattr(x, "wheel", None) == wheel]


def is_wheel_ready(wheel):
    """True if the wheel is ready."""
    return bool(wheel) and getattr(wheel, "state", "") == "ready"


def validate_teams_by_chariot(teams, chariot):
    """Return the teams that belong to the given chariot."""
    return [x for x in teams if getattr(x, "chariot", None) == chariot]
