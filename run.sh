#!/bin/bash

repository="https://github.com/NNTin/Reply-LoL-Reddit.git"
localFolder="/home/pi/Desktop/Reply-LoL-Reddit"
sensitive="/home/pi/Desktop/sensitive/Reply-LoL-Reddit"

rm -r -f "$localFolder"
git clone "$repository" "$localFolder"

cp "$sensitive/obot.py" "$localFolder/obot.py"
cp "$sensitive/riotapikey.py" "$localFolder/secret/riotapikey.py"

cd "$localFolder"

until python3 main.py; do
    echo "Respawning.." >&2
    sleep 1
done