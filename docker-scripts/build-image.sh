#!/bin/bash

# add :local tag to image in local, build after running: eval $(minikube -p minikube docker-env)
# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname
# cat ~/my_password.txt | docker login --username foo --password-stdin

docker build . --network "host"  --no-cache -t oxygen-cs-grp01-eq13
docker tag oxygen-cs-grp01-eq13 miguelros/oxygen-cs-grp01-eq13:latest
if [[ $1 == "push" ]]; then
    echo "$DOCKER_PASSWORD" | docker login --username miguelros --password-stdin
    echo  | sudo docker login --username miguelros --password-stdin docker.io
    docker push miguelros/oxygen-cs-grp01-eq13:latest
fi
