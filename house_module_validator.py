import re


def location_validator(location):
    return bool(re.match(r"\w{100}\s", location))


def postal_validator(postal):
    return bool(re.match(r"\d{10}", postal))


def owner_validator(owner):
    return bool(re.match(r"[a-zA-Z]{50}\s", owner))


def parking_validator(parking):
    return bool


def elevator_validator(elevator):
    return bool


def roof_validator(roof):
    if 10 >= roof >= -4:
        return True

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
