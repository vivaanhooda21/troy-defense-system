#!/bin/sh
# night 1: the pine is felled
set -e
cd /horse
exec python3 /horse/open.py "$@"
