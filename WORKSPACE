# SPDX-License-Identifier: MIT

# WORKSPACE file for legacy Bazel compatibility
# This project primarily uses MODULE.bazel for Bazel module dependency management

# Example: Using a local CIRCT repository instead of downloading from GitHub
# Uncomment and modify the path below to point to your local CIRCT build:
#
# local_repository(
#     name = "circt",
#     path = "/path/to/your/circt/build",
#     # Ensure your local CIRCT build has the following structure:
#     # - bin/firtool (the compiled firtool binary)
#     # You may need to create a BUILD.bazel file in your CIRCT build directory:
#     # 
#     # exports_files(["bin/firtool"], visibility = ["//visibility:public"])
# )

# Alternative: Using a local CIRCT source repository with custom build
# local_repository(
#     name = "circt", 
#     path = "/path/to/your/circt/source",
#     # This requires a proper BUILD.bazel file in the CIRCT source that 
#     # builds firtool and exports it
# )