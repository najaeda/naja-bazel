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

**Important:** Due to current limitations in the Bazel configuration, macOS users must manually install firtool and set the `FIRTOOL_BIN` environment variable. The MODULE.bazel file only supports automatic binary downloads for Linux.

#### Manual firtool Installation (Required for macOS)

You must install firtool manually before using this project on macOS:

**Option 1: Using Homebrew (recommended)**
```bash
# Install firtool via Homebrew (check availability)
brew install llvm
# firtool is typically included with LLVM installation
# Verify installation: firtool --version
```

**Option 2: Download prebuilt binaries**
1. Visit the [CIRCT releases page](https://github.com/llvm/circt/releases/tag/firtool-1.108.0)
2. Download the appropriate macOS binary (if available)
3. Extract to a convenient location (e.g., `/usr/local/bin/` or `~/bin/`)
4. Make executable: `chmod +x /path/to/firtool`

**Option 3: Build from source**
```bash
# Follow the official CIRCT build instructions
# https://circt.llvm.org/GettingStarted/
git clone https://github.com/llvm/circt.git
cd circt
# Follow build instructions in the repository
```

#### Setting up the Environment Variable

After installing firtool, you must set the `FIRTOOL_BIN` environment variable to tell Bazel where to find your local firtool binary:

```bash
# Find your firtool installation
which firtool

# Set the environment variable (add to your shell profile for persistence)
export FIRTOOL_BIN=$(which firtool)

# Or set to specific path if firtool is not in PATH
export FIRTOOL_BIN=/usr/local/bin/firtool

# Verify the variable is set correctly
echo $FIRTOOL_BIN
$FIRTOOL_BIN --version
```

For permanent setup, add the export line to your shell profile:
```bash
# For bash users
echo 'export FIRTOOL_BIN=$(which firtool)' >> ~/.bash_profile

# For zsh users (default on recent macOS)
echo 'export FIRTOOL_BIN=$(which firtool)' >> ~/.zshrc
```

#### Additional macOS Requirements
- Xcode Command Line Tools: `xcode-select --install`
- Compatible Java version (managed by Bazel)
- Docker (for OpenROAD flow components)

#### Troubleshooting macOS Issues

**Common issues and solutions:**

1. **"firtool not found" error**
   ```bash
   # Verify firtool installation
   which firtool
   firtool --version
   
   # Check environment variable
   echo $FIRTOOL_BIN
   ```

2. **FIRTOOL_BIN not set**
   ```bash
   # Make sure the environment variable is exported
   export FIRTOOL_BIN=$(which firtool)
   
   # Or set to absolute path
   export FIRTOOL_BIN=/path/to/your/firtool
   ```

3. **Apple Silicon (M1/M2) compatibility**
   - Ensure you have the correct architecture binary
   - If using Homebrew, it should handle architecture automatically
   - For manual downloads, look for arm64 or universal binaries

4. **Bazel build failures**
   - Verify that firtool is executable: `$FIRTOOL_BIN --version`
   - Check that the path in FIRTOOL_BIN has no spaces or special characters
   - Try an absolute path instead of using `$(which firtool)`

#### Why Manual Installation is Required

The current Bazel configuration (MODULE.bazel) only includes automatic binary downloads for Linux. While Bazel supports platform-aware binary selection, the CIRCT project doesn't consistently provide official macOS binaries for all releases. To ensure reliable builds, the configuration uses:

- **Linux**: Automatic firtool binary download via Bazel
- **macOS**: Manual installation with `FIRTOOL_BIN` environment variable
- **Future**: Platform-aware binary downloads may be added when official macOS binaries become consistently available

## Cross-Platform Compatibility

- **Linux**: Fully supported with automated firtool binary downloads
- **macOS**: Fully supported with manual firtool installation via `FIRTOOL_BIN` environment variable
- **All other Bazel rules**: Cross-platform compatible (Scala, Python, Java components)
- **Future improvements**: Platform-aware firtool binary downloads may be added when official macOS binaries are consistently available

## Build and view design

Global route is enough to learn everything there is to learn about this example design.

To build and view example design after global route:

    bazelisk run RetimeFanout_grt /tmp/grt gui_grt

![View design](view-design.png)

## Run naja_edit.py post synthesis and generate new netlist

The dependency of this rule is to run ORFS synthesis and pass the netlist to Naja. Naja will then read in this netlist, generate some reports and write out a new netlist. This netlist is fed into regular ORFS flow above `bazelisk run RetimeFanout_grt /tmp/grt gui_grt`

    bazelisk build naja
