from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# file path to the data
file_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "src", "data", "telecom_dataset.csv"
)
# Load the data
df = pd.read_csv(file_path)

# Example of satisfaction analysis: Scatter plot of engagement vs experience
satisfaction_data = df[
    ["Avg RTT DL (ms)", "Avg Bearer TP DL (kbps)", "Total UL (Bytes)"]
].dropna()

# Create the plot
fig = px.scatter(
    satisfaction_data,
    x="Avg RTT DL (ms)",
    y="Avg Bearer TP DL (kbps)",
    color="Total UL (Bytes)",
    title="Satisfaction Analysis",
)


# Page layout
def SatisfactionAnalyticsPage():
    return html.Div(
        [
            html.H2("Satisfaction Analysis"),
            dcc.Graph(figure=fig),
        ]
    )
