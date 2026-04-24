#!/bin/bash
set -e

echo "Starting release process..."

echo "Answer 'y' to cut a new release: regenerate client, bump version, tag, and publish."
echo "Answer 'n' to retry PyPI upload of the current version (after a failed twine upload)."
read -p "Cut a new release? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    CUT_RELEASE=1
else
    CUT_RELEASE=0
    echo "Skipping release-it. Will rebuild and upload current version from pyproject.toml."
fi

if [ "$CUT_RELEASE" -eq 1 ]; then
    # Update protos submodule to latest
    echo "Updating protos submodule to latest version..."
    git submodule update --init --remote protos

    # Generate latest client code
    echo "Generating client code..."
    python3 generate_client.py

    # Commit any proto/client changes so release-it sees a clean tree
    if [ -n "$(git status --porcelain)" ]; then
        echo "Proto submodule or generated client changed — committing..."
        git add protos parrygg
        git commit -m "Regenerate client from latest protos"
    else
        echo "No proto changes detected."
    fi

    # Run release-it to get new version and create git tag
    echo "Running release-it..."
    npx release-it --only-version

    # Get the latest git tag (which release-it just created)
    NEW_VERSION=$(git describe --tags --abbrev=0 | sed 's/^v//')
    echo "New version: $NEW_VERSION"

    # Update version in pyproject.toml
    echo "Updating pyproject.toml version..."
    sed -i.bak "s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml && rm pyproject.toml.bak

    # Update version in __init__.py
    echo "Updating __init__.py version..."
    sed -i.bak "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" parrygg/__init__.py && rm parrygg/__init__.py.bak

    # Commit the version updates
    echo "Committing version updates..."
    git add pyproject.toml parrygg/__init__.py
    git commit -m "Update version to $NEW_VERSION"
else
    NEW_VERSION=$(grep '^version' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
    echo "Rebuilding version $NEW_VERSION from pyproject.toml..."
fi

# Build and publish package
echo "Building package..."
python3 -m build

echo "Publishing to PyPI..."
python3 -m twine upload dist/*

echo "Release $NEW_VERSION complete!"
