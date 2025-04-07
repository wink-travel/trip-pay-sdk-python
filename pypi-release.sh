#!/bin/bash

###############################################################################
# pypi-release.sh
#
# A CD script to upload built SDK packages to PyPI.
#
# Steps:
#   1) Find all SDK subdirectories that begin with the given prefix.
#   2) For each SDK:
#        - Upload the built package in the "dist" folder to PyPI using Twine.
#
# Usage:
#   bash pypi-release.sh
#
# Requirements:
#   - Bash 4 or higher
#   - Python, pip, twine
#   - The built SDK artifacts must be present in each SDK subdirectory (in the "dist" folder)
#
# Environment Variables:
#   - PYPI_API_TOKEN: A PyPI (or TestPyPI) API token. Must be set securely in your CI/CD environment.
#
###############################################################################

# Exit immediately if any command fails
set -e

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

echo "=== PyPI Release Process Initiated ==="

###############################################################################
# Configuration
###############################################################################

PYPI_REPO_URL="https://upload.pypi.org/legacy/"
SDK_BASE_DIR="."                     # Base directory containing SDK subdirectories
SDK_PREFIX="trip-pay-sdk-"               # Prefix for SDK directories

###############################################################################
# Functions
###############################################################################

# Function to upload an individual SDK package to PyPI
upload_sdk() {
  local sdk_dir="$1"
  local max_retries=5
  local retry_count=0
  local wait_time=10

  echo "Processing SDK: $sdk_dir"
  cd "$sdk_dir"

  upload_command="twine upload --repository-url $PYPI_REPO_URL dist/* --username __token__ --password $PYPI_API_TOKEN --verbose"

  echo "Uploading the package to PyPI for $sdk_dir..."
  until $upload_command; do
    if [ $retry_count -ge $max_retries ]; then
      echo "Exceeded maximum retries for $sdk_dir. Exiting."
      cd -
      exit 1
    fi
    retry_count=$((retry_count+1))
    echo "Upload failed. Retrying in $wait_time seconds... (Attempt $retry_count of $max_retries)"
    sleep $wait_time
    wait_time=$((wait_time*2))
  done

  echo "Package for $sdk_dir uploaded to PyPI successfully."
  cd -
}

# Function to find all SDK subdirectories
find_all_sdks() {
  echo "Scanning for SDK subdirectories with prefix '$SDK_PREFIX'..."
  SDK_LIST=$(find "$SDK_BASE_DIR" -maxdepth 1 -type d -name "${SDK_PREFIX}*" | sort)
  
  if [[ -z "$SDK_LIST" ]]; then
    error "No SDK subdirectories found with prefix '$SDK_PREFIX'."
  fi
  
  echo "Found SDKs:"
  echo "$SDK_LIST"
}

###############################################################################
# Main Script Execution
###############################################################################

# Ensure PYPI_API_TOKEN is set; if not, exit with error
if [ -z "$PYPI_API_TOKEN" ]; then
  error "PYPI_API_TOKEN environment variable is not set."
fi

find_all_sdks

# Iterate over each SDK subdirectory and upload the built package to PyPI
for sdk in $SDK_LIST; do
  upload_sdk "$sdk"
done

echo "=== PyPI Release Process Completed Successfully ==="
