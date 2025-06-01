#!/usr/bin/env python3
"""
Kannadafy API Version Example.
This script demonstrates how to access the Kannadafy version programmatically.
"""

def check_version_via_import():
    """Check Kannadafy version via direct import."""
    try:
        # Import Kannadafy module
        import Kannadafy

        # Access version
        version = Kannadafy.__version__

        print(f"Kannadafy version (via import): {version}")
        return version
    except ImportError:
        print("Error: Could not import Kannadafy module")
        return None
    except AttributeError:
        print("Error: __version__ attribute not found in Kannadafy module")
        return None

def check_version_via_subprocess():
    """Check Kannadafy version via subprocess."""
    import subprocess
    import sys
    import re

    # Determine appropriate command based on platform
    cmd = "python -m Kannadafy version" if sys.platform == 'win32' else "Kannadafy version"

    try:
        # Run the command
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )

        # Parse the output to extract version
        version_pattern = r'version\s+(\d+\.\d+\.\d+)'
        match = re.search(version_pattern, result.stdout, re.IGNORECASE)

        if match:
            version = match.group(1)
            print(f"Kannadafy version (via command): {version}")
            return version
        else:
            print("Error: Could not extract version from command output")
            return None
    except subprocess.SubprocessError as e:
        print(f"Error executing command: {str(e)}")
        return None

def check_version_compatibility():
    """Example function to check compatibility with a specific version."""
    import packaging.version

    # Get current version
    current_version = check_version_via_import()

    if current_version:
        # Define minimum required version
        min_required = "2.0.9"

        # Parse versions for comparison
        current = packaging.version.parse(current_version)
        required = packaging.version.parse(min_required)

        # Check compatibility
        if current >= required:
            print(f"✅ Compatible: Current version {current_version} meets minimum requirement {min_required}")
        else:
            print(f"❌ Incompatible: Current version {current_version} does not meet minimum requirement {min_required}")
    else:
        print("❌ Could not determine version compatibility")

def main():
    """Main function to demonstrate version checking."""
    print("=" * 70)
    print("KANNADAFY API VERSION EXAMPLE".center(70))
    print("=" * 70)
    print()

    # Check version via different methods
    import_version = check_version_via_import()
    command_version = check_version_via_subprocess()

    # Verify versions match
    if import_version and command_version:
        if import_version == command_version:
            print("\n✅ Versions match across different access methods")
        else:
            print(f"\n❌ Version mismatch: import={import_version}, command={command_version}")

    print("\nVersion Compatibility Check:")
    print("-" * 70)
    try:
        check_version_compatibility()
    except ImportError:
        print("Note: packaging module not available - skipping compatibility check")
        print("To install: pip install packaging")

    print("\nUsage Example:")
    print("-" * 70)
    print("""
# How to check Kannadafy version in your code:

import Kannadafy

# Print version
print(f"Using Kannadafy version {Kannadafy.__version__}")

# Check compatibility
if Kannadafy.__version__ >= "2.0.9":
    print("This code is compatible with the current Kannadafy version")
else:
    print("This code requires Kannadafy 2.0.9 or higher")
""")

if __name__ == "__main__":
    main()
