from validator_collection import validators
from datetime import date, datetime
import pickle


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
    def days_to_birthday(contact: Contact):
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
