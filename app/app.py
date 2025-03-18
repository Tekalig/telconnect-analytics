# app.py
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = [
    'https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css',  # Example: Tailwind CSS
    # Add more external CSS URLs as needed
]
# Initialize the app
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

# Define the navigation bar
navbar = html.Nav(
    className="bg-gray-800 p-4",
    children=[
        html.Div(
            className="container mx-auto flex justify-between items-center",
            children=[
                html.A("Dashboard", href="/", className="text-white text-xl font-bold"),
                html.Div(
                    className="space-x-4",
                    children=[
                        dcc.Link("User Overview", href="/user-overview", className="text-gray-300 hover:text-white"),
                        dcc.Link("User Engagement", href="/user-engagement", className="text-gray-300 hover:text-white"),
                        dcc.Link("Experience Analysis", href="/experience-analysis", className="text-gray-300 hover:text-white"),
                        dcc.Link("Satisfaction Analysis", href="/satisfaction-analysis", className="text-gray-300 hover:text-white"),
                        dcc.Link("Comparative Analysis", href="/comparative-analysis", className="text-gray-300 hover:text-white")
                    ]
                )
            ]
        )
    ]
)


# Define the app layout
app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    html.Div(id="page-content", className="p-4")
])

# Callback to update page content
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/user-overview":
        from pages import user_overview
        return user_overview.UserOverviewPage()
    elif pathname == "/user-engagement":
        from pages import user_engagement
        return user_engagement.UserEngagementPage()
    elif pathname == "/experience-analysis":
        from pages import experience
        return experience.ExperienceAnalyticsPage()
    elif pathname == "/satisfaction-analysis":
        from pages import satisfaction
        return satisfaction.SatisfactionAnalyticsPage()
    elif pathname == "/comparative-analysis":
        from pages import comparative_analysis
        return comparative_analysis.update_comparison
    else:
        return html.Div("Welcome to the Dashboard! Use the navigation links above to explore different analyses.", className="text-lg")

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
