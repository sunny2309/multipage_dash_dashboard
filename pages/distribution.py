import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Distribution 📊")

####################### LOAD DATASET #############################
titanic_df = pd.read_csv("titanic.csv")

####################### HISTOGRAM ###############################
def create_distribution(col_name="Age"):
    return px.histogram(data_frame=titanic_df, x=col_name, height=600)

####################### WIDGETS ################################
columns = ["Age", "Fare", "SibSp", "Parch", "Survived", "Pclass", "Sex", "Embarked", "Cabin"]
dd = dcc.Dropdown(id="dist_column", options=columns, value="Age", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")
])

####################### CALLBACKS ################################
@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)

