import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)
layout = html.Div(
    [
        html.Div(
            [
                html.Hr(),
                html.Img(src="/assets/1_1.png"),
                html.Hr(),
                html.Img(src="/assets/2_2.png"),
                html.Hr(),
                html.Img(src="/assets/3.png"),
                html.Hr(),
            ],
            style={"textAlign": "center"}
        ),
    ]
)
