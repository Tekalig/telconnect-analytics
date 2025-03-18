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
# Aggregating the data for the page (example: total data usage per user)
user_data = df.groupby("IMSI").agg({"Total UL (Bytes)": "sum"}).reset_index()

# Create the plot for this page
fig = px.bar(
    user_data, x="IMSI", y="Total UL (Bytes)", title="Total Data Usage per User"
)


# Page layout
def UserOverviewPage():
    return html.Div(
        [
            html.H2("User Overview Analysis"),
            dcc.Graph(figure=fig),
        ]
    )
