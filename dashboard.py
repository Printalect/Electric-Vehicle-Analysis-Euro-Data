# importing libs
import os
import pandas as pd
import fastparquet
import plotly.express as px
# Dash libs
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# vis variables
# import plotly.io as pio
# pio.templates.default = 'seaborn'

color1 = '#cccccc'
color2 = '#858585'
color3 = '#5d5d5d'

color4 = '#cc0000'
color5 = '#e82127'
color6 = '#c01419'
color7 = '#ab2e32'

color8 = '#333333'
color9 = '#000000'

# enlarge the notebook
# from IPython.core.display import display, HTML
# display(HTML("<style>.container { width:95% !important; } </style>"))
#-------------------------
#-SECTION - row one
#--------------------------------------------------
catcol_select = sorted(['CarBody', 'FastchargePort', 'Segment'])

numcol_select = sorted([
    'RoofLoad', 'Width', 'FastchargePowerMax', 'Wheelbase', 'Length',
    'ChargePower', 'VehicleFuelEquivalent', 'TurningCircle', 'CargoVolumeMax',
    'TowingWeightUnbraked', 'MaxPayload', 'CargoVolume', 'VehicleConsumption',
    'TowingWeightBraked', 'Seats', 'RatedConsumption', 'Height', 'Range',
    'ChargeSpeed', 'Acceleration', 'TopSpeed', 'RatedFuelEquivalent',
    'BatteryCapacity', 'BatteryUseable', 'FastchargeSpeed', 'TotalPower',
    'TotalTorque', 'WeightUnladen', 'GrossVehicleWeight', 'ElectricRange'
])
# setting required variables
header_styling = {
    #      'width': '100%',
    'display': 'grid',
    'align-items': 'center',
    'justify-content': 'center',
    'align-self': 'auto'
}

dropdown_style_options = {
    'display': 'flex',
    'align-items': 'center',
    'justify-content': 'center',
}

child_inherit = {'display': 'inherit'}
#-------------------------
#-SECTION - row one
#--------------------------------------------------
fileurlraw = 'https://raw.githubusercontent.com/Printalect/Electric-Vehicle-Dashboard-Euro/master/assets/ev_rawdata.parquet.gzip'
rawdata = pd.read_parquet(fileurlraw)
#-------------------------
#-------------------------
# #DEBUGGING BREAK#
#  ADDING FIGURES
#-------------------------
#-------------------------
#-SECTION - row one
#--------------------------------------------------
header_main = dbc.Col([
    dbc.Row(html.H1('Electric Vehicle Models - 2020 European Market'),
            justify='center'),
    dbc.Row(html.H6('Review electric vehicle model specifications'),
            justify='center'),
])

#-----------
header_pie = dbc.Row(
    [html.H3('Charts: Manufacturer, Model, & Category - Tesla')],
    justify='center')
header_treemaps = dbc.Row(
    [html.H3('Charts: Manufacturer, Model, & Category Plus Range ')],
    justify='center')
header_scatter = dbc.Col([
    dbc.Row(html.H3('Charts:Price Review by Specifications - Tesla-Yes/No'),
            justify='center'),
    dbc.Row(html.P(
        'Cross compare current models by specifications like range, price, speed, and acceleration.'
    ),
            justify='center')
])
#-------------------------
#-SECTION - row one
#--------------------------------------------------
firstrow = html.Div([
    dbc.Row(
        [
            # COLUMN: 1
            dbc.Col(
                [
                    # PIE PLOT 1
                    #                     dbc.Row(html.P(' '), justify='center'),
                    dbc.Row(dcc.Graph(id='pie_plot_1')),
                ],
                width=6),
            # COLUMN: 2
            dbc.Col(
                [
                    # PIE PLOT 1
                    dbc.Row([dcc.Graph(id='treemap_1')],
                            style={'display': 'grid'})
                ],
                width=6),
        ],
        "style={'height': '800px'}")
])
#-----------
# Build App
firstrow_sel = html.Div([
    dbc.Row([
        html.Label([
            "Select Category:",
            dcc.Dropdown(id='categorical_dropdown',
                         clearable=False,
                         value=catcol_select[0],
                         options=[{
                             'label': c,
                             'value': c
                         } for c in catcol_select],
                         style={'width': '300px'})
        ]),
    ],
            style=dropdown_style_options),
    dbc.Row(html.P('(Selector for 4 subsequent illustrations.)'),
            justify='center'),
    dbc.Row(html.P('Left:Category & Model, Right: Category & Manufacturer'),
            justify='center'),
])
#-------------------------
#-SECTION - row two
#--------------------------------------------------
secondrow = html.Div([
    #     dbc.Row(html.P(
    #         'The graphs below replicate the information above, yet also add a visual scale for range.'
    #     ),
    #             justify='center'),
    dbc.Row([

        # COLUMN: 1
        dbc.Col([
            dbc.Row([dcc.Graph(id='pie_plot_2')]),
        ], width=6),
        # COLUMN: 2
        dbc.Col([
            dbc.Row([dcc.Graph(id='treemap_2')], style={'display': 'grid'}),
        ],
                width=6),
    ])
])
#-------------------------
#-SECTION - row four
#--------------------------------------------------
forthrow = dbc.CardBody([
    dbc.Row([
        dbc.Col([
            dbc.Row(dcc.Graph(id='scatterplot_1'), style={'display': 'grid'}),
            dbc.Row(html.P('Note: Data Uses Metric System. (km, km/h, mm, m, etc.)'))
        ]),
        dbc.Col([
            dbc.Row(dcc.Graph(id='scatterplot_2'), style={'display': 'grid'}),
        ])
    ])
])
#-----------
# Build App
numerical_sel1 = dbc.CardBody([
    dbc.Row([
        dbc.Col(html.Label([
            "Select by Value:",
            dcc.Dropdown(id='numerical_dropdown1',
                         clearable=False,
                         value='Range',
                         options=[{
                             'label': c,
                             'value': c
                         } for c in numcol_select],
                         style={'width': '300px'})
        ]),
                style=dropdown_style_options),
        dbc.Col(html.Label([
            "Select by Value:",
            dcc.Dropdown(id='numerical_dropdown2',
                         clearable=False,
                         value='Range',
                         options=[{
                             'label': c,
                             'value': c
                         } for c in numcol_select],
                         style={'width': '300px'})
        ]),
                style=dropdown_style_options)
    ])
])
#-------------------------
#-SECTION - blank row
#--------------------------------------------------
# sourcelinks = html.Div([
#     dbc.Row([
#         dbc.Col(html.Div(
#             html.A('Data Source (click)', href=sourcelink, target='_blank')),
#                 style=dropdown_style_options),
#     ])
# ])

