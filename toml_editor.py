# this one long import has the effect of making the code more compact as there is no 'sg.' prefix required for Elements
import encodings

import PySimpleGUI as sg
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, \
    Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, \
    OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, \
    TreeData, VerticalSeparator, Window, Sizer
import toml

sg.theme('GreenTan')

# test = toml.load("config1.toml")
# with open("config2.toml", 'w', encoding='utf-8') as f:
#     r = toml.dump(test, f)


class window_show:
    def __init__(self, list):
        self.window = self.generate_window_main()
        self.list = list
        pass

    def generate_window_main(self):
        a = Text('sdjfkalsjdfkla')
        a = sg.Listbox(self.list)
        col1 = Column([[sg.Button('刷新')],
                       [sg.Button('增加')],
                       [sg.Button('修改')],
                       [sg.Button('删除')]])

        layout = [[col1, a]]
        return Window('配置文件修改', layout)

    def run(self):
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                break
            if event == '增加':
                aa = window_show(self)
                aa.run()
        self.window.close()


if __name__ == '__main__':
    test = toml.load("config1.toml")
    window1 = window_show(test)
    window1.run()
