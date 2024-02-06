# implementig custom log
import os
import logging
import sys

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

# making a directory for keeping logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "runnig_logs.log")  # connecting file with the foler
os.makedirs(log_dir, exist_ok=True)   # creating foler and the file

logging.basicConfig(
    level= logging.INFO,
    format  = logging_str,

    handlers=[
        logging.FileHandler(log_filepath),   # for saving the logs in the file called running_logs.log
        logging.StreamHandler(sys.stdout)    # for showing the logs on the terminal
    ]
)

logger = logging.getLogger('TextSummarizerLogger')



