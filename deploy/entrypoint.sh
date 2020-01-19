#!/bin/sh
# night 15: the seams are sealed
set -e
cd /horse
exec python3 /horse/open.py "$@"
