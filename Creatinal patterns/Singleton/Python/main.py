

# First way of creating a Singleton in Python
class SingletonFirst():

    __instance = None

    @staticmethod
    def getInstance():
        if SingletonFirst.__instance == None:
            SingletonFirst()
        return SingletonFirst.__instance

    def __init__(self) -> None:
        if SingletonFirst.__instance != None:
            raise Exception("SingletonFirst already exists")
        else:
            SingletonFirst.__instance = self


s1 = SingletonFirst.getInstance()
print(s1)
s2 = SingletonFirst.getInstance()
print(s2)
# s3 = SingletonFirst()
# print(s3)

print("#" * 20)

# Second way of creating a Singleton in Python
class SignletonSecond:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


s4 = SignletonSecond()
print(s4)
s5 = SignletonSecond()
print(s5)
