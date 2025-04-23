#!/bin/sh
# night 35: the seams are sealed again
set -e
cd /horse
exec python3 /horse/open.py "$@"
