#!/usr/bin/env python3
"""
Comprehensive test script for Kannadafy.
This script runs and verifies all Kannadafy commands.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Print a header with formatting."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(80)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 80}{Colors.ENDC}\n")

def print_step(text):
    """Print a step with formatting."""
    print(f"{Colors.BLUE}{Colors.BOLD}[STEP]{Colors.ENDC} {text}")

def print_success(text):
    """Print a success message with formatting."""
    print(f"{Colors.GREEN}{Colors.BOLD}[SUCCESS]{Colors.ENDC} {text}")

def print_warning(text):
    """Print a warning message with formatting."""
    print(f"{Colors.YELLOW}{Colors.BOLD}[WARNING]{Colors.ENDC} {text}")

def print_error(text):
    """Print an error message with formatting."""
    print(f"{Colors.RED}{Colors.BOLD}[ERROR]{Colors.ENDC} {text}")

def run_command(command, expected_return_code=0):
    """Run a command and return its output."""
    print_step(f"Running command: {command}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            capture_output=True,
            text=True
        )

        if result.returncode != expected_return_code:
            print_error(f"Command failed with return code: {result.returncode}")
            print(f"Error output: {result.stderr}")
            return False, result.stdout

        print_success(f"Command executed successfully")
        return True, result.stdout
    except Exception as e:
        print_error(f"Exception occurred: {str(e)}")
        return False, str(e)

def verify_file_exists(file_path):
    """Verify that a file exists."""
    if os.path.exists(file_path):
        print_success(f"File exists: {file_path}")
        return True
    else:
        print_error(f"File does not exist: {file_path}")
        return False

def verify_file_executable(file_path):
    """Verify that a file is executable."""
    print_step(f"Verifying file is executable: {file_path}")
    success, output = run_command(f"python {file_path}")
    if success:
        print_success(f"File is executable")
        print(f"Output: {output.strip()}")
        return True
    else:
        print_error(f"File is not executable")
        return False

def setup_test_environment():
    """Set up the test environment."""
    print_header("Setting up test environment")

    # Create output directory
    if not os.path.exists("tests/output"):
        os.makedirs("tests/output")
        print_success("Created output directory")
    else:
        # Clean previous test outputs
        for item in os.listdir("tests/output"):
            item_path = os.path.join("tests/output", item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print_success("Cleaned output directory")

    # Create multi-file test directory
    if not os.path.exists("tests/output/multi"):
        os.makedirs("tests/output/multi")
        print_success("Created multi-file output directory")

def get_kannadafy_command():
    """Get the appropriate command to run Kannadafy based on the platform."""
    if sys.platform == 'win32':
        return "python -m Kannadafy"
    else:
        return "Kannadafy"

def run_basic_obfuscation_test():
    """Test basic obfuscation with default Kannada script."""
    print_header("Testing Basic Obfuscation (Kannada)")

    kannadafy_cmd = get_kannadafy_command()
    command = f"{kannadafy_cmd} obfuscate -i tests/test_script.py -o tests/output/kannada_obfuscated.py"

    success, _ = run_command(command)
    if success:
        file_exists = verify_file_exists("tests/output/kannada_obfuscated.py")
        if file_exists:
            return verify_file_executable("tests/output/kannada_obfuscated.py")

    return False

def run_script_variation_tests():
    """Test obfuscation with different script types."""
    print_header("Testing Script Variations")

    script_types = ["telugu", "tamil", "devanagari", "greek"]
    kannadafy_cmd = get_kannadafy_command()
    all_successful = True

    for script in script_types:
        print_step(f"Testing {script.capitalize()} script")
        command = f"{kannadafy_cmd} obfuscate -i tests/test_script.py -o tests/output/{script}_obfuscated.py -s {script}"

        success, _ = run_command(command)
        if success:
            file_exists = verify_file_exists(f"tests/output/{script}_obfuscated.py")
            if file_exists:
                script_success = verify_file_executable(f"tests/output/{script}_obfuscated.py")
                if not script_success:
                    all_successful = False
            else:
                all_successful = False
        else:
            all_successful = False

    return all_successful

def run_themed_obfuscation_tests():
    """Test obfuscation with different themed wordlists."""
    print_header("Testing Themed Obfuscation")

    themes = [
        {"name": "food", "pattern": "patterns/food_words.txt"},
        {"name": "animal", "pattern": "patterns/animal_pattern.txt"},
        {"name": "emoji", "pattern": "patterns/emoji_pattern.txt"}
    ]

    kannadafy_cmd = get_kannadafy_command()
    all_successful = True

    for theme in themes:
        print_step(f"Testing {theme['name']} theme")
        command = f"{kannadafy_cmd} text-obfuscate -i tests/test_script.py -o tests/output/{theme['name']}_obfuscated.py -t {theme['pattern']}"

        success, _ = run_command(command)
        if success:
            file_exists = verify_file_exists(f"tests/output/{theme['name']}_obfuscated.py")
            if file_exists:
                theme_success = verify_file_executable(f"tests/output/{theme['name']}_obfuscated.py")
                if not theme_success:
                    all_successful = False
            else:
                all_successful = False
        else:
            all_successful = False

    return all_successful

def run_multi_pattern_test():
    """Test obfuscation with multiple pattern files."""
    print_header("Testing Multi-Pattern Obfuscation")

    kannadafy_cmd = get_kannadafy_command()
    command = f"{kannadafy_cmd} text-obfuscate -i tests/test_script.py -o tests/output/mixed_patterns.py -t patterns/food_words.txt patterns/animal_pattern.txt"

    success, _ = run_command(command)
    if success:
        file_exists = verify_file_exists("tests/output/mixed_patterns.py")
        if file_exists:
            return verify_file_executable("tests/output/mixed_patterns.py")

    return False

def create_additional_test_scripts():
    """Create additional test scripts for multi-file processing."""
    test_files = [
        {"name": "script1.py", "content": """
