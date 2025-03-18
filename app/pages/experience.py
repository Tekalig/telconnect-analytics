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
# Example of experience analytics: RTT vs throughput
experience_data = df[["Avg RTT DL (ms)", "Avg Bearer TP DL (kbps)"]].dropna()

# Create the plot
fig = px.scatter(
    experience_data,
    x="Avg RTT DL (ms)",
    y="Avg Bearer TP DL (kbps)",
    title="RTT vs Throughput",
)


# Page layout
def ExperienceAnalyticsPage():
    return html.Div(
        [
            html.H2("Experience Analytics"),
            dcc.Graph(figure=fig),
        ]
    )
