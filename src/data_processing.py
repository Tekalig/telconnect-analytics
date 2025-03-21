import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """Load dataset and return a DataFrame."""
    return pd.read_csv(file_path)


def handle_missing_values(data):
    """Fill missing values with the mean or other strategies."""
    return data.fillna(data.mean(numeric_only=True))


def remove_missing_values(data, columns=None):
    """
    Remove rows with null values.

    Parameters:
        data (pd.DataFrame): The input DataFrame.
        columns (list, optional): Specific columns to check for null values.
                                  If None, checks all columns.

    Returns:
        pd.DataFrame: The DataFrame with rows containing null values removed.
    """
    if columns:
        # Remove rows with null values in the specified columns
        data = data.dropna(subset=columns)
    else:
        # Remove rows with null values in any column
        data = data.dropna()

    return data


def clean_and_treat_outliers(df):
    """Clean data by treating missing values and outliers."""
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        df[col].fillna(df[col].mean(), inplace=True)
        # Replace outliers using the 1.5*IQR rule
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df[col] = df[col].clip(lower_bound, upper_bound)
    return df


def perform_pca(data, columns):
    """Perform PCA and return explained variance ratio."""
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data[columns])
    explained_variance = pca.explained_variance_ratio_
    return principal_components, explained_variance


def normalize_engagement_metrics(engagement_metrics, columns):
    """Normalize engagement metrics using StandardScaler."""
    scaler = StandardScaler()
    engagement_metrics[columns] = scaler.fit_transform(engagement_metrics[columns])
    return engagement_metrics
