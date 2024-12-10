import dash, smtplib, matplotlib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import plotly.express as px
import smtplib 
from email.message import EmailMessage
import matplotlib.pyplot as plt

dash.register_page(
    __name__,
    title="Previous Board | NU-SIAM ",
    path="/previous",
)

layout = html.Div([
    html.H1(["Previous board members."], className = 'previous'),
    html.Hr(),
    html.Div([
        html.H1('2023-2024', className = 'members-year'), 
        html.Div([
            html.Div([
                html.Img(src = "/assets/previous/y23y24/pres.png"),
                html.H1('Siqiao Mu'),
                html.H2('President')
            ], className = "old-im")
        ], className = "members-container")
    ])
], className = "flex-container")