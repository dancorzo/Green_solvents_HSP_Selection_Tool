#from sre_parse import State
#from ast import If, Return
#from colorama import Style
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
#import pathlib
#from matplotlib.pyplot import text
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.exceptions import PreventUpdate
from helpers import make_dash_table

app = Dash(
    __name__,external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server

copyright_text = '©[dancorzo](https://www.github.com/dancorzo). Sourced with Love.'

graph_style = {'background':'#969998','padding-bottom':'2px', 'padding-top':'2px','padding-left':'2px','padding-right':'2px','height':'55vh'}

modeBarStyle = {'orientation': 'h', 'bgcolor': 'rgba(255 ,255 ,255 ,0.7)', 'iconColor' : 'rgba(0, 31, 95, 0.3)', 'logoColor': 'rgba(0, 31, 95, 0.3)', 'position': 'right' }

radio_style= {'display': 'inline-block', 'margin-left': '10px','margin-right':'8px','font-weight': 300 }

#URL of publication

link_paper = "https://www.omegalabresearch.com"

# Incorporate data into App

#These are the Dataframes 

#distance_hsp = pd.read_csv("data/distance-test.csv", index_col=0)

#solv_hsp = pd.read_csv("data/Solvent_Database_Rev.csv", index_col=0)



#Read from google Sheets
solv_hsp = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   '1EwTp0yTYgmwJwOcTNQ0pPyrm9AHnW0JevLYgA3Zp0hM' +
                   '/export?gid=0&format=csv',
                   # Set first column as rownames in data frame
                   index_col=0,
                   # Parse column values to datetime
                   #parse_dates=['Quradate']
                  )


# Define Starting values


STARTING_SOLVENT = "d-Limonene"
SOLVENT_DESCRIPTION = solv_hsp.loc[solv_hsp["Name"] == STARTING_SOLVENT]["Desc"].iloc[0]
SOLVENT_IMG = solv_hsp.loc[solv_hsp["Name"] == STARTING_SOLVENT]["Img_URL"].iloc[0]



# Plot the Data
# fig_opv = px.scatter(opv_df, x="LD50", y="PCE", color="Type",symbol="Type", template="ggplot2", hover_name="System", hover_data=["Solvent"], custom_data = ['URL','Year','System', 'Solvent', 'PCE', 'LD50'], 
#                  log_x=True, size_max=60, )

# fig_opv.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
#     ), 
#     modebar_orientation='v'
#     )


#Pot 3D points
# fig_3D = px.scatter_3d(solv_hsp, x="dD", y="dP", z="dH", labels={"BP":'Boining Point(°C)',"dD":'dD (MPa½)', "dP":'dP (MPa½)', "dH":'dH (MPa½)'},
#                 color="Classification", 
#                 hover_name="Name", hover_data=["BP","LD50"], custom_data = ['Name','SDS_Page','Img_URL','Desc'],
#                 #size_max=10, 
#                 )


# fig_3D.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
#     ), 
#     modebar_orientation='v'
#     )





#   {
    # modebar: {
    #   // vertical modebar button layout
    #   orientation: 'v',
    #   // for demonstration purposes
    #   bgcolor: 'salmon',
    #   color: 'white',
    #   activecolor: '#9ED3CD'
    # },
#     // move plotting area outside the modebar position
#     margin: {r: 50},
#     // move the legend inside the plot on the top right
#     legend: {x: 0, y: 1}
#   },


