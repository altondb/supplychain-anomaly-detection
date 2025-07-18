
# Data preprocessing utilities for supplier anomaly detection
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from typing import Tuple, Dict, List

def load_and_prepare_data(filepath: str) -> pd.DataFrame:
    """
    Load and prepare the supplier dataset for anomaly detection
    Input: filepath - path to the CSV file
    Returns: Prepared DataFrame
    """
    # Load data
    df = pd.read_csv(filepath)
    return df
