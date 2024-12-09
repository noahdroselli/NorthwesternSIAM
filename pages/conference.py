import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from email.message import EmailMessage

dash.register_page(
    __name__,
    title="Conference",
    path="/conference",
)

circles = html.Div([
    html.Div([], className = "conference-circle CC-01"),
    html.Div([], className = "conference-circle CC-02"),
    html.Div([], className = "conference-circle CC-03"),
    html.Div([], className = "conference-circle CC-10"),
    html.Div([], className = "conference-circle CC-11"),
    html.Div([], className = "conference-circle CC-12"),
    html.Div([], className = "conference-circle CC-13"),
])

layout = html.Div([
    circles,
    html.H1(["Conference!"], className = "conference"),
    html.H2(["Northwestern will be hosting the 2025 SIAM Chicago-Area conference. Come back to this webpage in the future for more information."], className = "conference-info"),
    html.A(["Home."], className = "BUTTON", href = "/")
], className = "conference-container")