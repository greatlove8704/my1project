import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import datetime
from dash.dependencies import Output, Input, State
import functions
import pickle
import plotly.express as px
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
from sklearn.metrics import r2_score


from datetime import date
from dateutil.relativedelta import relativedelta
next_year = date.today() + relativedelta(years=1)


model = pickle.load(open('random_model.pkl', 'rb'))
df = pd.read_csv('df.csv')
test_df = pd.read_csv('test_data.csv')
# print(test_df)

airlines = ['Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Vistara',
            'Other']
source = ['Bangalore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai']
destination = ['Bangalore', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi']
f_class = ['Business', 'First', 'Economy']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
server = app.server
app.title = 'Flight Price Prediction'
app._favicon = "fevicon.ico"

app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(html.A([dbc.CardImg(src='assets/sk2.png', style={'width': '70px', 'height': '30px'}
                                            , className='mx-5 my-1')],
                               )),
            dbc.NavItem(dbc.NavLink(html.A("Predict", href="#", className="me-1 text-decoration-none fs-5"))),
            dbc.NavItem(dbc.NavLink(html.A("Model", href="#model-report", className="me-1 text-decoration-none fs-5"))),
            dbc.NavItem(dbc.NavLink(html.A("Analysis", href="#eda", className="me-1 text-decoration-none fs-5"))),
            
            
            
        ], fixed='top',
        brand="Flight Price Prediction Dashboard",
        brand_href="#",
        color="primary",
        dark=True, className='py-0'),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([html.H1("Predict Flight Ticket Price",style={'text-align':'center'})]),
    html.Br(),
    html.Br(),



    dbc.Row([
        functions.input_field('Airline', 'airline-dpn', 'Select Airline', airlines, offset=1),
        functions.input_field('Source', 'source-dpn', 'Select Source', source),
        functions.input_field('Destination', 'dest-dpn', 'Select Destination', destination),
        functions.input_field('Stops', 'stops-dpn', 'Select Stops', [0, 1, 2, 3, 4], offset=0),
    ], justify='center'),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col([html.Header('Date of Journey'),
                 dcc.DatePickerSingle(
                     id='doj',
                     placeholder='dd-mm-yyyy',
                     # min_date_allowed=datetime.date.today(),
                     min_date_allowed=datetime.date.today(),
                     max_date_allowed=next_year,
                     initial_visible_month=datetime.date.today(),
                     # date=datetime.date.today()
                 )
                 ], xl={'size': 2, 'offset': 1}, lg={'size': 2, 'offset': 1}, md={'size': 2, 'offset': 1},
                sm={'size': 12, 'offset': 1}, xs={'size': 12, 'offset': 1}, style={'text-align': 'center'}),

        dbc.Col([html.Header('Departure Time(HH:MM)'),
                 functions.time_select('dhour_dpdn', 'dmin_dpdn')
                 ], xl={'size': 2, 'offset': 1}, lg={'size': 2, 'offset': 1}, md={'size': 2, 'offset': 1},
                sm={'size': 6, 'offset': 1}, xs={'size': 6, 'offset': 1}, style={'text-align': 'center'}),

        dbc.Col([html.Header('Travel Time (HH:MM)'),
                 functions.time_select('thour_dpdn', 'tmin_dpdn')
                 ], xl={'size': 2, 'offset': 1}, lg={'size': 2, 'offset': 1}, md={'size': 2, 'offset': 1},
                sm={'size': 6, 'offset': 1}, xs={'size': 6, 'offset': 1}, style={'text-align': 'center'}),

        functions.input_field('Class', 'class_dpdn', 'Select Class', f_class),

    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dbc.Button('Predict', id='btn', n_clicks=0),
            # dbc.Button('Reset', id='reset-btn', n_clicks=0,class_name='mx-2')
        ], width=3, style={'text-align': 'center'})

    ], justify='center', className='my-5'),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div(id='container-button-basic',  # displaying predicted price here
                         children='', className='fs-3'),
            ])
        ], width=12, style={'text-align': 'center'})
    ], justify='center', className='my-5'),
