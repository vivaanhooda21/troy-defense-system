#!/bin/sh
# night 24: the door is cut again
set -e
cd /horse
exec python3 /horse/open.py "$@"
