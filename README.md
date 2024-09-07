## Kannadafy
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Kannadafy** is a Python obfuscation tool that transforms Python scripts into obfuscated code using Kannada letters. It makes it difficult for others to reverse-engineer your code by encoding the script in Kannada script. This tool is ideal for Python developers who want to add an extra layer of obfuscation to their code, while also embracing the Kannada language.

## Features
- Obfuscates Python code using Kannada characters.
- Retains the original functionality of the script.
- Simple command-line interface (CLI).
- Supports Python 3.6 and above.

## Installation

You can install Kannadafy using `pip`:

```bash
pip install Kannadafy
```
or clone using the official GitHub Page
```bash
git clone http://github.com/mithun50/Kannadafy
cd Kannadafy
pip install -e
```

## Usage

### Command Line Interface (CLI)

After installation, you can obfuscate your Python scripts directly from the terminal using the `kannadafy` command.

#### Basic Usage
To obfuscate a Python script, use the following command:

```bash
kannadafy -i <input_script.py> -o <output_script.py> -k
```

- `-i` or `--input`: Input Python script file.
- `-o` or `--output`: Output obfuscated Python script file.
- `-k` or `--kannada`: Encode the script using Kannada letters (this flag is default).

#### Example

```bash
kannadafy -i sample_script.py -o obfuscated_script.py -k
```

This command will read `sample_script.py`, obfuscate it using Kannada characters, and save the obfuscated version as `obfuscated_script.py`.

### Using Kannadafy in Your Python Program

You can also use Kannadafy programmatically within your own Python code:

```python
import Kannadafy

input_file = "script_to_obfuscate.py"
output_file = "obfuscated_script.py"

# Obfuscate the Python script using Kannada letters
Kannadafy.main(input_file, output_file, kannada=True)
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **MithunGowda.B** 
- [GitHub](https://github.com/mithun50)

<div align="left">

  <a href="http://instagram.com/mithun.gowda.b" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="instagram logo"  />
  </a>
  <a href="https://t.me/MITHUNGOWDA_B" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Telegram&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="telegram logo"  />
  </a>
</div>