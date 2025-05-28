
# Prompts for interacting with AI
SYSTEM_PROMPT = """
You're an expert in code analysis.
Your task is to use all your knowledge about professional programming standards to generate high-quality reports.
"""

CODE_REVIEW_PROMPT = """
Create a report about the source code of the project.
Write 10 bugs, failed solutions or other problems as short as possible.
Do not write code samples, try to fit into 400 tokens.

{code}
"""

DOCS_REVIEW_PROMPT = """
Create a project documentation report.
Write 10 bugs, failed solutions or other problems as short as possible.
Do not write examples, try to fit within 400 tokens.

{doc_text}
"""

prompts = {
    "sys": SYSTEM_PROMPT,
    "code": CODE_REVIEW_PROMPT,
    "docs": DOCS_REVIEW_PROMPT
}


# Settings of the algorithm for reading the project structure
CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".hpp",
    ".cs", ".go", ".rb", ".php", ".swift", ".kt", ".rs", ".m", ".mm"
}

DOCS_EXTENSIONS = {
    ".md", ".markdown", ".txt", ".rst", ".pdf", ".docx", ".xlsx",
    ".xls", ".pptx", ".odt", ".rtf", ".log"
}

# List of files that will not be analyzed
FILTER_FILES = [
    "LICENSE",
    "requirements.txt",
    "__init__.py"
]

extentions = {
    "code": CODE_EXTENSIONS,
    "docs": DOCS_EXTENSIONS
}
