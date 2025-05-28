
import pathlib
import pathspec
from typing import Dict, List

from .config import extentions, FILTER_FILES, FILTER_DIRS


class ProjectScanner:

    """
    A class to scan a project directory and categorize its files based on their types.
    """

    def __init__(self, repository_dir: str) -> None:
        """
        Initializes the ProjectScanner with the given repository directory.

        Args:
            repository_dir (str): The path to the repository directory to be scanned.
        """

        # Resolve the repository directory to an absolute path
        self.repository_dir = pathlib.Path(repository_dir).resolve()

        # Categorize the files in the repository
        self.project_structure = self.categorize_files()

    def get_files_data(self, category: str) -> list:
        """
        Reads and returns the content of files in the specified category.

        Args:
            category (str): The category of files to read ('code' or 'docs').

        Returns:
            Dict[pathlib.Path, str]: A dictionary where keys are file paths and values are the file contents.
        """

        files_data = {}

        # Iterate over the files in the specified category
        for f in self.project_structure.get(category):
            with open(f, 'r') as file_data:
                files_data[f] = file_data.read()

        return files_data

    def read_gitignore(self) -> pathspec.PathSpec:
        """
        Reads the .gitignore file and returns a PathSpec object representing the patterns.

        Returns:
            pathspec.PathSpec: A PathSpec object containing the patterns from the .gitignore file.
        """

        # Define the path to the .gitignore file
        gitignore_path = self.repository_dir / ".gitignore"
        patterns = []

        # Check if the .gitignore file exists
        if gitignore_path.exists():
            # Open and read the .gitignore file
            with gitignore_path.open("r", encoding="utf-8") as f:
                for line in f:
                    # Strip whitespace and ignore empty lines and comments
                    line = line.strip()
                    if line and not line.startswith("#"):
                        patterns.append(line)

        # Create a PathSpec object from the collected patterns
        return pathspec.PathSpec.from_lines("gitwildmatch", patterns)

    def categorize_files(self) -> Dict[str, List[pathlib.Path]]:
        """
        Categorizes files in the repository into 'code' and 'docs' categories based on their extensions,
        while respecting the .gitignore file and a list of filtered files.

        Returns:
            Dict[str, List[pathlib.Path]]: A dictionary with two keys: 'code' and 'docs',
            each mapping to a list of file paths that belong to that category.
        """

        # Read the .gitignore patterns
        spec = self.read_gitignore()

        # Initialize the result dictionary with 'code' and 'docs' categories
        result = {
            "code": [],
            "docs": [],
        }

        # Recursively iterate over all files and directories in the repository
        for path in self.repository_dir.rglob("*"):
            # Get the relative path of the current file/directory
            rel_path = path.relative_to(self.repository_dir)

            # Skip files that match the .gitignore patterns
            if spec.match_file(rel_path):
                continue

            # Skip files that are in the FILTER_FILES list
            if path.name in FILTER_FILES:
                continue

            # Skip directories that are in the FILTER_DIRS list
            if any(rel_path.as_posix().startswith(dir) for dir in FILTER_DIRS):
                continue

            # Process only files (not directories)
            if path.is_file():
                # Get the file extension
                ext = path.suffix.lower()

                # Categorize the file based on its extension
                if ext in extentions.get("code"):
                    result["code"].append(path)
                elif ext in extentions.get("docs"):
                    result["docs"].append(path)

        return result
