#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

[ $# -ne 1 ] && { echo "Usage: $0 <URL>"; exit 1; }
size=$(curl -s "$1" | wc -c); [ -z "$size" ] && 
	echo "Unable to retrieve size of the response body." || echo "$size"
