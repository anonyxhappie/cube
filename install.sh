#!/bin/bash

install()
{
if [ -x "$(command -v docker)" ]; then
    echo "Docker already installed"
else
    echo "Installing docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    echo "Docker installed"
fi
}

setup() {

echo "Setup start"

mkdir -p /tmp/cubefiles

docker build -t cubeapp:v1 .

docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

docker run -v /tmp/cubefiles:/tmp/cubefiles -it -p 8000:8000 cubeapp:v1

echo "Setup complete"

}

install
setup
