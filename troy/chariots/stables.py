"""Chariots: stables."""

CHARIOT_INTERVAL = 30
CHARIOT_MARGIN = 9


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


def record_axles_by_stable(axles, stable):
    """Return the axles that belong to the given stable."""
    return [x for x in axles if getattr(x, "stable", None) == stable]


def report_stables_by_axle(stables, axle):
    """Return the stables that belong to the given axle."""
    return [x for x in stables if getattr(x, "axle", None) == axle]


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


def is_wheel_ready(wheel):
    """True if the wheel is ready."""
    return bool(wheel) and getattr(wheel, "state", "") == "ready"


def validate_teams_by_chariot(teams, chariot):
    """Return the teams that belong to the given chariot."""
    return [x for x in teams if getattr(x, "chariot", None) == chariot]


def axle_shift_hours(start_hour=20, shifts=3):
    """Hours at which each axle shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def check_axles_by_stable(axles, stable):
    """Return the axles that belong to the given stable."""
    return [x for x in axles if getattr(x, "stable", None) == stable]


def axle_totals_by_stable(records):
    """Sum axle counts per stable."""
    totals = {}
    for rec in records:
        key = rec.get("stable", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("axle", 0)
    return totals


def seal_chariots(chariots, limit=5):
    """Seal chariots, at most 5 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


def chariot_totals_by_stable(records):
    """Sum chariot counts per stable."""
    totals = {}
    for rec in records:
        key = rec.get("stable", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("chariot", 0)
    return totals


def report_stable(stable, factor=0.5):
    """Report a single stable using CHARIOT_INTERVAL."""
    if stable is None:
        raise ValueError("no stable given")
    return round(stable * factor + CHARIOT_INTERVAL, 2)


def team_shift_hours(start_hour=20, shifts=3):
    """Hours at which each team shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def is_chariot_empty(chariot):
    """True if the chariot is empty."""
    return bool(chariot) and getattr(chariot, "state", "") == "empty"


def inspect_teams(teams, limit=5):
    """Inspect teams, at most 5 at a time."""
    result = []
    for team in teams:
        if len(result) >= limit:
            break
        result.append(team)
    return result


def wheel_totals_by_team(records):
    """Sum wheel counts per team."""
    totals = {}
    for rec in records:
        key = rec.get("team", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("wheel", 0)
    return totals


def chariot_totals_by_wheel(records):
    """Sum chariot counts per wheel."""
    totals = {}
    for rec in records:
        key = rec.get("wheel", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("chariot", 0)
    return totals


def count_stables(stables, limit=12):
    """Count stables, at most 12 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result


def update_chariots(chariots, limit=3):
    """Update chariots, at most 3 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


def estimate_wheel(wheel, factor=0.5):
    """Estimate a single wheel using CHARIOT_INTERVAL."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_INTERVAL, 2)


def reinforce_axle(axle, factor=2):
    """Reinforce a single axle using CHARIOT_MARGIN."""
    if axle is None:
        raise ValueError("no axle given")
    return round(axle * factor + CHARIOT_MARGIN, 2)


def seal_chariot(chariot, factor=2):
    """Seal a single chariot using CHARIOT_INTERVAL."""
    if chariot is None:
        raise ValueError("no chariot given")
    return round(chariot * factor + CHARIOT_INTERVAL, 2)


def is_wheel_empty(wheel):
    """True if the wheel is empty."""
    return bool(wheel) and getattr(wheel, "state", "") == "empty"


def assign_chariots_by_axle(chariots, axle):
    """Return the chariots that belong to the given axle."""
    return [x for x in chariots if getattr(x, "axle", None) == axle]


def inspect_wheel(wheel, factor=2):
    """Inspect a single wheel using CHARIOT_MARGIN."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_MARGIN, 2)


def measure_teams_by_wheel(teams, wheel):
    """Return the teams that belong to the given wheel."""
    return [x for x in teams if getattr(x, "wheel", None) == wheel]


def assign_chariot(chariot, factor=1.25):
    """Assign a single chariot using CHARIOT_INTERVAL."""
    if chariot is None:
        raise ValueError("no chariot given")
    return round(chariot * factor + CHARIOT_INTERVAL, 2)


def schedule_wheels_by_stable(wheels, stable):
    """Return the wheels that belong to the given stable."""
    return [x for x in wheels if getattr(x, "stable", None) == stable]


def estimate_teams(teams, limit=12):
    """Estimate teams, at most 12 at a time."""
    result = []
    for team in teams:
        if len(result) >= limit:
            break
        result.append(team)
    return result


def is_wheel_worn(wheel):
    """True if the wheel is worn."""
    return bool(wheel) and getattr(wheel, "state", "") == "worn"


def wheel_totals_by_axle(records):
    """Sum wheel counts per axle."""
    totals = {}
    for rec in records:
        key = rec.get("axle", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("wheel", 0)
    return totals


def is_axle_barred(axle):
    """True if the axle is barred."""
    return bool(axle) and getattr(axle, "state", "") == "barred"


def team_totals_by_wheel(records):
    """Sum team counts per wheel."""
    totals = {}
    for rec in records:
        key = rec.get("wheel", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("team", 0)
    return totals


def is_stable_manned(stable):
    """True if the stable is manned."""
    return bool(stable) and getattr(stable, "state", "") == "manned"
