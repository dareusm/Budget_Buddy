import PySimpleGUI as sg
import mysql.connector

#Establish connection ot database
db = mysql.connector.connect(
    host = "DESKTOP-M2FOQCA",
    user = "DESKTOP-M2FOQCA\Dareus Morris",
    password = ""
)

#Create cursor
cursor = db.cursor()

#Create Gui Parameters
sg.theme('DarkAmber')   # Add a touch of color

#Set Font
font1 = ('Serpentine', 40)

# All the stuff inside your window.
layout = [  
            [sg.Text('Budget Buddy', font=font1)]
            [sg.Text('Enter your name'), sg.InputText()],
            [sg.Text('Enter your password'), sg.InputText()],
            [sg.Button('Enter'), sg.Button('Sign Up')]
            [sg.Button('Exit')]
        ]

#Create Window
window = sg.Window("Budget Buddy", layout, vertical_alignment='center', element_justification='center')

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    


