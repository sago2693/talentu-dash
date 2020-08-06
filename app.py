from logging import StrFormatStyle
import dash
import dash_core_components as dcc
from dash_core_components.Slider import Slider
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output,State
import pandas as pd
import requests
import json
###
#Custom components
###
import upper_panel
import left_panel
import right_panel
import comparison
import summary

################# 
#### Start dash engine
################

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP,{"rel":"stylesheet","href":"assets/font-awesome-4.7.0/css"}],suppress_callback_exceptions=True)


###
## Variables initialization
###

# #get values
# offer_id = "BB90AABFE6B5286561373E686DCF3405"
# dictToSend = {"offer_id":offer_id}
# res = requests.post('http://localhost:5000/todo/api/v1.0/tasks', json=dictToSend)
# df = pd.read_json(res.json())
df = pd.read_pickle("df_candidatos.pkl")
df["score_total"] = 1
list_universities = []
set_universities = set(df["sitios_de_estudio"].sum().split("-"))
for item in set_universities:
    list_universities.append({"label":item,"value":item})

list_keywords = []
set_keywords = set(df["palabras_claves"].sum().split("-"))
for item in set_keywords:
    list_keywords.append({"label":item,"value":item})

#Indices for comparison
indices = df.index
comparison_indexes = []
labels_dict = {'administrativo':[1,50], 'cajero':[1,50]}
#        



###
#Create multi-page elements
###

return_home_from_candidates = dbc.Button("Back to candidate list", size="lg", color="info", className="mr-1", block=True, id ="return-home-from-candidates")
go_to_comparison_button = dbc.Button("Compare",id="comparison-button",className="mr-2",color="primary")
go_to_summary_button = dbc.Button("See summary",id="summary-button",className="mr-2",color="primary")
return_home_from_summary = dbc.Button("Return to detailed information", id="return-home-from-summary", className="mr-2")
list_checkbox = []

for index in df.index:
    list_checkbox.append(right_panel.create_checkbox(index))
    
#Add validation layout to hold all id-relevant objects
#########################

left_hand_side = left_panel.return_filters_panel(list_universities,list_keywords)
right_hand_side = right_panel.create_right_panel(df,go_to_comparison_button,go_to_summary_button,labels_dict)[0]
new_scores = right_panel.create_right_panel(df,go_to_comparison_button,go_to_summary_button,labels_dict)[1]
contenido = [
          dbc.Row([dbc.Col([left_hand_side],width = 3),dbc.Col(right_hand_side)])
        ]

main_panel = html.Div(children=html.Div(contenido,id="page-content"))



# start layout
app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    upper_panel.panel,
    main_panel,
    html.Div([return_home_from_candidates,return_home_from_summary],id="validation",hidden=True),
    ]
)




###Collapse button callback 
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

