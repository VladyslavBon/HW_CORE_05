from collections import UserDict

class Field:
        pass
    
class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value=None):
        self.value = value

class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone]
    
    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def change_phone(self, phone):
        self.phones.pop()
        self.phones.append(phone)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data.update({record.name.value: record})

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
    
    @input_error
    def handler_add(string):
        parser = string.split(" ")
        name = Name(parser[1].capitalize())
        phone = Phone(parser[2])
        if name.value not in ab.data:
            rec = Record(name, phone)
            ab.add_record(rec)
        else:
            ab[name.value].add_phone(phone)

    @input_error
    def handler_remove(string):
        parser = string.split(" ")
        name = parser[1].capitalize()
        for phone in ab[name].phones:
            if phone.value == parser[2]:
                ab[name].remove_phone(phone)
            
    @input_error
    def handler_change(string):
        parser = string.split(" ")
        name = parser[1].capitalize()
        phone = Phone(parser[2])
        ab[name].change_phone(phone)
    
    @input_error
    def handler_phone(string):
        parser = string.split(" ")
        name = parser[1].capitalize()
        print([x.value for x in ab[name].phones]) 

    def handler_show_all():
        for v in ab.data.values():
            print(v.name.value, [x.value for x in v.phones])

    ab = AddressBook()
    while True:
        string = input().lower()
        if string in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif string == "hello":
            print("How can I help you?")
        elif string == "show all":
            handler_show_all()
        elif string.startswith("add"):
            handler_add(string)
        elif string.startswith("delete"):
            handler_remove(string)
        elif string.startswith("change"):
            handler_change(string)
        elif string.startswith("phone"):
            handler_phone(string)
    
if __name__ == "__main__":
    main()