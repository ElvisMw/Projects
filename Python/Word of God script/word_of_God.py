#!/usr/bin/python3


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import requests
import os

class WordOfGodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word of God App")

        # Variables
        self.file_name_var = tk.StringVar(value="Word_of_God.txt")

        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#333')
        self.style.configure('TButton', background='#3498db', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 12))

        # Create frame
        self.main_frame = ttk.Frame(root, padding=(20, 10))
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # File name entry
        self.file_name_entry = ttk.Entry(self.main_frame, width=30, textvariable=self.file_name_var)
        self.file_name_entry.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Text widget to display and write the verse
        self.verse_text = tk.Text(self.main_frame, wrap=tk.WORD, width=40, height=10)
        self.verse_text.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Run button
        self.run_button = ttk.Button(self.main_frame, text="Run Word of God", command=self.run_word_of_god)
        self.run_button.grid(row=1, column=0, pady=(10, 0))

        # Exit button
        self.exit_button = ttk.Button(self.main_frame, text="Exit", command=root.destroy)
        self.exit_button.grid(row=1, column=1, pady=(10, 0))

    def run_word_of_god(self):
        file_name = self.file_name_var.get()
        try:
            verse_content = WordOfGod.print_word_of_god(file_name)
            self.verse_text.delete(1.0, tk.END)  # Clear previous content
            self.verse_text.insert(tk.END, verse_content)
            messagebox.showinfo("Success", "Word of God written successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class DateTimeWriter:
    @staticmethod
    def write_current_date_time(file_name='date_time.txt'):
        current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(file_name, 'a') as file:
            file.write(current_date_time)

class BibleVerseReader:
    @staticmethod
    def read_random_verse(api_url='https://bible-api.com/?random=verse'):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            verse = data.get('text', '')
            topic = data.get('reference', 'Verse of the Day - Topic: Verse of the Day')
            return f"{topic}\n\n{verse}"
        else:
            return f"Failed to fetch Bible verse. Status code: {response.status_code}"

class WordOfGod(DateTimeWriter, BibleVerseReader):
    @staticmethod
    def print_word_of_god(file_name='Word_of_God.txt'):
        verse_content = BibleVerseReader.read_random_verse()
        DateTimeWriter.write_current_date_time(file_name)
        with open(file_name, 'a') as file:
            file.write('\nWord of God\n')
            file.write('-' * 20 + '\n')
            file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
            file.write(verse_content + '\n')
        return verse_content

if __name__ == "__main__":
    root = tk.Tk()
    app = WordOfGodApp(root)
    root.mainloop()
