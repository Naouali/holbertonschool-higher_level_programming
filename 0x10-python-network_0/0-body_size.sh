#!/bin/bash
#display the size of the content
curl -s $1 | wc -c
