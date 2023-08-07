import csv
import os
from validator_collection import validators
from datetime import date, datetime
import pickle


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

    def load(self):
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
        output_file = open("contacts", "wb")
        pickle.dump(self._contact_list, output_file)
        return

    def days_to_birthday(self, contact):
        today = date.today()
        month, day = contact.birthday.split("/")
        next = date(today.year, int(month), int(day))
        if next < today:
            next = next.replace(year=today.year + 1)
        time_to_birthday = abs(next - today)
        return time_to_birthday.days

    def next_b_day(self):
        sorted_list = sorted(self._contact_list, key=self.days_to_birthday)
        if len(sorted_list) > 0:
            return sorted_list[0]
        else:
            return None


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

    def change(self, first="", last="", birthday="", email=""):
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
            raise ValueError(
                "First name: All characters must be from alphabet")
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
            date = datetime.strptime(birthday, date_format)
            self._birthday = f"{date.month}/{date.day}"
        # If the date validation goes wrong
        except ValueError:
            raise ValueError("Incorrect date format, usage: MM/DD")
