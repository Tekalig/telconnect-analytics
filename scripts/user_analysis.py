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

