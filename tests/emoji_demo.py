#!/usr/bin/env python3
"""
Emoji Obfuscation Demo for Kannadafy.
This script demonstrates how to use emoji pattern obfuscation.
"""

import os
import sys
import subprocess
import shutil

def clear_output_dir(output_dir):
    """Clear the output directory."""
    if os.path.exists(output_dir):
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    else:
        # Make sure parent directories exist
        os.makedirs(output_dir, exist_ok=True)

    print(f"Output directory prepared: {output_dir}")

def create_demo_script():
    """Create a simple demo script."""
    demo_code = """#!/usr/bin/env python3
'''
Emoji Pattern Demo Script
This script demonstrates Kannadafy's emoji obfuscation.
'''

def greet(name):
    '''Greet the user with a personalized message.'''
    return f"Hello, {name}! Welcome to the emoji obfuscation demo."

def count_to_five():
    '''Count from 1 to 5 with emoji annotations.'''
    for i in range(1, 6):
        if i == 1:
            print(f"{i} - First step! 🥇")
        elif i == 2:
            print(f"{i} - Keep going! 🏃")
        elif i == 3:
            print(f"{i} - Half way there! ⏱️")
        elif i == 4:
            print(f"{i} - Almost done! ⚡")
        else:
            print(f"{i} - Complete! 🎉")

def main():
    '''Main function to demonstrate emoji obfuscation.'''
    print("===== Emoji Obfuscation Demo =====")
    name = input("What's your name? ")
    print(greet(name))
    print("\\nLet's count to five:")
    count_to_five()
    print("\\nThank you for trying the emoji obfuscation demo!")
    print("Isn't it amazing that this obfuscated code still works? 🤯")

if __name__ == "__main__":
    main()
"""

    # Ensure the tests directory exists
    os.makedirs("tests", exist_ok=True)

    demo_path = "tests/emoji_demo_script.py"
    with open(demo_path, "w", encoding="utf-8") as f:
        f.write(demo_code)

    print(f"Demo script created: {demo_path}")
    return demo_path

def run_emoji_obfuscation_demo():
    """Run the emoji obfuscation demo."""
    print("=" * 70)
    print("EMOJI OBFUSCATION DEMO".center(70))
    print("=" * 70)
    print()

    # Determine the correct Kannadafy command based on platform
    kannadafy_cmd = "python -m Kannadafy" if sys.platform == 'win32' else "Kannadafy"

    # Set up output directory
    output_dir = "tests/output/emoji_demo"
    clear_output_dir(output_dir)

    # Create demo script
    demo_script = create_demo_script()

    # Run the original script to show its output
    print("\nOriginal Script Output:")
    print("-" * 70)
    try:
        process = subprocess.run(
            f"python {demo_script}",
            shell=True,
            input=b"Demo User\n",
            capture_output=True,
            text=True
        )
        print(process.stdout)
    except Exception as e:
        print(f"Error running original script: {str(e)}")

    # Obfuscate the script using emoji pattern
    print("\nObfuscating Script with Emoji Pattern...")
    print("-" * 70)

    obfuscated_script = os.path.join(output_dir, "obfuscated_emoji.py")
    obfuscation_cmd = f'{kannadafy_cmd} text-obfuscate -i {demo_script} -o {obfuscated_script} -t patterns/emoji_pattern.txt'

    print(f"Running command: {obfuscation_cmd}")
    try:
        process = subprocess.run(
            obfuscation_cmd,
            shell=True,
            capture_output=True,
            text=True
        )
        print("Obfuscation " + ("successful!" if process.returncode == 0 else "failed."))
        if process.returncode != 0:
            print(f"Error: {process.stderr}")
    except Exception as e:
        print(f"Error during obfuscation: {str(e)}")
        return

    # Show the obfuscated code
    if os.path.exists(obfuscated_script):
        print("\nObfuscated Code (Emoji Pattern):")
        print("-" * 70)
        with open(obfuscated_script, "r", encoding="utf-8") as f:
            obfuscated_code = f.read()
            print(obfuscated_code)

        # Run the obfuscated script to show it works
        print("\nObfuscated Script Output:")
        print("-" * 70)
        try:
            process = subprocess.run(
                f"python {obfuscated_script}",
                shell=True,
                input=b"Demo User\n",
                capture_output=True,
                text=True
            )
            print(process.stdout)
            print("\nDEMO SUCCESSFUL! 🎉")
            print("The obfuscated script with emoji patterns works perfectly!")
        except Exception as e:
            print(f"Error running obfuscated script: {str(e)}")
    else:
        print(f"Error: Obfuscated script not found at {obfuscated_script}")

if __name__ == "__main__":
    run_emoji_obfuscation_demo()
