#!/bin/bash
if [[ -n "$2" ]]; then
    python img2json/main.py -i "$1" -o "$2" "${@:3}"
    python MSchemGen/blueprint/main.py "$2" >/dev/null
else
    python MSchemGen/blueprint/main.py "$1" >/dev/null
fi

../main -msch a.msch
viu /tmp/mindustry_schematics/image.png
