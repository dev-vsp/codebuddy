
import os
import sys


# Option to activate full-fledged testing using the language model
def pytest_addoption(parser):
    parser.addoption(
        "--full",
        action="store_true",
        help="Full-fledged test with connection to the language model."
    )

# Construct the absolute path to the 'src' directory
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))

# Insert the 'src' directory into the system path at the beginning
sys.path.insert(0, src_dir)