html.Br(),
html.Br(),
html.Br(),
    dbc.Row([
        dbc.Card([
            html.H3('Model Prediction Report'),
        ], style={'text-align': 'center'})
    ], justify='center', id='model-report'),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Label("Model: Random Forest Regressor", className='fs-5'),
            dcc.RadioItems(['Accuracy Score', 'Feature Importance','Histogram', 'KDE', 'Scatter-plot'], 'Accuracy Score',
                           id='result-radio'),
            html.Br(),
            dcc.Graph(id='result-graph', figure={})
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),

    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Card([
            html.H3('Data Analysis Report')
        ], style={'text-align': 'center'})
    ], justify='center', id='eda'),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H4('Analysis of Categorical Features'),
            dcc.RadioItems(['Airline', 'Source', 'Destination', 'Day Name', 'Month Name', 'Total_Stops'], 'Airline',
                           id='bar-radio'),
            html.Br(),
            dcc.Graph(id='bar-graph', figure={})
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([

        dbc.Col([
            html.H4('Analysis of Numerical Features'),
            html.Label('X-Axis:'),
            dcc.RadioItems(
                ['Arrival_Time', 'Day of Month', 'Week of Year', 'Duration', 'Departure_Time', 'Price', 'Total_Stops'],
                'Price', id='hist-radio'),
            html.Label('Color:'),
            dcc.RadioItems(['None', 'Airline', 'Day Name', 'Month Name', 'Total_Stops'], 'None', id='hist2-radio'),
            html.Br(),
            dcc.Graph(id='hist-graph', figure={})
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),

    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H4('Box plot(Outlier detection) of Price'),
            dcc.RadioItems(['Airline', 'Day Name', 'Month Name', 'Total_Stops'], 'Airline', id='box-radio'),
            html.Br(),
            dcc.Graph(id='box-graph', figure={})
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),

    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H4('More way to visualize Numerical Features'),
            dbc.Row([
                dbc.Col([
                    html.Label('Y-Axis'),
                    dcc.Dropdown(
                        sorted(['Arrival_Time', 'Duration', 'Departure_Time', 'Day of Month', 'Week of Year', 'Price']),
                        'Duration', id='scat-ydrop', style={'color': 'black'}),
                ]),
                dbc.Col([
                    html.Label('Color'),
                    dcc.Dropdown(sorted(['Airline', 'Source', 'Destination', 'Total_Stops', 'Month Name', 'Day Name']),
                                 'Airline', id='scat-cdrop', style={'color': 'black'}),
                ]),
                dbc.Col([
                    html.Label('Size'),
                    dcc.Dropdown(sorted(['Price', 'Total_Stops', 'Day of Month']), 'Price', id='scat-sdrop',
                                 style={'color': 'black'}),
                ])]),

            html.Br(),
            dcc.Graph(id='scat-graph', figure={})
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),

    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H4('Comparing two Categorical Features'),
            dbc.Row([
                dbc.Col([
                    html.Label('Y-Axis'),
                    dcc.Dropdown(sorted(
                        ['Airline', 'Source', 'Destination', 'Month Name', 'Day Name', 'Week of Year', 'Total_Stops',
                         'Month']), 'Month', id='heat-ydrop', style={'color': 'black'}),
                ]),
                dbc.Col([
                    html.Label('X-Axis'),
                    dcc.Dropdown(sorted(
                        ['Airline', 'Source', 'Destination', 'Month Name', 'Day Name', 'Week of Year', 'Total_Stops',
                         'Month']), 'Week of Year', id='heat-xdrop', style={'color': 'black'}),
                ]),
                html.Br(),
                dcc.Graph(id='heat-graph', figure={})])
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),

    html.Br(),
    html.Br(),
    dbc.Row([
        html.Div(id='empty'),
        dbc.Col([
            html.H4('Airport in Map'),
            html.Br(),
            dcc.Graph(id='map-graph', figure={})
        ], width={'size': 10, 'offset': 1}, style={'text-align': 'center'}),
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                html.Label('Thanks for visitng...', className='me-1 text-decoration-none fs-5 fs-3'), ]),
            ], style={'text-align': 'center'})
    ], justify='center', id='about')

], fluid=True)


