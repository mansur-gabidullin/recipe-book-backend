#!/bin/bash

# получаем путь к директории скрипта, чтобы можно было запускать скрипт из любой директории
dir_path="${0%/*}"

docker compose -f "$dir_path"/docker-compose.yml down
