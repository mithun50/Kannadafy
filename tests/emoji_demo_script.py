#!/usr/bin/env python3
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
    print("\nLet's count to five:")
    count_to_five()
    print("\nThank you for trying the emoji obfuscation demo!")
    print("Isn't it amazing that this obfuscated code still works? 🤯")

if __name__ == "__main__":
    main()
