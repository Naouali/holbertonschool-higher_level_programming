#!/bin/bash
s=$(curl -i -s "$1" | grep "Content-Length")
cut -d " " -f2 <<< $s
