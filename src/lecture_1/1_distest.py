import dis

def list_comprehension():
    return [x**2 for x in range(10)]

def for_loop():
    squares = []
    for x in range(10):
        squares.append(x**2)
    return squares

print("List comprehension:")
dis.dis(list_comprehension)
print("\nFor loop:")
dis.dis(for_loop)

