import dash, smtplib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import smtplib 
from email.message import EmailMessage

app = Dash(__name__, use_pages = True)
server = app.server
app.config.suppress_callback_exceptions = True
app.title = "Northwestern SIAM"

app.layout = html.Div([
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug = True)