import PySimpleGUI as sg
import psycopg2
import credentials

class login_signup():

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

        # Set up sign up page
        self.sign_up_column = [
            [sg.Text('First Name')],
            [sg.Text('Last Name')],
            [sg.Text('Username')],
            [sg.Text('Password')],
            [sg.Text('Confirm Password')],
        ]

        first_name_input = [sg.InputText()]
        last_name_input = [sg.InputText()]
        username_input = [sg.InputText()]
        password_input = [sg.InputText()]
        conf_password_input = [sg.InputText()]

        self.fill_out_column = [
            first_name_input,
            last_name_input,
            username_input,
            password_input,
            conf_password_input,
        ]

        self.sign_up_layout = [
            [sg.Text("Sign Up", font=font1, justification='center')],
            [sg.Column(self.sign_up_column), sg.Column(self.fill_out_column)],
            [sg.Button("Enter", key="SIGN_UP_ENTER")]    
        ]

        # Create Window
        self.window = sg.Window("Budget Buddy", self.login_layout, element_justification='center', size=(400, 200))

        # Window loop
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            # Set up button events
            if event == "ENTER":
                print("Enter was pressed")
            elif event == "SIGN UP":
                self.window.close()
                sign_up_window = sg.Window("Budget Buddy", self.sign_up_layout, size=(600, 300)).read()
                # Loop for sign up window
                while True:
                    event, values = self.window.read()
                    if event == sg.WIN_CLOSED:
                        break

                    if event == "SIGN_UP_ENTER":
                        if password_input != conf_password_input:
                            sg.popup('Passwords do not match!')
                        else:
                            cur.execute("INSERT INTO users (firstname, lastname, username, password) VALUE (%s, %s, %s, %s)", (first_name_input, last_name_input, username_input, password_input))
                            print('success')

gui = login_signup()
