import PySimpleGUI as sg

layout = [
  [sg.Text("Text", enable_events = True, key = '-TEXT-'), sg.Spin(["Item 1", "Item 2"])], 
  [sg.Button("Button", key = '-BUTTON1-')], 
  [sg.Input(key = '-INPUT-')],
  [sg.Text('Test'), sg.Button('Test Button', key = '-BUTTON2-')]
]

#.read() draws the element on the screen. .read() also waits for events or any kind of return value. On return, python goes to next line

window = sg.Window("Converter", layout)

while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED:
    break
  if event == "-BUTTON1-":
    window['-TEXT-'].update(values['-INPUT-'])
    # disables the element
    # window['-TEXT-'].update(visible = False)
  if event == "-BUTTON2-":
    print("Test Button pressed")
  if event == "-TEXT-":
    print("Text Button pressed")

window.close()