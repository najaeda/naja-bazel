<!--
SPDX-License-Identifier: MIT
-->
# Naja Bazel OpenROAD flow

Demonstrates how to use Naja and Bazel to generate reports.

## Installation

Install [Bazelisk](https://bazel.build/install/bazelisk), Bazelisk will download all other dependencies using Bazel.

### Linux

The project works out of the box on Linux with all dependencies automatically managed by Bazel, including firtool binary downloads.

### macOS

**Important:** Due to current limitations in the Bazel configuration, macOS users must manually install firtool. The MODULE.bazel file only supports automatic binary downloads for Linux.

#### Manual firtool Installation (Required for macOS)

You must install firtool manually before using this project on macOS:

**Option 1: Using Homebrew (recommended)**
```bash
# Note: Check if firtool is available in Homebrew
brew install firtool
```

**Option 2: Download prebuilt binaries**
1. Visit the [CIRCT releases page](https://github.com/llvm/circt/releases/tag/firtool-1.108.0)
2. Download the appropriate macOS binary (if available)
3. Extract and add to your PATH

**Option 3: Build from source**
```bash
# Follow the official CIRCT build instructions
# https://circt.llvm.org/GettingStarted/
git clone https://github.com/llvm/circt.git
cd circt
# Follow build instructions in the repository
```

#### Additional macOS Requirements
- Xcode Command Line Tools: `xcode-select --install`
- Compatible Java version (managed by Bazel)
- Docker (for OpenROAD flow components)

#### macOS Build Configuration

After installing firtool, you may need to update the local BUILD.bazel file if firtool is not in a standard location:

```starlark
# In the genverilog rule, you might need to replace:
# "$(execpath @circt//:bin/firtool)"
# with the path to your local firtool installation, such as:
# "/usr/local/bin/firtool"  # or wherever firtool is installed
```

#### Troubleshooting macOS Issues
- Verify firtool installation: `which firtool` and `firtool --version`
- For Apple Silicon Macs, ensure you have the correct architecture binary
- If build fails, check that firtool is accessible in your PATH

#### Why Manual Installation is Required

The current Bazel configuration (MODULE.bazel) only includes automatic binary downloads for Linux. While Bazel supports platform-aware binary selection, the CIRCT project doesn't consistently provide official macOS binaries for all releases. To avoid build failures, the configuration has been simplified to only support Linux automatic downloads.

## Cross-Platform Compatibility

- **Linux**: Fully supported with automated binary downloads
- **macOS**: Supported but requires manual firtool installation (see above)
- **Most Bazel rules**: Cross-platform compatible (Scala, Python, Java components)
- **Future improvements**: Platform-aware binary downloads may be added when official macOS binaries are consistently available

## Build and view design

Global route is enough to learn everything there is to learn about this example design.

To build and view example design after global route:

    bazelisk run RetimeFanout_grt /tmp/grt gui_grt

![View design](view-design.png)

## Run naja_edit.py post synthesis and generate new netlist

The dependency of this rule is to run ORFS synthesis and pass the netlist to Naja. Naja will then read in this netlist, generate some reports and write out a new netlist. This netlist is fed into regular ORFS flow above `bazelisk run RetimeFanout_grt /tmp/grt gui_grt`

    bazelisk build naja
