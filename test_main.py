import subprocess
import logging

logger = logging.getLogger(__name__)


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
        "Loading dataset..." in result.stderr
    ), "Script did not log 'Loading dataset...'"
