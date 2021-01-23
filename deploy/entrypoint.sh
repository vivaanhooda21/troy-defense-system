#!/bin/sh
# night 19: the fires are out
set -e
cd /horse
exec python3 /horse/open.py "$@"
