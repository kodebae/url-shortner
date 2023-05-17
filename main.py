import tkinter as tk
import string
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

def shorten_url():
    long_url = entry.get()
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    result_label.config(text=f"Short URL: {short_url}", fg="green")

def redirect_url():
    short_url = entry.get()
    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        result_label.config(text=f"Redirecting to: {long_url}", fg="blue")
        # Add your redirection logic here
    else:
        result_label.config(text="Invalid URL", fg="red")

url_mapping = {}

# Create the main window
window = tk.Tk()
window.title("URL Shortener")
window.configure(bg="#F0F0F0")

# Create GUI elements
label = tk.Label(window, text="Enter a URL:", fg="black", bg="#F0F0F0")
label.pack()

entry = tk.Entry(window, width=40)
entry.pack()

shorten_button = tk.Button(window, text="Shorten", command=shorten_url, fg="white", bg="green")
shorten_button.pack()

redirect_button = tk.Button(window, text="Redirect", command=redirect_url, fg="white", bg="blue")
redirect_button.pack()

result_label = tk.Label(window, text="", fg="black", bg="#F0F0F0")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()


