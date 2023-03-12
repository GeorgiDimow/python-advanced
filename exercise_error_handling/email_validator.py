import re

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class ContainTooManyAtSymbolError(Exception):
    pass


class ContainInvalidSymbolsError(Exception):
    pass


class ContainCapitalLettersError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
pattern_capital = r'[A-Z]+'

valid_domains = ['.com', '.bg', '.org', '.net']

email = input()
b = re.findall(pattern_name, email)[0]
a = email.split("@")[0]

while email != "End":

    try:
        if email.count('@') > 1:
            raise ContainTooManyAtSymbolError("Email must contain only one @")

        elif len(email.split("@")[0]) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        elif re.findall(pattern_capital, email):
            raise ContainCapitalLettersError("Email must contain only lower case letters")

        elif re.findall(pattern_name, email)[0] != email.split("@")[0]:
            raise ContainInvalidSymbolsError("Name contains different symbols than letters,digits, \"_\" and \".\"")

        elif "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        elif re.findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

        print("Email is valid")

    except IndexError:
        print("Invalid email")

    email = input()
