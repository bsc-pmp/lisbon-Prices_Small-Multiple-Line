from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd



# replace with your own data source
df = pd.read_csv('INEHousingPriceData.csv', sep=';')
mask = df['Parish'] == 'Lisboa'
df_new = pd.DataFrame(df[mask])

app = Dash(__name__)


app.layout = html.Div([
    html.Div(
        className="app-header",
        children = [
            html.Div('House Price Index by Lisbon Borough',
                     className="app-header--title"),
        ]
    ),
    html.Div(
        className="app-header",
        children = [
            html.Div('1st Quarter 2018 to 2nd Quarter 2022',
                     className="app-header--subtitle"),
        ]
    ),
    html.Div(
        className="app-header",
        children = [
            html.Div('Source: Instituto Nacional de Estatística, I.P. (INE)',
                     className="app-header--source"),
        ]
    ),
    html.Div([
        dcc.Graph(id="graph",
                  figure={},
                  className="graph-left"),
    ]),
    html.Div([
        dcc.Graph(id="graph1",
                  figure={},
                  className="graph-right"),
    ]),
    html.Div([
        dcc.Graph(id="graph2",
                  figure={},
                  className="graph-right"),
    ]),
    html.Div([
            dcc.Graph(id="graph3",
                      figure={},
                      className="graph-left"),
    ]),
    html.Div([
            dcc.Graph(id="graph4",
                      figure={},
                      className="graph-right"),
    ]),
    html.Div([
            dcc.Graph(id="graph5",
                      figure={},
                      className="graph-right"),
    ]),
    html.Div([
            dcc.Graph(id="graph6",
                      figure={},
                      className="graph-left"),
    ]),
    html.Div([
            dcc.Graph(id="graph7",
                      figure={},
                      className="graph-right"),
    ]),
    html.Div([
            dcc.Graph(id="graph8",
                      figure={},
                      className="graph-right"),
    ]),
    html.Div([
                dcc.Graph(id="graph9",
                          figure={},
                          className="graph-left"),
    ]),
    html.Div([
        html.Div(
            className="checklist-background",
            children=[
            html.Div('Lisbon House Price Index', className="checklist-title"),
            ]
        ),
        dcc.Checklist(
            id="checklist",
            className="checklist-background1",
            options=['Areeiro', 'Arroios', 'Avenidas Novas', 'Estrela', 'Misericórdia',
                     'Penha de França', 'Santa Clara', 'Santa Maria Maior', 'Santo António', 'São Vicente'],
            value=['Areeiro', 'Arroios', 'Avenidas Novas', 'Estrela', 'Misericórdia',
                   'Penha de França', 'Santa Clara', 'Santa Maria Maior', 'Santo António', 'São Vicente'],
            # only solution to make a list in the checklist
            labelStyle=dict(display='block'),
        ),
    ]),
])


@app.callback(
    Output("graph", "figure"),
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output("graph4", "figure"),
    Output("graph5", "figure"),
    Output("graph6", "figure"),
    Output("graph7", "figure"),
    Output("graph8", "figure"),
    Output("graph9", "figure"),
    Input("checklist", "value")
)



def update_line_chart(column_name):
    def chart(i, parish):
        var_holder = {}

        while range(0, i):
            df = pd.read_csv('INEHousingPriceData.csv', sep=';')
            var_holder['mask' + str(i)] = df['Parish'] == parish
            fig = px.line(df[var_holder['mask' + str(i)]], x="Quarters", y="Price", color="Parish", height=270, title= parish )

            backgroundcolor = "#000000"
            backgroundcolor_plot = "#333333"
            grid_color = "#878787"
            graph_font = "#ababab"
            line_color = "#65d6d6"

            fig.update_layout(yaxis_range=[1000, 6000],
                              margin=dict(l=20, r=20, t=20, b=20),
                              paper_bgcolor=backgroundcolor,
                              plot_bgcolor=backgroundcolor_plot,
                              title_font_color= graph_font,
                              title_font_size= 12,
                              title_x=0.5,
                              yaxis_title=None,
                              xaxis_title=None,
                              legend_font_color=backgroundcolor_plot,
                              legend_tracegroupgap=7,
                              showlegend=False
                              )

            fig.update_traces(line_color=line_color)

            fig.update_xaxes(visible=True,
                             fixedrange=True,
                             linecolor=grid_color,
                             tickangle=45,
                             tickfont_size=10,
                             tickfont_color=graph_font,
                             title_font_color=graph_font,
                             ticklabelstep=2,
                             gridcolor=grid_color,
                             griddash="dot",
                             gridwidth=1,
                             minor_tickcolor=backgroundcolor_plot,
                             )

            fig.update_yaxes(visible=True,
                             fixedrange=True,
                             linecolor="#000000",
                             tickfont_size=10,
                             tickfont_color=graph_font,
                             title_font_color=graph_font,
                             gridcolor=grid_color,
                             griddash="solid",
                             gridwidth=0.5,
                             )

            return fig

    fig1 = chart(1, "Areeiro")
    fig2 = chart(2, "Arroios")
    fig3 = chart(3, "Avenidas Novas")
    fig4 = chart(4, "Estrela")
    fig5 = chart(5, "Misericórdia")
    fig6 = chart(6, "Penha de França")
    fig7 = chart(7, "Santa Clara")
    fig8 = chart(8, "Santa Maria Maior")
    fig9 = chart(9, "Santo António")
    fig10 = chart(10, "São Vicente")

    return fig1, fig2, fig3, fig4, fig5, \
        fig6, fig7, fig8, fig9, fig10

app.run_server(debug=True)

if __name__=='__main__':

    app.run_server(port=8050,debug=False, use_reloader=True)
