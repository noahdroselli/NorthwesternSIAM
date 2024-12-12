import dash, smtplib
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import smtplib 
import dash_bootstrap_components as dbc
from email.message import EmailMessage

dash.register_page(
    __name__,
    title="Northwestern SIAM",
    path = "/",
)

circles = html.Div([
            html.Span([], className = "circle circle-0"),
            html.Span([], className = "circle circle-0"),
            html.Span([], className = "circle circle-0"),
            html.Span([], className = "circle circle-0"),
            html.Span([], className = "circle circle-0"),
            html.Span([], className = "circle circle-1"),
            html.Span([], className = "circle circle-1"),
            html.Span([], className = "circle circle-1"),
            html.Span([], className = "circle circle-1"),], className = "lp-circles")

lines = html.Div([
    html.Span([], className = "line line-1"),
    html.Span([], className = "line line-2"),
    html.Span([], className = "line line-3"),], className = "lp-lines")

layout = html.Div([
    # Landing page
    circles,
    lines,
    html.Div([
        html.Div([
            html.Img(src = 'assets/logo/siam.png', className = "logo"),
            html.Img(src = 'assets/logo/northwestern.png', className = "logo")
        ], className = "logo-container"),
        html.Div([
            html.H1("Northwestern SIAM", className = "lp-title"),
            html.H2("Society of Industrial and Applied Mathematics Chapter at Northwestern Univeristy", className = "lp-subtitle"),
            html.Div([
                    html.A("Conference", className = "BUTTON", href = "/conference"), 
                    html.A("Officers", className = "BUTTON", href = "#officers"),
                    html.A("Contact Us", className = "BUTTON", href = "#contactus"),
                    html.A("Events", className = "BUTTON", href = "/events"), 
                ], className = "button-list"),
        ], className = "lp-text"),
    ], className = "landing-page"), 

    # About us
    html.Div([
        html.Div([
            html.Div([], className = "CIRCLE-1"),
            html.H1("What is SIAM?", className = "title"),
            html.Div([html.A('SIAM (Society for Industrial and Applied Mathematics)', href = "https://www.siam.org/", target = "_blank", className = "underline"),
                        ' is the premier international professional organization for people in applied mathematics and related fields, including science and engineering. Our student chapter focuses on organizing events and activities to promote learning and involvement in applied mathematics. We hold a number of field trips and events each each, including trips to ',
                        html.A('Argonne National Laboratory', href = "https://www.anl.gov/", target = "_blank", className = "underline"), 
                        ' and ', 
                        html.A('Shedd Aquarium', href = "https://www.sheddaquarium.org/", target = "_blank", className = "underline"), 
                        ', social events such as pumpkin painting and boba tea times, and a series of ', 
                        html.A('journal talks.', href = "/events", className = "underline")
                    ], className = "text-wis")
            ], className = "wis"),
        html.Div([
            html.Div([], className = "CIRCLE-2"),
            html.H1("Membership", className = "title"),
            html.Div([
                'All Northwestern students, both undergraduate and graduate students, regardless of their major are eligible for ',
                        html.A('free membership with SIAM.', href = "https://www.siam.org/", target = "_blank", className = "underline"), 
                        ' We encourage all students to join the SIAM chapter here at Northwestern. To request to join the mailing list, simply use the ', 
                        html.A('Contact Us', href = "#contactus", className = "underline"), 
                        ' form and provide us with your name and email with the message that you want to join in our events. We will take it from there! Join us and tell us what kind of events you want to see!', 
                    ], className = "text-mem")
            ], className = "mem"),
    ], className = "about-us"),
    # eBoard
    html.Div([
        html.H1('Board Members', className = "title"),
        html.H2("2024-2025 Academic Year", className = "subtitle"),
        html.Div([
            html.A([
                html.Img(src = 'assets/people/siqiao.jpg', className = "img"),
                html.H1('Siqiao Mu', className = "bm-name"),
                html.H2('President', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=Rosemary%20Braun)-,Siqiao%20Mu,-Email%20Siqiao", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/ana.jpg', className = "img"),
                html.H1('Ana Barioni', className = "bm-name"),
                html.H2('Vice President', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "http://dyn.phys.northwestern.edu/group.html#:~:text=Ana%20Elisa%20D.%20Barioni", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/pietro.jpg', className = "img"),
                html.H1('Pietro Zanin', className = "bm-name"),
                html.H2('Treasurer', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "http://dyn.phys.northwestern.edu/group.html#:~:text=smith2027%40u.n...-,Pietro%20Zanin,-Research%3A%20Synchronization%20Dynamics", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/liam.jpg', className = "img"),
                html.H1('Liam O\'Connor', className = "bm-name"),
                html.H2('Academic Chair', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=Advisor%3A%20Diego%20Klabjan).-,Liam%20O%27Connor,-Email%20Liam", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/aaron.jpg', className = "img"),
                html.H1('Aaron Scheiner', className = "bm-name"),
                html.H2('Social Chair', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=Advisor%3A%20Diego%20Klabjan).-,Aaron%20Scheiner,-Email%20Aaron", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/divjyot.jpg', className = "img"),
                html.H1('Divjyot Singh', className = "bm-name"),
                html.H2('Outreach Chair', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=Email%20Elisheva-,Divjyot%20Singh,-Email%20Divjyot", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/noah.jpg', className = "img"),
                html.H1('Noah Roselli', className = "bm-name"),
                html.H2('Public Relations Chair', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=Advisor%3A%20Rosemary%20Braun).-,Noah%20Roselli,-Email%20Noah", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/aditi.jpg', className = "img"),
                html.H1('Aditi Ladda', className = "bm-name"),
                html.H2('Undergraduate Representative', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/christina.png', className = "img"),
                html.H1('Christina Catlett', className = "bm-name"),
                html.H2('Conference Chair', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=and%20Michael%20Miksis)-,Christina%20Catlett,-Email%20Christina", target = "_blank"),
            html.A([
                html.Img(src = 'assets/people/elisheva.jpg', className = "img"),
                html.H1('Elisheva Siegfried', className = "bm-name"),
                html.H2('Conference Chair', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "https://www.mccormick.northwestern.edu/applied-math/people/graduate-students.html#:~:text=Advisor%3A%C2%A0Daniel%20Abrams).-,Elisheva%20Siegfried,-Email%20Elisheva", target = "_blank"),
            html.Div([
            ], className = "empty-image"),
            html.A([
                html.Img(src = 'assets/people/adilson.jpg', className = "img"),
                html.H1('Adilson Motter', className = "bm-name"),
                html.H2('Faculty Advisor', className = "bm-role")
            ], className = "bm-image flex-col-center", href = "http://dyn.phys.northwestern.edu/", target = "_blank"),
        ], className = "board-members", id = "officers"),
        html.A(["Previous Board Members"], href = "/previous", className = "BUTTON PREVIOUS-MEMBERS")
    ], className = "flex-col-center eboard"),
    # Contact us
    html.Div([
        dbc.Form([
            # LAYER 0: CONTACT US
            html.Div(["Contact Us!"], className = "FORM-CONTACT FORM-ROW"),
            # LAYER 1: NAME INPUT
            html.Div([
                dbc.Label("Name:", html_for = "FORM-NAME", className = "form-label-1"),
                dbc.Input(type = "text", id = "FORM-NAME", className = "form-input-1")
            ], className = "FORM-1 FORM-ROW"),
            # LAYER 2: EMAIL INPUT
            html.Div([
                dbc.Label("Email: ", html_for = "FORM-EMAIL", className = "form-label-1"),
                dbc.Input(type = "email", id = "FORM-EMAIL", className = "form-input-1")
            ], className = "FORM-1 FORM-ROW"),
            # LAYER 3: QUESTION OR COMMENT TEXTAREA
            html.Div([
                html.Div(["Question/Comment:"], className = "form-label-2"),
                dcc.Textarea(id = "FORM-TEXTAREA", className = "form-input-2", draggable = False)
            ], className = "FORM-2 FORM-ROW"),
            # LAYER 4: SUBMIT BUTTON
            html.Div([
                html.Button(["Submit"], id = "FORM-SUBMIT", n_clicks = 0, className = "form-submit")
            ], className = "FORM-ROW"),
            # LAYER 4.5: ALERT FOR WHEN SUBMISSION IS SUCCESSFUL
            html.Div(children = [], id = "FORM-ALERT"),
            # LAYER 5: EXTRA STATEMENT
            html.Div([
                html.Div("Or directly email northwestern.siam.group@gmail.com.", className = "form-last-statement"),
                html.Div("Can contact us on Instagram @siam_northwestern!", className = "form-last-statement")]),
        ], className = "FORM", id = "contactus"),
        html.Div([
            html.Div([], className = "circle-end CIRCLE-END-0"),
            html.Div([], className = "circle-end CIRCLE-END-0"),
            html.Div([], className = "circle-end CIRCLE-END-0"),
            html.Div([], className = "circle-end CIRCLE-END-0"),
            html.Div([], className = "circle-end CIRCLE-END-1"),
            html.Div([], className = "circle-end CIRCLE-END-1"),
            html.Div([], className = "circle-end CIRCLE-END-1"),
            html.Div([], className = "circle-end CIRCLE-END-1"),
        ], className = "OTHER-CIRCLES")
    ], className = "contact")
], className = "FULL-CONTENT")

# CALLBACK FUNCTION FOR EMAILING
@callback(
    Output(component_id = "FORM-ALERT", component_property = "children"),
    Input(component_id = "FORM-SUBMIT", component_property = "n_clicks"),
    State(component_id = "FORM-TEXTAREA", component_property = "value"), 
    State(component_id = "FORM-EMAIL", component_property = "value"),
    State(component_id = "FORM-NAME", component_property = "value"),
)
def send_email(n_clicks, textfile, email, name):
    if (n_clicks > 0) & (textfile is not None) & (email is not None) & (name is not None):
        content = f"From: {name}\nWith address: {email}.\nThey say:\n{textfile}"
        msg = EmailMessage()
        msg.set_content(content)
        recipients = ['noahroselli2027@u.northwestern.edu', 'northwestern.siam.group@gmail.com']
        msg['subject'] = 'SIAM Notification'
        msg['to'] = ", ".join(recipients)

        user = "noahroselli2027@u.northwestern.edu"
        msg['from'] = user
        password = 'yyquefwsnbbwiplo'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
        return dbc.Alert("Email was sent.", duration = 3000, dismissable = True, class_name = "ALERT-FOR-EMAIL")