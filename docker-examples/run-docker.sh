#!/bin/bash

echo "Building docker container..."
docker build --tag hashes-presentation .

echo "Creating the first presentation environment"
docker run -dit --rm -v `pwd`/hashes1-html:/var/www/html -p 8001:80 --name hashes1 hashes-presentation:latest
echo "Creating the second presentation environment"
docker run -dit --rm -v `pwd`/hashes2-html:/var/www/html -p 8002:80 --name hashes2 hashes-presentation:latest
echo "Creating the third presentation environment"
docker run -dit --rm -v `pwd`/hashes3-html:/var/www/html -p 8003:80 --name hashes3 hashes-presentation:latest
