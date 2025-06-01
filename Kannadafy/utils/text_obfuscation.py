"""
Text-Based Obfuscation Utilities for Kannadafy

This module contains functions for obfuscating Python code using words
from text files instead of character sets.
"""

import os
from typing import List, Optional

def get_text_file_words(text_files: List[str]) -> Optional[List[str]]:
    """Extract words from text files for custom mapping.

    Args:
        text_files: List of file paths to read words from

    Returns:
        List of unique words, or None if not enough words found
    """
    words = []

    for file_path in text_files:
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} not found, skipping...")
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

                # If the file has commas, split by commas
                if "," in content:
                    parts = [p.strip() for p in content.replace("\n", " ").split(",")]
                    for part in parts:
                        # Split by spaces if needed
                        if " " in part:
                            words.extend([w for w in part.split() if w])
                        else:
                            words.append(part)
                else:
                    # Otherwise, split by lines
                    lines = content.split("\n")
                    words.extend([line.strip() for line in lines if line.strip()])
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Remove duplicates while preserving order
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # Filter out any empty strings
    unique_words = [w for w in unique_words if w]

    # Ensure we have enough characters
    if len(unique_words) < 10:
        print("Error: Need at least 10 unique words for mapping")
        return None

    return unique_words

def validate_word_mapping(words: List[str]) -> bool:
    """Validate if the word mapping has enough unique entries.

    Args:
        words: List of words to validate

    Returns:
        True if valid, raises ValueError otherwise
    """
    if len(words) < 10:
        raise ValueError("Word mapping must contain at least 10 unique entries")
    if len(words) != len(set(words)):
        raise ValueError("Word mapping contains duplicate entries")
    return True