@app.callback(
    Output('container-button-basic', 'children'),
    Input('btn', 'n_clicks'),
    State('airline-dpn', 'value'),  # v
    State('source-dpn', 'value'),  # v2
    State('dest-dpn', 'value'),  # v3
    State('stops-dpn', 'value'),  # v4
    State('doj', 'date'),  # v5
    State('dhour_dpdn', 'value'),  # v6
    State('dmin_dpdn', 'value'),  # v7
    State('thour_dpdn', 'value'),  # v8
    State('tmin_dpdn', 'value'),  # v9
    State('class_dpdn', 'value'))  # 10
def update_output(n_clicks, v, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    if n_clicks == 0:
        return ''
    elif v == None or v2 == None or v3 == None or v4 == None or v5 == None or v6 == None or v7 == None or v8 == None or v9 == None or v10 == None:
        return 'All fields are Mandatory!'
    else:
        airline_list = functions.airlines(v)
        source_list = functions.source(v2)
        dest_list = functions.destination(v3)
        stops = [v4]
        month_day_week = functions.date_month_wk(v5)
        dep_hour_min = [v6, v7]
        duration_hour_min = [v8, v9]
        class_f = [functions.flight_class(v10)]
        arrival_hour_min = functions.get_arrival_time(v6, v7, v8, v9)

        input_data = stops + class_f + month_day_week + dep_hour_min + arrival_hour_min + duration_hour_min + airline_list + source_list + dest_list
        pred = model.predict(np.array(input_data).reshape(1, 28))

        return f"Predicted Price: VND {int(pred)}"







@app.callback(
    Output('bar-graph', 'figure'), Input('bar-radio', 'value'))
def update_bar(x):
    temp = df[x].value_counts().reset_index()
    fig = px.bar(data_frame=temp, x='index', y=x, color='index', template='plotly_dark',
                 labels={x: 'No of Reocrds', 'index': x})
    fig.update_layout(title_text=f'{x} and \ntheir records in data', title_x=0.5)
    return fig


@app.callback(
    Output('hist-graph', 'figure')
    , Input('hist-radio', 'value')
    , Input('hist2-radio', 'value'))
def update_histogram(x, y):
    color = ''
    if y == 'None':
        color = None
    else:
        color = y

    fig = px.histogram(df, x=x, marginal="box", color=color, template='plotly_dark', labels={'count': 'No of Records'})
    fig.update_layout(title_text=f'Historgram of {x}', title_x=0.5)
    return fig


@app.callback(
    Output('box-graph', 'figure'),
    Input('box-radio', 'value'),
)
def update_bar(x):
    fig = px.box(df, x=x, y="Price", color=x, template='plotly_dark')
    fig.update_layout(title_text=f'Box plot of Price wrt. {x}', title_x=0.5)
    return fig


@app.callback(
    Output('scat-graph', 'figure'),
    Input('scat-ydrop', 'value'),
    Input('scat-cdrop', 'value'),
    Input('scat-sdrop', 'value'),
)
def update_bar(y, color, size):
    y_label = ''
    if y == 'Arrival_Time': y_label = 'Arrival Time(in 24 hr format)'
    if y == 'Departure_Time':
        y_label = 'Departure Time(in 24 hr format)'
    elif y == 'Day of Month':
        y_label = 'Day of Month'
    elif y == 'Week of Year':
        y_label = 'Week of Year'
    elif y == 'Day of Month':
        y_label = 'Week of Year (1-31)'
    elif y == 'Duration':
        y_label = 'Duration (in hour)'
    elif y == 'Price':
        y_label = 'Price (in INR)'

    fig = px.scatter(df, x='Price', y=y, color=color, size=size, template='plotly_dark', labels={y: y_label})
    fig.update_layout(title_text=f'Scatter plot of Price wrt. {y}', title_x=0.5)
    return fig


@app.callback(
    Output('heat-graph', 'figure'),
    Input('heat-ydrop', 'value'),
    Input('heat-xdrop', 'value'),
)
def update_bar(x, y):
    d = pd.crosstab(df[x], df[y])
    fig = px.imshow(d, text_auto=True, origin='lower',
                    # color_continuous_scale='gray',
                    template='plotly_dark')
    fig.update_layout(title_text=f'Heatmap of <br> {x} and {y}', title_x=0.5)
    return fig


@app.callback(
    Output('map-graph', 'figure'),
    Input('empty', 'id'),
)
def update_bar(x):
    import plotly.graph_objects as go
    latitude = [13.1986, 12.9941, 17.2403, 22.6531, 19.0931, 10.1518, 17.2403, 28.5562]
    longitude = [77.7066, 80.1709, 78.4294, 88.4449, 72.8568, 76.3930, 78.4294, 77.1000]
    locations = ['Banglore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai', 'Cochin', 'Hydrabad', 'New Delhi']
    fig = go.Figure(go.Scattermapbox(
        mode="markers",
        lon=longitude,
        lat=latitude,
        text=locations,
        marker={'size': 15}))
    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={
            'center': {'lon': 78.9629, 'lat': 20.5937},
            'style': "stamen-terrain",
            'center': {'lon': 78.9629, 'lat': 20.5937},
            'zoom': 3})
    return fig



