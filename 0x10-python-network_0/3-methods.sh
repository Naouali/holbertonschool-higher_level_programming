#!/bin/bash
# display all methods
s=$( curl -s -i "$1" |grep Allow | head -n 1 )
cut -d " " -f2- <<< "$s"
