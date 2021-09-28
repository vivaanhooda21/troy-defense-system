#!/bin/sh
# night 22: the ribs are bent again
set -e
cd /horse
exec python3 /horse/open.py "$@"
