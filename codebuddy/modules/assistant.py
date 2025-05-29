
from .api import LMAPI
from .config import PROMPTS


class Assistant:

    """
    An AI assistant that interacts with a LM API to provide various types of reviews and responses.
    """

    def __init__(self, api_url: str = None) -> None:
        """
        Initializes the Assistant with an optional API URL.

        Args:
            api_url (str, optional): The URL of the LM API. If not provided, a default URL is used.
        """

        if api_url:
            self.lm_api = LMAPI(api_url)
        else:
            self.lm_api = LMAPI()

        self.prompts = PROMPTS

    def get_response(self, prompt: list) -> str:
        """
        Sends a prompt to the API client and returns the response.

        Args:
            prompt (list): A list of dictionaries representing the conversation prompt.

        Returns:
            str: The response received from the API.
        """

        response = self.lm_api.get_response(prompt)
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

