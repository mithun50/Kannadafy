@echo off
echo Running Kannadafy Comprehensive Test Suite
echo.
echo This will test all Kannadafy functionality, including:
echo - Basic obfuscation with Kannada script
echo - Script variations (Telugu, Tamil, Devanagari, Greek)
echo - Themed obfuscation (Food, Animal, Emoji patterns)
echo - Multi-pattern obfuscation
echo - Multi-file processing
echo.
echo Press any key to start the tests...
pause > nul

python tests/run_all_tests.py

echo.
echo All tests completed.
echo.
pause
