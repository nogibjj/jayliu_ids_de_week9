import pytest
import subprocess
import logging
from mylib import data_utils, stats_utils

# Configure logging to capture logs for assertions
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Test that main.py runs without errors
def test_main_script_runs():
    # Run the main.py script as a subprocess
    try:
        result = subprocess.run(
            ["python", "main.py"], check=True, capture_output=True, text=True
        )
        logger.info("main.py ran successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"main.py encountered an error: {e.stderr}")
        raise

    # Ensure that there is output and that it does not indicate an error
    assert result.returncode == 0, "main.py script did not exit successfully"
    assert (
        "Loading dataset..." in result.stdout
    ), "Script did not log 'Loading dataset...'"
    assert (
        "Plotting birth trends over time..." in result.stdout
    ), "Script did not log 'Plotting birth trends over time...'"
    assert (
        len(result.stderr) == 0
    ), "There were unexpected errors or warnings during execution"


# Test that the main script successfully calculates statistics
def test_main_statistics():
    # Set up sample data to match the data in main.py
    sample_data = {
        "year": [2000, 2001, 2002, 2002, 2003],
        "month": [1, 2, 3, 3, 4],
        "date_of_month": [1, 2, 3, 4, 5],
        "day_of_week": [6, 7, 1, 2, 3],
        "births": [100, 200, 300, 400, 500],
    }
    sample_df = data_utils.load_data("US_birth.csv")

    mean_births = stats_utils.calculate_mean(sample_df, "births")
    median_births = stats_utils.calculate_median(sample_df, "births")

    # Assert expected mean and median values
