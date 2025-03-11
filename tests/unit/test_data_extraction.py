import pytest
import pandas as pd

# Add the path to the sys.path list
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))

# Import the function to be tested

from data_extraction import load_data

def test_load_data_success(tmp_path):
    # Create a temporary CSV file
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df.to_csv(file_path, index=False)
    
    # Load the data
    loaded_df = load_data(file_path)
    
    # Check if the data is loaded correctly
    pd.testing.assert_frame_equal(df, loaded_df)

def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("non_existent_file.csv")

def test_load_data_empty_file(tmp_path):
    # Create an empty CSV file
    file_path = tmp_path / "empty.csv"
    file_path.touch()
    
    with pytest.raises(ValueError, match="empty or the format is incorrect"):
        load_data(file_path)

def test_load_data_incorrect_format(tmp_path):
    # Create a file with incorrect format
    file_path = tmp_path / "incorrect_format.csv"
    file_path.write_text('a,"b,c\nd,e')  # Unmatched quote will cause a ParserError
   
    with pytest.raises(ValueError, match="could not be parsed"):
        load_data(file_path)
 