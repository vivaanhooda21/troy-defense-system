#!/bin/sh
# night 26: the pitch is boiling again
set -e
cd /horse
exec python3 /horse/open.py "$@"
