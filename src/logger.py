import os
import logging
from datetime import datetime

LOGS_DIR = os.path.join(os.getcwd(), "logs")

os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)