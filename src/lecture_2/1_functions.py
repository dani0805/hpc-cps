
a = 0


def test_func1():
    a = 1
    print(f"test_func1 {a}")


def test_func2():
    global a
    a = 2
    print(f"test_func2 {a}")


def nested_func():
    a = 3

    def inner_func1():
        a = 4
        print(f"inner_func1 {a}")

    def inner_func2():
        nonlocal a
        a = 5
        print(f"inner_func2 {a}")

    inner_func1()
    print(f"after inner_func1 {a}")
    inner_func2()
    print(f"after inner_func2 {a}")


test_func1()
print(f"after test_func1 {a}")
test_func2()
print(f"after test_func2 {a}")
nested_func()
print(f"after nested_func {a}")