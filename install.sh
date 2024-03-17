#!/bin/bash

#git clone https://github.com/Jagernau/monitoring_csv -b auto_create monitoring_db_autosave

#cd monitoring_db_autosave

#проверить установлен ли Docker
if ! [ -x "$(command -v docker)" ]; then
    echo 'Error: docker is not installed.' >&2
    exit 1
fi
