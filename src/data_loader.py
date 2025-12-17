import pandas as pd
import os

def load_data(filepath = '../data/StudentsPerformance.csv'):
    """reading data and returns dataframe"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Nie znaleziono pliku: {filepath}")
    
    df = pd.read_csv(filepath)
    return df