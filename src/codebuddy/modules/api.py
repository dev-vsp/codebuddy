
import requests
import urllib.parse
import logging

from .config import request_handler, response_handler
from .config import API as API_CONFIG


# Setting up the logger for this module
logger = logging.getLogger(__name__)


class LMAPI:

    """
    A class for interacting with the LM API.

    This class provides methods for sending requests to the LM API and receiving responses.

    """

    def __init__(self, url: str = API_CONFIG.get("url")) -> None:
        """
        Initialize the LMAPI with the base URL of the API.

        Args:
            url (str, optional): The base URL of the API.
        """

        # Construct the full URL
        self.url = urllib.parse.urljoin(url, API_CONFIG.get("endpoint"))
        logger.debug(f"Initialized LMAPI with URL: {self.url}")

    def get_response(self, prompt: list) -> str:
        """
        Send a request to the API with the given prompt and return the response text.

        Args:
            prompt (list): A list of messages representing the conversation history.

        Returns:
            str: The content of the first choice's message from the API response.
        """

        # Constructs the query in json format
        data = request_handler(prompt)
        logger.debug(f"Sending request with data: {data}")

        # Send a POST request to the API endpoint with the specified headers and data
        response = requests.post(self.url, headers=API_CONFIG.get("headers"), json=data)
        logger.debug(f"Received response with status code: {response.status_code}")
        logger.debug(f"Response text: '{response.text}'")

        if response.status_code == 200:
            # Parse the JSON response
            response_text = response_handler(response)
            logger.debug(f"Extracted response text: '{response_text}'")

            # Return the extracted content as a string
            return response_text
        else:
            # Error logging
            logger.error(f"Request failed with status code: {response.status_code}")

            # Return empty string
            return ""
