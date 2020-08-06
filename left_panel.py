import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


###
# Age
###

min_age = dbc.Input(id="min-age",type="number", min=15, max=90 ,bs_size="sm",plaintext=True ,style={"width":"100%"})
max_age = dbc.Input(id = "max-age",type="number", min=16, max=90,bs_size="sm",plaintext=True,style={"width":"100%"})

age_input = html.Div(
    [
        html.P("Age range"),
        dbc.Row([dbc.Col(min_age,style={"width":"100%"}),dbc.Col(max_age,style={"width":"100%"})])
        
    ],
    id="styled-numeric-input",
)

###
# marital status
###
marital_status_select = dbc.Checklist(
    options=[
        {'label': 'Soltero(a)', 'value': 'Soltero(a)'},
        {'label': 'Casado(a)', 'value': 'Casado(a)'},
        {'label': 'Separado(a)/\nDivorciado(a)', 'value': 'Separado(a)/Divorciado(a)'},
        {'label': 'Viudo(a)', 'value': 'Viudo(a)'}
    ],
    inline=False,
    labelCheckedStyle={"color": "red"},
    id="marital-status"
) 

marital_status_input = html.Div([html.P("Marital status"),marital_status_select])

###
# Gender
###
gender_select = dbc.Select(
    id="select-gender",
    options=[
        {"label": "Femenino", "value": "1"},
        {"label": "Masculino", "value": "2"},
        {"label": "Cualquiera", "value": "3"},
    ],
)

gender_input = html.Div([html.P("Género"),gender_select])


###
#Relocation and travel
###
select_cambio_residencia = dbc.Select(
    id="select-relocation",
    options=[
        {"label": "Si", "value": 'Sí'},
        {"label": "No", "value": 'No'},
        {"label": "Cualquiera", "value": "Cualquiera"},
    ],
)

change_location_input = html.Div([html.P("Relocate"),select_cambio_residencia])

select_travel = dbc.Select(
    id="select-travel",
    options=[
        {"label": "Si", "value": 'Sí'},
        {"label": "No", "value": 'No'},
        {"label": "Cualquiera", "value": "Cualquiera"},
    ],
)

travel_input = html.Div([html.P("Travel"),select_travel])

###
#Slider experience
####
range_slider = dcc.RangeSlider(
        id='experience-slider',
        min=0,
        max=72,
        step=3,
        allowCross=False,
        marks={
        12: {'label': '1', 'style': {'color': 'black'}},
        24: {'label': '2', 'style': {'color': 'black'}},
        36: {'label': '3', 'style': {'color': 'black'}},
        48: {'label': '4', 'style': {'color': 'black'}},
        60: {'label': '5', 'style': {'color': 'black'}},
        72: {'label': '6+', 'style': {'color': 'black'}}
    }
    )

slider_input = html.Div([html.P("Work experience in years"),range_slider])

###
# Education
###

checklist_education = dbc.Checklist(
    id="education-checklist",
    options=[
        {'label': 'Primaria', 'value': 'EducaciónMedia'},
        {'label': 'Secundaria', 'value': 'EducaciónBásicaSecundaria'},
        {'label': 'Técnico', 'value': 'Carreratécnica'},
        {'label': 'Tecnólogo', 'value': 'Carreratecnológica'},
        {'label': 'Profesional', 'value': 'CarreraProfesional'},
        {'label': 'Especialización', 'value': 'Especialización'},
        {'label': 'Maestría', 'value': 'Maestría'},
        {'label': 'Doctorado', 'value': 'Doctorado'}
    ],style={"column-count": 2,"column-gap": "2rem","list-style": "none"},inline=True,
    labelCheckedStyle={"color": "red"}
) 

education_input = html.Div([html.P("Level of education"),checklist_education])

###
# Language
###

