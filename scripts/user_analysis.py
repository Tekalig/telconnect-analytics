import pandas as pd

def get_top_handsets(data, top_n=10):
    """Identify the top N handsets used by customers."""
    return data['Handset Type'].value_counts().head(top_n)

def get_top_manufacturers(data, top_n=3):
    """Identify the top N handset manufacturers."""
    return data['Handset Manufacturer'].value_counts().head(top_n)


def get_top_handsets_per_manufacturer(data, manufacturers, top_n=5):
    """
    Identify the top N handsets per manufacturer and return a DataFrame.

    Parameters:
        data (pd.DataFrame): The input DataFrame.
        manufacturers (list): List of manufacturers to analyze.
        top_n (int): Number of top handsets to include for each manufacturer.

    Returns:
        pd.DataFrame: A DataFrame with manufacturer, handset, and count.
    """
    rows = []

    for manufacturer in manufacturers:
        # Get top N handsets for the manufacturer
        top_handsets = (
            data[data['Handset Manufacturer'] == manufacturer]['Handset Type']
            .value_counts()
            .head(top_n)
        )
        # Append results to rows
        for handset, count in top_handsets.items():
            rows.append({'Manufacturer': manufacturer, 'Handset': handset, 'Count': count})

    # Create a DataFrame from rows
    result_df = pd.DataFrame(rows)
    return result_df


def aggregate_user_behavior(data):
    """Aggregate user behavior metrics."""
    user_agg = data.groupby('IMSI').agg(
        xDR_sessions=('Bearer Id', 'count'),
        total_duration=('Dur. (ms)', 'sum'),
        total_download=('Total DL (Bytes)', 'sum'),
        total_upload=('Total UL (Bytes)', 'sum'),
    )
    user_agg['total_data_volume'] = user_agg['total_download'] + user_agg['total_upload']
    return user_agg.reset_index()


def aggregate_engagement_metrics(df):
    """Aggregate engagement metrics per customer (MSISDN)."""
    engagement_metrics = df.groupby('MSISDN/Number').agg(
        session_frequency=('Bearer Id', 'count'),
        session_duration=('Dur. (ms)', 'sum'),
        total_ul_traffic=('Total UL (Bytes)', 'sum'),
    total_dl_traffic = ('Total DL (Bytes)', 'sum')
    ).reset_index()
    engagement_metrics['total_traffic'] = engagement_metrics['total_ul_traffic'] + engagement_metrics['total_dl_traffic']
    return engagement_metrics


def aggregate_experience_metrics(df):
    """Aggregate experience metrics per customer."""
    experience_metrics = df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': 'mean',
        'TCP UL Retrans. Vol (Bytes)': 'mean',
        'Avg RTT DL (ms)': 'mean',
        'Avg RTT UL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Avg Bearer TP UL (kbps)': 'mean',
        'Handset Type': lambda x: x.mode()[0]
    }).reset_index()

    return experience_metrics

def analyze_top_bottom_frequent(df, column):
    """Compute and list top, bottom, and most frequent values."""
    top = df.nlargest(10, column)
    bottom = df.nsmallest(10, column)
    frequent = df[column].value_counts().head(10)
    return top, bottom, frequent

