def greet(name):
    """
    A simple greeting function that returns a personalized message.
    """
    return f"Hello, {name}! Welcome to Kannadafy emoji example."

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

    print("Emoji obfuscation is fun and creative!")

if __name__ == "__main__":
    main()
