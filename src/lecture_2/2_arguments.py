
def my_function(a, b: int, c=0, d: float = 0, *args, **kwargs):
    print(a, b, c, d, args, kwargs)
    e = args[0]
    f = kwargs['f']
    g = kwargs['g']
    print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))


my_function(1, 2, 3, 5.5, 6, f=7+3j, g=8)


def print_out(arg1:int, this_word: str, after_this_word: str) -> str:
    """
    This function returns a string with the words in the correct order
    it also prints out the words in the correct order

    param this_word: the word to print out second
    param after_this_word: the word to print out first
    return: the string with the words in the correct order
    """

    print(f"{after_this_word} {this_word}")
    return f"{after_this_word} {this_word}"


print_out(this_word="world", after_this_word="hello")
print(print_out.__annotations__)
print(print_out.__doc__)
print(print_out(this_word="world 2", after_this_word="hello"))