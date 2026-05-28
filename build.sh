#!/bin/bash

echo "Starting build process with PlatformIO..."
pio run

if [ $? -eq 0 ]; then
    echo "Build successful. Copying firmware to bin/ directory..."
    mkdir -p bin
    cp .pio/build/default/firmware.bin bin/crosspoint-apps.bin
    echo "Done! The compiled binary is located at: bin/crosspoint-apps.bin"
else
    echo "Build failed! Check the PlatformIO output above."
    exit 1
fi
