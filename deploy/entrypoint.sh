#!/bin/sh
# night 5: the hinges are greased
set -e
cd /horse
exec python3 /horse/open.py "$@"