app.layout = html.Div( #start of Main Div
    [
        html.Div([# Start of Banner

            html.Div([ #this is main logo
            # dbc.Col([
            # html.P("This is column 1"), 
            # ], width=12, style={"height":"100%", "background-color": "blue"}),
            
            html.Img(src=app.get_asset_url("kaust-logo-3.png"), ) 
            ], className="app__banner"), #End of main logo
            
            html.Div([ # Title
            # dbc.Col([
            # html.P("This is column 2"), 
            # ], width=12, style={"height":"100%", "background-color": "red"})

            html.H3("Green Solvent Selection Tool", style={'textAlign': 'center', 'color': 'black', 'fontSize': 38}),
            ], className="app__banner", id="title"), #End of Title

            html.Div([ # Logo 2
            # dbc.Col([
            # html.P("This is column 3"), 
            # ], width=12, style={"height":"100%", "background-color": "yellow"}),

            html.Img(src=app.get_asset_url("omega-logo.png"))#this is main logo)) 
            ], className="app__banner") #End of Logo 2
            
            ], className="app__banner" 
        ), #End of Banner



        html.Div([ # Start of Top Row Cards

            html.Div([ # Start Card Top 1

            html.Div( #Start of Instructions
                 [
                #html.H5("Instructions", className="bold",),
                html.H6('Instructions', style={'TextAlign':'Center', 'color': 'Black', 'fontSize': 24},),
                html.Span("Hover ", className="uppercase bold"),
                html.Span(
                    "and "
                ),
                html.Span("Click ", className="uppercase bold"),
                html.Span(
                    "over a solvent in the 3D graph to see its structure and properties"
                ),
                html.Br(),

                html.Span("Input ", className="uppercase bold"),
                html.Span(
                    "your materials in the fields below to plot them in Hansen space. "
                ),
                html.Br(),
                html.Span("Review ", className="uppercase bold"),
                html.Span(
                    "solubility affinity and boiling point vs distance to find most appropriate solvents for your application. For more information on solvent selection click "
                ),
                html.A('here', href=link_paper, target="_blank"),
                html.Br(),
                html.Span("Select ", className="uppercase bold"),
                html.Span(
                    "a solvent in the dropdown to add it to the candidates list"
                ),
                html.Br(),
                 ]
                ), #End of Instructions



                html.H6('Input your material', style={'TextAlign':'Center', 'color': 'Black', 'fontSize': 24}, ),
                dbc.Row([
                        dbc.Col([
                        #html.P('Material 1',style={'TextAlign':'Center', 'color': 'orange', 'fontSize': 20},),
                        html.Span("Material 1 ", className="uppercase bold"),
                        html.Div(id="mat_name"), # Input 1
                        dcc.Input(id='name_mat', type="text",style={'width': 200,'marginRight':'10px'},placeholder="Name",),
                    ], width=5, align="center"),

                    dbc.Col([
                        #html.P('dD',style={'TextAlign':'Center', 'color': 'orange', 'fontSize': 20},), # Input 1
                        html.Span("dD ", className="bold"),
                        html.Div(id="dX_mat_value"), # Input 1
                        dcc.Input(id="x_mat", type="number", step=0.1, value=0, placeholder="dX", style={'width': 80,'marginRight':'10px'}),
                    ], width=2),
                    dbc.Col([
                        html.Span("dP ", className="bold"),
                        #html.P('dP',style={'TextAlign':'Center', 'color': 'orange', 'fontSize': 20},), # Input 2
                        dcc.Input(id="y_mat", type="number", step=0.1, value=0, placeholder="dY", size='20', style={'width': 80, 'marginRight':'10px'}),
                        
                    ],width=2, align="center"),
                    dbc.Col([
                        html.Span("dH ", className="bold"),
                        #html.P('dH',style={'TextAlign':'Center', 'color': 'orange', 'fontSize': 20},), # Input 3
                        dcc.Input(id="z_mat", type="number", step=0.1, value=0, placeholder="dZ", style={ 'width': 80, 'marginRight':'10px'}),
                    ],width=2, align="center"),
                ], justify="evenly"), # End of Material 1 Input

                    html.Br(),


                    dbc.Row([ #Start of Material 2 Input
                        dbc.Col([
                        html.Span("Material 2 ", className="uppercase bold"),
                        html.Div(id="mat_name_2"), # Input 1
                        dcc.Input(id='name_mat_2', type='text',style={'width': 200,'marginRight':'10px'}, placeholder="Name",),
                    ], width=5, align="center"),

                    dbc.Col([
                        html.Span("dD ", className="bold"),
                        html.Div(id="dX_mat_value_2"), # Input 1
                        dcc.Input(id="x_mat_2", type="number", step=0.1,  value=0, placeholder="dX", style={'width': 80,'marginRight':'10px'}),
                    ], width=2),
                    dbc.Col([
                        html.Span("dP ", className="bold"),
                        dcc.Input(id="y_mat_2", type="number", step=0.1,  value=0, placeholder="dY", size='20', style={'width': 80, 'marginRight':'10px'}),
                        
                    ],width=2, align="center"),
                    dbc.Col([
                        html.Span("dH ", className="bold"),
                        dcc.Input(id="z_mat_2", type="number", step=0.1, value=0, placeholder="dZ", style={ 'width': 80, 'marginRight':'10px'}),
                    ],width=2, align="center"),
                ], justify="evenly"),# End of Material 2 Input
                
                html.Br(),
                html.Div([
                 #dbc.Button("Clear",  id='clear-val', n_clicks=0,outline=True, color="secondary", className="me-md-2"),   
                 dbc.Button("Submit",id='submit-val', n_clicks=0, color="secondary", className="me-1"),
                ], className="d-grid gap-2 d-md-flex justify-content-md-end"),


                ], className="create_container four columns card flexbox-item-1"), # End Card Top 1

            html.Div([ # Start Card Top 2

                    dcc.Graph(id='Solvents_3D', figure={}, config={'displayModeBar': True, 'scrollZoom': True, 'displaylogo': False}, style=graph_style),  

               ], className="create_container four columns card flexbox-item-2 "), # End Card Top 2
            


            html.Div([ # Start Card Top 3
               dbc.Row([

                #    dbc.Col([
                #     dcc.Graph(id='Solvents_3D', figure=fig_3D, config={'displayModeBar': True, 'scrollZoom': True, 'displaylogo': False}, style=graph_style),
                #        ],),

                    dbc.Col([ #Start of Info Col

                    html.H6('Cliked Solvent Information', style={'text-align': 'center','TextAlign':'Center', 'color': 'Black', 'fontSize': 24}, ),
                    html.Br(),

                    html.Div( #Start of Hover Image
                        [
                            html.Img(
                                id="solv_img",
                                src=SOLVENT_IMG,
                                className="solv-img",  
                                #style={'height':'50%', 'width':'50%'}
                            ) #Image style is to define size within Div object
                        ],
                        className="chem__img__container",
                    ), #End of Hover Image

                    html.Br(),

                    html.Div([ # Start of Solvent Hover Name & URL
                        html.Div([
                            html.A(
                            STARTING_SOLVENT,
                            id="solv_name",
                            href="https://pubchem.ncbi.nlm.nih.gov/compound/22311",
                            target="_blank", 
                            )
                            ], style={'text-align': 'center'}),

                        html.Br(),
                        html.Br(),
                        html.P(SOLVENT_DESCRIPTION, id="solv_desc"),
                    
                    ],className="chem__desc__container", style={'text-align': 'justify', 'marginRight':'30px','marginLeft':'30px'}), #End of Solvent Hover Name & URL

                       ], ), # End of Info Col
               ])
               
                           
                ], className="create_container four columns card flexbox-item-1"), # End Card Top 3

            ], className="flexbox-container"), # End of Top Row Cards

        
        html.Div([ # Start of Middle Row Cards
            html.Div([ #Start of Middle Card 1
            #html.P('Select Thing',style={'TextAlign':'Center', 'color': 'orange', 'fontSize': 40},),# Title Card
            #dcc.Dropdown(id='dropdown_1',multi=False, clearable=True, value='US', placeholder='Select Countries', options=['A', 'B', 'C'], className='dcc_compon'),
            dcc.RadioItems(['Boiling Point', 'Toxicity',], 'Boiling Point', inline=True,labelStyle= radio_style, id='type_affinity',),
            dcc.Graph(id='Affinity', figure={}, config={'displayModeBar': True, 'scrollZoom': True, 'displaylogo': False}, style=graph_style),

            ], className= "create_container four columns card"), # End of Midde Card 1

            html.Div([ #Start of Middle Card 2

            dcc.RadioItems(['Boiling Point', 'Toxicity',], 'Boiling Point', inline=True,labelStyle= radio_style, id='type_M1',),
            dcc.Graph(id='Solvents_Distance_M1', figure={}, config={'displayModeBar': True, 'scrollZoom': True, 'displaylogo': False}, style=graph_style),

            ], className= "create_container four columns card"), # End of Midde Card 2

            html.Div([ #Start of Middle Card 3

            dcc.RadioItems(['Boiling Point', 'Toxicity',], 'Boiling Point', inline=True,labelStyle= radio_style, id='type_M2',),
            dcc.Graph(id='Solvents_Distance_M2', figure={}, config={'displayModeBar': True, 'scrollZoom': True, 'displaylogo': False}, style=graph_style),

            ], className= "create_container four columns card"), # End of Midde Card 3




        ], className="flexbox-container"),#style={"display":"flex", "flex-flow": "row wrap", "justify-content": "space-evenly"}), # End of Middle Row Cards

        html.Div([ #Start of Bottom Row Cards
            html.Div([
            
                #     html.Div(
                #     [
                #         html.Table(
                #             make_dash_table([STARTING_SOLVENT], solv_hsp),
                #             id="table-element",
                #             className="table__container",
                #         )
                #     ],
                #     className="container bg-white p-0 app__banner",
                # ),


            ],className="create_container eleven columns"),


        ], className="flexbox-container"), #End of Bottom Row Cards

            html.Div([ #Start of Bottom Row Cards
            html.Div([

            dcc.Markdown(children=copyright_text, style={'text-align': 'center','TextAlign':'Center', 'color': 'Black', 'fontSize': 17},)
            
            #style={'textJustify': 'center', 'textAlign': 'middle', 'fontSize': 17, 'spacing':'1'})

            ],className="create_container three columns")

        ], className="flexbox-container"), #End of Bottom Row Cards



    ], className="app__container bg-white") #End of Main Div



