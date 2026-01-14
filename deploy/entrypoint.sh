#!/bin/sh
# night 38: the ships are hidden again
set -e
cd /horse
exec python3 /horse/open.py "$@"
