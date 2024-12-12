import dash, smtplib, matplotlib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import plotly.express as px
import smtplib 
from email.message import EmailMessage
import matplotlib.pyplot as plt

dash.register_page(
    __name__,
    title="Events | NU-SIAM",
    path="/events",
)

layout = html.Div([
        html.H1("Events", className = "events-title"), 
        html.Div([
            html.Div([
                html.Img(src = "/assets/events/journal.png", className = "event-img"),
                html.Div(["Academic event where people present on a paper, a computing skill, or an experimental result! ", 
                        html.A("Contact us", className = "underline", href = "/#contactus"),
                        " if you would like to present."])
            ], className = "event-example"), 
            html.Div([
                html.Img(src = "/assets/events/movie.png", className = "event-img"),
                html.Div(["Movie night! We watched ", html.Span("Hidden Figures.", className = "italics")]),
            ], className = "event-example")
        ], className = "events-container"),
        html.Div(['Keep up with our ',
                html.A('Instagram page', target = "_blank", href = "https://www.instagram.com/siam_northwestern", className = "underline events-subtitle"), 
                ' (@siam_northwestern) to stay updated with future events!'], className = "events-subtitle"),
        html.A("Home", href = "/", className = "BUTTON button-bottom")
], className = "events-page flex-col-center")