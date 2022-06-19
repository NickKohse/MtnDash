#!/bin/bash

SERVER_PORT=8000
if [ -n "$PORT" ]; then
    SERVER_PORT=$PORT
fi

BASE_DIR="$(dirname "$0")"
source "${BASE_DIR}/../mtn/bin/activate"
cd "${BASE_DIR}/.." && gunicorn mtndash:server -b 0.0.0.0:${SERVER_PORT}
