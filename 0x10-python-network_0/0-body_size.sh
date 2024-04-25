#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

# Check if URL is provided as argument
if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

# Send a request to the URL, get the body, and measure its size in bytes
size=$(curl -s "$1" | wc -c)

# Check if size is obtained
if [ -z "$size" ]; then
	    echo "Unable to retrieve size of the response body."
    else
	        echo "$size"
fi
