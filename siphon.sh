#!/bin/bash
echo "{"
for file in src/*.png; do
    if [[ $file == "src/spritesheet.png" ]]; then
        continue
    fi
    o=$(~/MSchemGen/img2json/avgcolor.py "$file")
    file=$(basename "$file")
    file=${file//$'-ui.png'/}
    file=${file//$'block-'/}
    echo "$o: \"$file\","
done
echo "}"
