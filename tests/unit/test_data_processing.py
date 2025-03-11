import pytest
import pandas as pd
from transformers import AutoTokenizer

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2] / 'src'))
from data_processing import clean_text, tokenize_text, preprocess_data, split_data


def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("  This is a Test.  ") == "this is a test"
    assert clean_text("123 ABC abc!") == "123 abc abc"

def test_tokenize_text():
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenize_text("hello world", tokenizer)
    assert 'input_ids' in tokens
    assert 'attention_mask' in tokens

def test_preprocess_data():
    df = pd.DataFrame({"text": ["Hello, World!", "This is a Test."]})
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    df = preprocess_data(df, 'text', tokenizer)
    assert 'tokens' in df.columns
    assert len(df['tokens']) == 2

def test_split_data():
    df = pd.DataFrame({"text": ["text1", "text2", "text3", "text4"], "label": [0, 1, 0, 1]})
    train_df, val_df = split_data(df, test_size=0.5, random_state=42)
    assert len(train_df) == 2
    assert len(val_df) == 2