print("Enter Conversion mode 1. for Dolar->RS 2. for RS->Dolar")
a = int(input())
print("Enter the amount which need to convert")

if a == 1:
    x = float(input())
    y = x * 80
    print("")
elif a == 2:
    x = float(input())
    y = x / 80
else:
    raise "Wrong data"

print(y)