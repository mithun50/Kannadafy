#Kannadafy/cli.py
import argparse
import os
import sys
from datetime import datetime
from typing import List, Optional
from importlib.metadata import version, PackageNotFoundError
from Kannadafy.core import (
    obfuscate, get_available_scripts,
    generate_mapping_template, obfuscate_multiple
)

# Use a direct version string instead of importing
__version__ = "2.0.9"

def print_banner():
    """Display a beautiful Kannada banner."""


    try:
        __version__ = version("kannadafy")
    except PackageNotFoundError:
        __version__ = "2.0.9"  # Updated version
    __author__ = "MithunGowda.B, Manvanth"
    __copyright__ = f"Copyright (c) {datetime.now().year}, MithunGowda.B"

    banner = """
╭──────────────────────────────────────────────────────╮
│                    ಕನ್ನಡಫೈ v{}                     │
│                    KANNADAFY                         │
├──────────────────────────────────────────────────────┤
│      Enhanced with text-based obfuscation!           │
│                                                      │
│ Author: {}                      │
│ {}                    │
╰──────────────────────────────────────────────────────╯
""".format(__version__, __author__, __copyright__)




    print(banner)
    print("  Version: 2.0.9")
    print("  Authors: MithunGowda.B, Manvanth.")
    print("  Enhanced with text-based obfuscation")
    print("-" * 50)

def obfuscate_cmd(args):
    """Handle the obfuscation command."""
    try:
        # Normalize paths based on whether we're handling single or multiple files
        if hasattr(args, 'multiple') and args.multiple:
            # For multiple files, normalize each path in the list
            normalized_inputs = [os.path.normpath(path) for path in args.input]
            args.output_dir = os.path.normpath(args.output_dir)
        else:
            # For single file, normalize the input and output paths
            args.input = os.path.normpath(args.input)
            if hasattr(args, 'output'):
                args.output = os.path.normpath(args.output)

        # Initialize all optional parameters to avoid attribute errors
        mapping_file = None
        text_files = None
        script_type = "kannada"  # Default to kannada

        # Check for mapping file
        if hasattr(args, 'mapping_file'):
            mapping_file = args.mapping_file
            if mapping_file:
                mapping_file = os.path.normpath(mapping_file)
                if not os.path.exists(mapping_file):
                    print(f"Error: Mapping file '{mapping_file}' not found.")
                    return 1

        # Check for text files
        if hasattr(args, 'text_files'):
            if args.text_files:
                text_files = [os.path.normpath(path) for path in args.text_files]
            else:
                text_files = None

        # Check for script type - might be None for text-based obfuscation
        if hasattr(args, 'script_type'):
            script_type = args.script_type if args.script_type is not None else "kannada"

        # Process multiple files if provided
        if hasattr(args, 'multiple') and args.multiple:
            if not os.path.exists(args.output_dir):
                os.makedirs(args.output_dir, exist_ok=True)

            input_files = []
            for path in normalized_inputs:  # Use normalized inputs
                if os.path.exists(path):
                    input_files.append(path)
                else:
                    print(f"Warning: Input file '{path}' not found, skipping...")

            if not input_files:
                print("Error: No valid input files provided.")
                return 1

            results = obfuscate_multiple(
                input_files,
                args.output_dir,
                script_type,
                mapping_file,
                None,
                text_files
            )

            if results:
                print(f"\n[✅] Successfully obfuscated {len(results)} files to {args.output_dir}")
                return 0
            else:
                print("\n[❌] No files were successfully obfuscated.")
                return 1
        else:
            # Single file obfuscation
            if not os.path.exists(args.input):
                print(f"Error: Input file '{args.input}' not found.")
                return 1

            # Get the script type if available
            script_type = args.script_type if hasattr(args, "script_type") and args.script_type else "kannada"

            obfuscate(
                args.input,
                args.output,
                script_type=script_type,
                mapping_file=mapping_file,
                custom_alphabet=None,
                text_files=text_files
            )
            print(f"[✅] Successfully obfuscated {args.input} to {args.output}")
            return 0

    except Exception as e:
        print(f"[❌] Error: {str(e)}")
        return 1

