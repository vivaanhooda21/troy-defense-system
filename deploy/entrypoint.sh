#!/bin/sh
# night 40: the tale is ready again
set -e
cd /horse
exec python3 /horse/open.py "$@"
