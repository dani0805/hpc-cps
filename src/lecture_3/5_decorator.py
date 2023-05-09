"""
In this example, we define a function decorator called log_calls that takes a class as an argument.
The decorator creates a new class called Wrapped, which inherits from the original class. The Wrapped class overrides
the __getattribute__ method, so when an attribute is accessed, it checks if the attribute is callable (i.e., a method).
If it is, it wraps the method call with the logger method.

'logger', any dunder methods, and the 'wrapped' attribute are excluded from the attribute resolution process, to avoid
infinite recursion or other unexpected behavior.

The logger method logs the method name before and after the method call, giving us insight into the method calls being made.

The MyClass class is decorated with the log_calls decorator using the @ syntax. This causes instances of MyClass to have
logging functionality for their method calls.
"""

import functools

def log_calls(cls):
    class Wrapped(cls):
        def __getattribute__(self, attr):
            if attr == 'logger' or attr.startswith('__') or attr == 'wrapped':
                return object.__getattribute__(self, attr)
            orig_attr = super().__getattribute__(attr)
            if callable(orig_attr) and attr != '__getattribute__':
                return functools.partial(self.logger, orig_attr)
            return orig_attr

        def logger(self, method, *args, **kwargs):
            print(f"Calling method {method.__name__}...")
            result = method(*args, **kwargs)
            print(f"Method {method.__name__} finished.")
            return result
    return Wrapped

@log_calls
class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

instance = MyClass(42)
print(instance.get_value())  # Output: 42
instance.set_value(24)
print(instance.get_value())  # Output: 24
