
import click
import pathlib
import logging

from .modules import assistant
from .modules import reports
from .modules import repository
from .modules import types


# Setting up the logger for this module
logger = logging.getLogger(__name__)


# Defining the main command-line interface (CLI) function using Click
@click.command(
    help="CodeBuddy is a script for analyzing git repositories using a language model."
)
@click.argument(
    "repository_dir",                       # Argument for the directory containing the repository
    type=click.Path(file_okay=False)        # Ensures the path is a directory, not a file
)
@click.option(
    "--api",                                # Option to specify the API URL
    "api_url",                              # Name of the variable to store the API URL
    type=types.APIURL(),                          # Custom type for API URLs
    help="URL of the language model API."
)
@click.option(
    "--clone",                              # Option to clone a repository from a URL
    "repository_url",                       # Name of the variable to store the repository URL
    type=types.GitURL(),                          # Custom type for Git URLs
    help="Cloning a remote repository before analyzing it."
)
@click.option(
    "--reports",                            # Option to specify the directory for storing reports
    "reports_dir",                          # Name of the variable to store the reports directory
    type=click.Path(file_okay=False),       # Ensures the path is a directory, not a file
    help="Directory path to storing reports."
)
@click.option(
    "--print",                              # Option to print reports to the terminal
    "print_reports",                        # Name of the variable to store the print flag
    is_flag=True,                           # This option acts as a boolean flag
    help="Display all reports in the terminal."
)
def cli(
        repository_dir,     # Directory containing the repository
        api_url,            # URL of the language model API
        repository_url,     # URL of the repository to clone
        reports_dir,        # Directory to store reports
        print_reports       # Flag to print reports to the terminal
    ):

    try:
        # Resolving the repository directory path
        repository_dir = pathlib.Path(repository_dir).resolve()
        logger.info(f"Repository directory: {repository_dir}")

        # Creating the repository directory if it doesn't exist
        if not repository_dir.exists():
            repository_dir.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Create repository directory: {repository_dir}")

        # Resolving the reports directory path if provided
        if reports_dir:
            reports_dir = pathlib.Path(reports_dir).resolve()
            logger.info(f"Reports directory: {reports_dir}")

            # Creating the reports directory if it doesn't exist
            if not reports_dir.exists():
                reports_dir.mkdir(parents=True, exist_ok=True)
                logger.debug(f"Created reports directory: {reports_dir}")

        # Cloning the repository from the provided URL if specified
        if repository_url:
            try:
                # Check if the repository is available
                if (repository_dir / ".git").exists():
                    logger.warning(f"Repository cloning failed ('{repository_dir.name}' already exists)")
                else:
                    logger.info(f"Cloning repository from {repository_url} to {repository_dir}")
                    repository.RepositoryTools.clone_from(repository_url, repository_dir)
            except Exception as e:
                logger.error(f"Repository cloning error: {e}")
                return

        # Initializing the assistant with the API URL
        ai = assistant.Assistant(api_url)

        # Initializing tools for handling the repository
        repo_tools = repository.RepositoryTools(repository_dir)

        # Initializing the report generator with the repository and reports directories
        report_generator = reports.ReportGenerator(repository_dir, reports_dir)

        # Logging the path of the report file
        logger.info(f"Report file: {report_generator.report_file_path}")

        # Logging the start of the analysis
        logger.info(f"Running analysis for repository '{repository_dir.name}'...")

        # Getting all files categorized by their types from the repository
        files = repo_tools.get_files()

        errors_counter = 0
        for category in files.keys():
            for file_path in files.get(category):
                try:
                    # Getting the data of the current file
                    file_data = repo_tools.get_file_data(file_path)

                    # Logging the start of the analysis for the current file
                    logger.info(f"[{category}] Analyzing file '{file_path}'...")

                    # Getting the review of the current file from the assistant
                    file_review = ai.review(category, file_data)

                    # Adding the review to the reports
                    report_generator.add_report_entry(file_path, file_review)

                    # Printing the review to the terminal if the print flag is set
                    if print_reports:
                        print(f"\nFile: {file_path}")
                        print(f"{reports.ReportGenerator.markdown_to_text(file_review)}\n")

                except Exception as e:
                    errors_counter += 1
                    logger.error(f"Error analyzing file '{file_path}': {e}")

        # Saving the final report file
        report_generator.save_report_file()

        # Checking for errors in the analysis process
        if errors_counter:
            logger.warning(f"Analysis is complete, but there were {errors_counter} error(s)")
        else:
            # Logging the successful completion of the analysis
            logger.info("Analysis successfully completed!")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