# @app.callback(
#     Output("dX_mat_value", "children"),
#     [Input("x_mat", "value")],
# )
# def cb_render(val):
#     return "the selected HSP is " + val + " "

dcc.RadioItems(['Boiling Point', 'Toxicity',], 'Boiling Point', inline=True,labelStyle= radio_style, id='type_M1',),

@app.callback(
    Output('Solvents_Distance_M1', 'figure'),
    Output('Solvents_Distance_M2', 'figure'),
    Output('Affinity', 'figure'),
    Output('Solvents_3D', 'figure'),

    Input('submit-val','n_clicks'),
    Input('type_M1', 'value'),
    Input('type_M2', 'value'),
    Input('type_affinity', 'value'),

    # Input('name_mat', "value"),
    # Input('name_mat_2', "value"),
    # Input('x_mat', 'value'),
    # Input('y_mat', 'value'),
    # Input('z_mat', 'value'),
    # Input('x_mat_2', 'value'),
    # Input('y_mat_2', 'value'),
    # Input('z_mat_2', 'value'), 
    #State('Solvents_3D', 'figure'),
    State('name_mat', "value"),
    State('name_mat_2', "value"),
    State('x_mat', 'value'),
    State('y_mat', 'value'),
    State('z_mat', 'value'),
    State('x_mat_2', 'value'),
    State('y_mat_2', 'value'),
    State('z_mat_2', 'value'), 

    )
