import PySimpleGUI as sg

sg.theme('Dark Brown')
layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

print(sg.theme_list())

window = sg.Window('Theme Browser', layout)

while True:  # Event Loop

    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()
