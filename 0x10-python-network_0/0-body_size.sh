#!/usr/bin/env bash
curl -i "$1" | grep "Content-Length" | cat -d " " -f 2
