# Coding Exercise 16.1
# Write a script that generates the following GUI.

import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input_box_1 = sg.InputText()

label2 = sg.Text("Enter inches: ")
input_box_2 = sg.InputText()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor", 
                            layout=[[label1, input_box_1],
                            [label2, input_box_2],
                            [convert_button]])

window.read()
window.close()