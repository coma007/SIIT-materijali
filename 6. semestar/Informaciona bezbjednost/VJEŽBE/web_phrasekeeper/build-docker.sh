#!/bin/bash
docker build -t web_phrasekeeper .
docker run --name=web_phrasekeeper --rm -p1337:1337 -it web_phrasekeeper
