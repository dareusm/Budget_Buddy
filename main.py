from login import Login
from sign_up import Signup
import PySimpleGUI as sg


def main():

    while True:
        login_page = Login()
        page = login_page.run()
        if page == "SIGN UP":
            signup_page = Signup()
            page = signup_page.run()

            if page == "login":
                continue
            elif page == "Exit" or page == sg.WIN_CLOSED:
                break

        elif page == "Exit" or page == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
