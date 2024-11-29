import re


def location_validator(location):
    print(re.match(r"\w{100}\s", location))


def postal_validator(postal):
    return bool(re.match(r"\d{10}", postal))


def owner_validator(owner):
    print(re.match(r"[a-z]{50}\s", owner))


def parking_validator(parking):
    print(re.match(r"\d{4}\s", parking))


def elevator_validator(elevator):
    print(re.match(r"\d{4}\s", elevator))


def roof_validator(roof):
    print(re.match(r"\d{4}\s", roof))


# def myFunction():
#     return True
#
#
# if myFunction():
#     print("Yes!")
# else:
#     print("No!")
# pass
#
#
# def myFunction():
#     return True
#
#
# if myFunction():
#     print("Yes!")
# else:
#     print("No!")
# pass
#
#
# def myFunction():
#     return True
#
#
# if myFunction():
#     print("Yes!")
# else:
#     print("No!")
