from tkinter import Tk, Label, Entry, Button, StringVar
from flask import Flask, redirect
import shortuuid
import threading

app = Flask(__name__)
url_mapping = {}
short_url_prefix = "http://localhost:5000/"

def run_flask():
    app.run(port=5000)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return 'URL not found'

def generate_short_url():
    return shortuuid.uuid()[:8]

def shorten_url():
    long_url = entry.get()
    if long_url:
        short_url = generate_short_url()
        url_mapping[short_url] = long_url
        output_var.set(f'Shortened URL: {short_url_prefix}{short_url}')
    else:
        output_var.set('Invalid URL')

# Start Flask in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Create the Tkinter GUI
root = Tk()
root.title("Link Shortener")

label = Label(root, text="Enter URL:")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=10)

shorten_button = Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

output_var = StringVar()
output_label = Label(root, textvariable=output_var)
output_label.pack(pady=10)

root.mainloop()
