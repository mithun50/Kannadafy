from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='kannadafy',
    version='2.0.9',
    author='MithunGowda.B, Manvanth.',
    author_email='mithungowda.b7411@gmail.com, appuka1431@gmail.com',
    description='Python code obfuscator using Kannada script and text-based mapping',
    long_description=long_description,  # Include long description from README
    long_description_content_type='text/markdown',  # Specify the format of the long description
    url='https://github.com/mithun50/Kannadafy',  # Replace with your project URL
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kannadafy = Kannadafy.cli:main',
            'Kannadafy = Kannadafy.cli:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        'pyyaml>=5.1',  # For YAML configuration files
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',  # Change as per your license
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security :: Cryptography',
    ],
    keywords='python obfuscator kannada script security text-based',  # Keywords for the package
    include_package_data=True,  # Include other files specified in MANIFEST.in
    zip_safe=False,  # Set to True if your package can be reliably used if installed as a .egg file
    project_urls={
        'Documentation': 'https://github.com/mithun50/Kannadafy/blob/main/README.md',
        'Source': 'https://github.com/mithun50/Kannadafy',
        'Tracker': 'https://github.com/mithun50/Kannadafy/issues',
    },
)
