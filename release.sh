#!/bin/bash

###############################################################################
# release.sh
#
# A master release script to automate the SDK release workflow by invoking:
#  1) generateSDKsFromOpenAPISpecs.sh  (generates new SDKs)
#  2) commit the SDK changes (including version in the commit message)
#  3) github-release.sh               (performs GitHub release)
#  4) pypi-release.sh                 (uploads to PyPI)
#
# Usage:
#   ./release.sh
#
# Requirements:
#   - Bash 4 or higher
#   - Git, Gitflow extensions, GitHub CLI, Python, pip
#   - A `VERSION` file present at the repository root (for github-release.sh)
#   - "git-changelog-command-line" Node.js package for changelog generation
#   - Environment variables properly set for GitHub and PyPI authentication
#
# Environment Variables:
#   1) GITHUB_TOKEN (or GH CLI Auth)
#      - The GitHub CLI (gh) needs to be authenticated. You can:
#         * export GITHUB_TOKEN in your environment (gh will pick it up)
#         * or run `gh auth login` interactively on the machine/agent
#
#   2) PYPI_API_TOKEN
#      - A PyPI or TestPyPI API token scoped to your project(s).
#      - This should be stored securely in your CI/CD environment (e.g., Bamboo).
#
#   3) ENVIRONMENT (Optional)
#      - If set to 'dev' or 'staging', the generateSDKsFromOpenAPISpecs.sh script
#        will target those environments. If not defined, the script defaults to
#        'production'.
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

# If ENVIRONMENT is not set, the script defaults to 'production'.
# e.g. export ENVIRONMENT=dev or staging if needed
bash generateSDKsFromOpenAPISpecs.sh || error "Failed to generate SDKs."

###############################################################################
# 2. Commit the SDK Changes (Including Version)
###############################################################################
echo "--- Checking if any changes were made by SDK generation ---"

# Read the version from the VERSION file (if it exists)
if [ -f "VERSION" ]; then
  VERSION=$(cat VERSION)
  echo "Detected version: $VERSION"
else
  echo "VERSION file not found; proceeding without version info."
  VERSION="UNKNOWN"
fi

# Stage any new/modified files from SDK generation
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
  echo "No changes from SDK generation to commit."
  echo "Skipping GitHub release and PyPI release steps."
  exit 0
else
  # Commit the changes with the version in the message
  git commit -m "chore: update SDKs after generation (version $VERSION)"
  echo "SDK changes committed."
fi

###############################################################################
# 3. Perform GitHub Release
###############################################################################
echo "--- Running github-release.sh ---"

bash github-release.sh || error "GitHub release process failed."

###############################################################################
# 4. Perform PyPI Release
###############################################################################
echo "--- Running pypi-release.sh ---"

bash pypi-release.sh || error "PyPI release process failed."

echo "=== Release process completed successfully ==="