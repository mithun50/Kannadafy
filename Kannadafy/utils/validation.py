"""Validation utilities for Kannadafy."""

from typing import List, Dict, Any, Optional

def validate_mapping(characters: List[str]) -> bool:
    """Validate if the mapping has enough unique characters.

    Args:
        characters: The character mapping to validate

    Returns:
        True if valid, raises ValueError otherwise
    """
    if len(characters) < 10:
        raise ValueError("Mapping must contain at least 10 unique characters")
    if len(characters) != len(set(characters)):
        raise ValueError("Mapping contains duplicate characters")
    return True

def validate_input_file(file_path: str, file_type: str = "input") -> bool:
    """Validate that an input file exists and is readable.

    Args:
        file_path: Path to the file to validate
        file_type: Type of file for error message (default: "input")

    Returns:
        True if valid, raises ValueError otherwise
    """
    import os
    if not file_path:
        raise ValueError(f"No {file_type} file path provided")

    # Normalize path (important for Windows backslash/forward slash handling)
    file_path = os.path.normpath(file_path)

    if not os.path.exists(file_path):
        raise ValueError(f"{file_type.capitalize()} file '{file_path}' not found")
    if not os.path.isfile(file_path):
        raise ValueError(f"{file_type.capitalize()} path '{file_path}' is not a file")
    return True

def validate_wordlist_files(wordlist_files: List[str]) -> bool:
    """Validate wordlist files for text-based obfuscation/deobfuscation.

    Args:
        wordlist_files: List of paths to wordlist files

    Returns:
        True if valid, raises ValueError otherwise
    """
    if not wordlist_files:
        raise ValueError("No wordlist files provided for text-based operation")

    import os
    valid_files = []
    for file_path in wordlist_files:
        # Normalize path (important for Windows backslash/forward slash handling)
        file_path = os.path.normpath(file_path)

        if not os.path.exists(file_path):
            raise ValueError(f"Wordlist file '{file_path}' not found")
        if not os.path.isfile(file_path):
            raise ValueError(f"Wordlist path '{file_path}' is not a file")
        valid_files.append(file_path)

    if not valid_files:
        raise ValueError("No valid wordlist files found")

    return True
