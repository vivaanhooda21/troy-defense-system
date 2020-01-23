#!/bin/sh
# Starts the city services. Keep this file LF-only.
set -e
cd /troy
[ -f /troy/config/walls.yaml ] || echo "[troy] warning: walls.yaml missing"
exec python3 -m troy "$@"
