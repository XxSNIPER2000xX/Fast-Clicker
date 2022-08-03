import tkinter as tk
from tkinter import Text

from pynput.mouse import Button, Controller

import time

def buttonToggle(toggle=False):
    global tracking_var
    global g_counter
    if toggle:
        if tracking_var:
            tracking_var = False
            print("done clicking")
            g_counter = 0
        else:
            tracking_var = True

    if tracking_var:
        if g_counter == 0:
            time.sleep(1) # delay 1 second before clicking
            g_counter += 1
        clicker()
        root.after(5, buttonToggle) # adjust speed by editing the first variable (delay in ms)

def clicker():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)
    print("click")

####################################################################
#
# UI STUFF DOWN HERE
#
####################################################################
root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

tracking_var = False
g_counter = 0
toggle_on = tk.Button(root, text="Toggle On", padx=10, pady=5, relief="raised", fg="#263d42", bg="white", command=lambda:buttonToggle(True)).pack()

root.mainloop()
