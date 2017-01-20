#!/bin/sh
# night 4: the door is cut
set -e
cd /horse
exec python3 /horse/open.py "$@"
