from inspect import signature
from types import FunctionType


class EnforceCodingStandardsMeta(type):
    def __new__(mcs, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, FunctionType):
                sig = signature(attr_value)
                for param in sig.parameters.values():
                    if param.annotation == param.empty and param.name != 'self':
                        raise TypeError(f'Missing type annotation for parameter "{param.name}" in method "{attr_name}" of class "{name}"')
                    if param.default == param.empty and param.kind != param.KEYWORD_ONLY and param.name != 'self':
                        raise TypeError(f'Parameter "{param.name}" in method "{attr_name}" of class "{name}" must be a keyword-only argument')

        return super().__new__(mcs, name, bases, attrs)


class BaseClass(metaclass=EnforceCodingStandardsMeta):
    pass


class MyClass(metaclass=EnforceCodingStandardsMeta):
    def my_method(self, *, a: int, b: str):
        pass


class MyClass2(BaseClass):
    def my_method(self, c: int, a: int, b=1):
        pass