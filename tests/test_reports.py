
import pytest
import pathlib

from codebuddy.modules import reports


def test_report_generator():
    # Initialize the ReportGenerator with paths to a fake repository and a directory for reports
    report_generator = reports.ReportGenerator(
        pathlib.Path('tests/fake_repo'),
        pathlib.Path('tests/reports')
    )

    # Assert that the reports directory exists after initialization
    assert report_generator.reports_dir.exists() == True

    # Add a report entry for a file in the fake repository
    result_1 = report_generator.add_report_entry(
        pathlib.Path('tests/fake_repo/main.py'),
        "Test report 1"
    )

    # Assert that adding the report entry was successful
    assert result_1 == True

    # Add another report entry without automatically saving it to the report file
    result_2 = report_generator.add_report_entry(
        pathlib.Path('tests/fake_repo/README.md'),
        "Test report 2",
        auto_save=False
    )

    # Assert that adding the second report entry was successful
    assert result_2 == True
    # Assert that the report file path exists after adding the second entry (even though it's not saved yet)
    assert report_generator.report_file_path.exists() == True

    # Read the current content of the report file
    with open(report_generator.report_file_path, "r") as f:
        report_data_1 = f.read()

    # Assert that the content of the report file matches the expected content after the first entry
    assert report_data_1 == "\n## File: tests/fake_repo/main.py\nTest report 1\n"

    # Save the report file to disk
    report_generator.save_report_file()

    # Read the content of the report file again after saving
    with open(report_generator.report_file_path, "r") as f:
        report_data_2 = f.read()

    # Assert that the content of the report file now includes both entries
    assert report_data_2 == report_data_1 + \
        "\n## File: tests/fake_repo/README.md\nTest report 2\n"

    # Delete the report file
    result_3 = report_generator.delete_report_file()

    # Assert that deleting the report file was successful
    assert result_3 == True
    # Assert that the report file no longer exists on disk
    assert report_generator.report_file_path.exists() == False

    # Delete the reports directory
    result_4 = report_generator.delete_reports_dir()

    # Assert that deleting the reports directory was successful
    assert result_4 == True
    # Assert that the reports directory no longer exists on disk
    assert report_generator.reports_dir.exists() == False
