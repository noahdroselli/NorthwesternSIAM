import dash, smtplib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import smtplib 
from email.message import EmailMessage

dash.register_page(
    __name__,
    title="Previous Board | NU-SIAM ",
    path="/previous",
)

layout = html.Div([
    html.Div("Previous and Associated Members", className = "O-PAGE-TITLE"),
    html.Div([
        html.H1("2023-2024 Officers", className = "title-p"),
        html.Div([
            html.Div([
                html.P("Siqiao Mu", className = "bm-name"),
                html.P("President", className = "bm-role"),
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Ana Barioni", className = "bm-name"), 
                html.P("Vice President", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Maria Warns", className = "bm-name"), 
                html.P("Treasurer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Pietro Zanin", className = "bm-name"), 
                html.P("Treasurer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Noah Roselli", className = "bm-name"), 
                html.P("Historian", className = "bm-role")
            ], className = "bm-image flex-col-center"),
        ], className = "officers")
    ], className = "o-list"),
    html.Div([
        html.H1("2022-2023 Officers", className = "title-p"),
        html.Div([
            html.Div([
                html.P("Maria Warns", className = "bm-name"),
                html.P("President", className = "bm-role"),
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Liam O'Connor", className = "bm-name"), 
                html.P("Vice President", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("April Zhou", className = "bm-name"), 
                html.P("Webmaster", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P(" ", className = "bm-name"), 
                html.P("Outreach Chair", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Sungsoo Lim", className = "bm-name"), 
                html.P("Treasurer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
        ], className = "officers")
    ], className = "o-list"),
    html.Div([
        html.H1("Other Associated Officers", className = "title-p"),
        html.Div([
            html.Div([
                html.P("Addison Howe", className = "bm-name"), 
                html.P("Associated Officer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Richard Suhendra", className = "bm-name"), 
                html.P("Associated Officer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Solomon Valore-Caplan", className = "bm-name"), 
                html.P("Associated Officer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Connor Pruitz", className = "bm-name"), 
                html.P("Associated Officer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Sungsoo Lim", className = "bm-name"), 
                html.P("Associated Officer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
            html.Div([
                html.P("Zoey Ho", className = "bm-name"), 
                html.P("Associated Officer", className = "bm-role")
            ], className = "bm-image flex-col-center"),
        ], className = "officers")
    ], className = "o-list"),
    html.Div([
    html.A("Home", href = "/", className = "BUTTON PREVIOUS-MEMBERS")
    ], className = "flex-col-center")
], className = "previous-and-associated-page")