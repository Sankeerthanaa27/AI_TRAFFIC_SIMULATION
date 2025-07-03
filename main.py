from tkinter import *
from tkinter import filedialog
from traffic_simulation import Simulation
from yolo_traffic import runYolo  # Assuming you define runYolo in yolo_traffic.py

def yoloTrafficDetection():
    global filename
    filename = filedialog.askopenfilename(initialdir="Videos", title="Select Traffic Video")
    if filename:
        pathlabel.config(text=filename)
        text.delete('1.0', END)
        text.insert(END, f"{filename} loaded\n")
        runYolo(filename)
    else:
        text.insert(END, "No file selected\n")

def runSimulation():
    sim = Simulation()
    sim.runSimulation()

def exitApp():
    main.destroy()

# Main window setup
main = Tk()
main.title("Smart Control of Traffic Light Using Artificial Intelligence")
main.geometry("1300x700")
main.config(bg='snow3')

font_title = ('times', 16, 'bold')
font_btn = ('times', 14, 'bold')
font_text = ('times', 12, 'bold')

# Title label
title = Label(main, text='Smart Control of Traffic Light Using Artificial Intelligence', bg='light cyan', fg='pale violet red', font=font_title, height=3, width=120)
title.place(x=0, y=5)

# Buttons
simulationButton = Button(main, text="Run Traffic Simulation", command=runSimulation, font=font_btn)
simulationButton.place(x=50, y=100)

yoloButton = Button(main, text="Run YOLO Traffic Detection & Counting", command=yoloTrafficDetection, font=font_btn)
yoloButton.place(x=300, y=100)

exitButton = Button(main, text="Exit", command=exitApp, font=font_btn)
exitButton.place(x=750, y=100)

# Path label for selected video
pathlabel = Label(main, bg='light cyan', fg='pale violet red', font=font_btn)
pathlabel.place(x=300, y=150)

# Text box with scrollbar for logs and output
text = Text(main, height=25, width=150, font=font_text)
text.place(x=10, y=200)

scroll = Scrollbar(main, command=text.yview)
scroll.place(x=1240, y=200, height=400)
text.config(yscrollcommand=scroll.set)

main.mainloop()
