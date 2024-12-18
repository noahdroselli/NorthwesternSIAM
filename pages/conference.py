import dash, smtplib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import smtplib 
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
    html.Div([], className = "conference-circle CC-04"),
    html.Div([], className = "conference-circle CC-05"),
    html.Div([], className = "conference-circle CC-10"),
    html.Div([], className = "conference-circle CC-11"),
    html.Div([], className = "conference-circle CC-12"),
    html.Div([], className = "conference-circle CC-13"),
])

layout = html.Div([
    circles,
    html.Div([
        html.H1(["Conference!"], className = "conference"),
        html.H2(["Nothing to see here...yet!"]),
        html.H2(["Northwestern will be hosting the 2025 SIAM Chicago-Area conference. Come back to this webpage in the future for more information."], className = "conference-info"),
        html.H3(["If you have any questions, please reach out to Christina Catlett (ccatlett@u.northwestern.edu) and Elisheva Siegfried (elisheva.siegfried@northwestern.edu); or use the ", html.A("Contact Us", href = "https://northwesternsiam.onrender.com/#contactus", className = "underline"), " form and we will put you in contact with them."], className = "chair-info"),
        html.A(["Home"], className = "BUTTON", href = "/")
    ], className = "conference-words flex-col-center")
], className = "conference-container")