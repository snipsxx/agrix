import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

project_name="agrix"

list_of_files=[
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py"
    "config/config.yaml",
    "dvc.yaml",
    "setup.py",
    "requirements.txt",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "research/trials.ipynb",
    "templates/index.html",
    "main.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"created directory: {filedir} for {filename}")

        if not os.path.exists(filepath):
            with open(filepath,"w") as file:
                logging.info(f"created file:{filepath}")