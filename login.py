import PySimpleGUI as sg
import psycopg2
import credentials
from db_access import DBAccess
import dashboard

conn = None
cur = None

# Establish connection to database
db = DBAccess()
db.connect()
"""
conn = psycopg2.connect(
    dbname=credentials.db_name,
    user=credentials.username,
    password=credentials.password,
    host="localhost",
    port="5432",
)
cur = conn.cursor()
"""
class Login:

    def __init__(self):
        # Create Gui Parameters
        sg.theme("DarkAmber")  # Add a touch of color

        # Set Font
        font1 = ("Serpentine", 40)

        # All the stuff inside your window.
        self.text_layout = [
            [sg.Text("Enter your Username")],
            [sg.Text("Enter your Password")],
        ]

        self.input_layout = [[sg.InputText(key="USERNAME")], [sg.InputText(key="PASSWORD")]]

        self.button_layout = [
            [
                sg.Button("Enter", key="ENTER"),
                sg.Button("Sign Up", key="SIGN UP"),
                sg.Button("Exit"),
            ]
        ]

        self.login_layout = [
            [sg.Text("Budget Buddy", font=font1)],
            [sg.Column(self.text_layout), sg.Column(self.input_layout)],
            [sg.Text("")],
            [self.button_layout],
        ]

        # Create Window
        self.window = sg.Window(
            "Budget Buddy",
            self.login_layout,
            element_justification="center",
            size=(400, 200),
        )

    # Loop to run login page
    def run(self):
        # Window loop
        running = True
        while running:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                running = False
                break

            # Set up button events
            if event == "ENTER":
                username_input = values["USERNAME"] #To Check password for this particular username
                password_input = values["PASSWORD"]
                print("HIT")
                db.cur.execute(
                    "SELECT password FROM users WHERE username = %s", (username_input,)
                )
                result = db.cur.fetchone()
                
                if result:
                    db_password = result[0]
                    if password_input == db_password:
                        self.window.close()
                        print("Success")
                        dashboard.Dashboard()
                        db.conn.commit()
                        db.conn.close()
                    else:
                        sg.Popup("Username and Password Do Not Match!")
                            
            elif event == "SIGN UP":
                self.window.close()
                db.conn.commit()
                db.conn.close()
                return "SIGN UP"


# gui = login.run()
