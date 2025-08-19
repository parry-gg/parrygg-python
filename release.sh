#!/bin/bash
set -e

echo "Starting release process..."

# Generate latest client code
echo "Generating client code..."
python3 generate_client.py

# Run release-it to get new version and create git tag
echo "Running release-it..."
npx release-it --only-version

# Get the latest git tag (which release-it just created)
NEW_VERSION=$(git describe --tags --abbrev=0 | sed 's/^v//')
echo "New version: $NEW_VERSION"

# Update version in pyproject.toml
echo "Updating pyproject.toml version..."
sed -i "s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

# Update version in __init__.py
echo "Updating __init__.py version..."
sed -i "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" parrygg/__init__.py

# Commit the version updates
echo "Committing version updates..."
git add pyproject.toml parrygg/__init__.py
git commit -m "Update version to $NEW_VERSION"

# Build and publish package
echo "Building package..."
python3 -m build

echo "Publishing to PyPI..."
python3 -m twine upload dist/*

echo "Release $NEW_VERSION complete!"
