import re  # imported for _check_phone_number//re means: regex
import string
from tinydb import TinyDB
from pathlib import Path
from typing import Any, List


class User:
    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: int, address: str = ""):
        self.first_name = first_name,
        self.last_name = last_name,
        self.phone_number = phone_number,
        self.address = address

    def __repr__(self):
        return f"User({self.first_name} ,{self.last_name})"

    def __str__(self):
        # return f"{self.first_name}\n{self.last_name}\n{self.phone_number}\n{self.address}"
        return f"{self.full_name}\n{self.f_replace()}\n{self.address}"

    @property
    def full_name(self):  # update will be made after initialisation
        return f"{self.first_name} {self.last_name}"

    def _checks(self):
        self._check_phone_number()
        self._check_names()

    def __check_phone_number(self):
        # patterns = r"!$%&'()*+,-./:;<=>?@[\]^_`{|}~" #r"[+()\s]*"
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number, flags=re.IGNORECASE)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Invalid phone_number {self.phone_number}.")

    def f_replace(self):  # created in purpose to replace _check_phone_number()

        phone_digits = (self.phone_number.__repr__()
                        .replace("+", "")
                        .replace("-", "")
                        .replace("(", "")
                        .replace(")", "")
                        .replace(" ", "")
                        .replace("''", ""))
        return phone_digits

        # Declaring private method

    def __fun(self):
        print("Private method")

    def __check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("First and last name cannot be empty.")
            # special_characters = string.punctuation + string.digits

            # for character in self.first_name + self.last_name:
            #    if character in special_characters:
            raise ValueError(f"Invalid name {self.full_name}.")

    def saveData(self, validate_data: bool = False) -> int:
        # if validate_data:
        # self._checks()
        # User.DB.insert({"first_name":self.first_name}) first option example
        # User.DB.insert(self.__dict__)
        if validate_data:
            return User.DB.insert(self.__dict__)

    def save(self, validate_data=False):
        if validate_data:
            '''return User.DB.insert(
                {"first_name": self.first_name, "last_name": self.last_name, "phone_number": self.phone_number,
                 "address": self.address})'''
            print("Validation....before insertion")
        User.DB.insert(self.__dict__)

def get_all_users():
    print(User.DB.all())

if __name__ == "__main__":
    print(string.punctuation)
    print(string.digits)
    from faker import Faker

    fake = Faker(locale="fr-FR")
    for _ in range(5):
        user = User(
            first_name=fake.first_name,
            last_name="",
            phone_number=fake.phone_number(),
            address=fake.address())
        # user._check_names()
        user.save(validate_data=True)
        #print(user.save(validate_data=True))
        print("-" * 5)
