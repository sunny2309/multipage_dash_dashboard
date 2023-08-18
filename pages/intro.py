import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction 😃")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Titanic Dataset Overview"),
        "The sinking of the Titanic is one of the most infamous shipwrecks in history.",
        html.Br(),html.Br(),
        "On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.",
        html.Br(), html.Br(),
        "While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.",
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("Survival: "), "0 = No, 1 = Yes",
        html.Br(),
        html.B("pclass: "), "Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)",
        html.Br(),
        html.B("sex: "), "Sex",
        html.Br(),
        html.B("Age: "), "Age in years",
        html.Br(),
        html.B("sibsp: "), "# of siblings / spouses aboard the Titanic",
        html.Br(),
        html.B("parch: "), "# of parents / children aboard the Titanic",
        html.Br(),
        html.B("ticket: "), "Ticket number",
        html.Br(),
        html.B("fare: "), "Passenger fare",
        html.Br(),
        html.B("cabin: "), "Cabin number",
        html.Br(),
        html.B("embarked: "), "Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)",
    ])
], className="bg-light p-4 m-2")