#!/bin/bash

###############################################################################
# pypi-build.sh
#
# A CI script that iterates through SDK subdirectories to build the packages.
#
# Steps:
#   1) Upgrade pip and install necessary build tools (setuptools, wheel, twine, build).
#   2) Find all SDK subfolders that start with the prefix (e.g., "wink-sdk-").
#   3) For each SDK:
#        - Clean the existing "dist" folder.
#        - Build the package using either "python setup.py sdist bdist_wheel"
#          (if setup.py exists) or "python -m build" (if pyproject.toml exists).
#
# Usage:
#   bash build.sh
#
# Requirements:
#   - Bash 4 or higher
#   - Python, pip
#   - The SDK subdirectories should contain either setup.py or pyproject.toml.
#
# Optional Environment Variable:
#   - ENVIRONMENT: If set to 'dev' or 'staging', the 
#     generateSDKsFromOpenAPISpecs.sh script (if called externally) will target that environment.
#     (Defaults to 'production' if not set.)
#
###############################################################################

# Exit immediately if any command fails
set -e

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

echo "=== Build Process Initiated ==="

###############################################################################
# Configuration
###############################################################################

# You can adjust these values as needed:
SDK_BASE_DIR="."                     # Base directory containing SDK subdirectories
SDK_PREFIX="trip-pay-sdk-"               # SDK directories must begin with this prefix

###############################################################################
# Functions
###############################################################################

# Function to build an individual SDK package
build_sdk() {
  local sdk_dir="$1"
  
  echo "Processing SDK: $sdk_dir"
  cd "$sdk_dir"

  # Determine the build method based on the presence of pyproject.toml.
  if [ -f "pyproject.toml" ]; then
    build_command="python -m build"
  else
    echo "No pyproject.toml found in $sdk_dir. Skipping build."
    cd -
    return
  fi

  echo "Cleaning the dist directory in $sdk_dir..."
  # Clean the dist folder if it exists
  if [ -d "dist" ]; then
    rm -rf dist
    echo "Existing dist directory removed."
  fi

  echo "Building the package in $sdk_dir..."
  $build_command

  echo "Package in $sdk_dir built successfully."
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

find_all_sdks

# Iterate over each SDK subdirectory and build it
for sdk in $SDK_LIST; do
  build_sdk "$sdk"
done

echo "=== Build Process Completed Successfully ==="
