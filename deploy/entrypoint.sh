#!/bin/sh
# night 39: the fires are out again
set -e
cd /horse
exec python3 /horse/open.py "$@"
