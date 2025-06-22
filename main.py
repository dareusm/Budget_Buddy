import PySimpleGUI as sg
import psycopg2
import credentials
import sign_up 

class login():

    def __init__(self):

        # Establish connection to database
        conn = psycopg2.connect(
            dbname=credentials.db_name,
            user=credentials.username,
            password=credentials.password,
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Create Gui Parameters
        sg.theme('DarkAmber')   # Add a touch of color

        # Set Font
        font1 = ('Serpentine', 40)

        # All the stuff inside your window.
        self.text_layout = [  
                    [sg.Text('Enter your Username')],
                    [sg.Text('Enter your Password')]
                ]

        self.input_layout = [
            [sg.InputText()],
            [sg.InputText()]
        ]

        self.button_layout = [
            [sg.Button('Enter', key="ENTER"), sg.Button("Sign Up", key="SIGN UP"), sg.Button("Exit")]
        ]

        self.login_layout = [
            [sg.Text('Budget Buddy', font=font1)],
            [
            sg.Column(self.text_layout),
            sg.Column(self.input_layout)
            ],
            [sg.Text("")],
            [self.button_layout]
        ]

        # Create Window
        self.window = sg.Window("Budget Buddy", self.login_layout, element_justification='center', size=(400, 200))

        # Window loop
        running = True
        while running:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                running = False
                break

            # Set up button events
            if event == "ENTER":
                print("Enter was pressed")
            elif event == "SIGN UP":
                print("success")
                self.window.close()
                sign_up.Signup()
gui = login()
