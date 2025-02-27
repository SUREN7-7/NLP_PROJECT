import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  #To cosider the folder as a local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",   #Deployement(user app)
    "main.py",
    "Dockerfile",
    "requirements.txt", #necessary packages
    "setup.py",         #file which installs the requrired packages
    "research/trials.ipynb",

]

for filepath in list_of_files:
    filepath = Path(filepath)       #In windows '\' In linux '/' to handle this 'Path' is used. It detects windows/linux
    filedir, filename = os.path.split(filepath)     #filedir contains folder name, filename consists of filename

    if filedir != "":       #If folder is specified
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  #If filesize is 0 then create an empty file and also create if file is not existing already 
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")