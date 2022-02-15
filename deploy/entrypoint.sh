#!/bin/sh
# night 23: the belly is hollowed again
set -e
cd /horse
exec python3 /horse/open.py "$@"