###
# Filter callback
###
@app.callback(
    [Output("candidates-table", "children"),Output("validation-after-filter", "children")],
    [Input("filter-button", "n_clicks"),
    Input("recalculate-button", "n_clicks")],
    [State("min-age", "value"),
    State("max-age", "value"),
    State("marital-status", "value"),  
    State("select-gender", "value"),
    State("select-relocation", "value"),
    State("select-travel", "value"),
    State('experience-slider', "value"),
    State("education-checklist", "value"),
    State("language-dropdown", "value"),
    State("school-name-dropdown", "value"),
    State("keywords-dropdown", "value"),
    State("numericadministrativo", "value"),
    State("numericcajero", "value"),
    State("slideradministrativo", "value"),
    State("slidercajero", "value")
    ]
)
def execute_filter(n_clicks_filter,n_clicks_recalculate,min_age,max_age,marital_status,gender,relocation,travel,experience,education,
language,school,keywords,years_administrativo,years_cajero,weight_administrativo,weight_cajero):
    ###Condiciones

    condiciones = []
    if min_age!= None and max_age != None:
        condiciones.append('@min_age <= edad <= @max_age') 
    if marital_status:
        condiciones.append('estado_civil == @marital_status') 
    if relocation:
        condiciones.append('disponibilidad_para_cambio_de_residencia == @relocation') 
    if travel:
        condiciones.append('disponibilidad_para_viajar == @travel') 
    
    if experience:
        inicio = experience[0]
        fin = experience[1]
        condiciones.append('@inicio<=duracion_trabajo_total<=@fin')

    if education:
        condiciones.append('max_nivel_educativo == @education')
    
    if language:
        condiciones.append('idioma1 == @language')

    if school:
        condiciones.append('lugar_formacion1 == @school')
    
    df_temp=df.copy()

    for condicion in condiciones:
        df_temp.query(condicion,inplace=True)
    
    global indices
    indices = df_temp.index

    list_checkbox = []
    
    
    for index in df[~df.index.isin(indices)].index:
        list_checkbox.append(right_panel.create_checkbox(index))
        
        global labels_dict
        labels_dict["administrativo"]= [years_administrativo,weight_administrativo]
        labels_dict["cajero"]= [years_cajero,weight_cajero]
        

    return right_panel.create_table(df_temp,labels_dict),list_checkbox

### 
# Clear filter selections callback
###

@app.callback(
    [
    Output("min-age", "value"),
    Output("max-age", "value"),
    Output("marital-status", "value"),
    Output("select-gender", "value"),
    Output("select-relocation", "value"),
    Output("select-travel", "value"),
    Output('experience-slider', "value"),
    Output("education-checklist", "value"),
    Output("language-dropdown", "value"),
    Output("school-name-dropdown", "value"),
    Output("keywords-dropdown", "value")],
    [Input("clear-button", "n_clicks")])

def clear_selection(n_clicks):
    
    return None,None,[],None,None,None,[],[], [],[],[]
    

###
#URL callback
###
@app.callback(
    Output("url", "pathname"),
    [Input("comparison-button", "n_clicks"),
     Input("return-home-from-candidates", "n_clicks"),
     Input("summary-button", "n_clicks"),
     Input("return-home-from-summary", "n_clicks")
     ],
    [State(f"checkbox-{i}", "value") for i in indices]
)
def compare_candidates(comparison, return_home_from_candidates,*args):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id=="comparison-button":
        
        global comparison_indexes
        comparison_indexes.clear()
        for arg in args:
            if arg:
                comparison_indexes.append(arg[0])
        
        if len(comparison_indexes) == 3:
            return "/candidates-comparison"
        else:
            return "/"
    elif button_id=="summary-button":
        return "/candidates-summary"
    else:
        return "/"



#### 
## predict callback
###

#Callback load examples
@app.callback(Output("label3-button", 'children'),
               [Input("load-descriptions-button", 'n_clicks')],
               [State("text-area", 'value')])

def display_descriptions(n,value):
    if n is None:
            return "cajero"
    else:
        dictToSend = {"text_to_predict":value}
        
        res = requests.post('http://localhost:5000/todo/api/v1.0/tasks', json=dictToSend)
        result = res.json()
        
        return result


######
### Show page content
#####



@app.callback([Output("page-content", "children"),Output("validation", "children")],
               [Input("url", "pathname")])

def render_page_content(pathname):
    
    if pathname =="/":
        return contenido,[return_home_from_candidates,return_home_from_summary]
    elif pathname =="/candidates-comparison":
        return comparison.return_candidates_comparison(df.loc[comparison_indexes].reset_index(drop=True),return_home_from_candidates),[go_to_comparison_button,go_to_summary_button,return_home_from_summary]+list_checkbox
    elif pathname == "/candidates-summary":
        
        df["score_total"]= new_scores[:40]
        return summary.return_candidates_summary(df,return_home_from_summary),[go_to_comparison_button,go_to_summary_button,return_home_from_candidates]+list_checkbox
    else:
        print("hubo un error")

if __name__ == '__main__':
    app.run_server(debug=True)


