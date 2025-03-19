# Description: This script contains functions to perform exploratory analysis on the dataset.
import pandas as pd

def compute_basic_metrics(data):
    """Compute basic metrics for the dataset."""
    return data.describe()

def segment_users_by_decile(data):
    """Segment users into deciles based on total duration."""
    data['decile'] = pd.qcut(data['total_duration'], 10, labels=False)
    decile_data = data.groupby('decile').agg(
        total_data_volume=('total_data_volume', 'sum'),
        avg_duration=('total_duration', 'mean')
    ).reset_index()
    return decile_data

def compute_correlation_matrix(data, columns):
    """Compute  correlation matrix."""
    correlation_matrix = data[columns].corr()

    return correlation_matrix



