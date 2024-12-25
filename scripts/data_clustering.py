from sklearn.cluster import KMeans

def apply_kmeans_clustering(engagement_metrics,  columns, n_clusters=3):
    """Apply k-means clustering to the engagement metrics."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    engagement_metrics['cluster'] = kmeans.fit_predict(engagement_metrics[columns])
    return engagement_metrics, kmeans

def elbow_method(engagement_metrics, columns):
    """Use the elbow method to find the optimal number of clusters."""
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(engagement_metrics[columns])
        wcss.append(kmeans.inertia_)
    return wcss
