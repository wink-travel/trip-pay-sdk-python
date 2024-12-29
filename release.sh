#!/bin/bash

###############################################################################
# release.sh
#
# A master release script to automate the SDK release workflow by invoking:
#  1) generateSDKsFromOpenAPISpecs.sh
#  2) github-release.sh
#  3) pypi-release.sh
#
# Usage:
#   ./release.sh
#
# Requirements:
#   - Bash, Git, Gitflow extensions, GitHub CLI, Python, pip
#   - A `VERSION` file present at the repository root (for github-release.sh)
#   - Environment variables properly set for GitHub and PyPI authentication
#   - The Node.js package "git-changelog-command-line" installed (for changelog generation)
#
# Notes on Environment Variables:
#   1) GITHUB_TOKEN (or GH CLI Auth):
#      - The GitHub CLI (gh) needs to be authenticated. You can:
#         * export GITHUB_TOKEN in your environment (gh will pick it up)
#         * or run `gh auth login` interactively on the machine/agent
#
#   2) PYPI_API_TOKEN:
#      - A PyPI or TestPyPI API token scoped to your project(s).
#      - This should be stored securely in your CI/CD environment (e.g., Bamboo).
#      - For usage in `pypi-release.sh`, example:
#           twine upload --username __token__ --password $PYPI_API_TOKEN
#
#   3) ENVIRONMENT (Optional):
#      - If set to 'dev' or 'staging', the generateSDKsFromOpenAPISpecs.sh script
#        will target those environments. If not defined, the script defaults to
#        'production'.
#      - Example usage if needed:
#           export ENVIRONMENT=dev
#
###############################################################################

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

echo "=== Release process initiated ==="

###############################################################################
# 1. Generate SDKs from OpenAPI Specs
###############################################################################
echo "--- Running generateSDKsFromOpenAPISpecs.sh ---"

# Ensure the script is executable
chmod +x generateSDKsFromOpenAPISpecs.sh

# If the environment variable ENVIRONMENT is not set, the script defaults to 'production'.
# Only define ENVIRONMENT if you need dev or staging behavior:
#   export ENVIRONMENT=dev    (or staging)
#
# If ENVIRONMENT is not set, the script uses production by default.

./generateSDKsFromOpenAPISpecs.sh || error "Failed to generate SDKs."

###############################################################################
# 2. Perform GitHub Release
###############################################################################
echo "--- Running github-release.sh ---"

chmod +x github-release.sh

# Before running, ensure:
#  - GITHUB_TOKEN is set OR `gh auth login` has been done on this machine.
#  - The Node.js package "git-changelog-command-line" is installed, since
#    github-release.sh depends on it for changelog generation:
#      npm install -g git-changelog-command-line

./github-release.sh || error "GitHub release process failed."

###############################################################################
# 3. Perform PyPI Release
###############################################################################
echo "--- Running pypi-release.sh ---"

chmod +x pypi-release.sh

# Ensure PYPI_API_TOKEN is set in your environment (securely stored in Bamboo).
# e.g., export PYPI_API_TOKEN=<your_token>

./pypi-release.sh || error "PyPI release process failed."

echo "=== Release process completed successfully ==="