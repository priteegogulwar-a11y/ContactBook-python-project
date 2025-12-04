---

# 📒 Contact Book (Python)

A simple command-line Contact Book application written in Python.
This program allows users to **add, view, search, update, and delete contacts** using an interactive menu-driven interface.

---

## 📌 Features

### ✔ Add Contact

Users can enter a name, phone number, and email to create a new contact.

### ✔ Display All Contacts

Shows a list of all stored contacts.

### ✔ Search Contact

Searches for a contact by name and displays the details if found.

### ✔ Update Contact

Allows modifying the contact’s name, phone number, or email.
The user may also leave a field empty to keep the previous value unchanged.

### ✔ Delete Contact

Removes a contact from the contact book by name.

### ✔ Exit Program

Closes the contact book application safely.

---

## 📂 Project Structure

```
project-folder/
│
├── contact.py              # Contains Contact class (structure for a single contact)
├── contact_book.py         # Contains ContactBook class (operations on contacts)
└── main.py                 # User interface and menu handling (your provided code)
```

---

## 🧩 How It Works (Theory)

### **Contact Class (`contact.py`)**

* Represents a single contact.
* Stores attributes: **name, phone, email**.
* Includes a method to display the contact details.

### **ContactBook Class (`contact_book.py`)**

* Stores all contacts in a list.
* Contains logic for:

  * Adding a contact
  * Searching a contact
  * Updating a contact
  * Deleting a contact
  * Displaying all contacts

### **Main Program (`main.py`)**

* Handles user interaction through a text-based menu.
* Delegates operations to the `ContactBook` class.
* Continuously runs until the user chooses to exit.

---

## ▶ Running the Program

Ensure all three files (`main.py`, `contact.py`, `contact_book.py`) are in the same folder.

Run the program using:

```bash
python main.py
```

---

## 📝 Example Usage (Menu)

```
==============================
Contact Book Menu
==============================
1. Add Contact
2. Display All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

The user enters the option number to perform that action.

---

## 🚀 Future Enhancements (Optional)

* Save contact data to a file (JSON, CSV, or database)
* Add validation for phone and email formats
* Implement a graphical user interface (GUI) using Tkinter
* Add sorting (A–Z) for contact list


