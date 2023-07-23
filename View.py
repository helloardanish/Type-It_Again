from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import random
import pyautogui as pau
from datetime import datetime
import sys
from tkinter import Entry, ttk
import tkinter as tk
from ttkbootstrap import Style
from tkcalendar import DateEntry
from ttkbootstrap.constants import *
from ttkbootstrap.constants import *
import threading
import Operation as op



class View:

    def __init__(self,root,keyControl):
        self.root = root
        self.keyControl = keyControl
        self.countTill = 5
       
        self.fixedSize(self.root) #Fixed size
        self.disableResizing(self.root) #Disable resizing
        
        self.countRow=0
        # Create a Text widget
        self.text_entry = tk.Text(self.root, height=30, width=52, wrap="word")
        self.text_entry.grid(row=self.countRow, column=0, padx=10, pady=10)
        #text_entry.pack(padx=10, pady=10)

        self.countRow+=1


        # Create a Submit button
        # submit_button = ttk.Button(self.root, text="Type It!", command=self.submit_text)
        self.typeit_button = ttk.Button(self.root, text="Type It!", command=self.start_countdown)
        self.typeit_button.grid(row=2, column=0)
        #submit_button.pack()
        
        self.countRow+=1

        #Close button
        self.close_btn_frame = ttk.Frame(self.root, width=200, height=100, borderwidth=1, padding=10)
        self.close_btn_frame.grid(row=3, column=0)


        self.close_btn = ttk.Button(self.close_btn_frame, text="Close It", style='Warning-outline.TButton', command=lambda: self.closeIt(self.root))
        self.close_btn.grid(row=3, column=0)

        self.countRow+=2

        self.counter_label = tk.Label(self.root, text="", font=("Arial", 20))
        # Use grid to place the counter_label
        self.counter_label.grid(row=5, column=0, pady=20)

        # Bind a function to the key press event for the Text widget
        self.text_entry.bind("<Key>", self.on_key_press)
    


    def disableResizing(self,rootRef):
        rootRef.resizable(False, False)

    def fixedSize(self,rootRef):
        window_width = 400
        window_height = 600
        rootRef.geometry(f"{window_width}x{window_height}")


    def closeIt(self,rootRef):
        rootRef.destroy()



    def submit_text(self):
        text = text_entry.get("1.0", tk.END)  # Get the text from the Text widget
        print("Submitted text:")
        print(text)


    def start_countdown(self):
        #RESET to 10
        self.countTill = 5
        # Disable the typeit_button after it is clicked
        self.typeit_button.config(state=tk.DISABLED)
        self.update_counter()


    def on_key_press(self, event):
        text = self.text_entry.get("1.0", tk.END)
        if len(text) > 10000:
            self.text_entry.delete("1.0", tk.END)  # Clear the existing text
            self.text_entry.insert("1.0", "Please enter less than 10000 letters.")  #
            #return "break"

    def update_counter(self):
        self.countTill -= 1
        if self.countTill >= 1:
            self.counter_label.config(text=f"Typing starting in: {self.countTill}")
            self.root.after(1000, self.update_counter)  # Update every 1000 milliseconds (1 second)
        elif self.countTill==0:
            self.counter_label.config(text=f"Started!")
            # Re-enable the typeit_button when countdown completes
            self.typeit_button.config(state=tk.NORMAL)
            #self.root.after(1000, self.update_counter) #For Typing
            enteredText = self.text_entry.get("1.0", tk.END)
            opObj = op.Operation()
            completed = opObj.autoType(self.keyControl,enteredText)
            if(completed):
                self.counter_label.config(text="Completed!")
            else:
                self.counter_label.config(text="Failed! Too Much Characters.")

        
    
'''
Extra:
        #root = ttk.Window()
        # Create a style object from ttkbootstrap
        #style = Style(theme='yeti')
'''

'''
if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()

'''