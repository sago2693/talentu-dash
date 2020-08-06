from logging import disable
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import graph_time
import math

## Functions for objects
total_scores = []
 ### Cards for collapse

def create_label_card(label,params):
    years = params[0]
    weight = params[1]
    numeric_input = daq.NumericInput(
        id="numeric"+label,
        value=years,
        label="Exp years",
        labelPosition='bottom'
    )
    slider = daq.Slider(
                        id="slider"+label,
                        value=weight
    )

    return dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row([dbc.Col(html.H6(label, className="card-title")),dbc.Col(numeric_input)]),
                        slider
                    ]
                ))

def create_label_card_deck(labels_dict):
    cards = []
    for k,v in labels_dict.items():
        cards.append(create_label_card(label=k,params=v))

    return dbc.CardDeck(cards)

def create_button(label,id):
    button_menu = dbc.Button(label, id=id, className="mr-2",color="primary")
    return button_menu

def create_checkbox(index):
    checkbox = dbc.Checklist(
            options=[
                {"label": "", "value": index}
            ],
            value=[],
            id = f"checkbox-{index}"
        )
    return checkbox
#####
# Collapse menu
###

def create_collapse_menu(compare_button,summary_button,labels_dict):
    weight_panel = html.Div(dbc.Row(create_label_card_deck( labels_dict)),
style = {"background-color": "white","height": "140px"},id="weight-panel")

    collapse = html.Div(
[

    collapse_button,
    filter_and_score_button,
    summary_button,
    compare_button,
    dbc.Collapse(
        dbc.Card(dbc.CardBody(weight_panel),style={"width":"1080px"}),
        id="collapse",
    ),
]
)
    return collapse


### 
# Create gauge
##

def create_gauge(ajuste):
    color = "red" if ajuste <50 else "green"
    return daq.Gauge(
        value=ajuste,
        label=f"Total Score: {ajuste}% ",
        max=100,
        min=0,
        size = 100,
        color=color
        ) 
### sliders and buttons

collapse_button = create_button(label="Open collapse",id="collapse-button")
filter_and_score_button = create_button(label="Filter and recalculate",id="recalculate-button")

 ###Collapsible menu



#Icons

calendario = html.I(className="fa fa-calendar-o", **{'aria-hidden': 'true'}, children=None,title="agendar")
circle_o = html.I(className="fa fa-times-circle-o", **{'aria-hidden': 'true'}, children=None,title="descartar")
handshake = html.I(className="fa fa-handshake-o", **{'aria-hidden': 'true'}, children=None,title="contratar")
notepad = html.I(className="fa fa-sticky-note-o ", **{'aria-hidden': 'true'}, children=None,title="notas")


iconos = html.Div([calendario,html.Br(),html.Br(),html.Br(),
circle_o,html.Br(),html.Br(),html.Br(),
handshake,html.Br(),html.Br(),html.Br(),
notepad])

###############
#Main function
################

table_header = [
    html.Thead(html.Tr([
        html.Th("Compare",style={"width":"80px"}),
        html.Th("Candidate",style={"width":"350px"}),
        html.Th("Work Experience",style={"width":"350px"}),
        html.Th("Score",style={"width":"200px"}),
        html.Th("Actions",style={"width":"100px"})
        ]))
    ]

def personal_info_card (row):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H5(row["nombre"], className="card-title"),
                html.P(str(row["edad"])+str(' años'), className="card-subtitle"),
                html.P(row["estado_civil"], className="card-subtitle"),
                html.P("No registra licencia conducción" if math.isnan(row["licencia_conduccion"]) else row["licencia_conduccion"], className="card-subtitle"),
                html.P(row["localizacion"], className="card-subtitle"),
                html.P(' '.join([row['idioma'+str(x)]+' ' for x in range(1,6) if str(row['idioma'+str(x)])!='0']), className="card-subtitle")
            ]
        ),
        style={"width": "18rem"},
    )
    return card


import pickle
import random
def work_experience_summary(row,labels_dict):

    list_elements = [html.Td(dcc.Graph(figure=graph_time.graph_time_experience(row["diccionario_experiencia"]), config={'displayModeBar': False}))]
    
    lista_scores = ["score_trabajo"+str(i) for i in range(1,6)]
    lista_years = ["years_trabajo"+str(i) for i in range(1,6)]
    candidate_label_scores ={}
    if bool(labels_dict):
               

        
        #Compute score for each label
        for k,v in labels_dict.items():
            years_required = v[0]
            label_score = 0
            for score_column,year_column in zip(lista_scores,lista_years):
                score = row[score_column]
                year = row[year_column]

                label_score += score[k]*(year/years_required)

            candidate_label_scores[k] = label_score
    
    #sum total weight for scoring
    total_weight=0
    for item in labels_dict.values():
        total_weight+=item[1]

    total_score = 0
    list_scores_to_display = []
    for k,v in candidate_label_scores.items():
        weight = labels_dict[k][1]/total_weight

        list_scores_to_display.append(html.H6(f"{k}:{round(v,2)}%"))
        total_score+= candidate_label_scores[k]*weight

    total_score = min(total_score,100)
    total_scores.append(total_score)
    total_score_gauge = create_gauge(round(total_score,2))
    list_elements.append(html.Td([total_score_gauge]+list_scores_to_display))

    return list_elements

     
def create_table(df,labels_dict):
    global total_scores
    total_scores.clear()
    column_names = df.columns
    
    rows = []
    for index, row in df.iterrows():       

        rows.append(
            html.Tr([
                html.Td(create_checkbox(index)),
                html.Td(personal_info_card(row)),
                ]+work_experience_summary(row,labels_dict) + [html.Td(iconos,style={"text-align":"center"})]
            ))

    table_body = [html.Tbody(rows)]
    table_content = table_header + table_body
    return table_content


def create_right_panel (df,go_to_comparison_button,go_to_summary_button,labels_dict):
    
    table = dbc.Table(create_table(df,labels_dict), bordered=True,style={"width":"1080px"},id="candidates-table")
    
    return (html.Div([create_collapse_menu(go_to_comparison_button,go_to_summary_button,labels_dict),table,html.Div("",id="validation-after-filter",hidden=True)]),total_scores)


    