import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Kannadafy",
    version="0.1",
    license="MIT",
    py_modules=["Kannadafy"],  # For a single Python file
    author="MithunGowda.B",
    author_email="mithungowda.b7411@gmail.com",
    description="Obfuscate your Python script by converting it to Kannada language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mithun50/Kannadafy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={  # Optional: allows for command-line execution
        'console_scripts': [
            'kannadafy=Kannadafy:main',  # 'kannadafy' will be the terminal command
        ],
    },
)