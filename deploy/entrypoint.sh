#!/bin/sh
# night 20: the tale is ready
set -e
cd /horse
exec python3 /horse/open.py "$@"
