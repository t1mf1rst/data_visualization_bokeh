# bokeh - library for interactive visualization in web browser, builging graphs
# 1. create jupyter notebook: jupyter notebook
# 2. New -> Python 3
# 3. Type in label:

# *** Building graph with circle points ***
from bokeh.plotting import figure, output_file, show

p = figure(plot_width=500, plot_height=400, logo=None, tools='pan, save, zoom_in, zoom_out, box_zoom, reset')

p.title.text = "Earthquake"
p.title.text_color = "Orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"

p.yaxis.minor_tick_line_color = "Yellow"

p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"

p.circle([1, 2, 3, 4, 5], [6, 7, 8, 9, 6], size=[i * 2 for i in[8, 12, 14, 15, 20]], color="red", alpha=0.5)

output_file("Scatter_plotting.html", mode="absolute")
show(p)

# *** Building line graph***
from bokeh.plotting import figure, output_file, show

p = figure(plot_width=500, plot_height=400, logo=None, tools='pan, save, zoom_in, zoom_out, box_zoom, reset')

p.title.text = "Earthquake"
p.title.text_color = "Orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"

p.yaxis.minor_tick_line_color = "Yellow"

p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"

p.line([1, 2, 3, 4, 5], [6, 7, 8, 9, 6], line_width=2, color="red", alpha=0.5)
# to show multiple graph on the same plot just add them like this one after one
p.circle([1,2,3,4,5], [6,7,8,9,6], size=[i*2 for i in[8,12,14,15,20]], color="red", alpha=0.5)

output_file("Scatter_plotting.html", mode="absolute")
show(p)

# *** Building chart ***
from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.read_csv("linkhere")

p = figure(width=500, height=250, x_axis_type="datetime", responsive=True)

p.line(df["Date"], df["Close"], color="Orange", alpha=0.5)

output_file("Timeseries.html")
show(p)
