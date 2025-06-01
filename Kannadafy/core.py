# Kannadafy/core.py
import os
import re
import json
import yaml
from pprint import pformat
import ast
from typing import List, Dict, Optional, Union

# Predefined character sets
CHARACTER_SETS = {
    "kannada": [
        "ಅ", "ಆ", "ಇ", "ಈ", "ಉ", "ಊ", "ಋ", "ಎ", "ಏ", "ಐ", "ಒ", "ಓ", "ಔ", "ಅಂ", "ಅ:",
        "ಕ", "ಖ", "ಗ", "ಘ", "ಙ", "ಚ", "ಛ", "ಜ", "ಝ", "ಞ", "ಟ", "ಠ", "ಡ", "ಢ", "ಣ",
        "ತ", "ಥ", "ದ", "ಧ", "ನ", "ಪ", "ಫ", "ಬ", "ಭ", "ಮ", "ಯ", "ರ", "ಲ", "ವ", "ಶ",
        "ಷ", "ಸ", "ಹ", "ಳ"
    ],
    "devanagari": [
        "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ", "क", "ख", "ग", "घ", "ङ",
        "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न",
        "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह"
    ],
    "telugu": [
        "అ", "ఆ", "ఇ", "ఈ", "ఉ", "ఊ", "ఋ", "ఎ", "ఏ", "ఐ", "ఒ", "ఓ", "ఔ", "క", "ఖ",
        "గ", "ఘ", "ఙ", "చ", "ఛ", "జ", "ఝ", "ఞ", "ట", "ఠ", "డ", "ఢ", "ణ", "త", "థ",
        "ద", "ధ", "న", "ప", "ఫ", "బ", "భ", "మ", "య", "ర", "ల", "వ", "శ", "ష", "స", "హ"
    ],
    "tamil": [
        "அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ", "க", "ங",
        "ச", "ஞ", "ட", "ண", "த", "ந", "ப", "ம", "ய", "ர", "ல", "வ", "ழ", "ள",
        "ற", "ன", "ஜ", "ஷ", "ஸ", "ஹ"
    ],
    "greek": [
        "α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ",
        "ο", "π", "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω", "Γ", "Δ", "Θ", "Λ",
        "Ξ", "Π", "Σ", "Φ", "Ψ", "Ω"
    ]
}

MAX_STR_LEN = 70

def validate_mapping(characters: List[str]) -> bool:
    """Validate if the mapping has enough unique characters."""
    if len(characters) < 10:
        raise ValueError("Mapping must contain at least 10 unique characters")
    if len(characters) != len(set(characters)):
        raise ValueError("Mapping contains duplicate characters")
    return True

def generate_mapping_template(output_file: str, script_type: str = "kannada") -> None:
    """Generate a template mapping file with example characters."""
    if script_type not in CHARACTER_SETS:
        available = ", ".join(CHARACTER_SETS.keys())
        raise ValueError(f"Unknown script type. Available types: {available}")

    template = {
        "name": f"Custom {script_type.title()} Mapping",
        "description": "Custom character mapping for Kannadafy",
        "author": "Your Name",
        "script_type": script_type,
        "characters": CHARACTER_SETS[script_type]
    }

    ext = os.path.splitext(output_file)[1].lower()

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            if ext == '.json':
                json.dump(template, f, ensure_ascii=False, indent=2)
            elif ext == '.yaml' or ext == '.yml':
                yaml.safe_dump(template, f, allow_unicode=True, default_flow_style=False)
            else:
                raise ValueError("Template file must have .json, .yaml, or .yml extension")
        print(f"[✅] Template mapping file created at: {output_file}")
    except Exception as e:
        raise ValueError(f"Failed to create template: {str(e)}")

