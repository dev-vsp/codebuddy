
import pathlib
import datetime


class ReportGenerator:

    """
    A class to generate and save reports in Markdown format.

    This class manages the creation of report files in a specified directory,
    allowing you to add entries to the report and save it with a timestamped filename.
    """

    def __init__(self, reports_dir: str = "reports") -> None:
        """
        Initializes the ReportGenerator with a specified directory for storing reports.
        
        Args:
            reports_dir (str): The directory where reports will be saved. Defaults to "reports".
        """

        # Convert the reports directory string to a Path object and resolve its absolute path
        self.reports_dir = pathlib.Path(reports_dir).resolve()

        # Check if the reports directory exists, and create it if it doesn't
        if not self.reports_dir.exists():
            self.reports_dir.mkdir(parents=True, exist_ok=True)

        # Get the current date and time
        current_datetime = datetime.datetime.now()
        # Format the current date and time as a string in the format YYYY-MM-DD_HH:MM:SS
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        # Create the full path for the report file using the formatted date and time
        self.report_file_path = self.reports_dir / (formatted_datetime + ".md")

        # Initialize an empty list to store report entries
        self.report_data = []

    def add_report_entry(self, file_path: str, report_entry_data: str) -> bool:
        """
        Adds an entry to the report data.
        
        Args:
            file_path (str): The path of the file being reported on.
            report_entry_data (str): The data to include in the report entry.
        
        Returns:
            bool: Always returns True after adding the report entry.
        """

        # Create a formatted report entry string with a header
        # for the file path and the report entry data
        report_entry = f"# File: {file_path}\n{report_entry_data}"

        # Append the report entry to the list of report data
        self.report_data.append(
            report_entry
        )

        return True

    def save_report_file(self) -> bool:
        """
        Saves the accumulated report data to a Markdown file.
        
        Returns:
            bool: Always returns True after saving the report file.
        """

        # Join all report entries into a single string
        report_data = "\n\n".join(self.report_data)

        # Open the report file in write mode and write the report data to it
        with open(self.report_file_path, 'w') as report_file:
            report_file.write(report_data)

        return True
