#!/bin/bash
# sends a GET request to URL and display response for a 200 status code
curl -s -o /dev/stdout -w "%{http_code}" "$1"