def load_custom_mapping(mapping_file: str) -> List[str]:
    """Load custom character mapping from a file.

    Supports:
    - YAML (.yaml, .yml): Recommended format with metadata
    - JSON (.json): Alternative format with metadata
    - Python (.py): Simple list assignment
    - Text (.txt): One character per line
    """
    if not os.path.exists(mapping_file):
        raise FileNotFoundError(f"Mapping file '{mapping_file}' not found")

    ext = os.path.splitext(mapping_file)[1].lower()

    try:
        if ext in ['.yaml', '.yml']:
            with open(mapping_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                if isinstance(data, dict) and 'characters' in data:
                    chars = data['characters']
                    validate_mapping(chars)
                    return chars
                else:
                    raise ValueError("YAML file must contain a 'characters' key with list of characters")

        elif ext == '.json':
            with open(mapping_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    validate_mapping(data)
                    return data
                elif isinstance(data, dict) and 'characters' in data:
                    chars = data['characters']
                    validate_mapping(chars)
                    return chars
                else:
                    raise ValueError("JSON file must contain a list or dict with 'characters' key")

        elif ext == '.py':
            with open(mapping_file, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'[A-Za-z_][A-Za-z0-9_]*\s*=\s*(\[.*?\])', content, re.DOTALL)
                if match:
                    chars = ast.literal_eval(match.group(1))
                    validate_mapping(chars)
                    return chars
                else:
                    raise ValueError("Python file must contain a list assignment")

        else:  # Default to .txt format
            with open(mapping_file, 'r', encoding='utf-8') as f:
                chars = [line.strip() for line in f if line.strip()]
                validate_mapping(chars)
                return chars

    except Exception as e:
        raise ValueError(f"Failed to load mapping file: {str(e)}")

def get_available_scripts() -> List[str]:
    """Get list of available predefined script types."""
    return list(CHARACTER_SETS.keys())

def chunk_string(in_s, n):
    """Chunk string to max length of n."""
    return "\n".join(
        "{}\\".format(in_s[i: i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")

def encode_string(in_s, alphabet):
    """Convert input string to encoded output string with the given alphabet."""
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
    )

def obfuscate(input_filepath, output_filepath, kannada=True, mapping_file=None, custom_alphabet=None, text_files=None, script_type="kannada"):
    """Obfuscate a Python script using Kannada letters or custom mapping.

    Args:
        input_filepath (str): Path to the input Python script
        output_filepath (str): Path to write the obfuscated output
        kannada (bool): Whether to use Kannada letters (default: True) - DEPRECATED, use script_type instead
        mapping_file (str, optional): Path to a custom mapping file
        custom_alphabet (list, optional): List of custom characters to use for mapping
        text_files (list, optional): List of text files to use for word-based mapping
        script_type (str): Type of script to use (default: "kannada")
    """
    # Normalize paths
    input_filepath = os.path.normpath(input_filepath)
    output_filepath = os.path.normpath(output_filepath)
    if mapping_file:
        mapping_file = os.path.normpath(mapping_file)
    if text_files:
        text_files = [os.path.normpath(path) for path in text_files]

    # Input validation
    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file {input_filepath} not found")

    # Determine which alphabet to use
    alphabet = None

    if text_files:
        # Use text files for mapping
        from Kannadafy.utils.text_obfuscation import get_text_file_words
        alphabet = get_text_file_words(text_files)
        if not alphabet:
            raise ValueError("Could not generate sufficient mapping from text files")
    elif custom_alphabet:
        # Use provided custom alphabet
        alphabet = custom_alphabet
        validate_mapping(alphabet)
    elif mapping_file:
        # Load mapping from file
        alphabet = load_custom_mapping(mapping_file)
    else:
        # Use specified script type or default to Kannada
        if script_type in CHARACTER_SETS:
            alphabet = CHARACTER_SETS[script_type]
        else:
            alphabet = CHARACTER_SETS["kannada"]

    try:
        # Read the input file
        with open(input_filepath, 'r', encoding='utf-8') as f:
            input_content = f.read()

        # Generate the obfuscated code
        obfuscated_content = encode_string(input_content, alphabet)

        # Write to output file
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(obfuscated_content)

        return True
    except Exception as e:
        raise RuntimeError(f"Obfuscation failed: {str(e)}")

def obfuscate_multiple(input_filepaths, output_dir, alphabet_type="kannada", mapping_file=None, custom_alphabet=None, text_files=None):
    """Obfuscate multiple Python scripts at once.

    Args:
        input_filepaths (list): List of paths to input Python scripts
        output_dir (str): Directory to write the obfuscated outputs
        alphabet_type (str): Type of alphabet to use (default: "kannada")
        mapping_file (str, optional): Path to a custom mapping file
        custom_alphabet (list, optional): List of custom characters to use for mapping
        text_files (list, optional): List of text files to use for word-based mapping

    Returns:
        dict: Dictionary mapping input files to output files
    """
    # Normalize paths
    output_dir = os.path.normpath(output_dir)
    input_filepaths = [os.path.normpath(path) for path in input_filepaths]
    if mapping_file:
        mapping_file = os.path.normpath(mapping_file)
    if text_files:
        text_files = [os.path.normpath(path) for path in text_files]

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Determine which alphabet to use
    alphabet = None

    if text_files:
        # Use text files for mapping
        from Kannadafy.utils.text_obfuscation import get_text_file_words
        alphabet = get_text_file_words(text_files)
        if not alphabet:
            raise ValueError("Could not generate sufficient mapping from text files")
    elif custom_alphabet:
        # Use provided custom alphabet
        alphabet = custom_alphabet
        validate_mapping(alphabet)
    elif mapping_file:
        # Load mapping from file
        alphabet = load_custom_mapping(mapping_file)
    elif alphabet_type in CHARACTER_SETS:
        # Use predefined character set
        alphabet = CHARACTER_SETS[alphabet_type]
    else:
        raise ValueError(f"Unknown alphabet type: {alphabet_type}")

    results = {}

    for input_file in input_filepaths:
        if not os.path.exists(input_file):
            print(f"Warning: Input file {input_file} not found, skipping...")
            continue

        # Generate output filename
        filename = os.path.basename(input_file)
        base_name, ext = os.path.splitext(filename)
        output_file = os.path.join(output_dir, f"{base_name}_obfuscated{ext}")

        try:
            # Obfuscate the file
            with open(input_file, 'r', encoding='utf-8') as f:
                input_content = f.read()

            # Generate the obfuscated code
            obfuscated_content = encode_string(input_content, alphabet)

            # Write to output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(obfuscated_content)

            results[input_file] = output_file
            print(f"[✅] Successfully obfuscated {input_file} to {output_file}")
        except Exception as e:
            print(f"[❌] Error obfuscating {input_file}: {str(e)}")

    return results
