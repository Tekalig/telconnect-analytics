import seaborn as sns
import matplotlib.pyplot as plt


def plot_top_apps(df):
    """Plot the top 3 most used applications based on traffic."""
    top_apps = df.groupby('Handset Type').agg(
        total_dl=('Total DL (Bytes)', 'sum'),
        total_ul=('Total UL (Bytes)', 'sum')
    ).reset_index()

    top_apps = top_apps.nlargest(3, 'total_dl')

    plt.figure(figsize=(10, 6))
    plt.bar(top_apps['Handset Type'], top_apps['total_dl'], label='Download Traffic')
    plt.bar(top_apps['Handset Type'], top_apps['total_ul'], bottom=top_apps['total_dl'], label='Upload Traffic')
    plt.title('Top 3 Most Used Applications')
    plt.xlabel('Application')
    plt.ylabel('Traffic (Bytes)')
    plt.legend()
    plt.show()

def plot_elbow_method(wcss):
    """Plot the elbow method for determining the optimal number of clusters."""
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, 11), wcss, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()



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

def plot_correlation_matrix(correlation_matrix):
    """visualize the correlation matrix using a heatmap."""
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()


def analyze_distributions(df, column, group_col):
    """
    Analyze distributions of a metric per group with improved visualization.
    """
    grouped = df.groupby(group_col)[column].mean().sort_values()

    # Plot using seaborn for better aesthetics
    plt.figure(figsize=(14, 12))
    sns.barplot(
        y=grouped.index,
        x=grouped.values,
        palette="viridis",
        hue=grouped.values,
        legend=False
    )
    plt.title(f"{column} Distribution per {group_col}", fontsize=16, weight='bold')
    plt.ylabel(group_col, fontsize=10)
    plt.xlabel(f"Average {column}", fontsize=12)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

def plot_clusters_2d(df, x_col, y_col, cluster_col):
    """
    Plot clusters in 2D space.

    Parameters:
        df (DataFrame): DataFrame containing the features and cluster labels.
        x_col (str): Column name for the x-axis.
        y_col (str): Column name for the y-axis.
        cluster_col (str): Column name for the cluster labels.
    """
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df[x_col], df[y_col], c=df[cluster_col], cmap='viridis', s=50, alpha=0.7
    )
    plt.colorbar(scatter, label='Cluster')
    plt.title(f"Clusters based on {x_col} and {y_col}", fontsize=16, weight='bold')
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.grid(alpha=0.5)
    plt.show()

