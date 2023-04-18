#!/bin/bash

# Install required packages
apt update
apt install -y libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcups2 libdbus-1-3 libdrm2 libgbm1 libnspr4 libnss3 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 libxtst6 libx11-xcb1 xdg-utils

# Check if the installation was successful
if [[ $? -ne 0 ]]; then
  echo "Error installing required packages"
  exit 1
fi

# Download and install chromium codecs
wget -q https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+build/23549042/+files/chromium-codecs-ffmpeg-extra_100.0.4896.127-0ubuntu0.18.04.1_arm64.deb
dpkg -i chromium-codecs-ffmpeg-extra_100.0.4896.127-0ubuntu0.18.04.1_arm64.deb

# Check if the installation was successful
if [[ $? -ne 0 ]]; then
  echo "Error installing chromium codecs"
  exit 1
fi

# Download and install chromium browser
wget -q https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+build/23549042/+files/chromium-codecs-ffmpeg_100.0.4896.127-0ubuntu0.18.04.1_arm64.deb
dpkg -i chromium-codecs-ffmpeg_100.0.4896.127-0ubuntu0.18.04.1_arm64.deb

# Check if the installation was successful
if [[ $? -ne 0 ]]; then
  echo "Error installing chromium browser"
  exit 1
fi

# Download and install chromium ffmpeg
wget -q http://launchpadlibrarian.net/597256110/chromium-browser_100.0.4896.127-0ubuntu0.18.04.1_arm64.deb
dpkg -i chromium-browser_100.0.4896.127-0ubuntu0.18.04.1_arm64.deb

# Check if the installation was successful
if [[ $? -ne 0 ]]; then
  echo "Error installing chromium ffmpeg"
  exit 1
fi

echo "Chromium browser installed successfully"
