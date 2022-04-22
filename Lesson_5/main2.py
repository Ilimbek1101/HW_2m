import re


# email = input("eMail: ")
# is_valid = re.search(r"[a-zA-Z0-9]+@(gmail|mail|yandex)\.",
#                      email)
# print(is_valid)

phone = input("Phone Number: ")
is_valid = re.search(r"\+996-([0-9]{3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)
print(is_valid)