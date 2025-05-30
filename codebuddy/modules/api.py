
import requests
import urllib.parse
import logging

from .config import API as API_CONFIG


# Setting up the logger for this module
logger = logging.getLogger(__name__)


class LMAPI:

    """
    A class for interacting with the LM API.

    This class provides methods for sending requests to the LM API and receiving responses.

    Attributes:
        url (str): The base URL of the LM API.
    """

    def __init__(self, url: str = API_CONFIG.get("url")) -> None:
        """
        Initialize the LMAPI with the base URL of the API.

        Args:
            url (str): The base URL of the API.
        """

        # Construct the full URL
        self.url = urllib.parse.urljoin(url, API_CONFIG.get("endpoint"))
        logger.debug(f"Initialized LMAPI with URL: {self.url}")

        # Set the default headers for HTTP requests
        self.headers = {"Content-Type": "application/json"}
        logger.debug(f"Set headers: {self.headers}")

    def get_response(self, prompt: list) -> str:
        """
        Send a request to the API with the given prompt and return the response text.

        Args:
            prompt (list): A list of messages representing the conversation history.

        Returns:
            str: The content of the first choice's message from the API response.
        """

        data = {
            "messages": prompt,
            "max_tokens": API_CONFIG.get("max_tokens"),
            "temperature": API_CONFIG.get("temperature")
        }

        logger.debug(f"Sending request with data: {data}")

        # Send a POST request to the API endpoint with the specified headers and data
        response = requests.post(self.url, headers=self.headers, json=data)
        logger.debug(f"Received response with status code: {response.status_code}")
        logger.debug(f"Response text: '{response.text}'")

        # Parse the JSON response to extract the content of the first choice's message
        response_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        logger.debug(f"Extracted response text: '{response_text}'")

        # Return the extracted content as a string
        return response_text

