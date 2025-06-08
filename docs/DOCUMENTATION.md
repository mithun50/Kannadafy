# Kannadafy Documentation

**Version: 2.0.9**

This comprehensive documentation covers all aspects of Kannadafy, from installation to advanced usage.

> ⚠️ **IMPORTANT DISCLAIMER**:

> This version only supports *ONE-WAY TRANSFORMATION* (obfuscation).  
> Deobfuscation is not yet available and will be added in an upcoming release!  
> ⚠️ Once obfuscated, there is *NO WAY* to automatically recover your original code.  
> *ALWAYS BACKUP YOUR ORIGINAL CODE BEFORE OBFUSCATION!*  
>  
> 🔓 For experimental deobfuscation support, check out:  
> [Kannadafy-deobfuscator](https://github.com/Seeking-jpg/Kannadafy-deobfuscator)
> 

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Command-Line Interface](#command-line-interface)
   - [Basic Commands](#basic-commands)
   - [Obfuscation Commands](#obfuscation-commands)
   - [Multiple File Processing](#multiple-file-processing)
   - [Utility Commands](#utility-commands)
4. [API Reference](#api-reference)
5. [Script Types](#script-types)
6. [Pattern Files](#pattern-files)
7. [Custom Pattern Creation](#custom-pattern-creation)
8. [Technical Details](#technical-details)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [Links and Resources](#links-and-resources)

---

## Introduction

Kannadafy is a Python tool that transforms Python code into obfuscated yet fully functional scripts using Kannada characters or themed wordlists. The tool preserves the exact functionality of the original code while giving it a completely different appearance.

The obfuscation process is one-way only, meaning there is no automatic way to recover the original code. This is intentional, as the primary purpose of Kannadafy is for educational and entertainment purposes, not for secure code protection.

For a quick overview and examples, see the [README](../README.md).

---

## Installation

### Via PyPI (Recommended)

```bash
pip install Kannadafy
```

### From Source

```bash
git clone https://github.com/mithun50/Kannadafy.git
cd Kannadafy
pip install .
```

### Requirements

- Python 3.6 or higher
- PyYAML (for YAML mapping file support)

---

## Command-Line Interface

Kannadafy provides a comprehensive command-line interface with several subcommands.

### Running Kannadafy

You can run Kannadafy in two ways:

```bash
# Direct command (Unix/Linux/macOS)
Kannadafy [command] [options]

# As a Python module (all platforms, especially Windows)
python -m Kannadafy [command] [options]
```

Using the Python module format (`python -m Kannadafy`) is recommended on Windows systems or when you have multiple Python versions installed, as it ensures that the correct Python environment is used.

### Basic Commands

#### Display Version

```bash
Kannadafy version
```

#### Show Available Scripts

```bash
Kannadafy scripts
```

### Obfuscation Commands

#### Basic Script Obfuscation

```bash
Kannadafy obfuscate -i input_script.py -o output_script.py
```

Options:
- `-i, --input`: Path to the input Python script (required)
- `-o, --output`: Path for the obfuscated output (required)
- `-s, --script-type`: Script type to use (default: "kannada")
- `-m, --mapping-file`: Path to custom mapping file

#### Text-Based Obfuscation

```bash
Kannadafy text-obfuscate -i input_script.py -o output_script.py -t wordlist1.txt wordlist2.txt
```

Options:
- `-i, --input`: Path to the input Python script (required)
- `-o, --output`: Path for the obfuscated output (required)
- `-t, --text-files`: Paths to text files with words for obfuscation (required)

### Multiple File Processing

#### Batch Script Obfuscation

```bash
Kannadafy multi-obfuscate -i script1.py script2.py -o output_dir -s kannada
```

Options:
- `-i, --input`: Paths to input Python scripts (required)
- `-o, --output-dir`: Output directory for obfuscated scripts (required)
- `-s, --script-type`: Script type to use (default: "kannada")
- `-m, --mapping-file`: Path to custom mapping file

#### Batch Text-Based Obfuscation

```bash
Kannadafy multi-text-obfuscate -i script1.py script2.py -o output_dir -t wordlist1.txt wordlist2.txt
```

Options:
- `-i, --input`: Paths to input Python scripts (required)
- `-o, --output-dir`: Output directory for obfuscated scripts (required)
- `-t, --text-files`: Paths to text files with words for obfuscation (required)

### Utility Commands

#### Generate Mapping Template

```bash
Kannadafy template -o mapping_template.yaml -s kannada
```

Options:
- `-o, --output`: Path for the template file (required)
- `-s, --script-type`: Script type to use for template (default: "kannada")

---

## API Reference

Kannadafy can be integrated directly into your Python applications.

### Basic Usage

```python
from Kannadafy import obfuscate_api

# Basic obfuscation with default Kannada script
obfuscate_api(
    input_filepath="input.py",
    output_filepath="output.py"
)

# Obfuscation with a different script
obfuscate_api(
    input_filepath="input.py",
    output_filepath="output.py",
    script_type="telugu"
)

# Text-based obfuscation
obfuscate_api(
    input_filepath="input.py",
    output_filepath="output.py",
    text_files=["wordlist1.txt", "wordlist2.txt"]
)

# Custom mapping file
obfuscate_api(
    input_filepath="input.py",
    output_filepath="output.py",
    mapping_file="custom_mapping.yaml"
)
```

### Batch Processing API

```python
from Kannadafy import obfuscate_multiple_api

# Batch process multiple files
obfuscate_multiple_api(
    input_filepaths=["script1.py", "script2.py", "script3.py"],
    output_dir="output_directory",
    script_type="kannada"
)

# Batch process with text files
obfuscate_multiple_api(
    input_filepaths=["script1.py", "script2.py"],
    output_dir="output_directory",
    text_files=["wordlist1.txt", "wordlist2.txt"]
)
```

---

## Script Types

Kannadafy supports multiple script types:

1. **kannada** (default): Kannada script (ಕನ್ನಡ)
2. **devanagari**: Devanagari script (देवनागरी)
3. **telugu**: Telugu script (తెలుగు)
4. **tamil**: Tamil script (தமிழ்)
5. **greek**: Greek script (Ελληνικά)

To use a specific script type:

```bash
Kannadafy obfuscate -i input.py -o output.py -s telugu
```

---

## Pattern Files

Kannadafy comes with several pre-made pattern files in the `patterns` directory:

### Basic Pattern Files
- `alphabet_pattern.txt`: Simple a-z characters
- `numbers_pattern.txt`: Numeric characters (0-20)
- `symbols_pattern.txt`: Common symbols and special characters

### Themed Pattern Files
- `kannada_words.txt`: Kannada words
- `english_words.txt`: English programming terms
- `food_words.txt`: Food-related words
- `animal_pattern.txt`: Animal names
- `emoji_pattern.txt`: Various emojis

### Complex Pattern Files
- `combined_pattern.txt`: Alphanumeric patterns (a1, b2, c3...)
- `complex_pattern.txt`: Complex strings (Alpha123, Beta456...)

To use a pattern file:

```bash
Kannadafy text-obfuscate -i input.py -o output.py -t patterns/food_words.txt
```

### Using Emoji Patterns

Emojis provide a visually distinctive way to obfuscate your code. The `emoji_pattern.txt` file contains a collection of common emojis that can be used for obfuscation.

Benefits of emoji-based obfuscation:

1. **Visual Appeal**: Creates colorful and visually engaging obfuscated code
2. **Educational Value**: Makes learning about code obfuscation more fun, especially for beginners
3. **Uniqueness**: Adds a modern touch to your obfuscated code

To use emoji patterns:

```bash
Kannadafy text-obfuscate -i your_script.py -o emoji_output.py -t patterns/emoji_pattern.txt
```

You can also create your own custom emoji pattern by creating a text file with your preferred emojis:

```bash
# Create a custom emoji pattern with space-themed emojis
echo -e "🚀\n🌍\n🌙\n🌠\n⭐\n🛰️\n🔭\n👨‍🚀\n👩‍🚀\n🌌" > patterns/space_emojis.txt

# Use it for obfuscation
Kannadafy text-obfuscate -i script.py -o space_themed.py -t patterns/space_emojis.txt
```

---

## Custom Pattern Creation

You can create your own pattern files for unique obfuscation themes.

### Requirements

- Each file must contain at least 10 unique entries
- Entries can be words, characters, or symbols
- No duplicate entries allowed

### Format Options

- **One item per line** (most common):
  ```
  apple
  banana
  cherry
  ```

- **Comma-separated values**:
  ```
  apple, banana, cherry, date, fig
  ```

- **Mixed format**:
  ```
  apple, banana, cherry
  date
  fig, grape
  ```

### Creating a Pattern File

```bash
# Create a simple pattern file with movie names
echo -e "Titanic\nAvatar\nInception\nMatrix\nGladiator\nJaws\nAlien\nCasablanca\nPsycho\nGodfather" > patterns/movies.txt

# Use it for obfuscation
Kannadafy text-obfuscate -i script.py -o obfuscated.py -t patterns/movies.txt
```

### Programmatic Pattern Creation

```python
# Generate a color-themed pattern file
colors = [
    "red", "blue", "green", "yellow", "purple",
    "orange", "pink", "brown", "black", "white",
    "gray", "cyan", "magenta", "teal", "indigo"
]

with open("patterns/colors.txt", "w") as f:
    f.write("\n".join(colors))
```

### Using Multiple Pattern Files

```bash
# Combine different themed wordlists
Kannadafy text-obfuscate -i script.py -o mixed.py -t patterns/food_words.txt patterns/animal_pattern.txt
```

---

## Technical Details

### How Obfuscation Works

1. **Character Mapping**: Each ASCII character is mapped to a sequence of Kannada characters or words
2. **Encoding Process**:
   - Each character in the original code is converted to its ASCII value
   - ASCII values are then mapped to corresponding elements from the chosen alphabet
   - The mapping is stored in a dictionary within the obfuscated code
3. **Execution Process**:
   - When the obfuscated code runs, it uses Python's `exec()` function
   - The mapping dictionary is used to reconstruct the original ASCII values
   - These values are converted back to characters and executed as Python code

### Mapping File Formats

Kannadafy supports multiple mapping file formats:

1. **YAML** (.yaml, .yml):
   ```yaml
   name: "Custom Mapping"
   description: "My character mapping"
   author: "Your Name"
   script_type: "custom"
   characters:
     - "α"
     - "β"
     - "γ"
     # ... more characters
   ```

2. **JSON** (.json):
   ```json
   {
     "name": "Custom Mapping",
     "description": "My character mapping",
     "author": "Your Name",
     "script_type": "custom",
     "characters": ["α", "β", "γ", "..."]
   }
   ```

3. **Python** (.py):
   ```python
   MY_MAPPING = [
       "α", "β", "γ", # ... more characters
   ]
   ```

4. **Text** (.txt):
   ```
   α
   β
   γ
   ...
   ```

---

## Troubleshooting

### Common Issues

1. **"Mapping must contain at least 10 unique characters"**
   - Ensure your pattern file or custom mapping has at least 10 unique entries
   - Check for duplicate entries in your pattern file

2. **"Could not generate sufficient mapping from text files"**
   - Make sure your text files contain enough unique words
   - Verify the file format is correct (one word per line or comma-separated)

3. **"Input file not found"**
   - Check that the specified input file path is correct
   - Verify the file exists and is readable

4. **"Unknown script type"**
   - Use one of the supported script types: kannada, devanagari, telugu, tamil, greek
   - Verify the script type parameter is spelled correctly

### Best Practices

1. **Always backup your code** before obfuscation
2. **Start with small test files** to understand the process
3. **Use absolute paths** if you encounter path-related issues
4. **Check permissions** on output directories and files

---

## Contributing

Contributions to Kannadafy are welcome! Here's how to contribute:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Make your changes**
4. **Run tests** to ensure compatibility
5. **Submit a pull request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/Kannadafy.git
cd Kannadafy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Code Style

- Follow PEP 8 guidelines
- Document all functions with docstrings
- Include type hints where appropriate

---

## Links and Resources

- [GitHub Repository](https://github.com/mithun50/Kannadafy)
- [Issue Tracker](https://github.com/mithun50/Kannadafy/issues)
- [README](../README.md)
- [Examples Documentation](EXAMPLES.md)

## Authors

Created with 💖 by:

**Mithun Gowda B**
- Email: [mithungowda.b7411@gmail.com](mailto:mithungowda.b7411@gmail.com)
- Instagram: [@MithunGowda.B](https://www.instagram.com/mithun.gowda.b)

**Manvanth**
- Email: [appuka1431@gmail.com](mailto:appuka1431@gmail.com)
- Instagram: [@Manvanth](https://www.instagram.com/_.appu_kannadiga)

---

**Remember**: Kannadafy is designed for fun, education, and artistic expression. It is not intended for secure code protection. Always keep backups of your original code!
