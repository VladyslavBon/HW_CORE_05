from collections import UserDict

def main():

    def input_error(func):
        def inner(string):
            try:
                func(string)
            except IndexError:
                print("Give me name and phone please")
            except (KeyError, ValueError):
                print("Enter user name")
        return inner
    
    class Field:
        pass
    
    class Name(Field):
        def __init__(self, name):
            self.name = name

    class Phone(Field):
        def __init__(self, phone=None):
            self.phone = phone

    class Record:
        def __init__(self, name):
            self.name = name
            self.phones = []
        
        def add_phone(self, phone):
            self.phones.append(phone)

        def remove_phone(self, phone):
            self.phones.remove(phone)

        def change_phone(self, new_phone):
            self.phones.pop()
            self.phones.append(new_phone)

    class AddressBook(UserDict):
        def add_record(self, record):
            self.data.update({record.name: record.phones})
    
    @input_error
    def handler_add(string):
        parser = string.split(" ")
        name = Name(parser[1].capitalize()).name
        phone = Phone(parser[2])
        if name not in contacts:
            current_record = Record(name)
            contacts.update({name: current_record})
            current_record.add_phone(phone.phone)
        else:
            contacts.get(name).add_phone(phone.phone)
        book.add_record(contacts.get(name))

    @input_error
    def handler_change(string):
        parser = string.split(" ")
        name = Name(parser[1].capitalize()).name
        phone = Phone(parser[2])
        contacts.get(name).change_phone(phone.phone)
        book.add_record(contacts.get(name))
    
    @input_error
    def handler_phone(string):
        parser = string.split(" ")
        print(book.data[parser[1].capitalize()]) 

    contacts = {}
    book = AddressBook()
    while True:
        string = input().lower()
        if string in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif string == "hello":
            print("How can I help you?")
        elif string == "show all":
            for k, v in book.data.items():
                print(k, v)
        elif string.startswith("add"):
            handler_add(string)
        elif string.startswith("change"):
            handler_change(string)
        elif string.startswith("phone"):
            handler_phone(string)
    
if __name__ == "__main__":
    main()