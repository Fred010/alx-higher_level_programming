#!/bin/bash
# sends a GET request to URL and display response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | { read status_code && [ $status_code -eq 200 ] && curl -s "$1" || true; }"
