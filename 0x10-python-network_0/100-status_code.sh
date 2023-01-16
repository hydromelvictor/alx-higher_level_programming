#!/bin/bash
#Write a Bash script that sends a request to a URL passed as an argumen
curl -s -o /dev/null -w "%{http_code}" "$1"
