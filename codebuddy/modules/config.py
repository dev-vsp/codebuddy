
import logging

# Define API configuration for interacting with the AI service
API = {
    "url": "http://localhost:1234",     # Base URL of the AI service
    "endpoint": "v1/chat/completions",  # Specific endpoint for generating completions
    "max_tokens": 500,                  # Maximum number of tokens to generate in the response
    "temperature": 0.5                  # Creativity level of the generated text
}

# Define logger configuration
LOGGER = {
    "level": logging.INFO,              # Set the logging level to DEBUG
    "log_file": None,                   # File where logs will be written
    "format": '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}

# Name of the directory for storing generated reports
REPORT_DIR_NAME = "reports"

# System prompt to set the context for the AI
SYSTEM_PROMPT = """
You're an expert in code analysis.
Your task is to use all your knowledge about professional programming standards to generate high-quality reports.
"""

# Prompt template for generating a code review report
CODE_REVIEW_PROMPT = """
Create a report about the source code of the project.
Write 10 bugs, failed solutions or other problems as short as possible.
Do not write code samples, try to fit into 400 tokens.

{data}
"""

# Prompt template for generating a documentation review report
DOCS_REVIEW_PROMPT = """
Create a project documentation report.
Write 10 bugs, failed solutions or other problems as short as possible.
Do not write examples, try to fit within 400 tokens.

{data}
"""

# Dictionary of prompts used for different types of reviews
PROMPTS = {
    "sys": SYSTEM_PROMPT,       # System prompt
    "code": CODE_REVIEW_PROMPT, # Code review prompt
    "docs": DOCS_REVIEW_PROMPT  # Documentation review prompt
}

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
    "code": CODE_EXTENSIONS,    # Extensions for code files
    "docs": DOCS_EXTENSIONS     # Extensions for documentation files
}

# List of all categories of files
ALL_CATEGORIES = EXTENTIONS.keys()

# List of files that should be excluded from analysis
FILTER_FILES = [
    "LICENSE",
    "requirements.txt",
    "__init__.py"
]

# List of directories that should be excluded from analysis
FILTER_DIRS = [
    REPORT_DIR_NAME
]
