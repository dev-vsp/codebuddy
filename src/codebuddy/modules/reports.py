
import bs4
import markdown
import pathlib
import datetime
import logging

from .config import REPORT_DIR_NAME


# Setting up the logger for this module
logger = logging.getLogger(__name__)


class ReportGenerator:

    """
    A class to generate, edit and save reports.

    This class manages the creation of report files,
    allowing you to add records to a report and save it with a time stamped name.
    """

    def __init__(self, repository_dir: pathlib.Path, reports_dir: pathlib.Path = None) -> None:
        """
        Initializes the ReportGenerator for storing reports.

        Args:
            repository_dir (Path): Repository directory path, is used to determine where reports are stored or to name files.
            reports_dir (Path, optional): Report directory path, used for storing reports.
        """

        if reports_dir:
            self.reports_dir = reports_dir
        else:
            # Convert the full path to the directory with reports
            self.reports_dir = (repository_dir / REPORT_DIR_NAME).resolve()

        # Check if the reports directory exists, and create it if it doesn't
        if self.reports_dir.exists():
            logger.debug(f"Reports directory '{self.reports_dir}' already exists.")
        else:
            logger.debug(f"Reports directory '{self.reports_dir}' does not exist. Creating it.")
            self.reports_dir.mkdir(parents=True, exist_ok=True)

        # Get the current date and time
        current_datetime = datetime.datetime.now()
        # Format the current date and time as a string in the format YYYY-MM-DD_HH:MM:SS
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")

        # Create the full path for the report file using the formatted date and time
        if reports_dir:
            report_file_name_prefix = repository_dir.name + "_"
        else:
            report_file_name_prefix = ""

        self.report_file_path = self.reports_dir / f"{report_file_name_prefix}{formatted_datetime}.md"
        logger.debug(f"Report file path set to: {self.report_file_path}")

        # Initialize an empty list to store report entries
        self.report_data = []
        logger.debug("Report data initialized as an empty list.")

    def add_report_entry(self, file_path: str, report_entry_data: str, auto_save: bool = True) -> bool:
        """
        Adds an entry to the report data.
        
        Args:
            file_path (str): The path of the file being reported on.
            report_entry_data (str): The data to include in the report entry.
            auto_save (bool, optional): If True, the method will immediately save the entry to a file.

        Returns:
            bool: Always returns True after adding the report entry.
        """

        # Create a formatted report entry string with a header
        # for the file path and the report entry data
        report_entry = f"\n## File: {file_path}\n{report_entry_data}\n"
        logger.debug(f"Adding report entry: {report_entry}")

        # Append the report entry to the list of report data
        self.report_data.append(report_entry)
        logger.debug(f"Report entry added. Total entries: {len(self.report_data)}")

        if auto_save:
            logger.debug("Auto-save enabled. Saving report file.")
            self.save_report_file()

        return True

    def save_report_file(self) -> bool:
        """
        Saves the accumulated report data to a Markdown file.
        
        Returns:
            bool: Always returns True if the reports exist, otherwise False.
        """

        # Checking for reports
        if self.report_data:
            # Join all report entries into a single string
            report_data = "\n\n".join(self.report_data)
            logger.debug(f"Joining report data into a single string: {report_data}")

            # Open the report file in write mode and write the report data to it
            with open(self.report_file_path, 'a') as report_file:
                report_file.write(report_data)

            logger.debug(f"Report data written to file: {self.report_file_path}")

            # Clearing the list of unsaved reports
            self.report_data.clear()
            logger.debug("Report data cleared after saving")

            return True
        else:
            logger.debug("Report file has not been saved, report list is empty")
            return False

    @staticmethod
    def markdown_to_text(markdown_string: str) -> str:
        """
        Converts a Markdown formatted string to plain text.

        This method takes a string formatted in Markdown, converts it to HTML,
        and then extracts the plain text from the HTML.

        Args:
            markdown_string (str): The input string containing Markdown formatted text.

        Returns:
            str: The extracted plain text from the Markdown input.
        """

        # Convert Markdown to HTML
        html = markdown.markdown(markdown_string)
        logger.debug(f"Markdown converted to HTML: {html}")
    
        # Parsing HTML and extracting text
        soup = bs4.BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        logger.debug(f"Extracted text from HTML: {text}")
        
        return text
