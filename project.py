import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from validator_collection import validators
from datetime import date, datetime
import pickle


def main():
    app = App()
    app.mainloop()
    return


def days_to_birthday(date: str):
    p = Contact("Example", date)

    return Contacts.days_to_birthday(p)


def nearest_birthday(contact_dict: dict):
    contacts = Contacts()
    for input in contact_dict:
        c = Contact(input, contact_dict[input])
        contacts.add(c)
    return contacts.next_b_day().first


def validate_contact(first_name, last_name, birthay, email):
    try:
        c = Contact(first_name, birthay, last_name, email)
        return True
    except:
        return False


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # WINDOW CONFIGURATION
        self.title("Birthday tracker")
        self.geometry(f"{350}x{350}")

        # CONTACTS VAR INITIALIZATION
        self.contact_list = Contacts()
        self.contact_list.load()

        # ---HEADER----
        self.header_frame = tk.Frame(
            self)
        self.header_frame.grid(sticky="nswe", padx=20, pady=(20, 10))
        self.header_label = tk.Label(
            self.header_frame,
            text="Birthday tracker",
            font=Font(size=30, weight="bold"),
        )
        self.header_label.grid(sticky="ew")

        # ---MAIN PAGE---
        self.main_frame = tk.Frame(
            self)
        self.main_frame.grid(row=1, sticky="nsew", padx=20, pady=(0, 20))
        # Birthday frame
        self.birthday_frame = tk.Frame(
            self.main_frame, width=310)
        self.birthday_frame.grid(row=2, sticky="news")
        # Contacts buttons
        self.contact_button = tk.Button(
            self.birthday_frame, command=self.display_contacts, text="Contacts", font=Font(size=15, weight="bold"))
        self.contact_button.grid(
            row=0, sticky="w", pady=5, padx=5)
        # Display variables
        self.birthday_phrase = tk.StringVar(value="")
        # Checks who has the next b-day
        self.check_next_b()
        # Next b-day display
        self.birthday_label = tk.Label(
            self.birthday_frame, font=Font(size=15), textvariable=self.birthday_phrase, wraplength=310)
        self.birthday_label.grid(row=1)

        # ---CONTACTS---
        # Initial display variable
        self.contact_display = tk.BooleanVar(value=False)
        # Contacts frame
        self.contacts_frame = tk.Frame(
            self.main_frame)
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
            self.main_frame)
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
        """Switches between main page and contacts page"""
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
        """Switches to contact add/ edit page, 
            button=add shows the add button
            button=edit shows the edit button
        """
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
        """Returns to contacts page"""
        self.add_contact_frame.grid_forget()
        self.contacts_frame.grid(row=2, padx=10, sticky="nsew")
        self.add_button.grid(row=6, column=0)

    def add_to_contacts(self):
        """Creates new contact based on data from entry boxes"""
        try:
            contact = Contact(first=self.first_name_entry.get(),
                              birthday=self.birthday_entry.get())
            last: str = self.last_name_entry.get()
            if last:
                contact.last = last
            email: str = self.email_entry.get()
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
            self.contact_list.save()
            self.return_to_contacts()
        return

    def remove_from_contacts(self):
        """Removes selected contact from contact list"""
        try:
            cur_index: int = self.contacts_listbox.curselection()[0]
        except IndexError:
            return
        self.contact_list.remove(cur_index)
        self.listbox_update()
        self.contact_list.save()
        return

    def go_to_edit(self):
        """Displays edit contact page and loads contact information in entry boxes"""
        # Gets index of contact list
        self.edited_contact_index = tk.IntVar()
        try:
            self.edited_contact_index: int = self.contacts_listbox.curselection()[
                0]
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
        """Deletes edites contact from list and adds a new one based on contact information typed in entry boxes"""
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
        """Updates listbox"""
        self.contacts_listbox.delete(0, self.contacts_listbox.size())
        for index, item in enumerate(self.contact_list.get()):
            self.contacts_listbox.insert(index, item.get())
        return

    def check_next_b(self):
        """Calculates contact with nearest birthday and updates the birthday phrase shown on main page"""
        next_b_day_contact = self.contact_list.next_b_day()
        if next_b_day_contact != None:
            self.birthday_name = tk.StringVar(value=next_b_day_contact.first)
            self.birthday_date = tk.StringVar(
                value=next_b_day_contact.birthday)
            self.birthday_phrase.set(
                f"Next birthday has {self.birthday_name.get()} on {self.birthday_date.get()}")
        else:
            self.birthday_phrase.set("")
        self.update_idletasks()
        return


