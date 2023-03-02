# from tkinter import *
import tkinter
import pyshorteners

def shorten_url():
    shortner = pyshortners.Shortener() # instance of Shorten class
    short_url = shortner.tinyurl.short(longurl_entry.get()) # passing in long url, wrapper for tiny url API
    print(shorturl_entry.insert(0, short_url))

root = tkinter.Tk() # creating a root window, our parent container for the UI. Every Tkinter widget must have a parent/root.
root.title("Tiny URL Shortener") # our URL title
root.geometry("300x150") # setting the size of the window, but can still resize the window manually. This will require a geometry manager. 
root.configure(background="red")

# main functionality of the app

longurl_label = tkinter.Label(root, text="Enter Long URL") 
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text="Your shortened URL")
shorturl_entry = tkinter.Entry(root)
shortenurl_button = tkinter.Button(root, text="Shorten URL", command=shorten_url)

# placing widgets on the screen and centering them with pack geometry manager.

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shortenurl_button.pack()

# how Tkinter runs apps, the infinite loop runs while the app is running.

root.mainloop() 
