import dash, smtplib, matplotlib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import plotly.express as px
import smtplib 
from email.message import EmailMessage
import matplotlib.pyplot as plt

app = Dash(__name__, use_pages = True)
server = app.server
app.config.suppress_callback_exceptions = True
app.title = "Northwestern SIAM"

app.layout = html.Div([
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug = True)