import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import math
import dash_table ##Para poder hacer tablas

def return_candidates_comparison(df_candidatos,return_home_button):
    
    #This script returns a div section containing the most relevant information about
    #three candidates previously select to comparison.
    
    #It contains: personal information, academic information and labo
    
    return html.Div([
                    #Fixed division to exhibit the candidates selected to comparison
                    html.Div([
                        #button to return to the comparison menu
                        return_home_button,
                        html.Br(),
                        
                        #card to show the name of the three candidates selected to comparison
                        dbc.Row([
                            dbc.Col(
                            dbc.Card([                                
                                    dbc.CardGroup([
                                        dbc.Card(dbc.CardBody([html.H5(df_candidatos.loc[0,'nombre'], className="card-title")]), color="dark", outline=True),
                                        dbc.Card(dbc.CardBody([html.H5(df_candidatos.loc[1,'nombre'], className="card-title")]), color="dark", outline=True),
                                        dbc.Card(dbc.CardBody([html.H5(df_candidatos.loc[2,'nombre'], className="card-title")]), color="dark", outline=True),
                                    ])
                                ]),#,style={'width':'100%'})
                                width={"size": 8, "offset": 2},
                                )
                            ])
                        ], style={"position":"fixed", 'top': '0','zIndex': '2147483647', 'backgroundColor':'white', 'width': '100%'}),#,'margin' : '0 0 0 -20px'}), #, 'color':'white', 'width': '100%'}),#
      
                    #,'padding-left':'10%','padding-right':'10%'
                    
                    
                    #Intentionally spaces to better visualization
                    
                    html.Div([html.Br()]),
                    html.Div([html.Br()]),
                    html.Div([html.Br()]),
                    
                    
                    #First section about personal information
                    
                    dbc.Row([
                        dbc.Col(
                        dbc.Card([
                            dbc.CardGroup([   
                                #card containing the personal information about the first candidate
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H5(df_candidatos.loc[0,'nombre'], className="card-title"),
                                            html.P(children=[html.B("Age: "), str(df_candidatos.loc[0,'edad'])+str(' años')], className="card-subtitle"),
                                            html.P(children=[html.B("Civil Status: "), df_candidatos.loc[0,'estado_civil']], className="card-subtitle"),                                        
                                            html.P(children=[html.B("Driving License: "), "No information" if math.isnan(df_candidatos.loc[0,'licencia_conduccion']) else df_candidatos.loc[0,'licencia_conduccion']], className="card-subtitle"),                                        
                                            html.P(children=[html.B("City: "), df_candidatos.loc[0,'localizacion']], className="card-subtitle"),
                                            html.P(children=[html.B("Languages: "), ' '.join([df_candidatos.loc[0,'idioma'+str(x)]+' ' for x in range(1,6) if str(df_candidatos.loc[0,'idioma'+str(x)])!='0'])], className="card-subtitle"),
                                        ]
                                    ), color="info", outline=True
                                ),
                                #card containing the personal information about the second candidate
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H5(df_candidatos.loc[1,'nombre'], className="card-title"),
                                            html.P(children=[html.B("Age: "), str(df_candidatos.loc[1,'edad'])+str(' años')], className="card-subtitle"),
                                            html.P(children=[html.B("Civil Status: "), df_candidatos.loc[1,'estado_civil']], className="card-subtitle"),                                        
                                            html.P(children=[html.B("Driving License: "), "No information" if math.isnan(df_candidatos.loc[1,'licencia_conduccion']) else df_candidatos.loc[1,'licencia_conduccion']], className="card-subtitle"),                                        
                                            html.P(children=[html.B("City: "), df_candidatos.loc[1,'localizacion']], className="card-subtitle"),
                                            html.P(children=[html.B("Languages: "), ' '.join([df_candidatos.loc[1,'idioma'+str(x)]+' ' for x in range(1,6) if str(df_candidatos.loc[1,'idioma'+str(x)])!='0'])], className="card-subtitle"),
                                        ]
                                    ), color="info", outline=True
                                ),
                                #card containing the personal information about the third candidate
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H5(df_candidatos.loc[2,'nombre'], className="card-title"),
                                            html.P(children=[html.B("Age: "), str(df_candidatos.loc[2,'edad'])+str(' años')], className="card-subtitle"),
                                            html.P(children=[html.B("Civil Status: "), df_candidatos.loc[2,'estado_civil']], className="card-subtitle"),                                        
                                            html.P(children=[html.B("Driving License: "), "No information" if math.isnan(df_candidatos.loc[2,'licencia_conduccion']) else df_candidatos.loc[2,'licencia_conduccion']], className="card-subtitle"),                                        
                                            html.P(children=[html.B("City: "), df_candidatos.loc[2,'localizacion']], className="card-subtitle"),
                                            html.P(children=[html.B("Languages: "), ' '.join([df_candidatos.loc[2,'idioma'+str(x)]+' ' for x in range(1,6) if str(df_candidatos.loc[2,'idioma'+str(x)])!='0'])], className="card-subtitle"),
                                        ]
                                    ), color="info", outline=True
                                ),
                                ])
                            ]),
                            width={"size": 8, "offset": 2},
                            )
                        ]),
                    
                    
                    html.Br(),
                    
                    #Second section: academic information
                    dbc.Row([
                        dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Academic Information", style={'text-align': 'center'}),
                        dbc.CardGroup([
                            
                                dbc.Card([
                                        
                                        dbc.CardBody(
                                            [
                                                html.Div([
                                                        html.H5(children=[html.B("Institution: "),df_candidatos.loc[0,'lugar_formacion'+str(i)]],className="card-title"),
                                                        html.P(children=[html.B("Area: "), df_candidatos.loc[0,'area_formacion'+str(i)] if df_candidatos.loc[0,'area_formacion'+str(i)]!='0' else "No information"],className="card-subtitle"),
                                                        html.P(children=[html.B("Degree: "),df_candidatos.loc[0,'descripcion_formacion'+str(i)] if df_candidatos.loc[0,'descripcion_formacion'+str(i)]!='0' else "No information"]),
                                                        html.Hr()
                                                    ])                                        
                                                for i in range(1,6) if str(df_candidatos.loc[0,'lugar_formacion'+str(i)])!='0'    
                                            ]
                                        )], color="secondary", outline=True
                                    ),
                                    
                            
                                dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div([
                                                        html.H5(children=[html.B("Institution: "),df_candidatos.loc[1,'lugar_formacion'+str(i)]],className="card-title"),
                                                        html.P(children=[html.B("Area: "), df_candidatos.loc[1,'area_formacion'+str(i)] if df_candidatos.loc[1,'area_formacion'+str(i)]!='0' else "No information"],className="card-subtitle"),
                                                        html.P(children=[html.B("Degree: "),df_candidatos.loc[1,'descripcion_formacion'+str(i)] if df_candidatos.loc[1,'descripcion_formacion'+str(i)]!='0' else "No information"]),
                                                        html.Hr()
                                                    ])                                        
                                                for i in range(1,6) if str(df_candidatos.loc[1,'lugar_formacion'+str(i)])!='0'    
                                            ]
                                        ), color="secondary", outline=True
                                        #style={"width": "18rem"},
                                    ),
                                    
                            
                                dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div([
                                                        html.H5(children=[html.B("Institution: "),df_candidatos.loc[2,'lugar_formacion'+str(i)]],className="card-title"),
                                                        html.P(children=[html.B("Area: "), df_candidatos.loc[2,'area_formacion'+str(i)] if df_candidatos.loc[2,'area_formacion'+str(i)]!='0' else "No information"],className="card-subtitle"),
                                                        html.P(children=[html.B("Degree: "),df_candidatos.loc[2,'descripcion_formacion'+str(i)] if df_candidatos.loc[2,'descripcion_formacion'+str(i)]!='0' else "No information"]),
                                                        html.Hr()
                                                    ])                                        
                                                for i in range(1,6) if str(df_candidatos.loc[2,'lugar_formacion'+str(i)])!='0'    
                                            ]
                                        ), color="secondary", outline=True
                                        #style={"width": "18rem"},
                                    ),
                                    
                                
                            
                            ]),
                        ], color='secondary', outline=True), #, style={'text-align': 'center'}                    
                            width={"size": 8, "offset": 2},
                            )
                        ]),
                    
                    html.Br(),
                    dbc.Row([
                        dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Work experience", style={'text-align': 'center'}),
                        dbc.CardGroup([
                            
                                dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div([
                                                        html.H5(df_candidatos.loc[0,'nombre_trabajo'+str(i)],className="card-title"),
                                                        html.P(children=[html.B("Company: "), df_candidatos.loc[0,'lugar_trabajo'+str(i)].split('/')[0] if df_candidatos.loc[0,'lugar_trabajo'+str(i)]!='0' else "No information"]),#className="card-subtitle"),
                                                        html.P(children=[html.B("Period: "),df_candidatos.loc[0,'tiempo_trabajo'+str(i)]]),#className="card-subtitle"),
                                                        html.P(children=[html.B("Description: "),df_candidatos.loc[0,'descripcion_trabajo'+str(i)] if df_candidatos.loc[0,'descripcion_trabajo'+str(i)]!='0' else "No information"]),#,className="card-subtitle"),                                              
                                                        html.Hr()
                                                    ])                                        
                                                for i in range(1,6) if str(df_candidatos.loc[0,'nombre_trabajo'+str(i)])!='0' 
                                            ]
                                        ), color="danger", outline=True
                                        #style={"width": "18rem"},
                                    ),
                                    
                            
                                dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div([
                                                        html.H5(df_candidatos.loc[1,'nombre_trabajo'+str(i)],className="card-title"),
                                                        html.P(children=[html.B("Company: "), df_candidatos.loc[1,'lugar_trabajo'+str(i)].split('/')[0] if df_candidatos.loc[1,'lugar_trabajo'+str(i)]!='0' else "No information"]),#className="card-subtitle"),
                                                        html.P(children=[html.B("Period: "),df_candidatos.loc[1,'tiempo_trabajo'+str(i)]]),#className="card-subtitle"),
                                                        html.P(children=[html.B("Description: "),df_candidatos.loc[1,'descripcion_trabajo'+str(i)] if df_candidatos.loc[1,'descripcion_trabajo'+str(i)]!='0' else "No information"]),#,className="card-subtitle"),                                              
                                                        html.Hr()
                                                    ])                                        
                                                for i in range(1,6) if str(df_candidatos.loc[1,'nombre_trabajo'+str(i)])!='0' 
                                            ]
                                        ), color="danger", outline=True
                                        #style={"width": "18rem"},
                                    ),
                                    
                            
                                dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.Div([
                                                        html.H5(df_candidatos.loc[2,'nombre_trabajo'+str(i)],className="card-title"),
                                                        html.P(children=[html.B("Company: "), df_candidatos.loc[2,'lugar_trabajo'+str(i)].split('/')[0] if df_candidatos.loc[2,'lugar_trabajo'+str(i)]!='0' else "No information"]),#className="card-subtitle"),
                                                        html.P(children=[html.B("Period: "),df_candidatos.loc[2,'tiempo_trabajo'+str(i)]]),#className="card-subtitle"),
                                                        html.P(children=[html.B("Description: "),df_candidatos.loc[2,'descripcion_trabajo'+str(i)] if df_candidatos.loc[2,'descripcion_trabajo'+str(i)]!='0' else "No information"]),#,className="card-subtitle"),                                              
                                                        html.Hr()
                                                    ])                                        
                                                for i in range(1,6) if str(df_candidatos.loc[2,'nombre_trabajo'+str(i)])!='0' 
                                            ]
                                        ), color="danger", outline=True
                                        #style={"width": "18rem"},
                                    ),
                                    
                                
                            
                            ])
                        ], color='danger', outline=True),
                            width={"size": 8, "offset": 2},
                            )
                        ]),
                    
                    
                
                
                    ])
        #style={'top': '0', 'backgroundColor':'white', 'width': '70%'}),#,'margin' : '0 0 0 -20px'}), #, 'color':'white', 'width': '100%'})
                    
                
            