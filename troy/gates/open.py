# -*- coding: utf-8 -*-
"""The horse. Built outside the walls, opened inside them."""
import hashlib
import os
import re
import sys
import unicodedata

CONFIG = "/horse/config/gate.yaml"

YEARS = [
    "The Landing on the Beach",
    "The Death of Protesilaus",
    "The Embassy to Priam",
    "The Raid on Thebe",
    "The Ambush of Troilus",
    "The Year of the Plague",
    "The Wrath of Achilles",
    "The Duel of Paris and Menelaus",
    "The Broken Truce",
    "The Night Raid",
    "The Battle at the Ships",
    "The Death of Patroclus",
    "The Shield of Achilles",
    "The Fall of Hector",
    "The Ransom of Hector",
    "The Coming of the Amazons",
    "The Death of Memnon",
    "The Death of Achilles",
    "The Bow of Philoctetes",
    "The Theft of the Palladium",
]
ORDINALS = ["first", "second"]


def normalise(name):
    name = unicodedata.normalize("NFKC", name or "").casefold().strip()
    return re.sub(r"\s+", " ", name)


def read_config(path):
    """Two levels of yaml is all a horse needs."""
    cfg, section = {}, None
    for raw in open(path):
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if not line.startswith(" "):
            section = line.strip().rstrip(":")
            cfg[section] = {}
        else:
            key, _, value = line.strip().partition(":")
            cfg[section][key.strip()] = value.strip().strip('"')
    return cfg


def main():
    if not os.path.exists(CONFIG):
        print "config/gate.yaml not found. The horse does not know where the gates are."
        sys.exit(1)
    cfg = read_config(CONFIG)
    gates = cfg["gate"]["address"]
    print "The horse stirs..."

    team = os.environ.get("TEAM", "").strip()
    if not team:
        print "...but it opens only for those who name themselves.  (set TEAM)"
        sys.exit(1)
    n = int(hashlib.sha256(normalise(team).encode("utf-8")).hexdigest(), 16) % (2 * len(YEARS))
    print "The horse opens for: %s" % team
    print "Sinon carved the horse's door (deploy/entrypoint.sh) twice in every year of the war."
    print "Yours is his %s carving during \"%s\"." % (ORDINALS[n % 2], YEARS[n // 2])

    oath = os.environ.get("OATH", "").strip()
    if not oath:
        print "Speak the door as Sinon carved it.  (set OATH)"
        sys.exit(1)
    print "The horse stands before the gates of Troy: %s" % gates
    print "Knock."


if __name__ == "__main__":
    main()
