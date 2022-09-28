class Person:
    firstName = ""
    surname = ""


def printPerson(personParam):
    return personParam.firstName, personParam.surname


def createPerson() -> Person:
    fn = input("Enter first name: ")
    sn = input("Enter surname: ")
    newPerson = Person()
    newPerson.firstName = fn
    newPerson.surname = sn
    return newPerson
