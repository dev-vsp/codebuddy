
from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


setup(
    name="codebuddy",
    version="0.1",
    author="Vadim Sergeev",
    author_email="dev-vsp@outlook.com",
    description="Script for git repository analysis and reporting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-vsp/CodeBuddy",
    packages=find_packages(),
    python_requires='>=3.12.3',
    install_requires=[
        "click==8.1.3"
    ],
    entry_points={
        'console_scripts': [
            "codebuddy=codebuddy.main:review"
        ]
    }
)
