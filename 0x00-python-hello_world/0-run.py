#!/bin/bash

PYFILE=$PYFILE
if
[ -f "$PYFILE" ]; then
/usr/bin/python3 "$PYFILE"
else
echo "Error: Python file not found!"
fi
