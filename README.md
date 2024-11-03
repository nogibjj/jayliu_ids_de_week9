# Week 9 Mini Project

## Project Overview
This project involves setting up a cloud-hosted Jupyter Notebook for data manipulation tasks using the `US_birth.csv` dataset.

## Data Description
- **Dataset**: U.S. birth data from 2000 to 2014.
- **Columns**: Year, Month, Day of Month, Day of Week, Number of Births.

## Setup Instructions
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the setup script: `bash setup.sh`

## Usage
- **Jupyter Notebook**: Open `main.ipynb` in Google Colab or a local Jupyter environment.
- **Scripts**: Run `main.py` for data manipulations in a command-line interface.

## CI/CD Pipeline
GitHub Actions has been used for:
- Linting (`flake8`)
- Running unit tests (`pytest`)

## Dependencies
- Python 3.9+
- Libraries: pandas, matplotlib, seaborn, flake8, pytest

