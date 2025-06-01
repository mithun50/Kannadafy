#!/usr/bin/env python3
"""
Version API Test for Kannadafy.
This script tests the version command/API functionality.
"""

import os
import sys
import subprocess
import importlib
import re

def test_version_command():
    """Test the version command via CLI."""
    print("Testing Kannadafy Version Command")
    print("=" * 50)

    # Use the correct command format based on platform
    kannadafy_cmd = "python -m Kannadafy" if sys.platform == 'win32' else "Kannadafy"

    # Run the version command
    command = f"{kannadafy_cmd} version"
    print(f"Running command: {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print("Command output:")
        print("-" * 50)
        print(result.stdout)

        # Check if the output contains version information
        if "version" in result.stdout.lower() and re.search(r'\d+\.\d+\.\d+', result.stdout):
            print("\nVersion command test PASSED! ✅")
            # Extract version number
            version_match = re.search(r'version\s+(\d+\.\d+\.\d+)', result.stdout.lower())
            if version_match:
                print(f"Detected version: {version_match.group(1)}")
            return True
        else:
            print("\nVersion command test FAILED! ❌")
            print("Could not detect version information in the output.")
            return False
    except subprocess.CalledProcessError as e:
        print("\nError executing version command:")
        print(e.stderr)
        print("\nVersion command test FAILED! ❌")
        return False

def test_version_api_import():
    """Test accessing version information via Python import."""
    print("\nTesting Kannadafy Version via Import")
    print("=" * 50)

    try:
        # Try to import the package
        print("Attempting to import Kannadafy...")
        import Kannadafy

        # Check if __version__ attribute exists
        if hasattr(Kannadafy, '__version__'):
            print(f"Kannadafy.__version__ = {Kannadafy.__version__}")
            print("\nVersion import test PASSED! ✅")
            return True
        # Check if version attribute exists
        elif hasattr(Kannadafy, 'version'):
            print(f"Kannadafy.version = {Kannadafy.version}")
            print("\nVersion import test PASSED! ✅")
            return True
        # Check if VERSION attribute exists
        elif hasattr(Kannadafy, 'VERSION'):
            print(f"Kannadafy.VERSION = {Kannadafy.VERSION}")
            print("\nVersion import test PASSED! ✅")
            return True
        else:
            # Try to find version-related attributes
            version_attrs = [attr for attr in dir(Kannadafy) if 'version' in attr.lower()]
            if version_attrs:
                print(f"Found version-related attributes: {version_attrs}")
                for attr in version_attrs:
                    print(f"Kannadafy.{attr} = {getattr(Kannadafy, attr)}")
                print("\nVersion import test PASSED! ✅")
                return True
            else:
                print("Could not find version information in the Kannadafy package.")
                print("\nVersion import test FAILED! ❌")
                return False
    except ImportError as e:
        print(f"Import error: {str(e)}")
        print("\nVersion import test FAILED! ❌")
        return False

def main():
    """Run all version tests."""
    print("=" * 70)
    print("KANNADAFY VERSION API TEST".center(70))
    print("=" * 70)
    print()

    cmd_test = test_version_command()
    import_test = test_version_api_import()

    print("\nTest Results Summary:")
    print("-" * 50)
    print(f"Command Line Version Test: {'PASSED ✅' if cmd_test else 'FAILED ❌'}")
    print(f"Import Version Test: {'PASSED ✅' if import_test else 'FAILED ❌'}")

    all_passed = cmd_test and import_test
    print(f"\nOverall Result: {'PASSED ✅' if all_passed else 'FAILED ❌'}")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
