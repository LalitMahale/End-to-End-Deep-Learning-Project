import os
import sys
import logging

logging_str = '[%(asctime)s : %(levelname)s: %(module)s: %(message)s]'
log_dir = "logs"
log_file = os.path.join(log_dir,"runing_logs.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers= [
        logging.FileHandler(log_file), # this will add logs in file
        logging.StreamHandler(sys.stdout) # this will print log in terminal

    ]
)

logger = logging.getLogger("CNNClassifierLogger")
