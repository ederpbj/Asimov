import dash
import dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4,1,2,2,4,5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
})

fig = px.bar(df, x="Fruit", y="Amount", color="City")


#============= Layout

app.layout = html.Div(
    children=[
        html.H1("Hello Dash")
    ]
)

