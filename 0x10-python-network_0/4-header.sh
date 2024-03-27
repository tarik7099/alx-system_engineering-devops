#!/bin/bash

# Send GET request using curl with the specified header and display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
