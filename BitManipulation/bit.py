x=13
y=5
z=3


a=13
b=9
print(a&b)
print(a|b)
# print(x&y)
# print(x&y&z)
# print(x|y)
# print(x^y)
# print(~x)
# print(x<<2)
# print(x>>2)


def even_odd(num):
    if num & 1:
        print("Odd")
    else:
        print("Even")

even_odd(13)
even_odd(10)
