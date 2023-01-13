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
            [sg.Text('Enter your Username')],
            [sg.Text('Enter your Password')]
        ]

input_layout = [
    [sg.InputText()],
    [sg.InputText()]
]

button_layout = [
    [sg.Button('Enter', key="ENTER"), sg.Button("Sign Up", key="SIGN UP"), sg.Button("Exit")]
]

login_layout = [
    [sg.Text('Budget Buddy', font=font1)],
    [
    sg.Column(text_layout),
    sg.Column(input_layout)
    ],
    [sg.Text("")],
    [button_layout]
]



sign_up_column = [
    [sg.Text('First Name')],
    [sg.Text('Last Name')],
    [sg.Text('Username')],
    [sg.Text('Password')],
    [sg.Text('Confirm Password')],
]

fill_out_column = [
    [sg.InputText()],
    [sg.InputText()],
    [sg.InputText()],
    [sg.InputText()],
    [sg.InputText()]
]

sign_up_layout = [
    [sg.Text("Sign Up", font=font1, justification='center')],
    [sg.Column(sign_up_column), sg.Column(fill_out_column)],
    [sg.Button("Enter", key="SIGN_UP_ENTER")]    
]


#Create Window
window = sg.Window("Budget Buddy", login_layout, element_justification='center', size=(400, 200))

#Window loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    #Set up button events
    if event == "ENTER":
        print("Enter was pressed")
    elif event == "SIGN UP":
        window.close()
        sign_up_window = sg.Window("Budget Buddy", sign_up_layout, size=(600, 300)).read()
        #Loop for sign up window
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event == "SIGN_UP_ENTER":
                print("Entered in Database")
                
        