def update_figure(n_clicks, type_M1, type_M2, type_affinity, mat_name, mat_name_2, x_mat, y_mat, z_mat, x_mat_2, y_mat_2, z_mat_2, ):


    #Get Names of Materials

    if mat_name is None:
         Mat1 = "Material 1"
    else:
         Mat1 = mat_name
    
    if mat_name_2 is None:
         Mat2 = "Material 2"
    else:
         Mat2 = mat_name_2
    

    
    #print(n_clicks)

    #Calculate dataframe
    dff =  solv_hsp #distance_hsp

    distance_between_materials = (((x_mat - x_mat_2)**2) + ((y_mat - y_mat_2)**2) + ((z_mat - z_mat_2)**2))**.5
    dff["distance_to_M1"] = (((dff["dD"] - x_mat)**2) + ((dff["dP"] - y_mat)**2) + ((dff["dH"] - z_mat)**2))**.5
    dff["distance_to_M2"] = (((dff["dD"] - x_mat_2)**2) + ((dff["dP"] - y_mat_2)**2) + ((dff["dH"] - z_mat_2)**2))**.5

    
    dff["Affinity"] = (dff["distance_to_M1"] - dff["distance_to_M2"])/ distance_between_materials


    #Select from Toxicity or BP

    if type_M1 == 'Toxicity':
        x_m1 = "LD50"
    else:
        x_m1 = "BP"
    
    if type_M2 == 'Toxicity':
        x_m2 = "LD50"
    else:
        x_m2 = "BP"
    
    if type_affinity == 'Toxicity':
        y_affinity = "LD50"
    else:
        y_affinity = "BP"
   



    #Update Distance to Material 1
    fig = px.scatter(dff, x=x_m1, y="distance_to_M1", labels={"LD50": 'LD50 (mg/kg)', "BP":'Boiling Point(°C)','distance_to_M1':'Distance to '+ Mat1 + ' (MPa½)'},
                 color="Classification",symbol="Classification", 
                 #template="ggplot2", 
                 hover_name="Name", hover_data=["BP","LD50"], custom_data = ['LD50'], 
                 log_x=True, size_max=60)

    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ), 
    modebar_orientation='v'
    )

    #Update Distance to Material 2

    fig_2 = px.scatter(dff, x=x_m2, y="distance_to_M2", labels={"LD50": 'LD50 (mg/kg)',"BP":'Boining Point(°C)','distance_to_M2':'Distance to '+ Mat2 + ' (MPa½)'},
                 color="Classification",symbol="Classification", 
                 #template="ggplot2", 
                 hover_name="Name", hover_data=["BP","LD50"], custom_data = ['LD50'], 
                 log_x=True, size_max=60)

    fig_2.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ), 
    modebar_orientation='v'
    )


    #Update Affinity Graph
    fig_3 = px.scatter(dff, x="Affinity", y=y_affinity, labels={"LD50": 'LD50 (mg/kg)',"BP":'Boining Point(°C)', "Affinity": 'Solubility Affinity'},
                 color="Classification",symbol="Classification", #template="ggplot2", 
                 hover_name="Name", hover_data=["dD","dP","dH","BP","LD50"], custom_data = ['LD50'], 
                 log_x=False, size_max=60, )

    fig_3.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ), 
    modebar_orientation='v'
    )

    fig_3.add_annotation(dict(font=dict(color='Black',size=15),
                                        x=0,
                                        y=0.02,
                                        showarrow=False,
                                        text= Mat1,
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper"))
    
    fig_3.add_annotation(dict(font=dict(color='Black',size=15),
                                        x=1,
                                        y=0.02,
                                        showarrow=False,
                                        text=Mat2,
                                        textangle=0,
                                        xanchor='right',
                                        xref="paper",
                                        yref="paper"))


    fig_3.update_xaxes(
    fixedrange=True,
    range=(-1.05,1.05),
    )

    #add shaded area
    fig_3.add_vrect(x0=0, x1=2, fillcolor = 'rgba(118, 54, 148, 0.49)', line_width=0, opacity=0.3)
    fig_3.add_vrect(x0=-2, x1=0, fillcolor = 'rgba(98, 195, 80, 0.9)', line_width=0, opacity=0.3)

    
    #Define trace dataframe
    Tracedata = [[Mat1, x_mat, y_mat,z_mat], [Mat2, x_mat_2,y_mat_2,z_mat_2]]

    td_df = pd.DataFrame(Tracedata, columns=['Name', 'x','y','z'])

    #print(td_df)

    
    
    fig_4 = px.scatter_3d(dff, x="dD", y="dP", z="dH", labels={"BP":'Boining Point(°C)',"dD":'dD (MPa½)', "dP":'dP (MPa½)', "dH":'dH (MPa½)'},
                color="Classification", 
                hover_name="Name", hover_data=["BP","LD50"], custom_data = ['Name','SDS_Page','Img_URL','Desc'],
                #size_max=10, 
                )


    fig_4.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ), 
    modebar_orientation='v'
    )

    # fig_4.add_trace(
    # go.Scatter3d(
    #     x=[x_mat,x_mat_2],
    #     y=[y_mat, y_mat_2],
    #     z=[z_mat, z_mat_2],
    #     mode="markers",
    #     #line=go.scatter.Line(color="gray"),
    #     showlegend=True)
    # )

    fig_4.add_trace(
    go.Scatter3d(x=td_df['x'],y=td_df['y'],z=td_df['z'],text=td_df['Name'], name='My Materials',
    mode="markers", #marker = {"color": 'black',},
    marker=dict(
        size=10,
        #color=td_df['z'],                # set color to an array/list of desired values
        #colorscale='Viridis',   # choose a colorscale
        opacity=0.8,
        symbol='cross'
    ),
    
    #line=go.scatter.Line(color="gray"),
    showlegend=True)
    )


  
    


    return fig, fig_2, fig_3, fig_4


