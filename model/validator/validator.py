import re


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def family_validator(cls, family, message):
        if isinstance(family, str) and re.match(r"^[a-zA-Z\s]{2,30}$", family):
            return family
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def national_validator(cls, national_id, message):
        if re.match(r"^\d{11}$", national_id):
            return national_id
        else:
            raise ValueError(message)

    @classmethod
    def card_number_validator(cls, card_number, message):
        if re.match(r"^[4-5]\d{12,15}$", card_number):
            return card_number
        else:
            raise ValueError(message)
