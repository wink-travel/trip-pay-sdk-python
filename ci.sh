#!/bin/bash

###############################################################################
# ci.sh
#
# Continuous Integration (CI) Script:
#
# This script performs the following tasks:
#  1) Runs generateSDKsFromOpenAPISpecs.sh to generate new SDKs.
#     - The script defaults to 'production' if the ENVIRONMENT variable is not set.
#       To target 'dev' or 'staging', set: export ENVIRONMENT=dev (or staging)
#  2) Stages and commits the generated SDK changes to the development branch.
#     - The commit message includes the version (read from the VERSION file).
#  3) Performs a GitHub release by invoking github-release.sh.
#
# Requirements:
#   - Bash 4 or higher
#   - Git, Gitflow extensions, GitHub CLI, Python, pip, openapi-generator
#   - "git-changelog-command-line" Node.js package installed (for changelog generation)
#
# Environment Variables:
#   - GITHUB_TOKEN: Required for GitHub CLI (gh) authentication.
#       * Example: export GITHUB_TOKEN=<your_github_token>
#
#   - ENVIRONMENT (Optional): Defaults to 'production' if not set.
#       * Set to 'dev' or 'staging' to target those environments.
#
###############################################################################

# Exit immediately if a command fails
set -e

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

echo "=== CI Process Initiated ==="

###############################################################################
# 1. Generate SDKs from OpenAPI Specs
###############################################################################
echo "--- Running generateSDKsFromOpenAPISpecs.sh ---"
# If ENVIRONMENT is not set, the script defaults to 'production'.
# To use a different environment, set for example: export ENVIRONMENT=dev
bash generateSDKsFromOpenAPISpecs.sh || error "Failed to generate SDKs."

###############################################################################
# 2. Commit the SDK Changes (Including Version)
###############################################################################
echo "--- Committing generated SDK changes ---"
if [ -f "VERSION" ]; then
  VERSION=$(cat VERSION)
  echo "Detected version: $VERSION"
else
  echo "Error: VERSION file not found. Exiting." >&2
  exit 1
fi

# Stage all changes made by SDK generation
git add .

# Check if there are changes staged for commit
if git diff --cached --quiet; then
  echo "No changes from SDK generation to commit."
  echo "Skipping GitHub and PyPI release steps."
  exit 0
else
  # Commit with a message that includes the version
  git commit -m "chore: update SDKs after generation (version $VERSION)" || error "Commit failed."
  git push origin develop || error "Failed to push commit to development branch."
  echo "SDK changes committed and pushed."
fi

###############################################################################
# 3. Perform GitHub Release
###############################################################################
echo "--- Running github-release.sh ---"
bash github-release.sh || error "GitHub release process failed."


###############################################################################
# 4. Build the SDK Artifacts for PyPI Release
###############################################################################
echo "--- Running pypi-build.sh to build SDK artifacts ---"

source pypi-build.sh || error "PyPI build process failed."

echo "=== CI Process Completed Successfully ==="