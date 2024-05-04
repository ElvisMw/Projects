import sqlite3
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

class ContactManagement:
    """
    Class to manage contacts using a SQLite database.
    """

    def __init__(self, db_name='contacts.db'):
        """
        Initialize the database.

        Parameters:
            db_name (str): name of the database file
        """
        self.db_name = db_name

    def add_contact(self, name, phone, email):
        """
        Add a new contact to the database.

        Parameters:
            name (str): name of the contact
            phone (str): phone number of the contact
            email (str): email of the contact
        """
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        conn.close()

    def view_contacts(self):
        """
        View all contacts in the database.

        Returns:
            list: list of contacts
        """
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM contacts")
        contacts = c.fetchall()
        conn.close()
        return contacts

    def update_contact(self, contact_id, name, phone, email):
        """
        Update a contact in the database.

        Parameters:
            contact_id (int): id of the contact to update
            name (str): new name of the contact
            phone (str): new phone number of the contact
            email (str): new email of the contact
        """
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
        conn.commit()
        conn.close()

    def delete_contact(self, contact_id):
        """
        Delete a contact from the database.

        Parameters:
            contact_id (int): id of the contact to delete
        """
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        conn.close()

    def export_to_csv(self, filename):
        """
        Export contacts to a CSV file.

        Parameters:
            filename (str): name of the CSV file
        """
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM contacts")
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['ID', 'Name', 'Phone', 'Email'])
            csv_writer.writerows(c.fetchall())
        conn.close()

    def export_to_pdf(self, filename):
        """
        Export contacts to a PDF file.

        Parameters:
            filename (str): name of the PDF file
        """
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM contacts")
        data = [['ID', 'Name', 'Phone', 'Email']]
        data.extend(c.fetchall())
        conn.close()

        pdf = SimpleDocTemplate(filename, pagesize=letter)
        table = Table(data)
        style = [('BACKGROUND', (0, 0), (-1, 0), colors.red),
                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                 ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                 ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                 ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                 ('GRID', (0, 0), (-1, -1), 1, colors.black)]
        table.setStyle(style)
        pdf.build([table])