language_dropdown = dcc.Dropdown(
    id ="language-dropdown",
    options=[
        {'label': 'Español(Nativo)', 'value': 'Español(Nativo)'},
        {'label': 'Español(Avanzado)', 'value': 'Español(Avanzado)'},
        {'label': 'Inglés(Básico)', 'value': 'Inglés(Básico)'},
        {'label': 'Inglés(Intermedio)', 'value': 'Inglés(Intermedio)'},
        {'label': 'Inglés(Avanzado)', 'value': 'Inglés(Avanzado)'},
        {'label': 'Alemán(Básico)', 'value': 'Alemán(Básico)'},
        {'label': 'Alemán(Intermedio)', 'value': 'Alemán(Intermedio)'},
        {'label': 'Alemán(Avanzado)', 'value': 'Alemán(Avanzado)'}
    ],
    multi=True,
    placeholder="Seleccione el idioma"
) 


language_input = html.Div([html.P("Language and level required"),language_dropdown])

###
# Institución educativa
###



###
# Keyrowrds dropdown
###

keywords_dropdown = dcc.Dropdown(
    id="keywords-dropdown",
    options=[
        {'label': 'Atención al cliente', 'value': 'NYC'},
        {'label': 'SQL', 'value': 'MTL'},
        {'label': 'Tienda a tienda', 'value': '1'},
        {'label': 'PQR', 'value': '2'},
        {'label': 'donaciones', 'value': '3'},
        {'label': 'cuidado de pacientes', 'value': '4'},
        {'label': 'trabajo nocturno', 'value': '5'},
        {'label': 'turnos rotativos', 'value': '6'}
    ],
    multi=True,
    placeholder="Select mandatory keywords"
)  

keywords_input = html.Div([html.P("Keywords"),keywords_dropdown])

### Filter button
##

button_filter = html.Div(
    [
        html.Br(),
        dbc.Button("Filter", id="filter-button", className="mr-2"),
        html.Span( style={"vertical-align": "middle"}),
    ]
)
button_clear_selection = html.Div(
    [
        html.Br(),
        dbc.Button("Clear filters", id="clear-button", className="mr-2"),
        html.Span( style={"vertical-align": "middle"}),
    ]
)


###
# Cards layout
###
cards_general_info = html.Div(
    [
        
        dbc.Card(dbc.Row([dbc.Col([age_input,gender_input]),dbc.Col(marital_status_input)]), body=True),
    ]
)

cards_relocation = html.Div(
    [
        
        dbc.Card(dbc.Row([dbc.Col(change_location_input),dbc.Col(travel_input)]), body=True),
    ]
)

cards_work_experience = html.Div(
    [
        
        dbc.Card(slider_input, body=True),
    ]
)

cards_education = html.Div(
    [
        dbc.Card(education_input, body=True),
    ]
)

cards_language = html.Div(
    [
        dbc.Card(language_input, body=True),
    ]
)


def return_cards_school_name(universities_list):

    school_dropdown = dcc.Dropdown(
    id ="school-name-dropdown",
    options=universities_list,
    multi=True,
    placeholder="Select a school name you want to filter")  

    school_input = html.Div([html.P("School Name"),school_dropdown])

    cards_school_name = html.Div(
        [
            dbc.Card(school_input, body=True),
        ]
    )
    return cards_school_name

def return_keywords_list(keywords_list):

    school_dropdown = dcc.Dropdown(
    id ="keywords-dropdown",
    options=keywords_list,
    multi=True,
    placeholder="Select mandatory keywords")  

    school_input = html.Div([html.P("Keywords"),school_dropdown])

    cards_school_name = html.Div(
        [
            dbc.Card(school_input, body=True),
        ]
    )
    return cards_school_name





def return_card_content(universities_list,keywords_list):
    rows = dbc.Col(
    [
    cards_general_info,
    cards_relocation,
    cards_work_experience,
    cards_education,
    cards_language,
    return_cards_school_name(universities_list),
    return_keywords_list(keywords_list),
    button_filter,
    html.Div(" ",id="dummy-div"),
    button_clear_selection
    ]
)

    card_content = [
        dbc.CardHeader("Filters",style ={"font-weight": "bold", "font-size": "20px"}),
        dbc.CardBody(
            [
                rows
            ]
        ),
    ]
    return card_content

def return_filters_panel(universities_list,keywords_list):

    filters_panel = dbc.Col(dbc.Card(return_card_content(universities_list,keywords_list), color="info", outline=True))
    return filters_panel