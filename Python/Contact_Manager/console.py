"""
Contact Management System GUI using tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image

from contact_manager import ContactManagement


def main():
    """
    Main function for the contact management system.
    """
    contact_manager = ContactManagement()

    root = tk.Tk()
    root.title("Contact Management System")
    root.configure(background='#FF5733')

    # Set window size and center the window
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

    # Convert PNG to ICO and set application icon
    img = Image.open('book_planner_address_bookmark.ico')
    img.save('book_planner_address_bookmark.ico')
    root.iconbitmap('book_planner_address_bookmark.ico')

    def add_contact():
        """
        Add a new contact to the database.
        """
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        contact_manager.add_contact(name, phone, email)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts():
        """
        View all contacts in the database.
        """
        contacts = contact_manager.view_contacts()
        if contacts:
            messagebox.showinfo("Contacts", "\n".join(map(str, contacts)))
        else:
            messagebox.showinfo("No Contacts", "No contacts found.")

    def export_to_csv():
        """
        Export contacts to a CSV file.
        """
        contact_manager.export_to_csv("contacts.csv")
        messagebox.showinfo("Exported", "Contacts exported to CSV successfully!")

    def export_to_pdf():
        """
        Export contacts to a PDF file.
        """
        contact_manager.export_to_pdf("contacts.pdf")
        messagebox.showinfo("Exported", "Contacts exported to PDF successfully!")

    def delete_contact():
        """
        Delete a contact from the database.
        """
        try:
            contact_id = int(id_entry.get())
            contact_manager.delete_contact(contact_id)
            messagebox.showinfo("Deleted", "Contact deleted successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid contact ID.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exit_application():
        """
        Exit the application.
        """
        root.destroy()

    # Font settings
    title_font = ("Helvetica", 16, "bold")
    label_font = ("Helvetica", 12)
    entry_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12, "bold")

    # GUI layout
    tk.Label(root, text="Contact Management System", bg='#FF5733', fg="white", font=title_font).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Name:", bg='#FF5733', fg="white", font=label_font).grid(row=1, column=0, pady=5, padx=5, sticky='e')
    tk.Label(root, text="Phone:", bg='#FF5733', fg="white", font=label_font).grid(row=2, column=0, pady=5, padx=5, sticky='e')
    tk.Label(root, text="Email:", bg='#FF5733', fg="white", font=label_font).grid(row=3, column=0, pady=5, padx=5, sticky='e')
    tk.Label(root, text="Contact ID:", bg='#FF5733', fg="white", font=label_font).grid(row=4, column=0, pady=5, padx=5, sticky='e')

    name_entry = tk.Entry(root, font=entry_font)
    phone_entry = tk.Entry(root, font=entry_font)
    email_entry = tk.Entry(root, font=entry_font)
    id_entry = tk.Entry(root, font=entry_font)

    name_entry.grid(row=1, column=1, pady=5, padx=5)
    phone_entry.grid(row=2, column=1, pady=5, padx=5)
    email_entry.grid(row=3, column=1, pady=5, padx=5)
    id_entry.grid(row=4, column=1, pady=5, padx=5)

    add_button = tk.Button(root, text="Add Contact", command=add_contact, bg='#FFC300', fg="white", font=button_font, relief=tk.RAISED, bd=3)
    add_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='we')

    view_button = tk.Button(root, text="View Contacts", command=view_contacts, bg='#FFC300', fg="white", font=button_font, relief=tk.RAISED, bd=3)
    view_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='we')

    export_csv_button = tk.Button(root, text="Export to CSV", command=export_to_csv, bg='#FFC300', fg="white", font=button_font, relief=tk.RAISED, bd=3)
    export_csv_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky='we')

    export_pdf_button = tk.Button(root, text="Export to PDF", command=export_to_pdf, bg='#FFC300', fg="white", font=button_font, relief=tk.RAISED, bd=3)
    export_pdf_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky='we')

    delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg='#FFC300', fg="white", font=button_font, relief=tk.RAISED, bd=3)
    delete_button.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky='we')

    exit_button = tk.Button(root, text="Exit", command=exit_application, bg='#FFC300', fg="white", font=button_font, relief=tk.RAISED, bd=3)
    exit_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, sticky='we')

    root.mainloop()


if __name__ == "__main__":
    main()