#Construction of Distance to Material 1 Plot

# @app.callback(
#     Output('Solvents_Distance_M1', 'figure'),
#     Input('x_mat', 'value'),
#     Input('y_mat', 'value'),
#     Input('z_mat', 'value'),)
# def update_figure(x_mat, y_mat, z_mat):
    
#     dff =  solv_hsp #distance_hsp

#     dff["distance_to_M1"] = (((dff["dD"] - x_mat)**2) + ((dff["dP"] - y_mat)**2) + ((dff["dH"] - z_mat)**2))**.5


#     fig = px.scatter(dff, x="BP", y="distance_to_M1",
#                  color="Classification",symbol="Classification", 
#                  template="ggplot2", hover_name="Name", hover_data=["BP","LD50"], custom_data = ['LD50'], 
#                  log_x=True, size_max=60)

#     fig.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
#     ), 
#     modebar_orientation='v'
#     )

#     return fig

#Construction of Distance to Material 2 Plot

# @app.callback(
#     Output('Solvents_Distance_M2', 'figure'),
#     Input('name_mat_2', 'value'),
#     Input('x_mat_2', 'value'),
#     Input('y_mat_2', 'value'),
#     Input('z_mat_2', 'value'),)
# def update_figure(name_mat_2, x_mat, y_mat, z_mat):


    
#     dff_2 =  solv_hsp