@app.callback(
    Output('result-graph', 'figure'),
    Input('result-radio', 'value'),
)
def update_bar(x):
    y_pred = model.predict(test_df.iloc[:, :-1].values)
    actual_val = test_df.iloc[:, -1]
    d = pd.DataFrame()
    d['Actual'] = pd.Series(actual_val).reset_index()['Price']
    d['Predicted'] = round(pd.Series(y_pred))
    hist_data = [d.Actual, d.Predicted]
    hist_data2 = d.Actual - d.Predicted
    group_labels = ['Actual', 'Predicted']
    colors = ['green', 'red']
    accuracy = round(r2_score(actual_val,y_pred)*100,1)

    if x == 'Accuracy Score':
        pio.templates.default = "plotly_dark"
        fig = go.Figure(go.Indicator(
            domain={'x': [0, 1], 'y': [0, 1]},
            value=accuracy,
            mode="gauge+number+delta",
            title={'text': "Accuracy %"},
            delta={'reference': 83},
            gauge={'axis': {'range': [None, 100]},
                   'steps': [
                       {'range': [0, 70], 'color': "lightgray"},
                       {'range': [70, 95], 'color': "gray"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 99}}))
        return fig

    elif x == 'Feature Importance':
        fi = pd.DataFrame(model.feature_importances_, index=test_df.iloc[:, :-1].columns).reset_index().sort_values(
            by=0).rename(
            columns={'index': 'feature', 0: 'value'})

        fig = px.bar(fi, x='feature', y='value', color='feature', template='plotly_dark')
        fig.update_layout(title_text='Feature Importance as per Random Forest Regressor', title_x=0.5)
        return fig
    elif x == 'Histogram':

        fig = px.histogram(x=hist_data2, marginal="rug", labels={'x':'Error Price'})
        fig.update_layout(title_text='Actual - Predicted Error', title_x=0.5)

        return fig
    elif x == 'KDE':
        pio.templates.default = "plotly_dark"
        fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)
        fig.update_layout(title_text='Actual vs Predicted Result on Test data', title_x=0.5)
        return fig
    elif x == 'Scatter-plot':
        fig2 = px.scatter(d, x='Actual', y='Predicted')
        fig2.update_layout(title_text='Scatter plot of Actual vs Predicted Result on Test data', title_x=0.5)
        return fig2


if __name__ == '__main__':
    # app.run_server(debug=True, host='0.0.0.0', port=8080)
    app.run_server(debug=True)
