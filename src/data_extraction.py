import pandas as pd

def load_data(file_path):
    """
    Load raw data from a CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    ValueError: If the file format is incorrect.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file at {file_path} is empty or the format is incorrect.")
    except pd.errors.ParserError:
        raise ValueError(f"The file at {file_path} could not be parsed.")
    except Exception as e:
        raise ValueError(f"An error occurred while loading the file: {e}")