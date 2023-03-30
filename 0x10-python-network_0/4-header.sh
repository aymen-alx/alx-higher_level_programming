#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sX GET -H "X-School-User-Id: 98" "$*"
