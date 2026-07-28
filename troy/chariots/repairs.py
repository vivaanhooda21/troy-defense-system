"""Chariots: repairs."""

CHARIOT_RESERVE = 6
CHARIOT_CAPACITY = 19


def chariot_shift_hours(start_hour=5, shifts=6):
    """Hours at which each chariot shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def rotate_chariots(chariots, limit=12):
    """Rotate chariots, at most 12 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


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


def is_axle_barred(axle):
    """True if the axle is barred."""
    return bool(axle) and getattr(axle, "state", "") == "barred"


def seal_teams_by_stable(teams, stable):
    """Return the teams that belong to the given stable."""
    return [x for x in teams if getattr(x, "stable", None) == stable]


def repair_wheel(wheel, factor=1.25):
    """Repair a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def assign_stables(stables, limit=3):
    """Assign stables, at most 3 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result


def wheel_shift_hours(start_hour=6, shifts=3):
    """Hours at which each wheel shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def compute_wheel(wheel, factor=0.5):
    """Compute a single wheel using CHARIOT_CAPACITY."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_CAPACITY, 2)


def wheel_totals_by_team(records):
    """Sum wheel counts per team."""
    totals = {}
    for rec in records:
        key = rec.get("team", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("wheel", 0)
    return totals


def is_team_worn(team):
    """True if the team is worn."""
    return bool(team) and getattr(team, "state", "") == "worn"


def team_totals_by_axle(records):
    """Sum team counts per axle."""
    totals = {}
    for rec in records:
        key = rec.get("axle", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("team", 0)
    return totals


def measure_wheel(wheel, factor=3):
    """Measure a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def is_stable_lit(stable):
    """True if the stable is lit."""
    return bool(stable) and getattr(stable, "state", "") == "lit"


def measure_axles(axles, limit=20):
    """Measure axles, at most 20 at a time."""
    result = []
    for axle in axles:
        if len(result) >= limit:
            break
        result.append(axle)
    return result


def chariot_totals_by_team(records):
    """Sum chariot counts per team."""
    totals = {}
    for rec in records:
        key = rec.get("team", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("chariot", 0)
    return totals


def is_team_sealed(team):
    """True if the team is sealed."""
    return bool(team) and getattr(team, "state", "") == "sealed"


def find_stables_by_axle(stables, axle):
    """Return the stables that belong to the given axle."""
    return [x for x in stables if getattr(x, "axle", None) == axle]


def assign_wheels_by_chariot(wheels, chariot):
    """Return the wheels that belong to the given chariot."""
    return [x for x in wheels if getattr(x, "chariot", None) == chariot]


def wheel_totals_by_chariot(records):
    """Sum wheel counts per chariot."""
    totals = {}
    for rec in records:
        key = rec.get("chariot", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("wheel", 0)
    return totals


def axle_shift_hours(start_hour=7, shifts=2):
    """Hours at which each axle shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def team_totals_by_stable(records):
    """Sum team counts per stable."""
    totals = {}
    for rec in records:
        key = rec.get("stable", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("team", 0)
    return totals


def allocate_axle(axle, factor=2):
    """Allocate a single axle using CHARIOT_CAPACITY."""
    if axle is None:
        raise ValueError("no axle given")
    return round(axle * factor + CHARIOT_CAPACITY, 2)


def check_wheel(wheel, factor=2):
    """Check a single wheel using CHARIOT_RESERVE."""
    if wheel is None:
        raise ValueError("no wheel given")
    return round(wheel * factor + CHARIOT_RESERVE, 2)


def stable_shift_hours(start_hour=5, shifts=4):
    """Hours at which each stable shift begins."""
    step = 24 // shifts
    return [(start_hour + i * step) % 24 for i in range(shifts)]


def measure_teams(teams, limit=8):
    """Measure teams, at most 8 at a time."""
    result = []
    for team in teams:
        if len(result) >= limit:
            break
        result.append(team)
    return result


def is_chariot_lit(chariot):
    """True if the chariot is lit."""
    return bool(chariot) and getattr(chariot, "state", "") == "lit"


def is_chariot_ready(chariot):
    """True if the chariot is ready."""
    return bool(chariot) and getattr(chariot, "state", "") == "ready"


def measure_chariot(chariot, factor=1.25):
    """Measure a single chariot using CHARIOT_CAPACITY."""
    if chariot is None:
        raise ValueError("no chariot given")
    return round(chariot * factor + CHARIOT_CAPACITY, 2)


def chariot_totals_by_stable(records):
    """Sum chariot counts per stable."""
    totals = {}
    for rec in records:
        key = rec.get("stable", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("chariot", 0)
    return totals


def axle_totals_by_team(records):
    """Sum axle counts per team."""
    totals = {}
    for rec in records:
        key = rec.get("team", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("axle", 0)
    return totals


def find_axles_by_team(axles, team):
    """Return the axles that belong to the given team."""
    return [x for x in axles if getattr(x, "team", None) == team]


def is_stable_breached(stable):
    """True if the stable is breached."""
    return bool(stable) and getattr(stable, "state", "") == "breached"


def validate_axles_by_chariot(axles, chariot):
    """Return the axles that belong to the given chariot."""
    return [x for x in axles if getattr(x, "chariot", None) == chariot]


def compute_chariots(chariots, limit=12):
    """Compute chariots, at most 12 at a time."""
    result = []
    for chariot in chariots:
        if len(result) >= limit:
            break
        result.append(chariot)
    return result


def count_chariot(chariot, factor=3):
    """Count a single chariot using CHARIOT_RESERVE."""
    if chariot is None:
        raise ValueError("no chariot given")
    return round(chariot * factor + CHARIOT_RESERVE, 2)


def estimate_team(team, factor=1.5):
    """Estimate a single team using CHARIOT_RESERVE."""
    if team is None:
        raise ValueError("no team given")
    return round(team * factor + CHARIOT_RESERVE, 2)


def validate_stable(stable, factor=2):
    """Validate a single stable using CHARIOT_CAPACITY."""
    if stable is None:
        raise ValueError("no stable given")
    return round(stable * factor + CHARIOT_CAPACITY, 2)


def repair_stables(stables, limit=3):
    """Repair stables, at most 3 at a time."""
    result = []
    for stable in stables:
        if len(result) >= limit:
            break
        result.append(stable)
    return result


def is_wheel_lit(wheel):
    """True if the wheel is lit."""
    return bool(wheel) and getattr(wheel, "state", "") == "lit"


def stable_totals_by_axle(records):
    """Sum stable counts per axle."""
    totals = {}
    for rec in records:
        key = rec.get("axle", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("stable", 0)
    return totals


def is_axle_breached(axle):
    """True if the axle is breached."""
    return bool(axle) and getattr(axle, "state", "") == "breached"


def stable_totals_by_chariot(records):
    """Sum stable counts per chariot."""
    totals = {}
    for rec in records:
        key = rec.get("chariot", "unknown")
        totals[key] = totals.get(key, 0) + rec.get("stable", 0)
    return totals
