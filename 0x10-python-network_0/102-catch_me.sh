#!/bin/bash
# POST request to 0.0.0.0:5000/catch_me to respond with "You got me!"
curl -LsX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
