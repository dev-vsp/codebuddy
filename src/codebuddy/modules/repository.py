
import git
import pathlib
import pathspec
import logging

from typing import Dict, List

from .config import EXTENTIONS, ALL_CATEGORIES, FILTER_FILES, FILTER_DIRS


# Setting up the logger for this module
logger = logging.getLogger(__name__)


class RepositoryTools:

    """
    A class for managing and analyzing files in a Git repository.
    """

    def __init__(self, repository_dir: pathlib.Path) -> None:
        """
        Initializes the RepositoryTools with the given repository directory.

        Args:
            repository_dir (Path): The path to the repository directory.
        """

        # Resolve the repository directory to an absolute path
        self.repository_dir = repository_dir.resolve()
        logger.debug(f"Resolved repository directory: {self.repository_dir}")

        # Categorize the files in the repository
        self.project_structure = self._categorize_files()

    def get_files(self, categories: list = ALL_CATEGORIES) -> Dict[str, List[pathlib.Path]]:
        """
        Retrieves a dictionary of file paths categorized by the specified categories.

        Args:
            categories (list): A list of categories for which to retrieve files. Defaults to ALL_CATEGORIES.

        Returns:
            Dict[str, List[pathlib.Path]]: Dictionary with file paths sorted by category.
        """

        if categories == ALL_CATEGORIES:
            # Return files of all categories
            logger.debug(f"Specifies all file categories, returns the project structure...")
            return self.project_structure
        else:
            # Retrieving files of specific categories
            logger.debug(f"Getting files for categories: {categories}")

            result = {}
            for category in categories:
                result[category] = self.project_structure.get(category)
                logger.debug(f"Files for category '{category}': {result[category]}")

            return result

    def get_file_data(self, file_path: pathlib.Path) -> str:
        """
        Reads and returns the content of the specified file.

        Args:
            file_path (Path): The path to the file whose content is to be read.

        Returns:
            str: The content of the file as a string.
        """

        # Reading data from a file
        logger.debug(f"Reading file: {file_path}")
        with open(file_path, 'r') as f:
            file_data = f.read()

        return file_data

    def _read_gitignore(self) -> pathspec.PathSpec:
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
            logger.debug(f"Found .gitignore file: {gitignore_path}")
            with gitignore_path.open("r", encoding="utf-8") as f:
                for line in f:
                    # Strip whitespace and ignore empty lines and comments
                    line = line.strip()
                    if line and not line.startswith("#"):
                        patterns.append(line)
                        logger.debug(f"Added pattern to .gitignore: {line}")

        # Create a PathSpec object from the collected patterns
        return pathspec.PathSpec.from_lines("gitwildmatch", patterns)

    def _categorize_files(self) -> Dict[str, List[pathlib.Path]]:
        """
        Categorizes files in the repository into 'code' and 'docs' categories based on their extensions,
        while respecting the .gitignore file and a list of filtered files and directories.

        Returns:
            Dict[str, List[pathlib.Path]]: A dictionary with two keys: 'code' and 'docs',
            each mapping to a list of file paths that belong to that category.
        """

        # Read the .gitignore patterns
        spec = self._read_gitignore()
        logger.debug(f"Read .gitignore patterns: {spec.patterns}")

        # Initialize the result dictionary with 'code' and 'docs' categories
        result = {}
        for category in ALL_CATEGORIES:
            result[category] = []

        # Recursively iterate over all files and directories in the repository
        for path in self.repository_dir.rglob("*"):
            # Get the relative path of the current file/directory
            rel_path = path.relative_to(self.repository_dir)
            logger.debug(f"Processing path: {rel_path}")

            # Skip files that match the .gitignore patterns
            if spec.match_file(rel_path):
                logger.debug(f"Skipped path due to .gitignore: {rel_path}")
                continue

            # Skip files that are in the FILTER_FILES list
            if path.name in FILTER_FILES:
                logger.debug(f"Skipped path due to FILTER_FILES: {rel_path}")
                continue

            # Skip directories that are in the FILTER_DIRS list
            if any(rel_path.as_posix().startswith(dir) for dir in FILTER_DIRS):
                logger.debug(f"Skipped path due to FILTER_DIRS: {rel_path}")
                continue

            # Process only files (not directories)
            if path.is_file():
                # Get the file extension
                ext = path.suffix.lower()
                logger.debug(f"File extension: {ext}")

                # Categorize the file based on its extension
                for category in ALL_CATEGORIES:
                    if ext in EXTENTIONS.get(category):
                        result[category].append(path)
                        logger.debug(f"Categorized file '{path}' as '{category}'")

        return result

    @staticmethod
    def clone_from(repo_url: str, local_dir: pathlib.Path) -> git.Repo:
        """
        Clones a Git repository from the specified URL into a local directory

        Args:
            repo_url (str): The URL of the Git repository to clone.
            local_dir (pathlib.Path): The local directory path where the repository should be cloned.

        Returns:
            git.Repo: A git.Repo object representing the cloned repository.
        """

        # Convert to a string with the full path to the local directory
        local_dir = local_dir.resolve().as_posix()

        # Cloning a repository
        logger.debug(f"Cloning repository from {repo_url} to {local_dir}")
        repo = git.Repo.clone_from(repo_url, f"{local_dir}")
        logger.debug(f"Cloned repository: {repo}")

        return repo
