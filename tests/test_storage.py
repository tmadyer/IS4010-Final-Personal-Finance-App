import json
import pytest
from src import storage

def test_load_data_non_existent_file(tmp_path):
    """Test loading data from a non-existent file returns an empty list."""
    file_path = tmp_path / "non_existent.json"
    assert storage.load_data(str(file_path)) == []

def test_save_and_load_data(tmp_path):
    """Test saving data and then loading it back."""
    file_path = tmp_path / "test_data.json"
    data_to_save = [{"id": 1, "description": "Test", "amount": 10.0, "date": "2025-12-06"}]
    
    storage.save_data(str(file_path), data_to_save)
    loaded_data = storage.load_data(str(file_path))
    
    assert loaded_data == data_to_save

def test_load_data_corrupted_file(tmp_path):
    """Test that loading a corrupted JSON file raises a ValueError."""
    file_path = tmp_path / "corrupted.json"
    with open(file_path, 'w') as f:
        f.write("{'invalid_json':}")

    with pytest.raises(ValueError, match="The data file is corrupted and cannot be read."):
        storage.load_data(str(file_path))
