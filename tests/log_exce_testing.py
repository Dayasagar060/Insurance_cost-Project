import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger import logging


from src.exceptions import CustomException, format_exception

# logging = logging.getLogger(__name__)


def trigger_error():
    return 1/0  # This will raise a 0.5


def main():
    logging.info("Starting smoke test for logger + exceptions")
    try:
        trigger_error()
    except Exception as e:
        # Log only short, readable message (no traceback)
        logging.error("Caught an exception in trigger_error(): %s", format_exception(e))

        # short, human-friendly description
        short = format_exception(e)
        logging.info("Short formatted exception: %s", short)

        try:
            raise CustomException(exc=e, message="An error occurred in main()")
        except CustomException as ce:
            logging.info("Wrapped as CustomException: %s", str(ce))

    logging.info("Smoke test completed.")



if __name__ == "__main__":
    main()