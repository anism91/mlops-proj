import re
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer

def clean_text(text):
    """
    Clean and preprocess the text.
    
    Parameters:
    text (str): The raw text.
    
    Returns:
    str: The cleaned text.
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove unnecessary characters
    text = text.strip()  # Remove leading and trailing whitespace
    return text

def tokenize_text(text, tokenizer):
    """
    Tokenize the text using the provided tokenizer.
    
    Parameters:
    text (str): The cleaned text.
    tokenizer (AutoTokenizer): The tokenizer to use.
    
    Returns:
    dict: The tokenized text.
    """
    return tokenizer(text, padding='max_length', truncation=True, return_tensors='pt')

def preprocess_data(df, text_column, tokenizer):
    """
    Preprocess the data by cleaning and tokenizing the text.
    
    Parameters:
    df (pd.DataFrame): The raw data.
    text_column (str): The name of the column containing the text.
    tokenizer (AutoTokenizer): The tokenizer to use.
    
    Returns:
    pd.DataFrame: The preprocessed data.
    """
    df[text_column] = df[text_column].apply(clean_text)
    df['tokens'] = df[text_column].apply(lambda x: tokenize_text(x, tokenizer))
    return df

def split_data(df, test_size=0.2, random_state=42):
    """
    Split the data into training and validation sets.
    
    Parameters:
    df (pd.DataFrame): The preprocessed data.
    test_size (float): The proportion of the data to include in the test split.
    random_state (int): The random seed.
    
    Returns:
    tuple: The training and validation sets.
    """
    train_df, val_df = train_test_split(df, test_size=test_size, random_state=random_state)
    return train_df, val_df

# Example usage
if __name__ == "__main__":
    # Load the data
    df = pd.read_csv('path/to/your/data.csv')
    
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    
    # Preprocess the data
    df = preprocess_data(df, 'text_column_name', tokenizer)
    
    # Split the data
    train_df, val_df = split_data(df)
    
    # Save the preprocessed data
    train_df.to_csv('path/to/save/train_data.csv', index=False)
    val_df.to_csv('path/to/save/val_data.csv', index=False)