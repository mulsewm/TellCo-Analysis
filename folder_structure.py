import os

# Define the folder structure
folders = [
    ".vscode",
    ".github/workflows",
    "src",
    "notebooks",
    "tests",
    "scripts",
]

# Define the files to be created
files = {
    ".gitignore": "",
    "README.md": "# TellCo Telecom Analysis\n\nThis repository contains the analysis and dashboards for TellCo telecom data.",
    "requirements.txt": "",
    ".vscode/settings.json": "{}",
    ".github/workflows/unittests.yml": """name: Run Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Run tests
      run: |
        source venv/bin/activate
        pytest
    """,
    "src/__init__.py": "",
    "src/analysis.py": "def placeholder_function():\n    return 'This is a placeholder for analysis functions.'\n",
    "notebooks/__init__.py": "",
    "notebooks/README.md": "# Jupyter Notebooks\n\nThis folder contains exploratory data analysis notebooks.",
    "tests/__init__.py": "",
    "tests/test_analysis.py": """from src.analysis import placeholder_function

def test_placeholder_function():
    assert placeholder_function() == 'This is a placeholder for analysis functions.'
""",
    "scripts/__init__.py": "",
    "scripts/data_preprocessing.py": """def preprocess_data():
    print('Data preprocessing placeholder')
""",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("Folder structure and files created successfully!")
