#!/bin/sh
# night 30: the hooves are shod again
set -e
cd /horse
exec python3 /horse/open.py "$@"
