
from setuptools import setup, find_packages


try:
    with open("README.md", "r", encoding="utf-8") as readme_file:
        long_description = readme_file.read()
except:
    long_description = ''

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
        "click==8.2.1",
        "requests==2.32.3",
        "urllib3==2.4.0",
        "pathspec==0.12.1",
        "GitPython==3.1.44",
        "markdown==3.8",
        "beautifulsoup4==4.13.4",
    ],

    entry_points={
        'console_scripts': [
            "codebuddy=codebuddy.console:cli"
        ]
    },

    license='MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],

    keywords='git analysis language-model code-review',
)
