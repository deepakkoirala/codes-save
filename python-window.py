# # Import module
# from tkinter import *

# # Create object
# root = Tk()
# root.title("Title")
# #root.overrideredirect(True)


# # Adjust size
# root.geometry("400x400+1500+500")

# #root.resizable(True, True)


# # Create transparent window
# root.attributes('-alpha',0.5)

# # Execute tkinter
# root.mainloop()

# Import tkinter and webview libraries
from tkinter import *
import webview
from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2


# define an instance of tkinter
root = tk.Tk()

# size of the window where we show our website

root.overrideredirect(True)

# Adjust size
root.geometry("400x400+1500+500")

root.attributes('-topmost', True)

#root.resizable(True, True)


# Create transparent window
root.attributes('-alpha',0.5)

frame = HtmlFrame(root) #create HTML browser

frame.load_website("http://localhost:8080") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window

root.mainloop()


# Open website
# webview.create_window('Geeks for Geeks', 'http://localhost:8080/transparent.html',  transparent=True, frameless=True)
# webview.start()


