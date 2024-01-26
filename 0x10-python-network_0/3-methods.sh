#!/bin/bash
# Script: Display HTTP methods accepted by the server
curl -s -I -X OPTIONS "$1" | grep "Allow" | cut -d' ' -f2-
