#!/bin/bash

###############################################################################
# github-release.sh
#
# A reusable Bash script to automate the release process for SDK repositories
# following the Gitflow branching model.
#
# Features:
# - Reads the version from a VERSION file.
# - Validates the version format (Semantic Versioning).
# - Ensures the working directory is clean.
# - Initiates a Gitflow release branch.
# - Generates and updates the CHANGELOG.md file.
# - Commits changelog changes.
# - Finishes the Gitflow release (merges into master and develop, tags the release).
# - Pushes commits and tags to the remote repository.
# - Creates a GitHub release using the GitHub CLI (`gh`).
#
# Usage:
#   ./github-release.sh
#
# Configuration:
#   - Customize the variables under the "Configuration" section as needed.
#
# Requirements:
#   - Git installed and configured.
#   - Gitflow extensions installed.
#   - GitHub CLI (`gh`) installed and authenticated.
#   - A `VERSION` file present at the repository root.
#
###############################################################################

# Exit immediately if a command exits with a non-zero status
set -e

###############################################################################
# Configuration
###############################################################################

# Repository Details
REPO_OWNER="wink-travel"             # GitHub repository owner
REPO_NAME="trip-pay-python-sdk"          # GitHub repository name

# Git Branch Names (Gitflow defaults)
MAIN_BRANCH="master"                 # Main branch name (e.g., master, main)
DEVELOP_BRANCH="develop"             # Development branch name

# GitHub Release Details
GH_RELEASE_NOTES_FILE="CHANGELOG.md" # Path to the changelog or release notes file

# Version File
VERSION_FILE="VERSION"               # Path to the VERSION file

# Tag Prefix
TAG_PREFIX="v"                       # Prefix for Git tags (e.g., 'v' for 'v1.0.0')

###############################################################################
# Functions
###############################################################################

# Function to display error messages
error() {
  echo "Error: $1" >&2
  exit 1
}

# Function to validate Semantic Versioning (e.g., 1.0.0)
validate_version() {
  local version_regex="^[0-9]+\.[0-9]+\.[0-9]+(-[A-Za-z0-9.-]+)?(\+[A-Za-z0-9.-]+)?$"
  if [[ ! "$1" =~ $version_regex ]]; then
    error "Version '$1' does not follow Semantic Versioning (e.g., 1.0.0)."
  fi
}

# Function to ensure the working directory is clean
ensure_clean_working_directory() {
  if [[ -n $(git status --porcelain) ]]; then
    error "Working directory is not clean. Please commit or stash your changes before releasing."
  fi
}

# Function to read the version from the VERSION file
read_version() {
  if [[ ! -f "$VERSION_FILE" ]]; then
    error "VERSION file not found at '$VERSION_FILE'. Please ensure it exists."
  fi
  VERSION=$(cat "$VERSION_FILE")
  echo "Current Version: $VERSION"
}

# Function to initialize Gitflow if not already initialized
initialize_gitflow() {
  if ! git flow config > /dev/null 2>&1; then
    echo "Initializing Gitflow..."
    git flow init -d
    echo "Gitflow initialized."
  else
    echo "Gitflow already initialized."
  fi
}

# Function to start a Gitflow release
start_gitflow_release() {
  echo "Starting Gitflow release for version $VERSION..."
  git flow release start "$VERSION"
  echo "Gitflow release 'release/$VERSION' started."
}

# Function to generate and update the CHANGELOG.md file
generate_changelog() {
  echo "Generating changelog..."
  npx git-changelog-command-line -of "$GH_RELEASE_NOTES_FILE"
  echo "Changelog generated/updated successfully."
}

# Function to commit changelog changes on the release branch
commit_changelog() {
  echo "Committing changelog changes..."
  git add "$GH_RELEASE_NOTES_FILE"
  git commit -m "chore: update CHANGELOG for release $VERSION" || echo "No changes to commit."
  echo "Committed changelog changes."
}

# Function to finish a Gitflow release with automated merge messages
finish_gitflow_release() {
  echo "Finishing Gitflow release..."
  
  # Finish the Gitflow release with a predefined commit message
  GIT_MERGE_AUTOEDIT=no git flow release finish -m "chore: release $TAG_PREFIX$VERSION" "$VERSION" || error "Failed to finish Gitflow release."
  
  echo "Gitflow release '$VERSION' finished."
}

# Function to push commits and tags to remote
push_to_remote() {
  echo "Pushing commits to remote repository..."
  git push origin "$MAIN_BRANCH"
  git push origin "$DEVELOP_BRANCH"
  echo "Pushing Git tags to remote repository..."
  git push origin --tags
  echo "Pushed commits and tags to remote."
}

# Function to create a GitHub release using `gh`
create_github_release() {
  if [[ ! -f "$GH_RELEASE_NOTES_FILE" ]]; then
    error "Release notes file '$GH_RELEASE_NOTES_FILE' not found."
  fi
  echo "Creating GitHub release for tag '$TAG_PREFIX$VERSION'..."
  gh release create "$TAG_PREFIX$VERSION" \
    --title "Release $TAG_PREFIX$VERSION" \
    --notes-file "$GH_RELEASE_NOTES_FILE" \
    --target "$MAIN_BRANCH" || error "Failed to create GitHub release."
  echo "GitHub release created successfully."
}

###############################################################################
# Main Script Execution
###############################################################################

echo "=== Gitflow-Based Release Process Initiated ==="

# Read and validate version
read_version
validate_version "$VERSION"

# Ensure the working directory is clean
ensure_clean_working_directory

# Initialize Gitflow if not already initialized
initialize_gitflow

# Start Gitflow release
start_gitflow_release

# Generate and commit the changelog
generate_changelog
commit_changelog

# Finish Gitflow release with automated merge messages
finish_gitflow_release

# Push commits and tags to remote repository
push_to_remote

# Create GitHub release
create_github_release

echo "=== Gitflow-Based Release Process Completed Successfully ==="
echo "Version $VERSION has been released."
