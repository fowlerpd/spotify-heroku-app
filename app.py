
# coding: utf-8

# In[72]:

import pandas as pd
from bokeh.plotting import figure,show
from bokeh.palettes import Spectral11
from bokeh.embed import components
from bokeh.layouts import row, column,gridplot
from bokeh.models import ColumnDataSource, HoverTool, Legend
from flask import Flask,render_template,request,redirect,session


app = Flask(__name__)

tools = "pan,wheel_zoom,reset,hover,save"
df = pd.read_csv('genres_by_year.csv')
#app.vars={}


@app.route('/')
def render_plot():
    source = ColumnDataSource(df)

    i = 0
    p = figure(title='Streams by Genre', plot_width = 800, plot_height = 600, tools = tools,
            x_axis_label='Release Year',y_axis_label = 'Number of Streams')#x_axis_type='datetime')
    for col in df.columns[1:]:
        p.line(x='release_year', y=col, source= source, legend = col, line_width=2,line_color=Spectral11[i])
        i+=1
        
    p.legend.orientation = "horizontal"
    hover = p.select_one(HoverTool)
    hover.tooltips = [('Release Year','$x{int}'),("Number of Streams", "$y{0.2f}")]
    script, div = components(p)
    return render_template('plot.html', script=script, div=div)

  
if __name__ == '__main__':
    app.run(port=33507)





