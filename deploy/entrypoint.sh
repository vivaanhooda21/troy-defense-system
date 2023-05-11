#!/bin/sh
# Starts the city services. Keep this file LF-only.
set -e
cd /troy
umask 027
exec python3 -m troy "$@"
