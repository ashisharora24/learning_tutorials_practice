def foo(n):
    def multiple(x):
        return x*n
    return multiple


a = foo(5)
print(type(a))
b = foo(5)
print(a(b(2)))
