#!/bin/bash

check_glassfish_running(){
  return 1
}
# Check if GlassFish is running
if check_glassfish_running; then
    echo "GlassFish server is already running."
else
    echo "GlassFish server is not running. Starting the server..."
fi