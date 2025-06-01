import os
import argparse
from pprint import pformat
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError
from .core import (
    obfuscate, generate_mapping_template,
    get_available_scripts, CHARACTER_SETS,
    obfuscate_multiple
)

try:
    __version__ = version("kannadafy")
except PackageNotFoundError:
    __version__ = "2.0.9"  # Updated version
__author__ = "MithunGowda.B, Manvanth"
__copyright__ = f"Copyright (c) {datetime.now().year}, MithunGowda.B"

BANNER = """
╭──────────────────────────────────────────────────────╮
│                    ಕನ್ನಡಫೈ v{}                        │
│                    KANNADAFY                         │
├──────────────────────────────────────────────────────┤
│      Enhanced with text-based obfuscation!           │
│                                                      │
│ Author: {}                                           │
│ {}                                                   │
╰──────────────────────────────────────────────────────╯
""".format(__version__, __author__, __copyright__)

def print_banner():
    """Print the Kannadafy banner."""
    print(BANNER)

def obfuscate_api(input_filepath, output_filepath, script_type="kannada",
                 mapping_file=None, custom_alphabet=None, text_files=None):
    """API function to obfuscate a Python file."""
    return obfuscate(
        input_filepath=input_filepath,
        output_filepath=output_filepath,
        script_type=script_type,
        mapping_file=mapping_file,
        custom_alphabet=custom_alphabet,
        text_files=text_files
    )

def obfuscate_multiple_api(input_filepaths, output_dir, script_type="kannada",
                           mapping_file=None, custom_alphabet=None, text_files=None):
    """API function to obfuscate multiple Python files."""
    return obfuscate_multiple(
        input_filepaths=input_filepaths,
        output_dir=output_dir,
        alphabet_type=script_type,
        mapping_file=mapping_file,
        custom_alphabet=custom_alphabet,
        text_files=text_files
    )

def main():
    """Command-line interface for the Kannadafy tool."""
    print_banner()

    parser = argparse.ArgumentParser(
        description="""
Kannadafy - A tool to obfuscate Python scripts using various scripts or text-based mapping.
"""
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Obfuscate command
    obf_parser = subparsers.add_parser('obfuscate', help='Obfuscate a Python script')
    obf_parser.add_argument("-i", "--input", required=True, help="Input Python script path")
    obf_parser.add_argument("-o", "--output", required=True, help="Output Python script path")
    obf_parser.add_argument("-s", "--script-type", dest="script", choices=get_available_scripts(), default="kannada",
                           help="Script type to use for obfuscation (default: kannada)")
    obf_parser.add_argument("-m", "--mapping-file", dest="mapping_file",
                           help="Path to custom mapping file (.yaml, .json, .py, or .txt)")

    # Text-based obfuscation command
    text_obf_parser = subparsers.add_parser('text-obfuscate',
                                           help='Obfuscate a Python script using words from text files')
    text_obf_parser.add_argument("-i", "--input", required=True, help="Input Python script path")
    text_obf_parser.add_argument("-o", "--output", required=True, help="Output Python script path")
    text_obf_parser.add_argument("-t", "--text-files", nargs="+", required=True,
                                help="Paths to text files containing words for obfuscation")

    # Multiple file obfuscation command
    multi_obf_parser = subparsers.add_parser('multi-obfuscate',
                                            help='Obfuscate multiple Python scripts at once')
    multi_obf_parser.add_argument("-i", "--input", nargs="+", required=True,
                                 help="Input Python script paths")
    multi_obf_parser.add_argument("-o", "--output-dir", required=True,
                                 help="Output directory for obfuscated scripts")
    multi_obf_parser.add_argument("-s", "--script-type", dest="script", choices=get_available_scripts(), default="kannada",
                                 help="Script type to use for obfuscation (default: kannada)")
    multi_obf_parser.add_argument("-m", "--mapping-file", dest="mapping_file",
                                 help="Path to custom mapping file")

    # Multiple file text-based obfuscation command
    multi_text_obf_parser = subparsers.add_parser('multi-text-obfuscate',
                                                 help='Obfuscate multiple Python scripts using words from text files')
    multi_text_obf_parser.add_argument("-i", "--input", nargs="+", required=True,
                                      help="Input Python script paths")
    multi_text_obf_parser.add_argument("-o", "--output-dir", required=True,
                                      help="Output directory for obfuscated scripts")
    multi_text_obf_parser.add_argument("-t", "--text-files", nargs="+", required=True,
                                      help="Paths to text files containing words for obfuscation")

    # Template command
    template_parser = subparsers.add_parser('template',
                                          help='Generate a template mapping file')
    template_parser.add_argument("-o", "--output", required=True,
                               help="Output template file path (.yaml, .json)")
    template_parser.add_argument("-s", "--script-type", dest="script", choices=get_available_scripts(),
                               default="kannada", help="Script type to use for template (default: kannada)")

    # List available scripts command
    scripts_parser = subparsers.add_parser('scripts',
                                         help='List available script types')

    # Version command
    ver_parser = subparsers.add_parser('version', help='Show version information')

    args = parser.parse_args()

    try:
        if args.command == 'obfuscate':
            if args.mapping_file:
                obfuscate(args.input, args.output, kannada=False, mapping_file=args.mapping_file)
            else:
                obfuscate(args.input, args.output, kannada=True,
                          mapping_file=None, custom_alphabet=CHARACTER_SETS.get(args.script))
            print(f"[✅] Successfully obfuscated {args.input} to {args.output}")

        elif args.command == 'text-obfuscate':
            obfuscate(args.input, args.output, kannada=False,
                      mapping_file=None, text_files=args.text_files)
            print(f"[✅] Successfully obfuscated {args.input} to {args.output} using text files")

        elif args.command == 'multi-obfuscate':
            if not os.path.exists(args.output_dir):
                os.makedirs(args.output_dir, exist_ok=True)

            results = obfuscate_multiple(
                args.input, args.output_dir, args.script, args.mapping_file
            )
            if results:
                print(f"[✅] Successfully obfuscated {len(results)} files to {args.output_dir}")
            else:
                print("[❌] No files were successfully obfuscated")

        elif args.command == 'multi-text-obfuscate':
            if not os.path.exists(args.output_dir):
                os.makedirs(args.output_dir, exist_ok=True)

            results = obfuscate_multiple(
                args.input, args.output_dir, "kannada", None, None, args.text_files
            )
            if results:
                print(f"[✅] Successfully obfuscated {len(results)} files to {args.output_dir} using text files")
            else:
                print("[❌] No files were successfully obfuscated")

        elif args.command == 'template':
            generate_mapping_template(args.output, args.script)
            print(f"[✅] Template mapping file created at: {args.output}")

        elif args.command == 'scripts':
            print("\nAvailable scripts:")
            for script in get_available_scripts():
                count = len(CHARACTER_SETS[script])
                print(f"  - {script}: {count} characters")
            print("\nUse with: kannadafy obfuscate -s <script_name> ...")

        elif args.command == 'version':
            print(f"Kannadafy version {__version__}")
        else:
            parser.print_help()
    except Exception as e:
        print(f"[❌] Error: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    main()
