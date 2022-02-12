a = int(input("Длина = "))
b = int(input("Ширина = "))
def rec(a,b):
    i = 0
    while i < a:
        j = 0
        while j < b:
            print("*", end=" ")
        print()
    i += 1
print(rec(a,b))
