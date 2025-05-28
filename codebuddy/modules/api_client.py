
import requests
import urllib.parse


class APIClient:

    """
    A class for interacting with the chat API.

    This class provides methods for sending requests to the chat API and receiving responses.
    It automatically generates the necessary headers and request parameters.

    Attributes:
        url (str): The full URL of the chat API endpoint.
    """

    def __init__(self, url: str) -> None:
        """
        Initialize the APIClient with the base URL of the API.

        Args:
            url (str): The base URL of the API endpoint.
        """

        # Construct the full URL for the chat completions endpoint
        self.url = urllib.parse.urljoin(url, "v1/chat/completions")

        # Set the default headers for HTTP requests
        self.headers = {"Content-Type": "application/json"}

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
            "max_tokens": 500,
            "temperature": 0.5
        }

        # Send a POST request to the API endpoint with the specified headers and data
        response = requests.post(self.url, headers=self.headers, json=data)

        # Parse the JSON response to extract the content of the first choice's message
        response_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")

        # Return the extracted content as a string
        return response_text

