from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field): #перевизначення конструктора для перевірки валідності номеру телефону
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be a 10-digit number.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name) #встановлюємо ім*я контакту
        self.phones = [] #створюєм порожній список телефонів

    def add_phone(self, phone):
        self.phones.append(Phone(phone)) #додаємо телефон до списку

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone): #редагування, замінюємо старий номер на новиц
        for i, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone): #шукаємо телефон за знчанням
        for p in self.phones:
            if str(p) == phone:
                return p

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}" # перевизначаємо стр для виведення контакту у вигляді рядку

class AddressBook(UserDict): #додавання до адресної книги, інд за ім. контакта
    def add_record(self, record): 
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == "__main__":
    book = AddressBook() #створення нової адресної книги

    john_record = Record("John") #створення запису для John
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record) #додавання запису John до адресної книги

    jane_record = Record("Jane") #створюємо та додаємо новий запис для Jane
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items(): #виводимо всі записи у книзі
        print(record)

    john = book.find("John")  #знаходимо та редагуємо телефон для John
    john.edit_phone("1234567890", "1112223333")

    print(john)  #виводимо: Contact name: John, phones: 1112223333; 5555555555

    found_phone = john.find_phone("5555555555") #пошук конкретного телефону у записі John
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    #удаляєм запис Jane
    book.delete("Jane")
