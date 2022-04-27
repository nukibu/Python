import PySimpleGUI as sg
# Graphing Module
import matplotlib
# Some backend functionality that connects matplotlib with tkinter, which is the backbone of PySimpleGUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import table

def update_figure(data):
  axes = fig.axes
  x = [int(i[0]) for i in data]
  y = [int(i[1]) for i in data]
  #'g-' is a kind of theme. makes the plot green. dash stands for line. * would make stars on values, no lines.
  axes[0].plot(x, y, 'g-')
  figure_canvas_agg.draw()
  figure_canvas_agg.get_tk_widget().pack()

sg.theme('DarkTeal6')
table_content = []

layout = [
  [sg.Table(
  headings = ['Observation', 'Result'], 
  values = table_content, 
  expand_x=True, 
  hide_vertical_scroll=True,
  key = '-TABLE-')],
  [sg.Input(key = '-INPUT-', 
  expand_x=True), 
  sg.Button('Submit')],
  [sg.Canvas(key = '-CANVAS-')]
]

window = sg.Window('Graph App', layout, finalize = True)

#matplotlib

# Create Figure (Empty Field). Subplots can be added on the "Canvas".
fig = matplotlib.figure.Figure(figsize = (5,4))
# Position of subplot on Figure. Graphs will be added on Subplots.
fig.add_subplot(111).plot([], [])

figure_canvas_agg = FigureCanvasTkAgg(fig,window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break

  if event == 'Submit':
    new_value = values['-INPUT-']
    if new_value.isnumeric():
      table_content.append([len(table_content) + 1, float(new_value)])
      window['-TABLE-'].update(table_content)
      window['-INPUT-'].update('')
      update_figure(table_content)

window.close()