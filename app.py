import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from helpers import Contact, Contacts


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # WINDOW CONFIGURATION
        self.title("Birthday tracker")
        self.geometry(f"{350}x{400}")

        # CONTACTS VAR INITIALIZATION
        self.contact_list = Contacts()
        self.contact_list.load()

        # ---HEADER----
        self.header_frame = tk.Frame(
            self, highlightbackground="blue", highlightthickness=2)
        self.header_frame.grid(sticky="nswe", padx=20, pady=(20, 10))
        self.header_label = tk.Label(
            self.header_frame,
            text="Birthday tracker",
            font=Font(size=30, weight="bold"),
        )
        self.header_label.grid(sticky="ew")

        # ---MAIN PAGE---
        self.main_frame = tk.Frame(
            self, highlightbackground="blue", highlightthickness=2)
        self.main_frame.grid(row=1, sticky="nsew", padx=20, pady=(0, 20))
        # Birthday frame
        self.birthday_frame = tk.Frame(
            self.main_frame, highlightbackground="blue", highlightthickness=2)
        self.birthday_frame.grid(row=2, sticky="news")
        # Contacts buttons
        self.contact_button = tk.Button(
            self.birthday_frame, command=self.display_contacts, text="Contacts", font=Font(size=15, weight="bold"))
        self.contact_button.grid(
            row=0, sticky="ns", pady=5, padx=5)
        # Display variables
        self.birthday_phrase = tk.StringVar(value="")
        # Checks who has the next b-day
        self.check_next_b()
        # Next b-day display
        self.birthday_label = tk.Label(
            self.birthday_frame, font=Font(size=15), textvariable=self.birthday_phrase)
        self.birthday_label.grid(row=1)

        # ---CONTACTS---
        # Initial display variable
        self.contact_display = tk.BooleanVar(value=False)
        # Contacts frame
        self.contacts_frame = tk.Frame(
            self.main_frame, highlightbackground="blue", highlightthickness=2)
        # Add to list button
        self.add_contact_button = tk.Button(
            self.contacts_frame, command=self.go_to_contact, text="Add new contact")
        self.add_contact_button.grid(
            row=2, column=1, sticky="nsew", pady=5, padx=5)
        # Remove from list button
        self.remove_contact_button = tk.Button(
            self.contacts_frame, command=self.remove_from_contacts, text="Remove from contacts")
        self.remove_contact_button.grid(
            row=3, column=1, sticky="nsew", pady=5, padx=5)
        # Edit contact button
        self.edit_contact_button = tk.Button(
            self.contacts_frame, command=self.go_to_edit, text="Edit contact")
        self.edit_contact_button.grid(
            row=2, column=2, sticky="nsew", pady=5, padx=5)
        # Return button
        self.return_to_cont = tk.Button(
            self.contacts_frame, command=self.display_contacts, text="Return to main menu")
        self.return_to_cont.grid(
            row=3, column=2, sticky="nsew", pady=5, padx=5)
        # Listbox of contacts
        self.contacts_listbox = tk.Listbox(
            self.contacts_frame, width=45, selectmode="SINGLE")
        self.contacts_listbox.grid(
            row=4, columnspan=3, pady=5, padx=5, sticky="news")
        self.listbox_update()

        # ---ADD CONTACT FRAME---
        # Frame
        self.add_contact_frame = tk.Frame(
            self.main_frame, highlightbackground="blue", highlightthickness=2)
        # Label
        self.add_contact_label = tk.Label(
            self.add_contact_frame, text="Add new contact", font=Font(size=20))
        self.add_contact_label.grid(
            columnspan=2, sticky="ewns", padx=10, pady=10)
        # Entry boxes with labels
        self.first_name_label = tk.Label(
            self.add_contact_frame, text="First name")
        self.first_name_label.grid(row=2, column=0)
        self.first_name_entry = tk.Entry(self.add_contact_frame)
        self.first_name_entry.grid(row=2, column=1)
        self.last_name_label = tk.Label(
            self.add_contact_frame, text="Last name")
        self.last_name_label.grid(row=3, column=0)
        self.last_name_entry = tk.Entry(self.add_contact_frame)
        self.last_name_entry.grid(row=3, column=1)
        self.birthday_label = tk.Label(
            self.add_contact_frame, text="Birthday MM/DD")
        self.birthday_label.grid(row=4, column=0)
        self.birthday_entry = tk.Entry(self.add_contact_frame)
        self.birthday_entry.grid(row=4, column=1)
        self.email_label = tk.Label(
            self.add_contact_frame, text="Email address")
        self.email_label.grid(row=5, column=0)
        self.email_entry = tk.Entry(self.add_contact_frame)
        self.email_entry.grid(row=5, column=1)
        # Buttons
        self.add_button = tk.Button(
            self.add_contact_frame, text="Add to contacts", command=self.add_to_contacts)
        self.add_button.grid(row=6, column=0, padx=10, pady=10)
        self.save_edit_button = tk.Button(
            self.add_contact_frame, text="Save contact", command=self.edit_contact)
        self.return_button = tk.Button(
            self.add_contact_frame, text="Return", command=self.return_to_contacts)
        self.return_button.grid(
            row=6, column=1, padx=10, pady=10, sticky="nse")

    def display_contacts(self):
        if self.contact_display == True:
            self.birthday_frame.grid(row=2)
            self.contacts_frame.grid_forget()
            self.contact_display = False
            self.check_next_b()
        else:
            self.birthday_frame.grid_forget()
            self.contacts_frame.grid(row=2, sticky="nsew", padx=10)
            self.contact_display = True
        return

    def go_to_contact(self, button="add"):
        self.contacts_frame.grid_forget()
        self.add_contact_frame.grid(row=2, padx=20, sticky="news")
        if button == "add":
            self.add_button.grid(row=6, column=0)
            self.save_edit_button.grid_forget()
        else:
            self.add_button.grid_forget()
            self.save_edit_button.grid(row=6, column=0)
        return

    def return_to_contacts(self):
        self.add_contact_frame.grid_forget()
        self.contacts_frame.grid(row=2, padx=10, sticky="nsew")
        self.add_button.grid(row=6, column=0)

    def add_to_contacts(self):
        try:
            contact = Contact(first=self.first_name_entry.get(),
                              birthday=self.birthday_entry.get())
            last = self.last_name_entry.get()
            if last:
                contact.last = last
            email = self.email_entry.get()
            if email:
                contact.email = email
        except Exception as e:
            print(str(e))
            messagebox.showerror(message=str(e))
        else:
            self.contact_list.add(contact)
            self.first_name_entry.delete(0, 100)
            self.last_name_entry.delete(0, 100)
            self.birthday_entry.delete(0, 100)
            self.email_entry.delete(0, 100)
            self.listbox_update()
            self.return_to_contacts()
            self.contact_list.save()
        return

    def remove_from_contacts(self):
        try:
            cur_index = self.contacts_listbox.curselection()[0]
        except IndexError:
            return
        self.contact_list.remove(cur_index)
        self.listbox_update()
        return

    def go_to_edit(self):
        # Gets index of contact list
        self.edited_contact_index = tk.IntVar()
        try:
            self.edited_contact_index = self.contacts_listbox.curselection()[0]
        except IndexError:
            return
        # Goes to add contact layout
        self.go_to_contact(button="edit")
        # Displays current values
        edited_contact = self.contact_list.get()[self.edited_contact_index]
        self.first_name_entry.insert(0, edited_contact.first)
        self.last_name_entry.insert(0, edited_contact.last)
        self.birthday_entry.insert(0, edited_contact.birthday)
        self.email_entry.insert(0, edited_contact.email)
        return

    def edit_contact(self):
        try:
            edited_contact = Contact(
                self.first_name_entry.get(), self.birthday_entry.get())
            edited_contact.last = self.last_name_entry.get()
            edited_contact.email = self.email_entry.get()
        except Exception as e:
            messagebox.showerror(message=str(e))
        else:
            self.contact_list.remove(self.edited_contact_index)
            self.contact_list.add(edited_contact)
            self.first_name_entry.delete(0, 100)
            self.last_name_entry.delete(0, 100)
            self.birthday_entry.delete(0, 100)
            self.email_entry.delete(0, 100)
            self.listbox_update()
            self.return_to_contacts()
        return

    def listbox_update(self):
        self.contacts_listbox.delete(0, self.contacts_listbox.size())
        for index, item in enumerate(self.contact_list.get()):
            self.contacts_listbox.insert(index, item.get())
        return

    def check_next_b(self):
        next_b_day_contact = self.contact_list.next_b_day()
        if next_b_day_contact != None:
            self.birthday_name = tk.StringVar(value=next_b_day_contact.first)
            self.birthday_date = tk.StringVar(
                value=next_b_day_contact.birthday)
            self.birthday_phrase.set(
                f"Next birthday has {self.birthday_name.get()} on {self.birthday_date.get()}")
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()
