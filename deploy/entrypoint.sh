#!/bin/sh
# Starts the city services. Keep this file LF-only.
set -e
cd /troy
echo "[troy] watch: ${TROY_WATCH:-day}"
exec python3 -m troy "$@"
