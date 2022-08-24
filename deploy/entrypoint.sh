#!/bin/sh
# night 25: the hinges are greased again
set -e
cd /horse
exec python3 /horse/open.py "$@"
