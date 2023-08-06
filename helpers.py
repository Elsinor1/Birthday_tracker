import csv
import os
from validator_collection import validators
import datetime


class Contacts():
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
        return self._contact_list

    def add(self, contact):
        self._contact_list.append(contact)
        self._contact_list.sort(key=lambda x: x.first)
        return

    def remove(self, index):
        self._contact_list.remove(self._contact_list[index])
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
    

    def get(self):
        return_string = self.first
        if self._last:
            return_string += " " + self._last
        return_string += f" has birthday on {self.birthday}"
        return return_string

    def change(self, first="", last="",birthday="", email=""):
        if first:
            self.first = first
        if last:
            self.last = last
        if email:
            self.email = email
        if birthday:
            self.birthday = birthday
        print("Contact has been updated")
        return

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        if not type(first) == str:
            raise TypeError("First name: Name must be a string")
        if not first.isalpha():
            raise ValueError("First name: All characters must be from alphabet")
        self._first = first.capitalize()


    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
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
    def email(self, email):
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
    def birthday(self, birthday):
        if type(birthday) != str:
            raise ValueError("Date must be a str")
        date_format = "%m/%d"
        try:
            date = datetime.datetime.strptime(birthday, date_format)
            self._birthday = f"{date.month}/{date.day}"
        # If the date validation goes wrong
        except ValueError:
            raise ValueError("Incorrect date format, usage: MM/DD")

