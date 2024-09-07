import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emojify",
    version="0.5",
    license="MIT",
    scripts=["kannadafy", "kannadafy.py"],
    author="MithunGowda.B",
    author_email="mithungowda.b7411@gmail.com",
    description="Obfuscate your python script by converting it to kannada language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mithun50/kannadafy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)