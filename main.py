from contact import Contact
from contact_book import ContactBook
def displa_menu():
    print("\n"+"="*30)
    print("Contact Book Menu")
    print("\n"+"="*30)
    print("1.Add Contact")
    print("2.Display All Contacts")
    print("3.Search contact")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Exit")
def add_contact_ui(contact_book):
    print("\n-- Add new contact--")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contact = Contact(name,phone,email)
    contact_book.add_contact(contact)
    print("Contact added successfully")
def search_contact_ui(contact_book):
    name = input("Enter name to search: ").strip()
    Contact = contact_book.search_contact(name)
    if Contact:
        print("\ncontact found.")
        Contact.display_contact()
    else:
        print("Contact not found.")
def update_contact_ui(contact_book):
    name =input("Enter name of contact to update: ").strip()
    new_name = input("Enter new name(or press Enter to keep current)")
    new_phone = input("Enter new phone(or press Enter to keep current)")
    new_email = input("Enter new email(or press Enter to keep current)")
    contact_book.update_contact(
        name,
        new_name if new_name else None,
        new_phone if new_phone else None,
        new_email if new_email else None,
    )
def delete_contact_ui(contact_book):
    name =input("Enter name of contact to delete: ").strip()
    contact_book.delete_contact(name)
def main():
    Contact_book =ContactBook()
    while True:
        displa_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice =='1':
            add_contact_ui(Contact_book)
        elif choice =='2':
            print("\nAll Contacts:" )
            Contact_book.display_all_contracts()
        elif choice =='3':
            search_contact_ui(Contact_book)
        elif choice =='4':
            update_contact_ui(Contact_book)
        elif choice =='5':
            delete_contact_ui(Contact_book)
        elif choice =='6':
            print("Exit contact book.Goodbay!")
            break
        else:
            print("Invalid choice.please enter a number between 1 to 6.")
            
main()