blankrow = html.Div([dbc.Row([html.Br()])], style={'marginBottom': '1.5em'})
#-------------------------
#-------------------------
# #DEBUGGING BREAK#
#  ADDING FIGURES
#-------------------------
#-------------------------
#-SECTION -
#--------------------------------------------------
#app = JupyterDash(__name__, external_stylesheets=[dbc.themes.LUX])
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
#-------------------------
#-SECTION -
#--------------------------------------------------
# second pieplot
@app.callback(Output('pie_plot_1', 'figure'),
              [Input('categorical_dropdown', 'value')])
#-----------
def pie_plot_1(attribute2):
    plotdata = rawdata.sort_values('Tesla')
    fig = px.sunburst(plotdata,
                      path=[str(attribute2), 'Model'],
                      color='Tesla',
                      color_discrete_sequence=[color1, color6],
                      height=800,
                      title=('Category: {}').format(attribute2))
    return\
        fig.update_layout(showlegend=False)
#-----------
# first pieplot
@app.callback(Output('pie_plot_2', 'figure'),
              [Input('categorical_dropdown', 'value')])
#-----------
def pie_plot_2(attribute='value'):
    plotdata = rawdata.sort_values('Range')
    fig = px.sunburst(
        plotdata,
        path=[attribute, 'Model'],
        color='Range',
        color_continuous_scale=[color1, color3],
        #          color_continuous_scale=px.colors.sequential.Greys,
        title=('Category:{}').format(attribute),
        height=800,
    ).update_traces(opacity=0.9)
    return\
        fig
#-------------------------
#-SECTION -
#--------------------------------------------------
# first treemap
@app.callback(Output('treemap_1', 'figure'),
              [Input('categorical_dropdown', 'value')])
#-----------
def treemap_1(attribute):
    plotdata = rawdata.sort_values('Tesla')
    fig = px.treemap(plotdata,
                     path=[str(attribute), 'Manufacturer'],
                     color='Tesla',
                     hover_data=['Manufacturer', attribute],
                     color_discrete_sequence=[color1, color6],
                     height=800,
                     title=('Category:{}').format(attribute))
    return\
        fig
#-----------
# first treemap
@app.callback(Output('treemap_2', 'figure'),
              [Input('categorical_dropdown', 'value')])
#-----------
def treemap_2(attribute='value'):
    plotdata = rawdata.sort_values('Range')
    fig = px.treemap(plotdata,
                     path=[attribute, 'Manufacturer'],
                     color='Range',
                     hover_data=['Manufacturer', attribute],
                     color_continuous_scale=[color1, color3],
                     title=('Category:{}').format(attribute),
                     height=800)  #.update(layout_showlegend=False)
    return\
        fig#.update(showlegend=False)
#-----------
# scatterplot
@app.callback(Output('scatterplot_1', 'figure'),
              [Input('numerical_dropdown1', 'value')])
#-----------
def scatterplot_1(attribute='value'):
    fig = px.scatter(
        rawdata,
        x=attribute,
        y='PriceAVG',
        color='Tesla',
        symbol='CarBody',
        hover_data=['Manufacturer', 'Model', 'CarBody', 'Segment', 'PriceAVG'],
        color_discrete_sequence=(color6, color2),
        opacity=0.7,
        title=('Attribute:{}').format(attribute),
        height=600)
    return\
        fig
#-----------
# scatterplot
@app.callback(Output('scatterplot_2', 'figure'),
              [Input('numerical_dropdown2', 'value')])
#-----------
def scatterplot_2(attribute='value'):
    fig = px.scatter(
        rawdata,
        x=attribute,
        y='PriceAVG',
        color='Tesla',
        symbol='CarBody',
        hover_data=['Manufacturer', 'Model', 'CarBody', 'Segment', 'PriceAVG'],
        color_discrete_sequence=(color6, color2),
        opacity=0.7,
        title=('Attribute:{}').format(attribute),
        height=600)
    return\
        fig
#-------------------------
#-------------------------
# #DEBUGGING BREAK#
#  RUN DASHBOARD
#-------------------------
#-------------------------
#-SECTION -
#--------------------------------------------------
app.layout = dbc.Card([
    dbc.CardBody([header_main, blankrow]),
    dbc.CardBody([
        header_pie,
        firstrow_sel,
        firstrow,
        blankrow,
        blankrow,
#         header_treemaps,
        secondrow,
        blankrow,
#         thirdrow,
        blankrow,
    ]),
    dbc.CardBody([header_scatter, numerical_sel1, forthrow, blankrow]),
],  color="secondary", outline=True)
#-----------
# app.run_server(debug=True, mode='external', 
#                port=8102
#               )

if __name__ == '__main__':
    app.run_server(debug=False, port=8901)
#-------------------------