def add(a, b):
    return a + b

print("Script 1 - Result:", add(5, 7))
"""},
        {"name": "script2.py", "content": """
def multiply(a, b):
    return a * b

print("Script 2 - Result:", multiply(5, 7))
"""},
        {"name": "script3.py", "content": """
def greet(name):
    return f"Hello, {name}!"

print("Script 3 - Result:", greet("Kannadafy"))
"""}
    ]

    for test_file in test_files:
        file_path = os.path.join("tests", test_file["name"])
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(test_file["content"])
        print_success(f"Created test file: {file_path}")

def run_multi_file_test():
    """Test multi-file obfuscation."""
    print_header("Testing Multi-File Obfuscation")

    # Create test scripts
    create_additional_test_scripts()

    kannadafy_cmd = get_kannadafy_command()
    command = f"{kannadafy_cmd} multi-obfuscate -i tests/script1.py tests/script2.py tests/script3.py -o tests/output/multi"

    success, _ = run_command(command)
    if success:
        all_successful = True
        for i in range(1, 4):
            file_path = f"tests/output/multi/script{i}.py"
            file_exists = verify_file_exists(file_path)
            if file_exists:
                file_success = verify_file_executable(file_path)
                if not file_success:
                    all_successful = False
            else:
                all_successful = False

        return all_successful

    return False

def run_multi_themed_test():
    """Test multi-file themed obfuscation."""
    print_header("Testing Multi-File Themed Obfuscation")

    kannadafy_cmd = get_kannadafy_command()
    command = f"{kannadafy_cmd} multi-text-obfuscate -i tests/script1.py tests/script2.py tests/script3.py -o tests/output/multi-themed -t patterns/emoji_pattern.txt"

    success, _ = run_command(command)
    if success:
        all_successful = True
        for i in range(1, 4):
            file_path = f"tests/output/multi-themed/script{i}.py"
            file_exists = verify_file_exists(file_path)
            if file_exists:
                file_success = verify_file_executable(file_path)
                if not file_success:
                    all_successful = False
            else:
                all_successful = False

        return all_successful

    return False

def main():
    """Main function to run all tests."""
    print_header("Kannadafy Comprehensive Test Suite")

    # Setup test environment
    setup_test_environment()

    # Run tests
    tests = [
        {"name": "Basic Obfuscation Test", "function": run_basic_obfuscation_test},
        {"name": "Script Variation Tests", "function": run_script_variation_tests},
        {"name": "Themed Obfuscation Tests", "function": run_themed_obfuscation_tests},
        {"name": "Multi-Pattern Test", "function": run_multi_pattern_test},
        {"name": "Multi-File Test", "function": run_multi_file_test},
        {"name": "Multi-File Themed Test", "function": run_multi_themed_test}
    ]

    results = []

    for test in tests:
        print_header(f"Running {test['name']}")
        success = test["function"]()
        results.append({"name": test["name"], "success": success})

    # Print summary
    print_header("Test Results Summary")

    all_passed = True
    for result in results:
        if result["success"]:
            print_success(f"{result['name']}: PASSED")
        else:
            print_error(f"{result['name']}: FAILED")
            all_passed = False

    if all_passed:
        print_header("All tests PASSED!")
    else:
        print_header("Some tests FAILED!")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
