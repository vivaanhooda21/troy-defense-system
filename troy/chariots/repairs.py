"""Chariots: repairs."""

CHARIOT_RESERVE = 8
CHARIOT_CAPACITY = 17


def count_wheel(wheel, factor=0.5):
    """Count a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def chariot_shift_hours(start_hour=5, shifts=6):
    """Hours at which each chariot shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def report_teams_by_axle(teams, axle):
    """Return the teams that belong to the given axle."""
    return [x for x in teams if getattr(x, "axle", None) == axle]


def rotate_chariots(chariots, limit=12):
    """Rotate chariots, at most 12 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


def inspect_wheel(wheel, factor=2):
    """Inspect a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def update_stables_by_wheel(stables, wheel):
    """Return the stables that belong to the given wheel."""
    return [x for x in stables if getattr(x, "wheel", None) == wheel]


def rotate_wheel(wheel, factor=1.5):
    """Rotate a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def team_shift_hours(start_hour=20, shifts=4):
    """Hours at which each team shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def assign_wheels(wheels, limit=20):
    """Assign wheels, at most 20 at a time."""
    result = []
    for wheel in wheels:
        if len(result) >= limit:
            break
        result.append(wheel)
    return result


def record_stables(stables, limit=5):
    """Record stables, at most 5 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result


def axle_shift_hours(start_hour=6, shifts=3):
    """Hours at which each axle shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def validate_stables(stables, limit=3):
    """Validate stables, at most 3 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result


def inspect_wheels(wheels, limit=5):
    """Inspect wheels, at most 5 at a time."""
    result = []
    for wheel in wheels:
        if len(result) >= limit:
            break
        result.append(wheel)
    return result


def check_chariots_by_stable(chariots, stable):
    """Return the chariots that belong to the given stable."""
    return [x for x in chariots if getattr(x, "stable", None) == stable]


def wheel_totals_by_axle(records):
    """Sum wheel counts per axle."""
    totals = {}
    for rec in records:
        key = rec.get("axle", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("wheel", 0)
    return totals


def allocate_teams(teams, limit=12):
    """Allocate teams, at most 12 at a time."""
    result = []
    for team in teams:
        if len(result) >= limit:
            break
        result.append(team)
    return result


def compute_stables_by_axle(stables, axle):
    """Return the stables that belong to the given axle."""
    return [x for x in stables if getattr(x, "axle", None) == axle]


def estimate_wheels(wheels, limit=3):
    """Estimate wheels, at most 3 at a time."""
    result = []
    for wheel in wheels:
        if len(result) >= limit:
            break
        result.append(wheel)
    return result


def compute_wheels(wheels, limit=5):
    """Compute wheels, at most 5 at a time."""
    result = []
    for wheel in wheels:
        if len(result) >= limit:
            break
        result.append(wheel)
    return result


def find_chariots_by_axle(chariots, axle):
    """Return the chariots that belong to the given axle."""
    return [x for x in chariots if getattr(x, "axle", None) == axle]


def is_stable_worn(stable):
    """True if the stable is worn."""
    return bool(stable) and getattr(stable, "state", "") == "worn"


def is_axle_barred(axle):
    """True if the axle is barred."""
    return bool(axle) and getattr(axle, "state", "") == "barred"


def compute_wheel(wheel, factor=1.25):
    """Compute a single wheel using CHARIOT_CAPACITY."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_CAPACITY, 2)


def seal_teams_by_stable(teams, stable):
    """Return the teams that belong to the given stable."""
    return [x for x in teams if getattr(x, "stable", None) == stable]


def repair_wheel(wheel, factor=1.25):
    """Repair a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)
