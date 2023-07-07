#!/bin/bash

# add :local tag to image in local, build after running: eval $(minikube -p minikube docker-env)
# docker tag local-image:tagname new-repo:tagname
# docker push new-repo:tagname
# cat ~/my_password.txt | docker login --username foo --password-stdin
docker build . --network "host"  --no-cache -t "miguelros/oxygen-cs-grp01-eq13:latest"
echo $PUSH_FLAG
if [[ $1 == "push" ]]; then
    docker push miguelros/oxygen-cs-grp01-eq13:latest
fi
