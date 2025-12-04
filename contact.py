class Contact:
    def __init__(self,name,phone,email):
        self.name = name.strip() 
        self.phone = phone.strip()
        self.email = email.strip()
    def display_contact(self):
        print(f"Name :{self.name}")
        print(f"phone :{self.phone}")
        print(f"email :{self.email}")
        print("_" * 30)

        