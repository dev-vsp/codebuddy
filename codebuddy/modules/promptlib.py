
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
