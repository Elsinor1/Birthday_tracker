# BIRTHDAY TRACKER
#### Description: 
Desktop tkinter application that allows the user to input and store contact information such as name, date of birthday or e-mail address. Application then displays the name and birthday date of the person, that has the closest birtday.
        
- Main page: Displays the name and birthday date of the person, that has the closest birtday. Use "Contacts" button to go to contact page.

- Contact page: Displays list of contacts as well as buttons for adding new contact, editing or removing selected contact.

- Adding / Editing of contact page: Displays entry boxes for input. Changes are saved after using the "Add to contacts" or "Save contact" button.

#### Video Demo:  https://www.youtube.com/watch?=4ka-r5-knNA&b_channel=Elsinor999

#### Design overview: 
For purpose of easy contact information management two classes have been created. 

#### Class Contact 
Encapsulates the person's contact information such as first name, last name, birtday date, e-mail address. 

##### Methods overview:
- setter, getter: Each the instance variables have setter and getter methods for input validation. Setter methods raise ValueError when required input conditions are not met. 

- .get()  Returns string of contact information

- .change() Changes contact information based on given arguments


#### Class Contacts 
Incorporates instance variable called contact_list and methods for contacts management and manipulation

##### Methods overview:
- setter, getter: .contact_list can't be given or edited, trying so will raise an exception.

- .get() Returns a instance variable contact_list of type list

- .add(Contact) Appends a given contact to the contact_list and sort it alphabetically. Will raise TypeError when given argument is not of type Contact.

- .remove(index)  Removes a contact on given list index. Will raise IndexError if the index is invalid.
- .load() Loads contact list from binary data stored in "contacts" file located in application directory. If file is not present or is empty, no data will be loaded.

- .save() Transfers the contacts list information to binary data and stores it to "contacts" file in the application directory
- .days_to_birthday(contact) Returns an int of days remaining to given contact's birthday. Returns TypeError when argument is not of type Contact.

- .next_b_day() Returns a contact from contact_list with closest birthday

