#!/bin/bash
# Sends a request to the given URL and display size of the response
curl - sI "$1" | grep - i Content-Length | awk '{print $2}'
