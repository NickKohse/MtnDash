#!/bin/bash
# pull latest code and restart the service
BASE_DIR="$(dirname "$0")"
cd "${BASE_DIR}/.." && git pull origin master
systemctl service restart mtndash