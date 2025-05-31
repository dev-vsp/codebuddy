# CodeBuddy

CodeBuddy is a tool that automates source code analysis of projects submitted as Git repositories. It helps developers to get analytical information about projects using language models. CodeBuddy can categorize files by extension, filter unnecessary files and generate detailed reports.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [System requirements](#system-requirements)
- [License](#license)

## Installation

1. Cloning the repository:
```bash
git clone https://github.com/dev-vsp/codebuddy.git
cd codebuddy
```

2. Creating a virtual environment (if needed):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Installing dependencies:
```bash
pip install -r requirements.txt
```

4. Configuration setting (optional):
```bash
# Open the configuration file using the nano editor
nano src/codebuddy/modules/config.py
```

5. Local installation of the package (optional):
```bash
pip install .
```

## Usage

**Before running, take care of [configuring](#configuration) the script to connect to the language model APIs.</br>By default the script is configured to work with [LM Studio](https://lmstudio.ai/) server.**

For information regarding the command line interface, run:
```bash
$ python3 codebuddy.py --help
Usage: codebuddy.py [OPTIONS] REPOSITORY_DIR

  CodeBuddy is a script for analyzing git repositories using a language model.

Options:
  --api URL            URL of the language model API.
  --clone URL          Cloning a remote repository before analyzing it.
  --reports DIRECTORY  Directory path to storing reports.
  --print              Display all reports in the terminal.
  --help               Show this message and exit.
```

Clone the repository and run its analysis:

```bash
python3 codebuddy.py --clone https://github.com/dev-vsp/codebuddy.git project
```

A list of actions that this command performs:

1. Cloning the "codebuddy" repository and place it in the "project" directory
2. Connecting to the language model using the default configuration
3. Analyzing a cloned repository
4. Once the analysis is complete, the report will be saved in the repository directory

Re-analyze the cloned repository with API changes:
```bash
python3 codebuddy.py --api http://192.168.10.10:1234 project
```

Analyze the cloned repository again, saving the new reports to the "project_reports" directory:
```bash
python3 codebuddy.py --reports project_reports project
```

Example of using SSH protocol for cloning:
```bash
python3 codebuddy.py --clone git@github.com:dev-vsp/codebuddy.git project
```

Run in [Docker](https://docker.com/):
```bash
docker build -t codebuddy .
docker run codebuddy --help
```

## Configuration

CodeBuddy is configured by default to work with [LM Studio](https://lmstudio.ai/) software. However, you can customize it to suit your needs. The default configuration may not have something you need to solve your problem, so you are given the opportunity to modify it at the source code level.

The main changeable configuration parameters:

- API
- Prompts
- Filters
- File categories
- Logging
- Report storage directory

**Config file path: ```src/codebuddy/modules/config.py```**

The configuration of the script determines the quality of reports and the speed of their creation, as you have the opportunity to choose the necessary language model and fine-tune CodeBuddy to your tasks:

```python
API = {
    # Base URL of the AI service
    "url": "http://localhost:1234",
    
    # Specific endpoint for generating completions
    "endpoint": "v1/chat/completions",

    # Useful when setting up authorization
    "headers": {
        "Content-Type": "application/json", 
    },

    # Maximum number of tokens to generate in the response
    "max_tokens": 500,

    # Creativity level of the generated text                  
    "temperature": 0.5,
}
```

Example of authorization configuration:
```python
API_KEY = "your_api_key"

API = {
    # ...
    "headers" = {
        "Content-Type": "application/json",
        "Authorization": {API_KEY},
    },
    # ...
}
```

It is recommended to modify the standard prompts prescribed in the configuration, as the standard version may not take into account the peculiarities of your project:

```python
# Standard prompt for source code analysis.
# Instead of {data}, the script puts the
# contents of analyzed files into it.
CODE_REVIEW_PROMPT = """
Create a report about the source code of the project.
Write 10 bugs, failed solutions or other problems as short as possible.
Do not write code samples, try to fit into 400 tokens.

{data}
"""
```

Standard configuration of file categories and extensions:

```python
# Define file extensions for different categories of files
CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".hpp",
    ".cs", ".go", ".rb", ".php", ".swift", ".kt", ".rs", ".m", ".mm"
}

DOCS_EXTENSIONS = {
    ".md", ".markdown", ".txt", ".rst", ".pdf", ".docx", ".xlsx",
    ".xls", ".pptx", ".odt", ".rtf", ".log"
}

# Dictionary mapping categories to their respective file extensions
# Note: you have the option to add your own categories
EXTENTIONS = {
    "code": CODE_EXTENSIONS,  # Extensions for code files
    "docs": DOCS_EXTENSIONS,  # Extensions for documentation files
}

# List of all categories of files
ALL_CATEGORIES = EXTENTIONS.keys()
```

Filtering files and directories by name:

```python
# List of files that should be excluded from analysis
FILTER_FILES = [
    "LICENSE",
    "requirements.txt",
    "__init__.py",
]

# List of directories that should be excluded from analysis
FILTER_DIRS = [
    # File reports, there is no need to analyze the reports...
    REPORT_DIR_NAME,
]
```

## Testing

Running the test:

```bash
pytest
```

Full-fledged test launch (with API connection):

```bash
pytest --full
```

## Contributing

Community contributions are welcome! If you would like to contribute to CodeBuddy, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make the changes and commit them
4. Move the changes to your branch
5. Submit a pull request to the main repository

## System requirements

- Python 3.12 or higher
- Git installed and configured
- Internet access to work with language models (if needed)

## License

CodeBuddy is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
