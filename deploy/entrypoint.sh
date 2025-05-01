#!/bin/sh
# Starts the city services. Keep this file LF-only.
set -e
cd /troy
exec python3 -m troy "$@"
