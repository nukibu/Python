from pydoc import visiblename
from tracemalloc import start
import PySimpleGUI as sg
from time import time

def create_window():
  sg.theme('black')
  layout = [
    [sg.Push(), sg.Image('cross.png', size=(32,32), pad = 0, enable_events=True, key = '-CLOSE-')],
    [sg.VPush()],
    [sg.Text('0.0', font='Calibri 50', key = '-TIME-')],
    [sg.Button(
      'Start', 
      button_color = ('#FFFFFF', '#FF0000'), 
      border_width=0, key = '-STARTSTOP-'), 
      sg.Button('Lap', 
      button_color = ('#FFFFFF', '#FF0000'), 
      border_width=0, key = '-LAP-', 
      visible=False)],
    [sg.Column([[]], key = '-LAPS-')],
    [sg.VPush()]
  ]

  return sg.Window(
    'Stopwatch', 
    layout,
    size = (300, 600),
    no_titlebar = True,
    element_justification='center'
  )

window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
  event, values = window.read(timeout = 10)
  if event in (sg.WIN_CLOSED, '-CLOSE-'):
    break

  if event == '-STARTSTOP-':
    # From active to stop
    if active:
      active = False
      window['-STARTSTOP-'].update('Reset')
      window['-LAP-'].update(visible=False)
    else:
      # From stop to reset
      if start_time > 0:
        window.close()
        window = create_window()
        start_time = 0
        lap_amount = 1

      else:
        # From start to active
        start_time = time()
        active = True
        window['-STARTSTOP-'].update('Stop')
        window['-LAP-'].update(visible=True)

  if active:
    elapsed_time = round(time() - start_time, 1)
    window['-TIME-'].update(elapsed_time)

  if event == '-LAP-':
    window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeperator(), sg.Text(elapsed_time)]])
    lap_amount += 1

window.close()