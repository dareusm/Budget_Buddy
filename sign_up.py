import PySimpleGUI as sg
import psycopg2
import credentials


class Signup:

    def __init__(self):
        # Establish connection to database
        conn = psycopg2.connect(
            dbname=credentials.db_name,
            user=credentials.username,
            password=credentials.password,
            host="localhost",
            port="5432",
        )
        cur = conn.cursor()

        # Set Font
        font1 = ("Serpentine", 40)

        # Set up sign up page
        self.sign_up_column = [
            [sg.Text("First Name")],
            [sg.Text("Last Name")],
            [sg.Text("Email")],
            [sg.Text("Username")],
            [sg.Text("Password")],
            [sg.Text("Confirm Password")],
            [sg.Text("Birthday (YYYY-MM-DD)")],
        ]

        first_name_input = [sg.InputText(key="first_name")]
        last_name_input = [sg.InputText(key="last_name")]
        email_input = [sg.InputText(key="email")]
        username_input = [sg.InputText(key="username")]
        password_input = [sg.InputText(key="password")]
        conf_password_input = [sg.InputText(key="conf_password")]
        birthday_input = [sg.InputText(key="birthday")]

        self.fill_out_column = [
            first_name_input,
            last_name_input,
            email_input,
            username_input,
            password_input,
            conf_password_input,
            birthday_input,
        ]

        self.sign_up_layout = [
            [sg.Text("Sign Up", font=font1, justification="center", expand_x=True)],
            [sg.Text("")],
            [sg.Column(self.sign_up_column), sg.Column(self.fill_out_column)],
            [sg.Text("")],
            [sg.Push(), sg.Button("Enter", key="SIGN_UP_ENTER", size=(10, 2))],
        ]

        self.window = sg.Window("Budget Buddy", self.sign_up_layout, size=(600, 380))

        # Set Loop
        running = True
        while running:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                running = False
                break

            if event == "SIGN_UP_ENTER":
                password_in = values["password"]
                conf_password_in = values["conf_password"]
                first_name_in = values["first_name"]
                last_name_in = values["last_name"]
                email_in = values["email"]
                username_in = values["username"]
                birthday_in = values["birthday"]
                if not all ([first_name_in, last_name_in, email_in, username_in, birthday_in]):
                    sg.popup("Please fill in all fields")
                elif password_in != conf_password_in:
                    sg.popup("Passwords do not match!")
                else:
                    print("success")
                    
                    cur.execute("INSERT INTO users (firstname, lastname, email, username, password, birthday) VALUES (%s, %s, %s, %s, %s, %s)", (first_name_in, last_name_in, email_in, username_in, password_in, birthday_in))
                    conn.commit()
                    conn.close()
                    
