# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:54:01 2019

@author: Nitin
"""

# Import Necessary Libraries related to HTML tags and various core components like slider, checboxes, dropdowns etc.
import dash
import dash_html_components as html
import dash_core_components as dcc

#Code to start an application
app = dash.Dash()

#HTML layout and Graph components are defined in this section
app.layout = html.Div(children=[html.H1(children='Sample Dash Web App Dashboard'),
                                
  #-----------------------
                                html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Item:'),
                        dcc.Checklist(
                                id = 'Item_List',
                                options=[
                                    {'label': 'Bread', 'value': 'Bread'},
                                    {'label': 'Milk', 'value': 'Milk'},
                                    {'label': 'Sugar', 'value': 'Sugar'}
                                ],
                                values=['Bread', 'Milk', 'Sugar'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),
#-----------------------
                                
                                html.Div(children = '''Dash: A web based app to show Bar Graph'''),
                                dcc.Graph(id='dash_graph',

),
                                dcc.Graph(id='dash_graph_2',
                                          figure = {'data': [{'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'bar', 'name':'Aeroplane'},
                                          {'x':[1,2,3,4,5], 'y':[9,3,1,9,4], 'type': 'bar', 'name':'Car'},
                                          {'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'line', 'name':'Train'},],
                                        'layout':{'title': 'Dash Example App 2'}
} 
)
                                ])
                            

@app.callback(
    dash.dependencies.Output('dash_graph', 'figure'),
    [dash.dependencies.Input('Item_List', 'values')])
def update_graph(selector):
    data = []
    if 'Bread' in selector:
        data.append({'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'bar', 'name':'Bread'})
    if 'Milk' in selector:
        data.append({'x':[1,2,3,4,5], 'y':[9,3,1,9,4], 'type': 'bar', 'name':'Milk'})
    if 'Sugar' in selector:
        data.append({'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'bar', 'name':'Sugar'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Item Graph',
            'xaxis' : dict(
                title='X-Axis',
                titlefont=dict(
                family='Calibri, monospace',
                size=20,
                color='#3FFF33'
            )),
            'yaxis' : dict(
                title='Y-Axis',
                titlefont=dict(
                family='Garamond, monospace',
                size=20,
                color='#F9FF33'
            ))
        }
    }
    return figure

#Code to run the application
if __name__ == '__main__':
    app.run_server(debug = True)