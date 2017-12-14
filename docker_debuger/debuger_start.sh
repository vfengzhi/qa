#! /bin/bash
IMG="vfengzhi/centos"
docker run -it \
    -d \
    --privileged \
    -e DISPLAY=$display \
    -e DOCKER_USER=$USER \
    -e USER=$USER \
    -e DOCKER_USER_ID=$USER_ID \
    -e DOCKER_GRP=$GRP \
    -e DOCKER_GRP_ID=$GRP_ID \
    -p 127.0.0.1:8080:8080 \
    $IMG \
    /bin/bash

#docker run -i -t -p 127.0.0.1:8080:8080 -v /Users:/home/wwwroot/default vfengzhi/centos /bin/bash
