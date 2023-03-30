#!/bin/bash
# displays size of body of a url
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
