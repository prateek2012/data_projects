# End to End Data Engineering Project

This project focuses on processing and analyzing a real-world dataset provided by the open-source [ListenBrainz Dataset](https://listenbrainz.org)
 project. It aims to explore user listening habits and generate insights through a series of targeted queries.
Key features include:
- Scripts for initial data exploration and analysis.
- Tools for creating a structured database from the raw dataset.
- SQL queries to extract meaningful insights from user listening data.
- Proposed System Design. 
- Poposed Production Setup.
This project is a practical demonstration of data engineering and analysis workflows, showcasing how user behavior can be understood through effective data processing techniques.

## Setup a Virtual Environment
Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

##Install Dependencies
Install the required packages:

pip install -r requirements.txt

## Run the Analysis
Execute the data analysis and output the results in terminal

python src/main.py

## Code Formatting and Linting

Format Code with 'black'

black src/

Lint Code with 'flake8'

flake8 src/



### File Explanations

- **data/**
  - `dataset.txt`: Contains the dataset used for analysis. It is expected to be in JSON lines format.

- **src/**
  - `__init__.py`: Marks the directory as a Python package.
  - `data_analysis.py`: Contains functions for performing initial data analysis.
  - `db_queries.py`: Contains functions for setting up the database and running SQL queries.
  - `main.py`: The main script that ties everything together, executing the data analysis workflow.
  - `utils.py`: Contains utility functions used across the project.

- **Documentation/**
  - `Challenge_3_System_Design`: Response to the challenge 3 - System Design with System Design Architecture.
  - `Production_Setup`: Proposed Production Setup for this challenge
- **.flake8**: Configuration file for `flake8`
- **pyproject.toml**: Configuration file for `black`, a code formatting tool for Python. It defines formatting rules and exclusions
- **.gitignore**: Specifies files and directories that should be ignored by Git. This includes environment directories, compiled code, and other temporary files.
- **requirements.txt**: Lists the Python dependencies required for the project. This can be used to install all necessary packages using `pip`.
- **README.md**: This file provides an overview of the project, setup instructions, and explanations for each file.

