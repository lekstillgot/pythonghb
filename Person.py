class Person:

    __name = ""
    __age = 0
# constructure

    def __init__(self, name="", age=0):
        self.__name = name
        self.__age = age

        # getter and setter

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age
# method

    def get_profile(self):
        return self.__name + " is " + str(self.__age) + " years old."
# destructure

    def __del__(self):
        return True


# create an object
Person1 = Person("john", 36)
print(Person1.getage())
print(Person1.get_profile())

Person2 = Person("sara", 39)
print(Person2.getage())
print(Person2.get_profile())
