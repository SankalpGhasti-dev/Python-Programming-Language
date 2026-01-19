# (F - 32) * 5/9 = C
# F = C * 9/5 + 32

def F_to_C(Celsius):
    Fahrenheit = Celsius * 9/5 + 32
    return Fahrenheit

Celsius = float(input("Enter Celsius: "))

F_to_C(Celsius)

print(f"Conversion of Temp of Celsius {Celsius} in Fahrenheit is {F_to_C(Celsius)}.")

