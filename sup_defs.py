import plotly.express as px
import plotly.graph_objects as go

def box_plot(dataf, y, color, title, height=600, width=1000):
    fig = px.box(dataf,  
                 y=y,
                 color=color,
                 title=title,
                 color_discrete_sequence=['#20bf6b', '#fa8231', '#3867d6', '#eb3b5a'], 
                 points="all"
                )
    fig.update_layout(height = height, 
                      width = width,
                      font_color='#484848',
                      template='plotly_white'
                     )
    return fig

def bar_plot(dataf, x, y, color, title, x_label='X', y_label='Y', height=600, width=1000):
    fig = px.bar(dataf, 
                 x=x, 
                 y=y, 
                 color=color,
                 title=title,
                 color_discrete_sequence=['#20bf6b', '#fa8231', '#3867d6', '#eb3b5a'],
                 barmode="group"
                )
    fig.update_layout(height = height, 
                      width = width,
                      xaxis_title=x_label,
                      yaxis_title=y_label,
                      font_color='#484848',
                      template='plotly_white',
                     )
    return fig

def scatmat_plot(dataf, dimensions, color, title, height = 1500, width = 1500):
    fig = px.scatter_matrix(dataf,
                            dimensions=dimensions,
                            color=color,
                            title=title,
                            color_discrete_sequence=['#20bf6b', '#fa8231', '#3867d6', '#eb3b5a']
                           )
    fig.update_traces(diagonal_visible=False)
    fig.update_layout(height = height, 
                      width = width,
                      font_color='#484848',
                      template='plotly_white'
                     )
    return fig

def corr_plot(x, y , z, title, height = 900, width = 900):
    trace = go.Figure(go.Heatmap(x=x,
                                 y=y,
                                 z=z,
                                 colorscale=px.colors.diverging.PRGn,
                                 zmin=-1,
                                 zmax=1,
                                ))
    trace.update_layout(title=title,
                        height = height, 
                        width = width,
                        font_color='#484848',
                       )
    trace.update_traces(text=z,
                        texttemplate="%{text:.2f}",
                        hovertemplate=None,
                       )
    return trace

def scree_plot(x, y , height = 500, width = 500):
    fig = go.Figure(data=go.Scatter(x=x, 
                                    y=y,
                                    mode='lines+markers'))
    fig.update_layout(title='Scree Plot',
                      height = height, 
                      width = width,
                      font_color='#484848',
                      template='plotly_white',
                      xaxis_title='Principal Component',
                      yaxis_title='Variance Explained',
                     )
    fig.update_traces(marker=dict(color='#46B3B3'))
    return fig

def line_plot(x, y , title, xaxis_title, yaxis_title, height = 500, width = 500):
    fig = px.line(x=x,
                  y=y, 
                  text=y)
    fig.update_layout(title=title,
                      height = height, 
                      width = width,
                      font_color='#484848',
                      template='plotly_white',
                      xaxis_title=xaxis_title,
                      yaxis_title=yaxis_title,
                     )
    fig.update_traces(line=dict(color='#46B3B3'),
                      textposition='top right')
    return fig

def scat_plot(dataf, x, y, color, title, height=600, width=1000):
    fig = px.scatter(dataf,  
                     x=x, 
                     y=y,
                     title=title, 
                     color='Clusters', 
                     color_discrete_sequence=['#20bf6b', '#fa8231', '#3867d6', '#eb3b5a']
                    )
    fig.update_layout(height = height, 
                      width = width,
                      font_color='#484848',
                      template='plotly_white'
                     )
    return fig

def pie_plot(labels, values, title, height=400, width=400):
    fig = go.Figure(go.Pie(labels=labels, 
                           values=values,
                           marker_colors=['#20bf6b', '#fa8231', '#3867d6', '#eb3b5a'],
                           hole=.1,
                           sort=False
                          ))
    fig.update_layout(height = height,
                      width=width,
                      title=title,
                      font_color='#484848',
                      template='plotly_white',
                      showlegend=False,
                     )
    fig.update_traces(textinfo='label+value+percent',
                      textfont_size=14
                     )
    return fig