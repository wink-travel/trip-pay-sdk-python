#!/bin/bash

###############################################################################
# cd.sh
#
# Continuous Delivery/Deployment (CD) Script:
#
# This script performs the following task:
#  1) Runs pypi-release.sh to upload the generated SDK artifacts to PyPI.
#
# Note:
#   - This CD script does not pull the Git repository; it assumes that the
#     artifacts (the generated SDKs) produced during the CI phase are available.
#
# Requirements:
#   - Bash 4 or higher
#   - Python, pip and twine installed
#   - The generated SDK artifacts present in the working directory
#
# Environment Variables:
#   - PYPI_API_TOKEN: A PyPI or TestPyPI API token stored securely in your CI/CD
#     environment (e.g., Bamboo). This is required for Twine to authenticate uploads.
#
# Usage:
#   bash cd.sh
#
###############################################################################

# Exit immediately if a command fails
set -e

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

echo "=== CD Process Initiated ==="

###############################################################################
# 1. Perform PyPI Release
###############################################################################
echo "--- Running pypi-release.sh ---"
source pypi-release.sh || error "PyPI release process failed."

echo "=== CD Process Completed Successfully ==="