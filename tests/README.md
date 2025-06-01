# Kannadafy Test Suite

This directory contains a comprehensive test suite for Kannadafy, designed to verify that all functionality works correctly across different platforms.

## Test Structure

The test suite consists of the following components:

1. **test_script.py** - A sample Python script with various features used for obfuscation testing
2. **run_all_tests.py** - The main test runner that executes all tests and reports results
3. **emoji_test.py** - A focused test for emoji pattern obfuscation
4. **version_test.py** - A test for the version API functionality
5. **api_version_example.py** - Example of how to access Kannadafy version programmatically
6. **run_tests.bat** - Windows batch file for easy test execution
7. **run_tests.sh** - Shell script for Unix-based systems

## Running the Tests

### On Windows

Simply run the batch file:

```
cd tests
run_tests.bat
```

Or run the Python script directly:

```
python tests/run_all_tests.py
```

### On Unix/Linux/macOS

Make the shell script executable and run it:

```
chmod +x tests/run_tests.sh
./tests/run_tests.sh
```

Or run the Python script directly:

```
python3 tests/run_all_tests.py
```

## Testing Specific Features

### Emoji Obfuscation Test

To test only the emoji obfuscation feature:

```
python tests/emoji_test.py
```

### Version API Test

To test the version API functionality:

```
python tests/version_test.py
```

### API Version Example

To see how to programmatically access and use the Kannadafy version:

```
python tests/api_version_example.py
```

## Test Outputs

All test outputs are stored in the `tests/output` directory:

- **tests/output/kannada_obfuscated.py** - Basic Kannada obfuscation
- **tests/output/telugu_obfuscated.py** - Telugu script obfuscation
- **tests/output/tamil_obfuscated.py** - Tamil script obfuscation
- **tests/output/devanagari_obfuscated.py** - Devanagari script obfuscation
- **tests/output/greek_obfuscated.py** - Greek script obfuscation
- **tests/output/food_obfuscated.py** - Food-themed obfuscation
- **tests/output/animal_obfuscated.py** - Animal-themed obfuscation
- **tests/output/emoji_obfuscated.py** - Emoji-themed obfuscation
- **tests/output/mixed_patterns.py** - Multi-pattern obfuscation
- **tests/output/multi/** - Multi-file obfuscation outputs
- **tests/output/multi-themed/** - Multi-file themed obfuscation outputs

## Interpreting Test Results

The test suite will report each test's results individually and provide a summary at the end. If all tests pass, you'll see a "All tests PASSED!" message. If any test fails, it will be highlighted in the summary.

## Troubleshooting

If tests fail, check the following:

1. Ensure Kannadafy is properly installed
2. Verify that all required pattern files exist in the patterns directory
3. Check if any file paths need to be adjusted for your specific environment
4. Ensure the Python executable is in your PATH

## Adding New Tests

To add a new test:

1. Add a new test function to `run_all_tests.py`
2. Add your test to the `tests` list in the `main()` function
3. Run the test suite to verify your new test works correctly

Happy Testing!
