#!/bin/bash
#Write a Bash script that takes in a URL, sends a POST
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