#     dff_2["distance_to_M2"] = (((dff_2["dD"] - x_mat)**2) + ((dff_2["dP"] - y_mat)**2) + ((dff_2["dH"] - z_mat)**2))**.5


#     fig = px.scatter(dff_2, x="BP", y="distance_to_M2", 
#                  color="Classification",symbol="Classification", 
#                  template="ggplot2", hover_name="Name", hover_data=["BP"], custom_data = ['LD50'], 
#                  log_x=True, size_max=60)

#     fig.update_layout(legend=dict(
#     orientation="h",
#     yanchor="bottom",
#     y=1.02,
#     xanchor="right",
#     x=1
#     ), 
#     modebar_orientation='v'
#     )

#     return fig


# @app.callback(
    
#     Output('Affinity', 'figure'),
#     Input('submit-val', 'n_clicks'),
#     # State('name_mat', 'value'),
#     # State('name_mat_2', 'value'),
#     State('x_mat', 'value'),
#     State('y_mat', 'value'),
#     State('z_mat', 'value'),
#     State('x_mat_2', 'value'),
#     State('y_mat_2', 'value'),
#     State('z_mat_2', 'value'),)
# def update_figure(n_clicks, x_mat, y_mat, z_mat, x_mat_2, y_mat_2, z_mat_2, ):


    
#     #dff_3 =  solv_hsp

