#!/bin/sh
# night 11: the ladder is hidden
set -e
cd /horse
exec python3 /horse/open.py "$@"
