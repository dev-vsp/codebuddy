
import pytest

from codebuddy.modules import assistant


def test_assistant(request):
    # Retrieve the value of the '--full' command-line option
    full_test = request.config.getoption("--full")

    # Check if the '--full' option is set to True
    if full_test:
        # Initialize the Assistant class
        ai = assistant.Assistant()

        # Request a review of a code snippet using the Assistant
        file_review = ai.review('code', 'print("hello world")')

        # Assert that the review is not an empty string, indicating that the review was generated successfully
        assert file_review != ""
