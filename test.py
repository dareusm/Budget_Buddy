import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the layout of the GUI
layout = [
    [sg.Canvas(size=(400, 400), key="-CANVAS-")],
    [sg.Button("Plot"), sg.Button("Exit")],
]

# Create the GUI window
window = sg.Window("Matplotlib Example", layout, finalize=True)

# Main event loop
while True:
    event, values = window.read()

    # Exit if the window is closed or 'Exit' button is clicked
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    # Plot the data if 'Plot' button is clicked
    if event == "Plot":
        # Create some sample data
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]

        # Create a Matplotlib figure and plot the data
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Sample Plot")

        # Convert the Matplotlib figure to a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, window["-CANVAS-"].TKCanvas)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

# Close the GUI window
window.close()
