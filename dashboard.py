import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as FigureCanvasTkAgg

class dashboard:

    def __init__(self):
        sg.theme("DarkAmber")

        # Set Font
        self.font1 = ("Serpentine", 40)
        
        self.data_layout = [[sg.Canvas(size=(200, 200), key="-CANVAS-")],
                       [sg.Text("Monthly Income")],
                       [sg.Text("Current Balance")],
                       [sg.Text("Most Recent Purchase")]
                       ]
        
        self.button_layout = [[sg.Button("Add")],
                         [sg.Button("Update")],
                         [sg.Button("Delete")]]
        
        self.dashboard_layout = [[sg.Text("Welcome User", font=self.font1)],
                  [
                      sg.Column(self.data_layout),
                      sg.Column(self.button_layout)
                  ]
                  ]

        #Create window
        running = True
        self.window = sg.Window("Budget Buddy", self.dashboard_layout, element_justification="center", size=(800, 450))
        
        while running:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break  
        
user_dashboard = dashboard()