#!/bin/bash
# JSON POST request to the specified URL with content of a file
curl -s -X POST -H "Content-Type: application/json" -d "@$2" $1
