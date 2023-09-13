def hello():
    print("Hello")


hello()


def area(width=0, height=0):
    total = width * height
    return total


print("Area is ", area(5, 100))
