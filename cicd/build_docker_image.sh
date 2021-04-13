#!/bin/bash
cd ..
docker build --no-cache -t cicd:wunderground .
docker tag cicd:wunderground registry:5000/wunderground:$VERSION
docker push registry:5000/wunderground:$VERSION
docker rmi cicd:wunderground

