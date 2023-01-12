import PySimpleGUI as sg
import mysql.connector

#Establish connection ot database
"""
db = mysql.connector.connect(
    host = "DESKTOP-M2FOQCA",
    user = "DESKTOP-M2FOQCA\Dareus Morris",
    password = ""
)
"""
#Create cursor
#cursor = db.cursor()

#Create Gui Parameters
sg.theme('DarkAmber')   # Add a touch of color

#Set Font
font1 = ('Serpentine', 40)

# All the stuff inside your window.
text_layout = [  
            [sg.Text('Budget Buddy', font=font1)],
            [sg.Text('Enter your name')],
            [sg.Text('Enter your password')],
        ]

input_layout = [
    [sg.InputText()],
    [sg.InputText()]
]

button_layout = [
    [sg.Button('Enter'), sg.Button('Sign Up', key='SIGN UP')],
    [sg.Button('Exit')]
]

layout = [
    sg.Column()
]

#Create Window
window = sg.Window("Budget Buddy", layout, element_justification='center')

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == 'Sign Up':
        window.close()
        sg.Popup('Sign Up')
        
        


