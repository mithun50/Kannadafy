#!/usr/bin/env python3
"""
Emoji Obfuscation Test for Kannadafy.
This script tests the emoji pattern obfuscation.
"""

import os
import sys
import subprocess

def run_emoji_test():
    print("Testing Emoji Obfuscation")
    print("=" * 50)

    # Use the correct command format based on platform
    kannadafy_cmd = "python -m Kannadafy" if sys.platform == 'win32' else "Kannadafy"

    # Create a simple test script
    test_code = """
def emoji_test():
    '''Test function for emoji obfuscation'''
    print("Emoji obfuscation is working! 😎")

    for i in range(5):
        print(f"Count: {i} 🔢")

    return "Success! 🎉"

result = emoji_test()
print(result)
"""

    # Write the test script to a file
    with open("tests/emoji_sample.py", "w", encoding="utf-8") as f:
        f.write(test_code)

    print("Created test script: tests/emoji_sample.py")

    # Create output directory if it doesn't exist
    if not os.path.exists("tests/output"):
        os.makedirs("tests/output")

    # Run the obfuscation command
    command = f'{kannadafy_cmd} text-obfuscate -i tests/emoji_sample.py -o tests/output/emoji_obfuscated.py -t patterns/emoji_pattern.txt'
    print(f"Running command: {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print("Obfuscation successful!")
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error during obfuscation:")
        print(e.stderr)
        return False

    # Check if the output file exists
    if not os.path.exists("tests/output/emoji_obfuscated.py"):
        print("Error: Output file not created")
        return False

    # Print the obfuscated code
    print("\nObfuscated Code:")
    print("=" * 50)
    with open("tests/output/emoji_obfuscated.py", "r", encoding="utf-8") as f:
        obfuscated_code = f.read()
        print(obfuscated_code)

    # Try to execute the obfuscated code
    print("\nExecuting obfuscated code:")
    print("=" * 50)
    try:
        result = subprocess.run(
            f"python tests/output/emoji_obfuscated.py",
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print("\nEmoji obfuscation test PASSED! ✅")
        return True
    except subprocess.CalledProcessError as e:
        print("Error executing obfuscated code:")
        print(e.stderr)
        print("\nEmoji obfuscation test FAILED! ❌")
        return False

if __name__ == "__main__":
    success = run_emoji_test()
    sys.exit(0 if success else 1)
