#!/bin/sh
# night 34: the planks are sanded again
set -e
cd /horse
exec python3 /horse/open.py "$@"
