class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        return cls.instance


        
s1 = SingletonClass()
s2 = SingletonClass()

s1.name = "Wald"

print(s1 is s2)
print(s2.name)
