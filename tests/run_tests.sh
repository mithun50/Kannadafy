#!/bin/bash

echo "Running Kannadafy Comprehensive Test Suite"
echo
echo "This will test all Kannadafy functionality, including:"
echo "- Basic obfuscation with Kannada script"
echo "- Script variations (Telugu, Tamil, Devanagari, Greek)"
echo "- Themed obfuscation (Food, Animal, Emoji patterns)"
echo "- Multi-pattern obfuscation"
echo "- Multi-file processing"
echo
echo "Press Enter to start the tests..."
read

python3 run_all_tests.py

echo
echo "All tests completed."
echo
read -p "Press Enter to exit..."
