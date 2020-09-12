#!/bin/sh
# night 18: the ships are hidden
set -e
cd /horse
exec python3 /horse/open.py "$@"
