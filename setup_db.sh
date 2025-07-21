#!/bin/sh
cd ./server/database
docker build . -t nodeapp
docker-compose up
# FIND ENDPOINT VIA LAUNCH FUNCTION & REPLACE DJANGOAPP .env URL, ADD SLASH AT END
