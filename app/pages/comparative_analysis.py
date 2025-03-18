import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os

# file path to the data
file_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "src", "data", "telecom_dataset.csv"
)
# Load the data
df = pd.read_csv(file_path)

# Extract relevant columns for DL and UL
dl_columns = [col for col in df.columns if "DL" in col]
ul_columns = [col for col in df.columns if "UL" in col]

# Layout for the page
layout = html.Div(
    className="p-6 bg-gray-100 min-h-screen",
    children=[
        html.H1(
            "Comparative Analysis: Download vs Upload",
            className="text-2xl font-bold mb-4",
        ),
        html.Div(
            className="flex space-x-4 mb-4",
            children=[
                dcc.Dropdown(
                    id="dl-metric",
                    options=[{"label": col, "value": col} for col in dl_columns],
                    placeholder="Select Download Metric",
                    className="flex-1 p-2 rounded border",
                ),
                dcc.Dropdown(
                    id="ul-metric",
                    options=[{"label": col, "value": col} for col in ul_columns],
                    placeholder="Select Upload Metric",
                    className="flex-1 p-2 rounded border",
                ),
            ],
        ),
        html.Div(id="comparison-output", className="bg-white p-4 rounded shadow"),
        dcc.Graph(id="comparison-graph", className="mt-4"),
    ],
)


# Callback for updating the graph
@dash.callback(
    [Output("comparison-graph", "figure"), Output("comparison-output", "children")],
    [Input("dl-metric", "value"), Input("ul-metric", "value")],
)
def update_comparison(dl_metric, ul_metric):
    if dl_metric is None or ul_metric is None:
        return (
            dash.no_update,
            "Please select both a Download and Upload metric to compare.",
        )

    # Prepare the data
    comparison_df = df[[dl_metric, ul_metric]].copy()
    comparison_df["Index"] = comparison_df.index

    # Create the comparison figure
    fig = px.line(
        comparison_df.melt(
            id_vars="Index",
            value_vars=[dl_metric, ul_metric],
            var_name="Metric",
            value_name="Value",
        ),
        x="Index",
        y="Value",
        color="Metric",
        title=f"Comparison: {dl_metric} vs {ul_metric}",
        labels={"Value": "Value", "Metric": "Metric Name", "Index": "Sample Index"},
    )

    summary = (
        f"Selected Metrics: \n"
        f"Download: {dl_metric} \n"
        f"Upload: {ul_metric} \n"
        f"Total Samples: {len(comparison_df)}"
    )

    return fig, summary
