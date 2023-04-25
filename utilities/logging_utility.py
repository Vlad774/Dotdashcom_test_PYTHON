import os
import logging

# Get the path of the parent directory of the project directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_logger(name, log_filename, test_status):
    # Create a logger instance with the given name
    logger = logging.getLogger(name)

    # Create a file handler that writes log messages to the log file
    file_handler = logging.FileHandler(os.path.join(parent_dir, "logs", log_filename))

    # Create a formatter that specifies the format of the log messages
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    # Set the formatter for the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Set the logging level to INFO
    logger.setLevel(logging.INFO)

    # Log a message based on the test status
    if test_status == "pass":
        logger.info("Test passed")
    elif test_status == "fail":
        logger.error("Test failed")

    return logger
