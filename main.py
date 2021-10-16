
from PySimpleGUI import *

theme('Default')

layout = [
    [Text("", size=(1, 1))],
   [Text("Hello World")],
   [Text("", size=(1, 1))],
   [InputText(key="input")],
   [Text("", size=(1, 1))],
   [Button("Click Me!")],
   [Text("", size=(1, 1))],
   [Text("", size=(None, None), key="Show")]
    
]
window = Window("Test", layout, element_justification='c').Finalize()
window.Maximize()

while True:
    event, value = window.read()
    if event == "Click Me!":
        window["Show"].update(value["input"])
    if event == WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()
