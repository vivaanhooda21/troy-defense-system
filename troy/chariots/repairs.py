"""Chariots: repairs."""

CHARIOT_RESERVE = 10
CHARIOT_CAPACITY = 9


def count_wheel(wheel, factor=0.5):
    """Count a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def chariot_shift_hours(start_hour=5, shifts=6):
    """Hours at which each chariot shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def measure_chariots(chariots, limit=12):
    """Measure chariots, at most 12 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


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


def chariot_totals_by_axle(records):
    """Sum chariot counts per axle."""
    totals = {}
    for rec in records:
        key = rec.get("axle", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("chariot", 0)
    return totals


def list_team(team, factor=1.5):
    """List a single team using CHARIOT_RESERVE."""
    if team is None:
        raise ValueError("no team given")
    return round(team * factor + CHARIOT_RESERVE, 2)


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
