#!/bin/bash

# URL to send a request (replace with your website URL)
URL="https://intranet.alxswe.com/users/my_profile"

# Send a request and capture the User-Agent header
userAgent=$(curl -sI $URL | grep -i '^User-Agent:' | cut -d' ' -f2-)

# Print the User-Agent information
echo "User Agent: $userAgent"
