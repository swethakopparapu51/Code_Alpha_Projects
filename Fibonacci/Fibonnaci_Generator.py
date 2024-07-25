def fibonnaci_generator():
    yield third
n=int(input("Enter a number:"))
first=0
second=1
print(first)
print(second)
for i in range(n):
    third=first+second
    first=second
    second=third
    print(third)




f1=fibonnaci_generator()