import logging
import os
from datetime import datetime

LOG_FOLDER = "logs"

DATE_FOLDER_NAME = datetime.now().strftime('%m_%d')

# full folder path logs/mm_dd
LOG_DIR = os.path.join(LOG_FOLDER,DATE_FOLDER_NAME)
os.makedirs(LOG_DIR,exist_ok=True)

#log file with full datetime name
LOG_FILE_NAME = f"{datetime.now().strftime('%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s -%(levelname)s %(message)s",
    level=logging.INFO,
)

