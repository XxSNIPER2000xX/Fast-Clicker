import tkinter as tk
from tkinter import W

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

import time

def buttonToggle(toggle=False):
    global g_tracking_var
    global g_counter
    if toggle:
        if g_tracking_var:
            g_tracking_var = False
            print("done clicking")
            g_counter = 0
        else:
            g_tracking_var = True

    if g_tracking_var:
        if g_counter == 0:
            time.sleep(1) # delay 1 second before clicking
            g_counter += 1
        clicker()
        root.after(5, buttonToggle) # adjust speed by editing the first variable (delay in ms)

def clicker():
    g_mouse.press(Button.left)
    g_mouse.release(Button.left)
    print("click")

####################################################################
#
# GLOBALS
#
####################################################################
g_tracking_var = False
g_counter = 0
g_mouse = Controller()

####################################################################
#
# UI STUFF
#
####################################################################
root = tk.Tk()
root.resizable(False, False)
root.title('Fast Clicker')

canvas = tk.Canvas(root, bg="blue", height=200, width=400)
canvas.pack()

#canvas.create_text(20, 30, anchor=W, font="Times", text="Toggle (F10)")

toggle_on = tk.Button(root, text="Toggle On", fg="#263d42", bg="white", command=lambda:buttonToggle(True)).pack()

root.mainloop()
