import os
from pathlib import Path
import logging

# store logs 
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "CNNClassifier"

list_file = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
  f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",


]



for file in list_file:
    file_path = Path(file)
    filepath, filename = os.path.split(file_path)
    if filepath != "":
        os.makedirs(filepath,exist_ok=True)
        logging.info(f"creating directory : {filepath} for file : {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already exists.")