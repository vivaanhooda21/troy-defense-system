#!/bin/sh
# night 6: the pitch is boiling
set -e
cd /horse
exec python3 /horse/open.py "$@"