def template_cmd(args):
    """Handle the template command."""
    try:
        # Use script_type if available
        script_type = args.script_type if hasattr(args, 'script_type') else "kannada"
        generate_mapping_template(args.output, script_type)
        print(f"[✅] Template mapping file created at: {args.output}")
        return 0
    except Exception as e:
        print(f"[❌] Error: {str(e)}")
        return 1

def version_cmd(_):
    """Handle the version command."""
    print(f"Kannadafy version {__version__}")
    return 0

def available_scripts_cmd(_):
    """Handle the available scripts command."""
    print("\nAvailable scripts:")
    for script in get_available_scripts():
        print(f"  - {script}")
    print("\nUse with: kannadafy obfuscate -s <script_name> ...")
    return 0

def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Kannadafy - A tool to obfuscate Python scripts using various scripts or text-based mapping."
    )

    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    # OBFUSCATION COMMANDS

    # Regular obfuscation
    obf_parser = subparsers.add_parser('obfuscate', help='Obfuscate a Python script')
    obf_parser.add_argument("-i", "--input", required=True, help="Input Python script path")
    obf_parser.add_argument("-o", "--output", required=True, help="Output Python script path")
    obf_parser.add_argument("-s", "--script-type", choices=get_available_scripts(), default="kannada",
                          help="Script type to use for obfuscation (default: kannada)")
    obf_parser.add_argument("-m", "--mapping-file", help="Path to custom mapping file")
    obf_parser.set_defaults(func=obfuscate_cmd)

    # Text-based obfuscation
    text_obf_parser = subparsers.add_parser('text-obfuscate',
                                         help='Obfuscate a Python script using words from text files')
    text_obf_parser.add_argument("-i", "--input", required=True, help="Input Python script path")
    text_obf_parser.add_argument("-o", "--output", required=True, help="Output Python script path")
    text_obf_parser.add_argument("-t", "--text-files", nargs="+", required=True,
                               help="Paths to text files containing words for obfuscation")
    text_obf_parser.set_defaults(func=obfuscate_cmd, script_type=None)

    # Multiple file obfuscation
    multi_obf_parser = subparsers.add_parser('multi-obfuscate',
                                          help='Obfuscate multiple Python scripts at once')
    multi_obf_parser.add_argument("-i", "--input", nargs="+", required=True,
                                help="Input Python script paths")
    multi_obf_parser.add_argument("-o", "--output-dir", required=True,
                                help="Output directory for obfuscated scripts")
    multi_obf_parser.add_argument("-s", "--script-type", choices=get_available_scripts(), default="kannada",
                                help="Script type to use for obfuscation (default: kannada)")
    multi_obf_parser.add_argument("-m", "--mapping-file", help="Path to custom mapping file")
    multi_obf_parser.set_defaults(func=obfuscate_cmd, multiple=True)

    # Multiple file text-based obfuscation
    multi_text_obf_parser = subparsers.add_parser('multi-text-obfuscate',
                                               help='Obfuscate multiple Python scripts using words from text files')
    multi_text_obf_parser.add_argument("-i", "--input", nargs="+", required=True,
                                     help="Input Python script paths")
    multi_text_obf_parser.add_argument("-o", "--output-dir", required=True,
                                     help="Output directory for obfuscated scripts")
    multi_text_obf_parser.add_argument("-t", "--text-files", nargs="+", required=True,
                                     help="Paths to text files containing words for obfuscation")
    multi_text_obf_parser.set_defaults(func=obfuscate_cmd, multiple=True, script_type=None)

    # UTILITY COMMANDS

    # Template generation
    template_parser = subparsers.add_parser('template',
                                         help='Generate a template mapping file')
    template_parser.add_argument("-o", "--output", required=True,
                               help="Output template file path (.yaml, .json)")
    template_parser.add_argument("-s", "--script-type", choices=get_available_scripts(), default="kannada",
                               help="Script type to use for template (default: kannada)")
    template_parser.set_defaults(func=template_cmd)

    # Version command
    version_parser = subparsers.add_parser('version', help='Show version information')
    version_parser.set_defaults(func=version_cmd)

    # Available scripts command
    scripts_parser = subparsers.add_parser('scripts', help='List available script types')
    scripts_parser.set_defaults(func=available_scripts_cmd)

    return parser.parse_args(args)

def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI."""
    try:
        print_banner()
        parsed_args = parse_args(args)
        return parsed_args.func(parsed_args)
    except Exception as e:
        print(f"[❌] Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
