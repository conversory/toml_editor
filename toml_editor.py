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
    def __init__(self, list1):
        self.config = list1
        self.list1 = []
        for i in list1:
            self.list1.append(i)
        self.list1.append("")
        print(self.list1)
        self.list2 = []
        self.window = self.generate_window_main()
        pass

    def generate_window_main(self):
        self.a = sg.Listbox(self.list1, size=(20, 12), key='-LIST-', enable_events=True)
        self.b = sg.Listbox(self.list2, size=(20, 12), key='sublist')
        self.col1 = Column([[sg.Button('刷新', font=('宋体', 18))],
                            [sg.Button('增加', font=('宋体', 18))],
                            [sg.Button('修改', font=('宋体', 18))],
                            [sg.Button('删除', font=('宋体', 18))]])

        self.layout = [[self.col1, self.a, self.b]]
        return Window('配置文件修改', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                break
            if event == '修改':
                try:
                    temp = self.config[values['-LIST-'][0]]
                    print(type(temp))
                    print(type(type(temp)))
                    try:
                        temp2 = self.config[values['-LIST-'][0]][temp]
                    except:
                        sg.popup('最后一级')
                        pass
                    else:
                        aa = window_show(self.config[values['-LIST-'][0]])
                        aa.run()
                except:
                    sg.popup('最后一级')
                    pass
            if event == '增加':
                if values['-LIST-'][0] == "":
                    temp = sg.popup_get_text('输入增加值')
                    # print(temp)
                    self.list1[-1] = temp
                    self.list1.append("")
                    print(self.list1)
                else:
                    pass
            if event == '-LIST-':
                self.list2 = []
                a = values['-LIST-'][0]
                try:
                    for i in self.config[a]:
                        try:
                            temp = self.config[a][i]
                        except:
                            self.list2.append(self.config[a])
                            break
                        else:
                            self.list2.append(i)
                except:
                    self.list2 = []
                # print(self.list2)
                self.window['sublist'].update(values=self.list2)

        self.window.close()

    def refresh(self):
        pass

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass


if __name__ == '__main__':
    test = toml.load("config.toml")
    window1 = window_show(test)
    window1.run()
