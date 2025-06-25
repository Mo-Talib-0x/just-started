def square_root(num):
    square=num**0.5
    return round(square,2)
num = int(input("Enter the number: "))

square= square_root(num)
print(square)