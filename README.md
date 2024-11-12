# Kannadafy  ✨

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Welcome to *Kannadafy, where Python meets Kannada! 🚀 This quirky little tool takes your regular Python scripts and *magically obfuscates them using Kannada letters. Yes, you read that right — Kannada! What’s more fun than transforming your code into a beautiful script that only the initiated can decode? 🎭

Whether you're a developer looking for a challenge, a language enthusiast, or just in it for the fun, *Kannadafy* adds a layer of linguistic mystique to your Python code. But don’t worry — it's still Python, just a bit more... puzzling. 🤔

---

## Table of Contents 🗂

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Options](#advanced-options)
  - [Using Kannadafy in Your Code](#using-kannadafy-in-your-code)
- [How It Works](#how-it-works)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

---

## Features ✨

- *Obfuscation with Kannada*: Convert your Python code into an artistic jumble of Kannada characters while keeping it executable.
- *Command-Line Interface (CLI)*: Easy-to-use CLI for obfuscating Python scripts with a simple command.
- *Customizable Alphabet*: By default, Kannada is used, but feel free to explore using other alphabets.
- *Portable*: Just run python -m Kannadafy and you're ready to roll, no complicated setup needed.
- *Use in Your Python Code: You can also integrate **Kannadafy* directly into your Python code, making it easy to obfuscate scripts programmatically.

---

## Installation 🔧

Ready to Kannadafy your code? Here’s how to get started:

### Install via PyPI

If *Kannadafy* is available on PyPI (soon!), just run:

```bash
pip install Kannadafy
```
### Install from Source (for the daring ones)

If you want to tinker with the source or if *Kannadafy* isn’t on PyPI yet, you can install it directly from GitHub:

```bash
git clone https://github.com/mithun50/Kannadafy.git
cd Kannadafy
pip install .
```


---

## Usage 💻

### Basic Usage

Once installed, *Kannadafy* can be run from the command line to obfuscate your Python scripts. Here's how:

bash
python -m Kannadafy -i input_script.py -o obfuscated_script.py


Where:
- -i or --input: The input Python script that you want to obfuscate.
- -o or --output: The name of the output file where the obfuscated code will be saved (with .py extension).
- -v or --version: *Optional* flag to display the version of Kannadafy.

### Advanced Options 🧑‍💻

You can use the -v flag to check the version of *Kannadafy*:

bash
python -m Kannadafy -v


### Using Kannadafy in Your Code 🧑‍💻

You can also use *Kannadafy* directly in your Python code for more flexibility. For example:

python
from Kannadafy import obfuscate

# Specify input and output file paths
input_file = "input_script.py"
output_file = "obfuscated_script.py"

# Obfuscate the Python script
obfuscate(input_file, output_file)

print(f"Your script has been obfuscated and saved as {output_file}")


Here, you can programmatically obfuscate Python code by importing the obfuscate function from the Kannadafy module and calling it with the input and output file paths.

### Example: Obfuscating a Python Script

Let’s say you have a Python script like this:

python
print("Hello, World!")


Run this command to obfuscate it:

bash
python -m Kannadafy -i hello.py -o obfuscated_hello.py


This will generate a file obfuscated_hello.py that looks like this (an obfuscated Kannada version):

python
exec("".join(map(chr,[int("".join(str({'ಅ': 0,
 'ಅ:': 14,
 'ಅಂ': 13,
 'ಆ': 1,
 'ಇ': 2,
 'ಈ': 3,
 'ಉ': 4,
 'ಊ': 5,
 'ಋ': 6,
 'ಎ': 7,
 'ಏ': 8,
 'ಐ': 9,
 'ಒ': 10,
 'ಓ': 11,
 'ಔ': 12,
 'ಕ': 15,
 'ಖ': 16,
 'ಗ': 17,
 'ಘ': 18,
 'ಙ': 19,
 'ಚ': 20,
 'ಛ': 21,
 'ಜ': 22,
 'ಝ': 23,
 'ಞ': 24,
 'ಟ': 25,
 'ಠ': 26,
 'ಡ': 27,
 'ಢ': 28,
 'ಣ': 29,
 'ತ': 30,
 'ಥ': 31,
 'ದ': 32,
 'ಧ': 33,
 'ನ': 34,
 'ಪ': 35,
 'ಫ': 36,
 'ಬ': 37,
 'ಭ': 38,
 'ಮ': 39,
 'ಯ': 40,
 'ರ': 41,
 'ಲ': 42,
 'ಳ': 48,
 'ವ': 43,
 'ಶ': 44,
 'ಷ': 45,
 'ಸ': 46,
 'ಹ': 47}[i]) for i in x.split())) for x in
"ಆ ಆ ಇ  ಆ ಆ ಉ  ಆ ಅ ಊ  ಆ ಆ ಅ  ಆ ಆ ಋ  ಉ ಅ  ಈ ಉ  ಎ ಇ  ಆ ಅ ಆ  ಆ ಅ ಏ  ಆ ಅ ಏ \
 ಆ ಆ ಆ  ಉ ಉ  ಈ ಇ  ಏ ಎ  ಆ ಆ ಆ  ಆ ಆ ಉ  ಆ ಅ ಏ  ಆ ಅ ಅ  ಈ ಈ  ಈ ಉ  ಉ ಆ  ಆ ಅ"
.split("  ")])))



It will still print "Hello, World!" when executed, but good luck reading that code! 😎

---

## How It Works 🛠

### 1. *The Obfuscation Process* 🤫

The tool reads your Python script, processes each character, and maps it to a character from the Kannada alphabet (or another alphabet, if specified). This is all done behind the scenes, so all you need to do is run the command.

### 2. **Execution with exec()** 🎭

To make sure the obfuscated script is still executable, we wrap it in an exec() function. When you run the obfuscated code, the Python interpreter will execute it normally — though it might take a second to figure out how it works. 😜

### 3. *Chunking for Readability* 📏

To prevent the obfuscated code from being a single, massive line, the tool breaks it into chunks of a manageable size. This makes it slightly more readable and prevents issues with long line lengths in the Python interpreter.

---

## Disclaimer ⚠

*Important Note: **Kannadafy* does *not* provide a reverse process. Once a Python script is obfuscated using Kannada letters, *there is no built-in way to de-obfuscate or reverse the process* back to the original source code.

This tool is meant purely for fun, learning, and experimentation. If you need to keep a backup of your original code, please make sure to store it in a safe place before obfuscating it. 😄

---



## Contributing 🌱

We’d love to have you on board! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and write tests (if applicable).
4. Submit a pull request with a description of your changes.

Got an idea or found a bug? [Open an issue!](https://github.com/mithun50/Kannadafy/issues)

---

## Authors 👨‍💻💻 👨

*Mithun Gowda B* and *Manvanth* are the creators of *Kannadafy*. Both are passionate about Python, languages, and making programming fun and more accessible to people of all backgrounds. They aim to combine creativity with code to explore new possibilities in software development.

Feel free to reach out to the authors if you have any questions or just want to say "hello!" 👋

- *Mithun Gowda B*:
  Email: [mithungowda.b7411@gmail.com](mailto:mithungowda.b7411@gmail.com)
  Instagram: [@MithunGowda.B](https://www.instagram.com/mithun.gowda.b)

- *Manvanth*:
  Email: [appuka1431@gmail.com](mailto:appuka1431@gmail.com)
  Instagram: [@Manvanth](https://www.instagram.com/_.appu_kannadiga)

---

## License 📝

This project is licensed under the *MIT License*. See the [LICENSE](LICENSE) file for more details.

---

### Why Kannada?

You might be wondering, “Why Kannada?” Well, why not! 😄 Kannada is a beautiful and ancient language, and using it to obfuscate Python code just adds a unique twist. Plus, it’s a fun way to learn about language encoding and Python internals.

---

*Disclaimer: While **Kannadafy* is a fun tool for learning and experimenting, please use it responsibly. Obfuscating code for malicious purposes or for hiding malicious content is not condoned. Keep coding fun and ethical! 🧑‍💻💡
