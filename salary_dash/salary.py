import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('/Users/martinalexandersson/Dev/lon/2017/pandas/af_data.csv',sep=';')
years = df['year'].unique()

app.layout = html.Div([

    html.H1(children='Akademikerföreningens lönestatistik 2018'),


    dcc.Graph(
        id='salary_history',
        figure={
            'data': [
                go.Scatter(
                    x=df_person['year'],
                    y=df_person['salary'],

                    text=namn,
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=namn
                ) for namn,df_person in df.groupby('Namn')
            ],

            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'År'},
                yaxis={'title': 'Lön'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
        ),

    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].max(),
        step=None,
        marks={str(year): str(year) for year in years}
    ),

    dcc.Graph(id='sallary_year')


])

@app.callback(
    dash.dependencies.Output('sallary_year', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    year_groups = df.groupby('year')
    df_year = year_groups.get_group(selected_year)

    line = go.Scatter(
        x=df_year['Examen'],
        y=df_year['salary'],
        text=selected_year,
        mode='markers',
        opacity=0.7,
        marker={
            'size': 15,
            'line': {'width': 0.5, 'color': 'white'}
        },
        name=selected_year)
    lines = [line]

    return {
        'data': lines,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Examensår'},
            yaxis={'title': 'Lön'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()