
import pytest
import pathlib

from codebuddy.modules import repository
from codebuddy.modules.config import ALL_CATEGORIES


def test_repository():
    # Create an instance of RepositoryTools with the path to the fake repository
    repo_tools = repository.RepositoryTools(
        pathlib.Path('tests/fake_repo')
    )

    # Retrieve the list of files categorized into 'code' and 'docs'
    files = repo_tools.get_files()

    # Assert that the retrieved files match the expected structure and paths
    assert files.keys() == ALL_CATEGORIES
    assert len(files.get("code")) == 1
    assert len(files.get("docs")) == 1
    assert files.get("code")[0].name == "main.py"
    assert files.get("docs")[0].name == "README.md"

    # Retrieve the content of the first file in the 'code' category
    file_data = repo_tools.get_file_data(
        files.get("code")[0]
    )

    # Assert that the content of the file matches the expected string
    assert file_data == "print('hello world')"
