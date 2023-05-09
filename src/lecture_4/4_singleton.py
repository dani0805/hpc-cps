class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MySingleton(metaclass=SingletonMeta):
    pass

class OtherSingleton(metaclass=SingletonMeta):
    pass

a = MySingleton()
b = MySingleton()
c = OtherSingleton()

print(a is b)
print(a is c)
print(SingletonMeta._instances)