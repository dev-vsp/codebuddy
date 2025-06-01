
from setuptools import setup, find_packages


# Attempt to read the README.md file for the long description of the package
try:
    with open("README.md", "r", encoding="utf-8") as readme_file:
        long_description = readme_file.read()
except Exception as e:
    # If there is an error reading the README.md file,
    # print the error and set long_description to an empty string
    print(f"\nError reading file 'README.md': {e}")
    long_description = ''

# Attempt to read the LICENSE file to include it in the package metadata
try:
    with open("LICENSE", "r", encoding="utf-8") as license_file:
        license_file_text = license_file.read()
except Exception as e:
    # If there is an error reading the LICENSE file,
    # print the error and set license_file_text to 'MIT'
    print(f"\nError reading file 'LICENSE': {e}")
    license_file_text = 'MIT'

# Setup function to define package metadata and configurations
setup(
    name="codebuddy",
    version="0.1.0",
    author="Vadim Sergeev",
    author_email="dev-vsp@outlook.com",
    description="Script for analyzing git repositories using a language model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-vsp/CodeBuddy",
    packages=find_packages(),
    python_requires='>=3.12',
    install_requires=[
        "click>=8.2.1,<9.0.0",
        "requests>=2.32.3,<3.0.0",
        "urllib3>=2.4.0,<3.0.0",
        "pathspec>=0.12.1,<0.13.0",
        "GitPython>=3.1.44,<4.0.0",
        "markdown>=3.8,<4.0",
        "beautifulsoup4>=4.13.4,<5.0",
    ],

    entry_points={
        'console_scripts': [
            "codebuddy=src:cli"
        ]
    },

    license=license_file_text,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],

    keywords='git analysis language-model code-review',
)
