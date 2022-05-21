import time

import toml


# config = toml.load('config.toml')

# with open('test.txt', 'w') as f:
#     f.write("test")
#
# c = 'a'
#
# a = lambda: open('test.txt', 'r').read()
# print(a())


# import requests
# # pip install requests_toolbelt
# from requests_toolbelt import MultipartEncoder
#
#
# def upload_file(host, token, filename):
#     url = f"{host}/upload"
#     fields = {
#         'personVideo': (f'{filename}', open(f'{filename}', 'rb'), 'application/mp4')
#     }
#     boundary = '----WebKitFormBoundaryJVpKw2XlPggKaD87'
#     m = MultipartEncoder(fields=fields, boundary=boundary)
#     print(m.content_type)
#     # multipart/form-data; boundary=----WebKitFormBoundaryJVpKw2XlPggKaD87
#     headers = {
#         'Authorization': 'Bearer {}'.format(token),
#         'Content-Type': m.content_type
#     }
#     r = requests.post(url, headers=headers, data=m)
#     return r.text
#
#
# if __name__ == '__main__':
#     host = 'http://101.43.208.107:8011/video_test/camera1'
#     token = 'xxxx-xxxx-xxxx-xxxx'
#     filename = 'test.txt'
#     upload_file(host, token, filename)


# def foo(num):
#     print("starting...")
#     while num < 10:
#         num = num + 1
#         yield num
#         time.sleep(1)
#
#
# for n in foo(0):
#     print(n)

# def testtest(num=0):
#     while 1:
#         num += 1
#         yield print(num)
#         time.sleep(1)
#
#
# for n in testtest(10):
#     n
#     # print(n)

import PySimpleGUI as ps
ps.theme('dark grey 9')
def make_window1():
    layout = [[ps.Text('Window 1'), ],
              [ps.Input(key='-IN-')],
              [ps.Text(size=(20, 1), key='-OUTPUT-')],
              [ps.Button('Launch 2'), ps.Button('Output')]]
    return  ps.Window("window_1", layout, finalize=True)

def make_window2():
    layout = [[ps.Text('Window 2')],
              [ps.Button('Exit')]]

    return ps.Window('Window 2', layout, finalize=True)

def run():

    window2=None
    window1 = make_window1()

    while True:
        window, event, values = ps.read_all_windows()
        if event == ps.WIN_CLOSED and window == window1:
            break

        if window == window1:
            window1['-OUTPUT-'].update(values['-IN-'])

        if event == 'Launch 2' and not window2:
            window1.hide()
            window2 = make_window2()

        if window == window2 and (event in (ps.WIN_CLOSED, 'Exit')):
            window2.close()
            window2 = None
            window1.un_hide()
    window1.close()
    pass


if __name__ == '__main__':
    run()

