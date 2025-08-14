<!--
SPDX-License-Identifier: MIT
-->
# Naja Bazel OpenROAD flow

Demonstrates how to use Naja and Bazel to generate reports.

## Installation

Install [Bazelisk](https://bazel.build/install/bazelisk), Bazelisk will download all other dependencies using Bazel.

### Linux

The project should work out of the box on Linux with the dependencies managed by Bazel.

### macOS

The project is designed to be cross-platform and most rules and dependencies work on macOS. However, some binaries like firtool may require additional setup:

#### Option 1: Use prebuilt binaries (if available)
The MODULE.bazel file is configured to automatically download the appropriate firtool binary for macOS when available. Check the [CIRCT releases page](https://github.com/llvm/circt/releases/tag/firtool-1.108.0) for availability.

#### Option 2: Manual installation (fallback)
If prebuilt macOS binaries are not available for firtool, you'll need to:

1. Install firtool manually:
   ```bash
   # Using Homebrew (if available)
   brew install firtool
   
   # Or build from source following CIRCT documentation
   # https://circt.llvm.org/GettingStarted/
   ```

2. Update your local BUILD.bazel to point to the locally installed firtool:
   ```starlark
   # In the genverilog rule, replace:
   # "$(execpath @circt//:bin/firtool)"
   # with the path to your local firtool installation
   ```

#### Additional macOS Requirements
- Xcode Command Line Tools: `xcode-select --install`
- Compatible Java version (managed by Bazel)
- Docker (for OpenROAD flow components)

#### Troubleshooting macOS Issues
- If firtool download fails, check the [CIRCT releases page](https://github.com/llvm/circt/releases/tag/firtool-1.108.0) for available binaries
- For Apple Silicon Macs, ensure you're using the ARM64 version if available
- If using manual installation, verify firtool is in your PATH: `which firtool`

## Cross-Platform Compatibility

This project is designed to work across different platforms:
- **Linux**: Fully supported with automated binary downloads
- **macOS**: Supported with platform-aware configuration (may require manual firtool installation)
- **Most Bazel rules**: Cross-platform compatible (Scala, Python, Java components)
- **Platform-specific binaries**: Handled via Bazel's select() mechanism

## Build and view design

Global route is enough to learn everything there is to learn about this example design.

To build and view example design after global route:

    bazelisk run RetimeFanout_grt /tmp/grt gui_grt

![View design](view-design.png)

## Run naja_edit.py post synthesis and generate new netlist

The dependency of this rule is to run ORFS synthesis and pass the netlist to Naja. Naja will then read in this netlist, generate some reports and write out a new netlist. This netlist is fed into regular ORFS flow above `bazelisk run RetimeFanout_grt /tmp/grt gui_grt`

    bazelisk build naja
