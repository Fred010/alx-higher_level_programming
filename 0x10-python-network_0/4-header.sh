#!/bin/bash
# GET request to provided URL with header set to 98 and reponse
curl -s -H "X-School-User-Id: 98" "$1"
