import argparse
import sys
from datetime import datetime
from . import storage

DATA_FILE = "budget_data.json"

def handle_add(args):
    """Handles the 'add' command."""
    if args.amount <= 0:
        print("Error: The amount must be a positive number.", file=sys.stderr)
        sys.exit(1)
        
    try:
        datetime.strptime(args.date, '%Y-%m-%d')
    except ValueError:
        print("Error: The date format must be YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    transactions = storage.load_data(DATA_FILE)
    
    new_transaction = {
        "id": len(transactions) + 1,
        "description": args.description,
        "amount": args.amount,
        "date": args.date
    }
    
    transactions.append(new_transaction)
    storage.save_data(DATA_FILE, transactions)
    print("Expense added successfully.")

def handle_list(args):
    """Handles the 'list' command."""
    transactions = storage.load_data(DATA_FILE)
    if not transactions:
        print("No transactions found.")
        return

    print(f"{'ID':<5}{'Date':<12}{'Amount':<10}{'Description':<30}")
    print("-" * 57)
    for t in transactions:
        print(f"{t['id']:<5}{t['date']:<12}{t['amount']:<10.2f}{t['description']:<30}")

def handle_summary(args):
    """Handles the 'summary' command."""
    transactions = storage.load_data(DATA_FILE)
    if not transactions:
        print("No transactions to summarize.")
        return

    total_expenses = sum(t['amount'] for t in transactions)
    num_transactions = len(transactions)
    
    print("Expense Summary:")
    print(f"  Total number of transactions: {num_transactions}")
    print(f"  Total expenses: {total_expenses:.2f}")

def main():
    """Main function to run the CLI."""
    parser = argparse.ArgumentParser(description="A simple command-line budgeting tool.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new expense.")
    add_parser.add_argument("amount", type=float, help="The amount of the expense.")
    add_parser.add_argument("-d", "--description", type=str, required=True, help="A description of the expense.")
    add_parser.add_argument("--date", type=str, default=datetime.now().strftime('%Y-%m-%d'), help="The date of the expense (YYYY-MM-DD).")
    add_parser.set_defaults(func=handle_add)

    # 'list' command
    list_parser = subparsers.add_parser("list", help="List all expenses.")
    list_parser.set_defaults(func=handle_list)

    # 'summary' command
    summary_parser = subparsers.add_parser("summary", help="Show a summary of all expenses.")
    summary_parser.set_defaults(func=handle_summary)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
