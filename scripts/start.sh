#!/bin/bash
BASE_DIR="$(dirname "$0")"
source "${BASE_DIR}/../mtn/bin/activate"
cd "${BASE_DIR}/.." && gunicorn mtndash:server -b 0.0.0.0:8000
