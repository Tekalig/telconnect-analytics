import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
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
    """Compute and visualize correlation matrix."""
    correlation_matrix = data[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
    return correlation_matrix

def perform_pca(data, columns):
    """Perform PCA and return explained variance ratio."""
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data[columns])
    explained_variance = pca.explained_variance_ratio_
    return principal_components, explained_variance

def plot_histograms(df):
    """
    Plots histograms for session duration and total data volume.
    """
    df['xDR_sessions'].hist(bins=30, alpha=0.5, label='Session Duration')
    df['total_data_volume'].hist(bins=30, alpha=0.5, label='Total Data Volume')
    plt.legend()
    plt.show()

def plot_pca_result(pca_result):
    """
    Plots the result of PCA analysis.
    """
    plt.scatter(pca_result[:, 0], pca_result[:, 1])
    plt.title('PCA Result (2 Components)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()