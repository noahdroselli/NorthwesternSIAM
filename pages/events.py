import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import plotly.express as px
from email.message import EmailMessage

dash.register_page(
    __name__,
    title="Events | NU-SIAM",
    path="/events",
)

layout = html.Div([
    html.H1("Events", className = "events-title"), 
    html.Div(['We host multiple events through the quarter. See below for some recent events and keep up with our ',
            html.A('Instagram page', target = "_blank", href = "https://www.instagram.com/siam_northwestern", className = "underline"), 
            ' to stay updated with future events!']),
    html.Div([
        html.Div([
            html.Img(src = "/assets/events/journal.png", className = "event-img"),
            html.Div(["Academic event where people present on a paper, a computing skill, or an experimental result! ", 
                    html.A("Contact us", className = "underline", href = "/#contactus"), 
                    " if you would like to present."])
        ], className = "event-example"), 
        html.Div([
            html.Img(src = "/assets/events/movie.png", className = "event-img"),
            html.Div(["Move night! We watched ", html.Span("Hidden Figures", className = "italics")]),
        ], className = "event-example")
    ], className = "events-container"),
    html.A("Home.", className = "BUTTON", href = "/")
], className = "events-page")