class Contact():
    """Contains a person contact information"""

    def __init__(self, first, birthday, last="", email=""):
        self.first = first
        self.last = last
        self.email = email
        self.birthday = birthday
        return

    def __str__(self):
        return_string = self.first
        if self._last:
            return_string += " " + self._last
        if self._email:
            return_string += ", email: " + self._email
        if self._phone:
            return_string += ", phone: " + self._phone
        return return_string

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first: str):
        if not type(first) == str:
            raise TypeError("First name: Name must be a string")
        if not first.isalpha():
            raise ValueError(
                "First name: All characters must be from alphabet")
        self._first = first.capitalize()

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last: str):
        if last == "" or last == None:
            self._last = ""
            return
        if not type(last) == str:
            raise TypeError("Last name: Name must be a string")
        if not last.isalpha():
            raise ValueError("Last name: All characters must be from alphabet")
        self._last = last.capitalize()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        if email == "" or email == None:
            self._email = ""
            return
        if not email or type(email) != str:
            raise ValueError("Email must be a string")
        try:
            email = validators.email(email, whitelist=None).strip()
        except ValueError:
            raise ValueError("Incorrect email adress")
        else:
            self._email = email

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: str):
        if type(birthday) != str:
            raise ValueError("Date must be a str")
        date_format = "%m/%d"
        try:
            date = datetime.strptime(birthday, date_format)
            self._birthday = f"{date.month}/{date.day}"
        # If the date validation goes wrong
        except ValueError:
            raise ValueError("Incorrect date format, usage: MM/DD")

    def get(self):
        """
        Returns short string, f.e. Martin has birthday on 01/17

        :return: A string with names and birthday
        "rtype: str
        """
        return_string = self.first
        if self._last:
            return_string += " " + self._last
        return_string += f" has birthday on {self.birthday}"
        return return_string

    def change(self, first: str = "", last: str = "", birthday: str = "", email: str = ""):
        """
        Changes instance variables of the contact

        :param first: First name
        :type first: str
        :param last: Last name
        :type last: str
        :param birthday: Birthday in format MM/DD
        :type birthday: str
        :param email: E-mail address
        :type email: str
        :raise TypeError: If argument(s) are not str(s)
        :raise ValueError: If birthday param is not in MM/DD format
        :raise ValueError: If e-mail address is not valid e-mail address
        """
        if first:
            self.first = first
        if last:
            self.last = last
        if email:
            self.email = email
        if birthday:
            self.birthday = birthday
        return


class Contacts():
    """Contains list of Contacts"""

    def __init__(self):
        self._contact_list = list()
        return

    def __str__(self):
        return "Contact list: /n" + self.contact_list

    @property
    def contact_list(self):
        raise Exception("Wrong usage, use .get() method")

    @contact_list.setter
    def contact_list(self):
        raise Exception("Wrong usage, use .add() or .remove method")

    def get(self):
        """Returns list of contacts

        :return: List of contacts
        :rtype: list
        """
        return self._contact_list

    def add(self, contact: Contact):
        """
        Adds a contact to the list

        :param contact: Contact
        :type contact: Contact
        """
        self._contact_list.append(contact)
        self._contact_list.sort(key=lambda x: x.first)
        return

    def remove(self, index: int):
        """
        Removes a contact from the list based on the given list index

        :param index: List index of removed contact
        :type index: int
        """
        self._contact_list.remove(self._contact_list[index])
        return

    def load(self):
        """Loads contact list from data file called 'contacts'"""
        try:
            input_file = open("contacts", "rb")
        except FileNotFoundError as e:
            return
        try:
            self._contact_list = pickle.load(input_file)
        except EOFError:
            pass
        return

    def save(self):
        """Saves contact list to data file called 'contacts'"""
        output_file = open("contacts", "wb")
        pickle.dump(self._contact_list, output_file)
        return

    @classmethod
    def days_to_birthday(cls, contact: Contact):
        """
        Returns amount of days between today and given contact's next birthday

        :param contact: A contact for which the remaining days are calculated 
        :type contact: Contact
        :return: Amount of days to next birthday
        :rtype: int
        """
        today = date.today()
        month, day = contact.birthday.split("/")
        next = date(today.year, int(month), int(day))
        if next < today:
            next = next.replace(year=today.year + 1)
        time_to_birthday = abs(next - today)
        return time_to_birthday.days

    def next_b_day(self):
        """
        Returns a contact with closest birthday

        :return: Contact with nearest birthday, in case of no contacts in contact list, return None
        :rtype: Contact / None
        """
        sorted_list = sorted(self._contact_list, key=self.days_to_birthday)
        if len(sorted_list) > 0:
            return sorted_list[0]
        else:
            return None


if __name__ == "__main__":
    main()
