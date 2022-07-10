def square_cube(no):
    sq=no*no
    cb=no*no*no
    return sq,cb



print("Enter value")
a=int(input())
s,c=square_cube(a)
print("Square",s)
print("Cube",c)