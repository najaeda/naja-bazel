#!/bin/bash
# SPDX-License-Identifier: MIT
# Script to check if firtool is available and provide setup guidance

set -e

echo "Checking firtool availability..."

if command -v firtool >/dev/null 2>&1; then
    echo "✓ firtool found in PATH: $(which firtool)"
    echo "✓ Version: $(firtool --version 2>/dev/null || echo "Unable to get version")"
    echo ""
    echo "You can now build the project with:"
    echo "  bazelisk build genverilog"
else
    echo "✗ firtool not found in PATH"
    echo ""
    echo "To fix this, you have several options:"
    echo ""
    echo "1. Install firtool in your PATH:"
    echo "   - Build CIRCT from source (see README.md for instructions)"
    echo "   - Add the firtool binary to your PATH"
    echo ""
    echo "2. Use a local CIRCT repository:"
    echo "   - Uncomment the local_repository rule in WORKSPACE"
    echo "   - Point it to your local CIRCT build"
    echo "   - Update BUILD.bazel to use @circt//:bin/firtool"
    echo ""
    echo "3. Re-enable the external repository (Linux x64 only):"
    echo "   - Uncomment the http_archive rule in MODULE.bazel"
    echo "   - Update BUILD.bazel to use @circt//:bin/firtool"
    echo ""
    echo "See README.md for detailed instructions."
    exit 1
fi