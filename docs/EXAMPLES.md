# Kannadafy Examples

This file contains practical examples showcasing different ways to use Kannadafy.

> ⚠️ **IMPORTANT DISCLAIMER**: The current version (2.0.9) only supports obfuscation. Deobfuscation functionality will be added in a future release. Once obfuscated, there is **NO WAY** to automatically recover your original code. **ALWAYS BACKUP YOUR ORIGINAL CODE BEFORE OBFUSCATION!**
>
> 
> **🔓 For experimental deobfuscation support, check out:  
> [Kannadafy-deobfuscator](https://github.com/Seeking-jpg/Kannadafy-deobfuscator)**

> 📝 **COMMAND USAGE NOTE**: Throughout this examples guide, the commands are shown in the direct format (`Kannadafy command`). On Windows or when using multiple Python environments, you may need to use the Python module format: `python -m Kannadafy command`. Both formats are functionally identical.

## Table of Contents

- [Basic Examples](#basic-examples)
- [Advanced Examples](#advanced-examples)
- [API Integration Examples](#api-integration-examples)
- [Themed Obfuscation Examples](#themed-obfuscation-examples)
- [Multi-File Processing Examples](#multi-file-processing-examples)
- [Custom Template Examples](#custom-template-examples)
- [Real-World Use Cases](#real-world-use-cases)
- [Coming Soon: Deobfuscation](#coming-soon-deobfuscation)
- [Related Documentation](#related-documentation)

---

## Basic Examples

### Simple Obfuscation

Transform a basic Python script using Kannada script:

**Original Script (hello.py):**
```python
def greet(name):
    """
    A simple greeting function that returns a personalized message.
    """
    return f"Hello, {name}! Welcome to Kannadafy testing."

def main():
    # Get the user's name
    name = input("Please enter your name: ")

    # Print greeting
    message = greet(name)
    print(message)

    # Add a conditional for fun
    if len(name) > 5:
        print("That's a nice long name!")
    else:
        print("Your name is short and sweet!")

    # Let's calculate something
    letters = len(name)
    print(f"Your name has {letters} letters.")

    print("Testing complete!")

if __name__ == "__main__":
    main()
```

**Command:**
```bash
# On Unix/Linux/macOS
Kannadafy obfuscate -i hello.py -o hello_obfuscated.py

# On Windows (or any platform as Python module)
python -m Kannadafy obfuscate -i hello.py -o hello_obfuscated.py
```

**Result (real obfuscated output):**

```python
exec("".join(map(chr,[int("".join(str({'ಅ': 0, 'ಆ': 1, 'ಇ': 2, 'ಈ': 3, 'ಉ': 4, 'ಊ': 5, 'ಋ': 6, 'ಎ': 7, 'ಏ': 8, 'ಐ': 9}[i]) for i in x.split())) for x in
"ಅ ಇ ಆ  ಅ ಇ ಆ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಅ ಉ  ಅ ಅ ಇ  ಅ ಅ ಊ  ಅ ಅ ಇ  ಅ ಅ ಇ  ಅ ಅ ಎ  ಅ ಇ ಊ  ಅ ಇ ಇ  ಅ ಇ ಇ  ಅ ಇ ಇ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಆ ಉ  ಅ ಆ ಆ  ಅ ಆ ಉ  ಅ ಆ ಊ  ಅ ಆ ಇ  ಅ ಆ ಇ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಆ ಉ  ಅ ಆ ಆ  ಅ ಆ ಉ  ಅ ಆ ಉ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಆ ಉ  ಅ ಆ ಆ  ಅ ಆ ಉ  ಅ ಇ ಊ  ಅ ಇ ಊ  ಅ ಇ ಊ"
.split("  ")]))
)
```

This obfuscated code looks completely different but runs exactly the same as the original script when executed.

---

## Advanced Examples

### Using Different Scripts

Obfuscate using different script types:

```bash
# Telugu script
Kannadafy obfuscate -i calculator.py -o calculator_telugu.py -s telugu

# Tamil script
Kannadafy obfuscate -i calculator.py -o calculator_tamil.py -s tamil

# Greek script
Kannadafy obfuscate -i calculator.py -o calculator_greek.py -s greek
```

**Sample Telugu Output:**
```python
exec("".join(map(chr,[int("".join(str({'అ': 0, 'ఆ': 1, 'ఇ': 2, 'ఈ': 3, 'ఉ': 4, 'ఊ': 5, 'ఋ': 6, 'ఎ': 7, 'ఏ': 8, 'ఐ': 9}[i]) for i in x.split())) for x in
"అ ఇ ఊ  అ అ ఈ  అ అ ఉ  అ అ ఉ  అ అ ఋ  ఇ ఈ ఊ  ఇ ఊ ఇ  ఇ ఊ ఇ  ఇ ఊ ఋ  ఈ ఉ ఆ  ఈ ఊ ఉ  ఈ ఋ ఊ"
.split("  ")]))
)
```

### Creating and Using Custom Mapping

1. Generate a template:
```bash
Kannadafy template -o custom_mapping.yaml -s kannada
```

2. Edit the template to customize your mapping
3. Use your custom mapping:
```bash
Kannadafy obfuscate -i script.py -o custom_obfuscated.py -m custom_mapping.yaml
```

**Sample Custom Mapping YAML:**
```yaml
name: "Custom Symbols Mapping"
description: "Special symbols mapping for Kannadafy"
author: "Your Name"
script_type: "custom"
characters:
  - "★"
  - "☆"
  - "◆"
  - "◇"
  - "○"
  - "●"
  - "□"
  - "■"
  - "△"
  - "▲"
  - "▽"
  - "▼"
  - "♠"
  - "♥"
  - "♦"
  - "♣"
```

---

## API Integration Examples

### Basic API Usage

```python
from Kannadafy import obfuscate_api

# Simple script
obfuscate_api("simple.py", "simple_obfuscated.py")

# Using Tamil script
obfuscate_api("script.py", "tamil_script.py", script_type="tamil")

# Using a custom mapping file
obfuscate_api("script.py", "custom_script.py", mapping_file="mapping.yaml")
```

### Integration in Larger Applications

```python
import os
from Kannadafy import obfuscate_api, obfuscate_multiple_api

def process_python_files(directory, output_dir, script_type="kannada"):
    """Process all Python files in a directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    if python_files:
        obfuscate_multiple_api(python_files, output_dir, script_type=script_type)
        return True
    return False

# Usage
process_python_files("src", "obfuscated_src")
```

---

## Themed Obfuscation Examples

### Food-Themed Obfuscation

```bash
Kannadafy text-obfuscate -i hello.py -o food_hello.py -t patterns/food_words.txt
```

Result (real example):
```python
exec("".join(map(chr,[int("".join(str({'pizza': 0, 'pasta': 1, 'burger': 2,
'taco': 3, 'sushi': 4, 'curry': 5, 'biryani': 6, 'noodles': 7, 'sandwich': 8,
'salad': 9, 'chocolate': 10, 'icecream': 11, 'cookie': 12, 'cake': 13,
'brownie': 14, 'muffin': 15, 'donut': 16, 'pancake': 17, 'waffle': 18,
'bread': 19, 'cheese': 20}[i]) for i in x.split())) for x in
"pizza burger curry  pizza burger curry  pizza burger curry  pizza burger curry
pizza pizza sushi  pizza pizza burger  pizza pizza burger  pizza pasta sushi
pizza pasta pasta  pizza pasta pasta  pizza pasta sushi  pizza pasta sushi
pizza pasta burger  pizza pasta burger  pizza pasta sushi  pizza burger curry
pizza pizza biryani  pizza pizza biryani  pizza pizza biryani  pizza pasta sushi
pizza pasta pasta  pizza pasta pasta  pizza pasta burger  pizza pasta pasta
pizza pasta sushi".split("  ")]))
)
```

### Animal-Themed Obfuscation

```bash
Kannadafy text-obfuscate -i calculator.py -o animal_calculator.py -t patterns/animal_pattern.txt
```

Real example output:
```python
exec("".join(map(chr,[int("".join(str({'cat': 0, 'dog': 1, 'elephant': 2,
'tiger': 3, 'lion': 4, 'zebra': 5, 'giraffe': 6, 'monkey': 7, 'panda': 8,
'koala': 9, 'fox': 10, 'wolf': 11, 'bear': 12, 'deer': 13,
'rabbit': 14, 'squirrel': 15, 'mouse': 16, 'eagle': 17, 'dolphin': 18,
'penguin': 19, 'turtle': 20, 'crocodile': 21, 'snake': 22, 'frog': 23}[i]) for i in x.split())) for x in
"cat elephant zebra  cat cat tiger  cat cat lion  cat cat lion  cat cat giraffe
elephant tiger zebra  elephant zebra elephant  elephant zebra elephant
elephant zebra giraffe  tiger lion dog  tiger zebra lion  tiger giraffe zebra
tiger giraffe giraffe  lion dog tiger  lion dog zebra  lion dog giraffe
lion cat lion  lion elephant dog  lion elephant cat".split("  ")]))
)
```

### Creating a Custom Theme

1. Create a movies-themed wordlist:
```bash
echo -e "Titanic\nAvatar\nInception\nMatrix\nGladiator\nJaws\nAlien\nCasablanca\nPsycho\nGodfather" > patterns/movies.txt
```

2. Use it for obfuscation:
```bash
Kannadafy text-obfuscate -i script.py -o movies_script.py -t patterns/movies.txt
```

Real movie-themed output:
```python
exec("".join(map(chr,[int("".join(str({'Titanic': 0, 'Avatar': 1, 'Inception': 2,
'Matrix': 3, 'Gladiator': 4, 'Jaws': 5, 'Alien': 6, 'Casablanca': 7,
'Psycho': 8, 'Godfather': 9}[i]) for i in x.split())) for x in
"Titanic Inception Jaws  Titanic Titanic Matrix  Titanic Titanic Alien
Titanic Titanic Alien  Titanic Titanic Gladiator  Inception Matrix Jaws
Inception Jaws Inception  Inception Jaws Inception  Inception Jaws Gladiator
Matrix Alien Avatar  Matrix Jaws Alien  Matrix Gladiator Jaws  Matrix Gladiator Gladiator"
.split("  ")]))
)
```

### Combining Multiple Themes

```bash
Kannadafy text-obfuscate -i script.py -o mixed_script.py -t patterns/food_words.txt patterns/animal_pattern.txt
```

Real mixed-themed output:
```python
exec("".join(map(chr,[int("".join(str({'pizza': 0, 'pasta': 1, 'burger': 2, 'taco': 3,
'sushi': 4, 'curry': 5, 'biryani': 6, 'noodles': 7, 'sandwich': 8, 'salad': 9,
'cat': 10, 'dog': 11, 'elephant': 12, 'tiger': 13, 'lion': 14, 'zebra': 15,
'giraffe': 16, 'monkey': 17, 'panda': 18, 'koala': 19}[i]) for i in x.split())) for x in
"pizza burger curry  pizza pizza taco  pizza pizza sushi  pizza pizza sushi
pizza pizza biryani  burger taco curry  burger curry burger  burger curry burger
burger curry biryani  taco sushi pasta  taco curry sushi  taco biryani curry
taco biryani biryani  cat dog elephant  cat dog tiger  cat dog lion
cat dog zebra  cat dog giraffe  cat dog monkey".split("  ")]))
)
```

### Emoji-Themed Obfuscation

Add some fun and creativity to your obfuscation with emojis:

```bash
Kannadafy text-obfuscate -i examples/emoji_example.py -o emoji_obfuscated.py -t patterns/emoji_pattern.txt
```

Emoji-themed output:
```python
exec("".join(map(chr,[int("".join(str({'😀': 0, '😂': 1, '🤣': 2, '😊': 3,
'😍': 4, '🤔': 5, '😎': 6, '🙄': 7, '😴': 8, '🤯': 9, '👍': 10, '👎': 11,
'👏': 12, '🙌': 13, '🤝': 14, '💪': 15, '🧠': 16, '👀': 17, '👁️': 18,
'👄': 19, '❤️': 20, '💔': 21, '💖': 22, '💯': 23, '🔥': 24, '✨': 25,
'⭐': 26, '🌟': 27, '💫': 28, '💥': 29}[i]) for i in x.split())) for x in
"😀 🤣 💯  😀 😀 😊  😀 😀 😍  😀 😀 😍  😀 😀 🤔  😂 😊 💯  😂 💯 😂
😂 💯 😂  😂 💯 🤔  😊 😍 😀  😊 💯 😍  😊 🤔 💯  😊 🤔 🤔  😍 😀 😊
😍 😀 💯  😍 😀 🤔  😍 😀 😍  😍 😂 😀  😍 😂 😂".split("  ")]))
)
```

Using emojis as obfuscation tokens can make your code not only functional but also visually engaging. This is particularly useful for educational demonstrations or when you want to add a playful touch to your obfuscated code.

---

## Multi-File Processing Examples

### Basic Multi-File Processing

```bash
# Create output directory
mkdir obfuscated_output

# Process multiple files
Kannadafy multi-obfuscate -i script1.py script2.py script3.py -o obfuscated_output
```

### Themed Multi-File Processing

```bash
# Process multiple files with animal theme
Kannadafy multi-text-obfuscate -i file1.py file2.py -o themed_output -t patterns/animal_pattern.txt
```

### Processing a Project Directory

Using the API for more complex scenarios:

```python
import os
from Kannadafy import obfuscate_multiple_api

# Collect all Python files in a directory
def get_python_files(directory):
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

# Process an entire project
project_files = get_python_files('my_project')
obfuscate_multiple_api(project_files, 'obfuscated_project', script_type='kannada')
```

---

## Custom Template Examples

You can create your own custom templates to make your obfuscated code truly unique:

### Musical Notes Template

Create a musical notes-themed pattern file:

```bash
echo -e "♩\n♪\n♫\n♬\n𝄞\n𝄡\n𝄢\n𝄫\n𝄪\n𝄆\n𝄇\n𝄈\n𝄐\n𝄑\n𝄒" > patterns/musical_notes.txt
```

Use it for obfuscation:
```bash
Kannadafy text-obfuscate -i script.py -o musical_script.py -t patterns/musical_notes.txt
```

Result:
```python
exec("".join(map(chr,[int("".join(str({'♩': 0, '♪': 1, '♫': 2, '♬': 3, '𝄞': 4, '𝄡': 5, '𝄢': 6, '𝄫': 7, '𝄪': 8, '𝄆': 9}[i]) for i in x.split())) for x in
"♩ ♫ ♬  ♩ ♩ ♪  ♩ ♩ 𝄞  ♩ ♩ 𝄞  ♩ ♩ 𝄢  ♫ ♪ ♬  ♫ ♬ ♫  ♫ ♬ ♫  ♫ ♬ 𝄢  ♪ 𝄞 ♩  ♪ ♬ 𝄞"
.split("  ")]))
)
```

### Emoji Template

Create an emoji-themed pattern file:

```bash
echo -e "😀\n😂\n🤣\n😊\n😍\n🤔\n😎\n🙄\n😴\n🤯\n👍\n👎\n👏\n🙌\n🤝" > patterns/emoji.txt
```

Use it for obfuscation:
```bash
Kannadafy text-obfuscate -i script.py -o emoji_script.py -t patterns/emoji.txt
```

Result:
```python
exec("".join(map(chr,[int("".join(str({'😀': 0, '😂': 1, '🤣': 2, '😊': 3, '😍': 4, '🤔': 5, '😎': 6, '🙄': 7, '😴': 8, '🤯': 9}[i]) for i in x.split())) for x in
"😀 🤣 😎  😀 😀 😊  😀 😀 😍  😀 😀 😍  😀 😀 🤔  🤣 😊 😎  🤣 😎 🤣  🤣 😎 🤔  😊 😍 😀  😊 💯 😍  😊 🤔 💯  😊 🤔 🤔  😍 😀 😊
😍 😀 💯  😍 😀 🤔  😍 😀 😍  😍 😂 😀  😍 😂 😂".split("  ")]))
)
```

### Technical Template

Create a technical symbols pattern file:

```bash
echo -e "∑\n∏\n∫\n∂\n∇\n√\n∛\n∜\n∞\n∝\n∠\n∡\n∢\n∴\n∵" > patterns/math_symbols.txt
```

Use it for obfuscation:
```bash
Kannadafy text-obfuscate -i script.py -o math_script.py -t patterns/math_symbols.txt
```

Result:
```python
exec("".join(map(chr,[int("".join(str({'∑': 0, '∏': 1, '∫': 2, '∂': 3, '∇': 4, '√': 5, '∛': 6, '∜': 7, '∞': 8, '∝': 9}[i]) for i in x.split())) for x in
"∑ ∫ √  ∑ ∑ ∂  ∑ ∑ ∇  ∑ ∑ ∇  ∑ ∑ ∛  ∫ ∂ √  ∫ √ ∫  ∫ √ ∫  ∫ √ ∛  ∂ ∇ ∏  ∂ √ ∇"
.split("  ")]))
)
```

---

## Real-World Use Cases

### Educational Demonstrations

Use Kannadafy to create puzzles for students learning Python:

```bash
# Create a puzzle
Kannadafy text-obfuscate -i simple_algorithm.py -o puzzle.py -t patterns/food_words.txt
```

Have students try to guess what the code does before running it.

### Code Art

Create visual code art by obfuscating simple scripts:

```bash
Kannadafy obfuscate -i art_generator.py -o kannada_art.py
```

### Cultural Programming

Combine programming with cultural appreciation:

```bash
# Create a Kannada-themed programming project
Kannadafy text-obfuscate -i cultural_game.py -o kannada_game.py -t patterns/kannada_words.txt
```

---

## Coming Soon: Deobfuscation

In the upcoming version , Kannadafy will support deobfuscation capabilities. This will allow you to:

- Recover original code from obfuscated files
- Convert between different obfuscation types
- Track changes across obfuscated versions

For now, remember that obfuscation is a one-way process in version 2.0.9, so always keep backups of your original code!

Planned deobfuscation syntax:
```bash
# Future deobfuscation command (coming in v)
Kannadafy deobfuscate -i obfuscated_script.py -o recovered_script.py
```

## Related Documentation

- [Main README](../README.md): Overview and quick start guide
- [Technical Documentation](DOCUMENTATION.md): Complete reference guide

## Authors

Created with 💖 by:

**Mithun Gowda B**
- Email: [mithungowda.b7411@gmail.com](mailto:mithungowda.b7411@gmail.com)
- Instagram: [@MithunGowda.B](https://www.instagram.com/mithun.gowda.b)

**Manvanth**
- Email: [appuka1431@gmail.com](mailto:appuka1431@gmail.com)
- Instagram: [@Manvanth](https://www.instagram.com/_.appu_kannadiga)

---

⚠️ **REMEMBER**: Once a file is obfuscated with Kannadafy v2.0.9, it CANNOT be automatically deobfuscated. Always keep backups of your original code!
