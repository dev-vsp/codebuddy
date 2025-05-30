
import click
import urllib
import logging


# Setting up the logger for this module
logger = logging.getLogger(__name__)


class APIURL(click.ParamType):

    name = 'url'

    def convert(self, value, param, ctx):
        try:
            # Parse the URL using urllib's urlparse
            result = urllib.parse.urlparse(value)

            # Check if both scheme (e.g., http, https) and netloc (network location) are present
            if all([result.scheme, result.netloc]):
                # Log the valid URL at the debug level
                logger.debug(f"Valid API URL: {value}")

                # Return the valid URL
                return value
            else:
                # Log an error if the URL is invalid
                logger.error(f"Invalid API URL: {value} - Missing scheme or netloc")

                # Raise a ValueError to indicate invalid input
                raise ValueError
        except ValueError:
            # Handle the ValueError and provide a user-friendly error message
            self.fail(f"'{value}' is not a valid URL.", param, ctx)


class GitURL(click.ParamType):

    name = 'url'

    # Note: The conversion method is missing here, so this class is incomplete.
