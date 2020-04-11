#!/bin/bash
# display all methods
s=$(curl -s -i "$1" |grep "Allow")
cut -d " " -f2 <<< s
