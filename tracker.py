import csv
import os
import validators
import datetime
import customtkinter as CTk
from tkinter import *


class Contacts():
    def __init__(self, source_path=""):
        self.source_path = source_path
        self.contact_list = list()
        self.load(source_path)
        return

    def __str__(self):
        return "Contact list: /n" + self.contact_list

    def add(self, person):
        return

    def remove(self, person):
        return

    def load(self, input_path):
        # file = os.path.basename(input_path)
        # # file_name = file.split[0]
        # file_extension = file.split[1]
        # if not os.path.isfile(input_path) or file_extension != "csv":
        #     raise ValueError("Not a valid csv file")
        # with open(input_path) as csvfile:
        #     reader = csv.DictReader(csvfile):
        #     for line in reader:

        print("Contacts loaded")
        return

    def save(self, output_path):
        return


class Contact():
    def __init__(self, first, middle="", last="", relationship="friend", email="", phone="", birthday=""):
        self._relationship_types = ["friend", "family", "colleague", "other"]
        self.first = first
        self.middle = middle
        self.last = last
        self.relationship = relationship
        self.email = email
        self.phone = phone
        self.birthday = birthday

        return

    def __str__(self):
        return_string = self.first
        if self._middle:
            return_string += " " + self._middle
        if self._last:
            return_string += " " + self._last
        if self._relationship:
            return_string += ", relationship: " + self._relationship
        if self._email:
            return_string += ", email: " + self._email
        if self._phone:
            return_string += ", phone: " + self._phone

        return return_string

    def change(self, first="", middle="", last="", relationship="", email="", phone=""):
        if first:
            self.first = first
        if middle:
            self.middle = middle
        if last:
            self.last = last
        if relationship:
            self.relationship = relationship
        if email:
            self.email = email
        if phone:
            self.phone = phone
        print("Contact has been updated")
        return

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        if not type(first) == str:
            raise TypeError("Name must be a string")
        if not first.isalpha():
            raise ValueError("All characters must be from alphabet")
        self._first = first.capitalize()

    @property
    def middle(self):
        return self._middle

    @middle.setter
    def middle(self, middle):
        if middle == "" or middle == None:
            self._middle = ""
            return
        if not type(middle) == str:
            raise TypeError("Name must be a string")
        if not middle.isalpha():
            raise ValueError("All characters must be from alphabet")
        self._middle = middle.capitalize()

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        if last == "" or last == None:
            self._last = ""
            return
        if not type(last) == str:
            raise TypeError("Name must be a string")
        if not last.isalpha():
            raise ValueError("All characters must be from alphabet")
        self._last = last.capitalize()

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        if relationship == "" or relationship == None:
            self.relationship = ""
            return
        if not type(relationship) == str:
            raise TypeError("Relationship must be a string")
        if not relationship.isalpha():
            raise ValueError("All characters must be from alphabet")
        if relationship.lower() not in self._relationship_types:
            raise ValueError(
                f"Relationship must be one of following: {self._relationship_types}")
        self._relationship = relationship.lower()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email == "" or email == None:
            self._email = ""
            return
        if not email or type(email) != str:
            raise ValueError("Email must be a string")
        if not validators.email.email(email, whitelist=None):
            raise ValueError("Incorrect email adress")
        self.email = email.strip()

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if phone == "" or phone == None:
            self._phone = ""
            return
        if not phone or not phone.strip(" ").isdigit():
            raise ValueError("Phone number must be a number")
        self._phone = phone.strip(" ")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        if birthday == "" or birthday == None:
            self._birthday = ""
            return
        if type(birthday) != str:
            raise ValueError("Date must be a str")
        date_format = "%m/%d"
        try:
            date = datetime.datetime.strptime(birthday, date_format)
            self._birthday = f"{date.month}/{date.day}"

        # If the date validation goes wrong
        except ValueError:
            raise ValueError("Incorrect date format, usage: MM/DD")


class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        # WINDOW CONFIGURATION
        self.title("Birthday tracker")
        self.geometry(f"{800}x{400}")

        # ---HEADER----
        self.header_frame = CTk.CTkFrame(self, corner_radius=0)
        self.header_frame.grid(row=0, column=0, sticky="nsew", pady=(20, 20))
        self.header_label = CTk.CTkLabel(
            self.header_frame,
            text="Birthday tracker",
            font=CTk.CTkFont(size=30, weight="bold"),
        )
        self.header_label.grid(row=1, column=0, sticky="ew")

        # ---OPTIONS---
        self.main_frame = CTk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 20))
        # Option buttons
        self.contact_button = CTk.CTkButton(
            self.main_frame, command=self.display_contacts, text="Contacts")
        self.contact_button.grid(
            row=0, sticky="nsew", pady=(5, 5))

        # Next birthday
        self.birthday_name = StringVar(value="Martin")
        self.birthday_date = StringVar(value="01/17")
        self.birthday_label = CTk.CTkLabel(
            self.main_frame, text=f"Next birthday has {self.birthday_name.get()} on {self.birthday_date.get()}", font=CTk.CTkFont(size=15))
        self.birthday_label.grid(row=1)
        # ---CONTACTS---

        # self.option_list.pack()

    def display_contacts():
        # ...
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()
