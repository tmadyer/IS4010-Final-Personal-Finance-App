# BudgetCLI

A robust command-line application designed to help users track their personal finances directly from the terminal.

![Tests](https://github.com/[YOUR-USERNAME]/Tmadyer/IS4010-Final-Personal-Finance-App/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

## Description

BudgetCLI is a lightweight, scriptable alternative to complex GUI finance apps, allowing users to log expenses, view transaction histories, and analyze spending habits without leaving their development environment. The project is engineered to serve as a professional portfolio piece, demonstrating mastery of modern software development practices including modular architecture, automated testing, and CI/CD.

## Features

- ✅ **Add Expenses**: Log new transactions with a description, amount, and date.
- ✅ **List Transactions**: View a formatted table of all recorded expenses.
- ✅ **Summarize Spending**: Get a quick summary of total expenses and transaction count.
- ✅ **Data Persistence**: All data is saved locally in a `budget_data.json` file.
- ✅ **Input Validation**: Ensures data integrity, such as preventing negative expense amounts.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[YOUR-USERNAME]/Tmadyer/IS4010-Final-Personal-Finance-App.git
    cd Tmadyer/IS4010-Final-Personal-Finance-App
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

BudgetCLI is run from the command line using `python -m src.main` followed by a command.

### Add an Expense

To add a new expense, use the `add` command with an amount and a description.

```bash
python -m src.main add 19.99 --description "Monthly subscription"
```

You can also specify a date (in YYYY-MM-DD format):

```bash
python -m src.main add 85.50 --description "Grocery shopping" --date 2025-12-07
```

### List All Expenses

To see all recorded transactions, use the `list` command.

```bash
python -m src.main list
```

**Example Output:**
```
ID   Date        Amount    Description
---------------------------------------------------------
1    2025-12-06  19.99     Monthly subscription
2    2025-12-07  85.50     Grocery shopping
```

### Show a Summary

To get a summary of your expenses, use the `summary` command.

```bash
python -m src.main summary
```

**Example Output:**
```
Expense Summary:
  Total number of transactions: 2
  Total expenses: 105.49
```

## Testing

To run the automated test suite, use `pytest`.

```bash
pytest
```

For more detailed output:
```bash
pytest -v
```

## AI-Assisted Development

This project was developed with assistance from AI tools. For a detailed log of AI interactions and prompts used, please see the [AGENTS.md](AGENTS.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
