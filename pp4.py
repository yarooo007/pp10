a = list(input("Введите список "))
b = int(input("Введите елемент списка "))
def ps(a,b):
    if b in a:
        return a.index(b)
    else:
        return "-1"
print(ps(a,b))
