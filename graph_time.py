# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:09:27 2020

@author: jdroj
"""
import plotly.graph_objects as go 

def graph_time_experience(dictionary):
    
    colors = ['gray','rgba(88,107,164,1)','rgba(50,67,118,1)' ,'rgba(245,221,144,1)', 'rgba(246,142,95,1)','rgba(247,108,94,1)']
    
    #y_data = ['2016','2017','2018','2019','2020']
    y_data = [2016,2017,2018,2019,2020]
    descripciones=set([''])
    for yd in y_data:
        for _,ay,_,_ in dictionary[yd]:
            descripciones.add(ay)
    
    
    fig2 = go.Figure()
    
    for yd in y_data:
        for i in range(0, len(dictionary[yd])):
            if dictionary[yd][i][1]=='':
                texto=''
            else:
                texto=dictionary[yd][i][1]+'<br>'+dictionary[yd][i][2]+'<br>'+dictionary[yd][i][3]
            fig2.add_trace(go.Bar(
                x=[dictionary[yd][i][0]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[list(descripciones).index(dictionary[yd][i][1])],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                ),
                hoverinfo='text',
                hovertext=[texto]
            ))
    fig2.update_layout(
        xaxis=dict(
            showgrid=True,
            showline=False,
            showticklabels=True,
            zeroline=False,            
            domain=[0, 1],
            tickmode='array',
            tickvals=[-1,0,1,2,3,4,5,6,7,8,9,10,11],
            ticktext=['','January','February','March','April','May','June','July','August','September','October','November','December'],
            tickfont=dict( size=12, color='black'),#family='Arial',
            gridwidth=0.9,
            tickangle=-90
        ),
        height=280,
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
    )
    
    
    annotations = []
    
    #annotations.append()
    
    for yd in y_data:
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='paper',
                                x=-0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict( size=14,#family='Arial',
                                          color='black'),
                                showarrow=True, align='right'))
    
    
    
    fig2.update_layout(annotations=annotations)
            
    return fig2