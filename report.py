import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from config import SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_DATABASE


def show_report():
    # Create a new window for the report
    report_window = Toplevel()
    report_window.title("Customer Report")
    report_window.geometry("1000x500")

    # Connect to MySQL database
    try:
        conn = mysql.connector.connect(
        host=SQL_HOST,
        user=SQL_USER,
        password=SQL_PASSWORD,
        database=SQL_DATABASE
    )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer")
        rows = cursor.fetchall()

        # Create a Treeview widget to display the data
        columns = ('Ref', 'Name', 'Mother', 'Gender', 'PostCode', 'Mobile', 'Email', 'Nationality', 'Idproof', 'Idnumber', 'Address')
        tree = ttk.Treeview(report_window, columns=columns, show='headings')

        # Define column headings and set width for each column
        tree.heading('Ref', text='Ref')
        tree.column('Ref', width=80)

        tree.heading('Name', text='Name')
        tree.column('Name', width=150)

        tree.heading('Mother', text='Mother')
        tree.column('Mother', width=150)

        tree.heading('Gender', text='Gender')
        tree.column('Gender', width=100)

        tree.heading('PostCode', text='PostCode')
        tree.column('PostCode', width=100)

        tree.heading('Mobile', text='Mobile')
        tree.column('Mobile', width=120)

        tree.heading('Email', text='Email')
        tree.column('Email', width=180)

        tree.heading('Nationality', text='Nationality')
        tree.column('Nationality', width=120)

        tree.heading('Idproof', text='Idproof')
        tree.column('Idproof', width=120)

        tree.heading('Idnumber', text='Idnumber')
        tree.column('Idnumber', width=120)

        tree.heading('Address', text='Address')
        tree.column('Address', width=200)

        # Add data to the Treeview widget
        for row in rows:
            tree.insert('', END, values=row)

        tree.pack(expand=True, fill='both')

        # Close the database connection
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return

# Main function to create the report window
def report_window():
    root = Tk()
    root.title("Hotel Management System - Report")
    root.geometry("400x200")

    # Button to open report window
    report_button = Button(root, text="Show Customer Report", command=show_report)
    report_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    report_window()
