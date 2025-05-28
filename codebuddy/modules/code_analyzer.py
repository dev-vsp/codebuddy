
from .api_client import APIClient


class CodeAnalyzer:

    """
    A class for analyzing code and documentation using an API client.

    Attributes:
        api_client (APIClient): An instance of the API client used to interact with the API.
        prompts (dict): A dictionary containing prompts for different types of analysis.
    """

    def __init__(self, api_client: APIClient, prompts: str) -> None:
        """
        Initializes the CodeAnalyzer with an API client and a set of prompts.

        Args:
            api_client (APIClient): The API client used to send requests and receive responses.
            prompts (dict): A dictionary containing system and user prompts for code and documentation review.
        """

        self.api_client = api_client
        self.prompts = prompts

    def get_response(self, prompt: list) -> str:
        """
        Sends a prompt to the API client and returns the response.

        Args:
            prompt (list): A list of dictionaries representing the conversation prompt.

        Returns:
            str: The response received from the API.
        """

        response = self.api_client.get_response(prompt)
        return response

    def code_review(self, code: str) -> str:
        """
        Sends a code snippet to the API for review and returns the response.

        Args:
            code (str): The code snippet to be reviewed.

        Returns:
            str: The review response from the API.
        """

        prompt = [
            {"role": "system", "content": self.prompts.get("sys")},
            {"role": "user", "content": self.prompts.get("code").format(code=code)}
        ]

        response = self.get_response(prompt=prompt)
        return response
    
    def docs_review(self, doc_text: str) -> str:
        """
        Sends a documentation text to the API for review and returns the response.

        Args:
            doc_text (str): The documentation text to be reviewed.

        Returns:
            str: The review response from the API.
        """

        prompt = [
            {"role": "system", "content": self.prompts.get("sys")},
            {"role": "user", "content": self.prompts.get("docs").format(doc_text=doc_text)}
        ]

        response = self.get_response(prompt=prompt)
        return response

