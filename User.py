import re  # imported for _check_phone_number//re means: regex


class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name,
        self.last_name = last_name,
        self.phone_number = phone_number,
        self.address = address

    def __repr__(self):
        return f"User({self.first_name} ,{self.last_name})"

    def __str__(self):
        # return f"{self.first_name}\n{self.last_name}\n{self.phone_number}\n{self.address}"
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self):  # update will be made after initialisation
        return f"{self.first_name} {self.last_name}"

    def _check_phone_number(self):
        # self.phone_number.replace("+"," ").replace("(", "") // You manage manually, but using regex is better
        # pattern: str = r'[+()\s]*'
        pattern = r"[+()\s]*"
        replacement = ""
        # phone_digits = re.sub(pattern, replacement, self.phone_number)
        phone_digits = re.sub(pattern,replacement,self.phone_number)
        if(len(phone_digits)<10 or not phone_digits.isdigit()):
            raise ValueError(f"Invalid phone_number {self.phone_number}")
        #print(phone_digits)


if __name__ == "__main__":
    from faker import Faker

    fake = Faker(locale="fr-FR")
    for _ in range(25):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number=fake.phone_number(),
            address=fake.address())
        print((user))
        # user.check_phone_number()

        # print("-" * 10)
