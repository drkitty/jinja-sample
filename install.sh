#!/usr/bin/env bash

set -o errexit
shopt -s nullglob

if ! [[ -d .env ]]; then
    virtualenv .env -p $(which python2)
fi

source .env/bin/activate

pip install jinja2