#     # dff_3["distance_to_MA"] = (((dff_3["dD"] - x_mat)**2) + ((dff_3["dP"] - y_mat)**2) + ((dff_3["dH"] - z_mat)**2))**.5
#     # dff_3["distance_to_MB"] = (((dff_3["dD"] - x_mat_2)**2) + ((dff_3["dP"] - y_mat_2)**2) + ((dff_3["dH"] - z_mat_2)**2))**.5

#     #distance_between_materials = (((x_mat - x_mat_2)**2) + ((y_mat - y_mat_2)**2) + ((z_mat - z_mat_2)**2))**.5
    
#     # dff_3["Affinity"] = (dff_3["distance_to MA"] - dff_3["distance_to_MB"])/ distance_between_materials

    


#     # fig = px.scatter(dff_3, x="Affinity", y="BP", 
#     #              color="Classification",symbol="Classification", 
#     #              template="ggplot2", hover_name="Name", hover_data=["BP"], custom_data = ['LD50'], 
#     #              log_x=True, size_max=60)

#     # fig.update_layout(legend=dict(
#     # orientation="h",
#     # yanchor="bottom",
#     # y=1.02,
#     # xanchor="right",
#     # x=1
#     # ), 
#     # modebar_orientation='v'
#     # )

#     #return fig

#     return u'''
#         The Button has been pressed {} times,
#         Input 1 is "{}",
#         and Input 2 is "{}"
#     '''.format(n_clicks, x_mat, y_mat)


# @app.callback(
#     [
#         Output('solv_name', 'children'),
#         Output('solv_name', 'href'),
#         Output('solv_img', 'src'),
#         Output('solv_desc', 'children'),
#     ],
#     [Input('Solvents_3D', 'hoverData')],
# )

# def chem_info_on_hover(hoverData):
#     """
#     Display chemical information on graph hover.
#     Update the image, link, description.

#     :params hoverData: data on graph hover
#     """

#     if hoverData is None:
#         raise PreventUpdate

#     try:
#         row = df_row_from_hover(hoverData)
#         if row.empty:
#             raise Exception
#         return (
#             row['Name'].iloc[0],
#             row['SDS_Page'].iloc[0],
#             row['Img_URL'].iloc[0],
#             row['Desc'].iloc[0],
#         )

#     except Exception as error:
#         print(error)
#         raise PreventUpdate

# Click Data Information
@app.callback(
    
    [
        Output('solv_name', 'children'),
        Output('solv_name', 'href'),
        Output('solv_img', 'src'),
        Output('solv_desc', 'children'),
    ],
    [Input('Solvents_3D', 'clickData')] 
    )

def display_click_data(hoverData):
    if hoverData is None:
        raise PreventUpdate
    
    try:
        #print (hoverData)
        point_number=hoverData['points'][0]['pointNumber']
        # print(point_number)
        solvent_name = hoverData['points'][0]['customdata'][0]
        solv_url= hoverData['points'][0]['customdata'][1]
        solv_img = hoverData['points'][0]['customdata'][2]
        solv_desc = hoverData['points'][0]['customdata'][3]
        # print(solvent_name)
        # print(solv_url)
        # print(solv_img)
        # print(solv_desc)

        return(solvent_name, solv_url, solv_img, solv_desc)
        # if the_link is None:
        #     return 'No Website Available'
        # else:
        #     return html.A(the_link, href=the_link, target="_blank")
    
    except Exception as error:
        print(error)
        raise PreventUpdate





# @app.callback(
    
#     [
#         Output('Solvents_3D', 'children'),
#         Output('solv_name', 'href'),
#         Output('solv_img', 'src'),
#         Output('solv_desc', 'children'),
#     ],
#     [Input('Solvents_3D', 'hoverData')] 
#     )

# fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))


if __name__ == "__main__":
    app.run_server(port=8060)

