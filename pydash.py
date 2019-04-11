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
                                html.Div(children = '''Dash: A web based app to show Bar Graph'''),
                                dcc.Graph(id='dash_graph',
                                          figure = {'data': [{'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'bar', 'name':'Bread'},
                                          {'x':[1,2,3,4,5], 'y':[9,3,1,9,4], 'type': 'bar', 'name':'Milk'},
                                          {'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'line', 'name':'Sugar'},],
                                        'layout':{'title': 'Dash Example App'}
} 
),
                                dcc.Graph(id='dash_graph 2',
                                          figure = {'data': [{'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'bar', 'name':'Aeroplane'},
                                          {'x':[1,2,3,4,5], 'y':[9,3,1,9,4], 'type': 'bar', 'name':'Car'},
                                          {'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'line', 'name':'Train'},],
                                        'layout':{'title': 'Dash Example App 2'}
} 
)
                                ])
                                
#Code to run the application
if __name__ == '__main__':
    app.run_server(debug = True)