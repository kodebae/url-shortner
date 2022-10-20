import tkinter

root = tkinter.Tk() # creating a root window, our parent container for the UI. Every Tkinter widget must have a parent/root.
root.title("Tiny URL Shortener") # our URL title
root.geometry("350x150") # setting the size of the window, but can still resize the window manually. This will require a geometry manager. 

# main functionality of the app

longurl_label = tkinter.Label(root, text="Enter Long URL") 
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text="Your shortened URL")
shorturl_entry = tkinter.Entry(root)
shortenurl_button = tkinter.Button(root, text="Shorten URL")


root.mainloop() # how Tkinter runs apps, the infinite loop runs while the app is running.
