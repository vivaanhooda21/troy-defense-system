#!/bin/sh
# night 27: the wheels are fitted again
set -e
cd /horse
exec python3 /horse/open.py "$@"
