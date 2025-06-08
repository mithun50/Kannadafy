# Kannadafy | ಕನ್ನಡಫೈ

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org)
[![Version](https://img.shields.io/badge/version-2.0.9-orange)](https://pypi.org/project/Kannadafy/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/mithun50/Kannadafy/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/Kannadafy.svg)](https://badge.fury.io/py/Kannadafy)

![Kannadafy Logo](https://raw.githubusercontent.com/mithun50/Kannadafy/main/assets/logo_enhanced.png)

**Kannadafy** transforms ordinary Python code into mysterious yet fully functional scripts using Kannada characters or themed wordlists. Your code keeps working exactly as before but appears as an elegant tapestry of linguistic art.

> **IMPORTANT DISCLAIMER - VERSION 2.0.9 LIMITATIONS**


> This version only supports *ONE-WAY TRANSFORMATION* (obfuscation).  
> Deobfuscation is not yet available and will be added in an upcoming release!  
> ⚠️ Once obfuscated, there is *NO WAY* to automatically recover your original code.  
> *ALWAYS BACKUP YOUR ORIGINAL CODE BEFORE OBFUSCATION!*  
>  
> 🔓 For experimental deobfuscation support, check out:  
> [Kannadafy-deobfuscator](https://github.com/Seeking-jpg/Kannadafy-deobfuscator)
## Features

- 📜 **Script Obfuscation**: Transform code with beautiful Kannada, Telugu, Tamil, Devanagari, or Greek scripts
- 🔤 **Text-Based Obfuscation**: Use themed wordlists (food, animals, etc.) instead of scripts
- 📚 **Multi-file Processing**: Batch transform entire projects with one command
- 🌍 **Cross-Platform**: Works perfectly on Windows, macOS, and Linux
- 🧩 **API Integration**: Import and use directly in your Python applications
- 🔄 **Multiple Alphabets**: Choose from 5 different script systems
- 📝 **Custom Text Templates**: Create your own themed wordlists for unique obfuscation styles

## Installation

```bash
# Via PyPI
pip install Kannadafy

# From source
git clone https://github.com/mithun50/Kannadafy.git
cd Kannadafy
pip install .
```

## Quick Usage

```bash
# Basic usage
Kannadafy obfuscate -i your_script.py -o obfuscated_output.py

# With themed wordlist
Kannadafy text-obfuscate -i script.py -o themed.py -t patterns/food_words.txt

# Python API usage
from Kannadafy import obfuscate_api
obfuscate_api("input.py", "output.py")
```

## Example

Input:
```python
print("Hello, World!")
```

Output:
```python
exec("".join(map(chr,[int("".join(str({'ಅ': 0, 'ಆ': 1, 'ಇ': 2}[i]) for i in x.split())) for x in """
ಅ ಆ ಇ  ಅ ಆ ಇ  ಅ ಆ ಇ  ಅ ಅ ಆ  ಅ ಅ ಇ  ಅ ಇ ಅ  ಅ ಇ ಆ
""".split("  ")]))
)
```

## Documentation

- [Full Documentation](https://github.com/mithun50/Kannadafy/blob/main/docs/DOCUMENTATION.md)
- [Examples Guide](https://github.com/mithun50/Kannadafy/blob/main/docs/EXAMPLES.md)
- [GitHub Repository](https://github.com/mithun50/Kannadafy)

## Authors

**Mithun Gowda B**
- Email: mithungowda.b7411@gmail.com
- Instagram: [@MithunGowda.B](https://www.instagram.com/mithun.gowda.b)

**Manvanth**
- Email: appuka1431@gmail.com
- Instagram: [@Manvanth](https://www.instagram.com/_.appu_kannadiga)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/mithun50/Kannadafy/blob/main/LICENSE) file for details.

---

⚠️ **Remember**: Always backup your original code before obfuscation!
