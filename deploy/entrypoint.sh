#!/bin/sh
# night 10: the hooves are shod
set -e
cd /horse
exec python3 /horse/open.py "$@"
