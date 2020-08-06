import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots


import descriptions
import time

#### Inicializar página
################

##Default offer
default_offer = "Se requiere cajero con experiencia como administrador de tienda con funciones que incluyen, pero no se limitan a arqueo, conteo de dinero, manejo de datáfono y gestión de la nómina. Horario de 7 am a 6 pm lunes a sábados con día compensatorio" 


text_area = dbc.Textarea(style = {"height": "150px"},id="text-area",value = default_offer)

text_input2 = dbc.FormGroup(
    [
        dbc.Label("Insert the job offer and role description. Make sure that your description specifies what you look for in a candidate"),
        text_area
        
        
    ]
)

button = html.Div(
    [
        dbc.Button("Estimate category", id="load-descriptions-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)

button2 = html.Div(
    [
        dbc.Button("administrativo", id="label2-button", className="mr-2",color="light"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)

button3 = html.Div(
    [
        dbc.Button("cajero", id="label3-button", className="mr-2", color="primary"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)

button4 = html.Div(
    [
        dbc.Button("", id="label4-button", className="mr-2", color="primary"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)
power_button = daq.PowerButton(
        on=True
    )

div_button2 = dbc.Row([dbc.Col(button2),dbc.Col(power_button)])
div_button3 = dbc.Row([dbc.Col(button3),dbc.Col(power_button)])
div_button4 = dbc.Row([dbc.Col(button4),dbc.Col(power_button)])

results_panel = [button,div_button3]

            
            
            
        
        

####

### Falta este
def button_return_to_detail(return_button):
    return html.Div(
        [
            return_button,
            html.Span(id="example-output2", style={"vertical-align": "middle"}),
        ],
        style={"margin": "auto","width": "20%"}
    )


radio_exp_requerida = dbc.RadioItems(
                    id="exp-requerida-selector",
                    options=[
                        {"label": "Without experience", "value": True},
                        {"label": "with experience", "value": False}
                    ],
                    inline=True,
                )


radio_exp_unidad_tiempo = dbc.RadioItems(
                    id="exp-tiempo_unit-selector",
                    options=[
                        {"label": "Meses", "value": True},
                        {"label": "Años", "value": False}
                    ],
                    inline=True,
                )

#Layout


###Tabs
####

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Grupo 1"),
        dbc.Tab(tab2_content, label="Grupo 2"),
        dbc.Tab(
            "This tab's content is never seen", label="Grupo 3"
        ),
    ]
)


###Plots

### Score

def fig_score(df_candidatos):
    series_score = pd.cut(df_candidatos.score_total, bins=range(0,110,25), labels=[str(x)+'% - '+str(x+25)+'%' for x in range(0,100,25)]).value_counts().reset_index().sort_values(by='index')
    series_score.columns=['Range', 'Quantity']
    fig_score = px.bar(series_score, y='Range', x='Quantity',color='Range',height=300)
    fig_score.update_layout(title='Score', showlegend=False, hoverlabel=dict(
            bgcolor="white", 
            font_size=16, 
            font_family="Rockwell"
        )
    )
    fig_score.update_xaxes(title_text='Number of candidates')
    fig_score.update_yaxes(title_text='')
    return fig_score


### Age
def fig_age(df_candidatos):
    series_edad = pd.cut(df_candidatos.edad, bins=range(17,67,6), labels=[str(x+1)+' - '+str(x+6) for x in range(17,62,6)]).value_counts().reset_index().sort_values(by='index')
    series_edad.columns=['Range', 'Quantity']
    fig_edad = px.bar(series_edad, y='Range', x='Quantity',color='Range', orientation='h',height=300)
    fig_edad.update_layout(title='Age', showlegend=False, hoverlabel=dict(
            bgcolor="white", 
            font_size=16, 
            font_family="Rockwell"
        ))
        
    fig_edad.update_yaxes(title_text='Age ranges')
    fig_edad.update_xaxes(title_text='Number of candidates')
    return fig_edad


###Education
def fig_education(df_candidatos):
    fig_educacion = px.histogram(df_candidatos, y="max_nivel_educativo", orientation='h', height=300, 
                                title='Max nivel educativo', color="max_nivel_educativo",category_orders={"max_nivel_educativo":["niguno","EducaciónBásicaSecundaria","EducaciónMedia","Carreratécnica","Carreratecnológica","CarreraProfesional"]})
    fig_educacion.update_layout(title='Education', showlegend=False, hoverlabel=dict(
            bgcolor="white", 
            font_size=16, 
            font_family="Rockwell"
        ))
    fig_educacion.update_xaxes(title_text='Number of candidates')
    fig_educacion.update_yaxes(title_text='')
    return fig_educacion


###Work experience
def fig_experience(df_candidatos):
    bins_trabajo = [-1,0,6,12,24,36,60,1000]
    labels_trabajo = ['Sin experiencia', '1 a 6 meses', '6 meses a 1 año', '1 a 2 años', '2 a 3 años', '3 a 5 años', 'Más de 5 años']
    series_trabajo = pd.cut(df_candidatos.duracion_trabajo_total, bins=bins_trabajo, labels = labels_trabajo).value_counts().reset_index().sort_values(by='index')
    series_trabajo.columns=['Rango', 'Cantidad']
    fig_trabajo = px.bar(series_trabajo, y='Rango', x='Cantidad',color='Rango', orientation='h',height=300)
    fig_trabajo.update_layout(title='Work experience', showlegend=False, hoverlabel=dict(
            bgcolor="white", 
            font_size=16, 
            font_family="Rockwell"
        ))
    fig_trabajo.update_yaxes(title_text='Work experience time range')
    fig_trabajo.update_xaxes(title_text='Number of candidates')
    return fig_trabajo


###
# Define layout
###
def return_candidates_summary(df, return_home_from_summary):
    return [
        dbc.Row([
                dbc.Col([
                    html.Img(src='https://stg.candidatos.talentu.co/images/creacion_perfil.svg'),
                    html.H1("Profile creation "),
                    html.H5("You are one step away from finding your ideal candidate!"
                    " Please provide the following details about the offer:"),
                    html.Br(),
                    html.H2("Experience requirement"),
                    radio_exp_requerida,
                    html.Br(),
                    html.H2("Job description"),
                    text_input2,
                    ]+results_panel
                    , width=5
                ),
                dbc.Col(
                    [
                        html.H1("Candidates summary",style={"text-align":"center"}),
                        html.Br(),
                        html.H5("The characteristics of your candidates at a glance"),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(dcc.Graph(figure=fig_score(df))),
                            dbc.Col(dcc.Graph(figure=fig_age(df)))
                            
                            ]),
                        dbc.Row([
                            dbc.Col(dcc.Graph(figure=fig_education(df))),
                            dbc.Col(dcc.Graph(figure=fig_experience(df)))
                            
                            ]),
                        button_return_to_detail(return_home_from_summary)
                    ],
                    width=7
                    )
            
            
            ])
        

    ]


