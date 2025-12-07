import pytest
from unittest.mock import patch, call
from src import main
import sys

@patch('src.storage.save_data')
@patch('src.storage.load_data')
def test_handle_add_success(mock_load_data, mock_save_data, capsys):
    """Test successfully adding a new expense."""
    mock_load_data.return_value = []
    args = main.argparse.Namespace(description="Groceries", amount=50.75, date="2025-12-06")
    
    main.handle_add(args)
    
    mock_load_data.assert_called_once_with(main.DATA_FILE)
    mock_save_data.assert_called_once()
    saved_data = mock_save_data.call_args[0][1]
    assert len(saved_data) == 1
    assert saved_data[0]['description'] == "Groceries"
    assert saved_data[0]['amount'] == 50.75

    captured = capsys.readouterr()
    assert "Expense added successfully." in captured.out

def test_handle_add_negative_amount(capsys):
    """Test that adding an expense with a negative amount fails."""
    args = main.argparse.Namespace(description="Invalid", amount=-10, date="2025-12-06")
    with pytest.raises(SystemExit) as e:
        main.handle_add(args)
    
    assert e.value.code == 1
    captured = capsys.readouterr()
    assert "Error: The amount must be a positive number." in captured.err

def test_handle_add_invalid_date(capsys):
    """Test that adding an expense with an invalid date format fails."""
    args = main.argparse.Namespace(description="Invalid", amount=10, date="2025/12/06")
    with pytest.raises(SystemExit) as e:
        main.handle_add(args)
        
    assert e.value.code == 1
    captured = capsys.readouterr()
    assert "Error: The date format must be YYYY-MM-DD." in captured.err

@patch('src.storage.load_data')
def test_handle_list_with_data(mock_load_data, capsys):
    """Test listing expenses when data exists."""
    mock_load_data.return_value = [
        {"id": 1, "date": "2025-12-05", "amount": 25.00, "description": "Lunch"},
        {"id": 2, "date": "2025-12-06", "amount": 12.50, "description": "Coffee"}
    ]
    main.handle_list(None)
    
    captured = capsys.readouterr()
    assert "Lunch" in captured.out
    assert "Coffee" in captured.out
    assert "ID   Date        Amount    Description" in captured.out

@patch('src.storage.load_data')
def test_handle_list_no_data(mock_load_data, capsys):
    """Test listing expenses when no data exists."""
    mock_load_data.return_value = []
    main.handle_list(None)
    
    captured = capsys.readouterr()
    assert "No transactions found." in captured.out

@patch('src.storage.load_data')
def test_handle_summary_with_data(mock_load_data, capsys):
    """Test summarizing expenses when data exists."""
    mock_load_data.return_value = [
        {"id": 1, "date": "2025-12-05", "amount": 25.00, "description": "Lunch"},
        {"id": 2, "date": "2025-12-06", "amount": 12.50, "description": "Coffee"}
    ]
    main.handle_summary(None)
    
    captured = capsys.readouterr()
    assert "Total number of transactions: 2" in captured.out
    assert "Total expenses: 37.50" in captured.out

@patch('src.storage.load_data')
def test_handle_summary_no_data(mock_load_data, capsys):
    """Test summarizing expenses when no data exists."""
    mock_load_data.return_value = []
    main.handle_summary(None)
    
    captured = capsys.readouterr()
    assert "No transactions to summarize." in captured.out
