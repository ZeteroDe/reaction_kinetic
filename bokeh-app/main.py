import numpy as np

from bokeh.io import curdoc, output_file, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure


# Set up data
N=100
A=100
x = np.linspace(0, N, num=100) #num= Anzahl der zahlen, N= letzte zahl
y = A*np.exp(-0.1*x)
y2= (0.1*A*(np.exp(-0.1*x)-np.exp(-0.2*x)))/(0.2-0.1)
y3= A*(1+(0.1*np.exp(-0.2*x)-0.2*np.exp(-0.1*x))/(0.2-0.1))
source = ColumnDataSource(data=dict(x=x, y=y, y2=y2, y3=y3))


# Set up plot
plot = figure(height=400, width=400, title="Reaction network",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 100], y_range=[0, 101])

plot.line('x', 'y',  source=source, line_width=1, line_alpha=0.6)
plot.line('x', 'y2', source=source, line_width=1, line_alpha=0.6)
plot.line('x', 'y3', source=source, line_width=1, line_alpha=0.6)

# Set up widgets

fir = Slider(title="k1", value=0.1000000001, start=0.001, end=1, step=0.01)
sec = Slider(title="k2", value=0.2, start=0.001, end=1, step=0.01)

# Set up callbacks

def update_data(attrname, old, new):

    # Get the current slider values
    k = fir.value
    kk = sec.value

    # Generate the new curve
    x = np.linspace(0, N, num=100) #num= Anzahl der zahlen, N= letzte zahl
    y = A*np.exp(-k*x)
    y2= (k*A*(np.exp(-k*x)-np.exp(-kk*x)))/(kk-k)
    y3= A*(1+(k*np.exp(-kk*x)-kk*np.exp(-k*x))/(kk-k))

    source.data = dict(x=x, y=y, y2=y2, y3=y3)

for w in [fir, sec]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = column(fir, sec)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"


