
# First implementation
# class SingletonClass(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = object.__new__(cls)
#         return cls.instance


        
# s1 = SingletonClass()
# s2 = SingletonClass()

# s1.name = "Wald"

# print(s1 is s2)
# print(s2.name)



# Second implementation
class Singleton_2:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Singleton_2.__instance == None:
             Singleton_2()
        return Singleton_2.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Singleton_2.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton_2.__instance = self



s1 = Singleton_2().getInstance()
print(s1)
s2 = Singleton_2.getInstance()
print(s2)

print(s1 is s2)
