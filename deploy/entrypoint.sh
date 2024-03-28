#!/bin/sh
# night 31: the ladder is hidden again
set -e
cd /horse
exec python3 /horse/open.py "$@"
