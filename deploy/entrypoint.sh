#!/bin/sh
# night 21: the pine is felled again
set -e
cd /horse
exec python3 /horse/open.py "$@"
