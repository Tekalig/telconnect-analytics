from dash import html, dcc
import plotly.express as px
import pandas as pd
import os

# file path to the data
file_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "src", "data", "telecom_dataset.csv"
)
# Load the data
df = pd.read_csv(file_path)
# Example of engagement analysis: Data consumption over time
engagement_data = df.groupby("Start").agg({"Total UL (Bytes)": "sum"}).reset_index()

# Create the plot
fig = px.line(
    engagement_data, x="Start", y="Total UL (Bytes)", title="Data Consumption Over Time"
)


# Page layout
def UserEngagementPage():
    return html.Div(
        [
            html.H2("User Engagement Analysis"),
            dcc.Graph(figure=fig),
        ]
    )
