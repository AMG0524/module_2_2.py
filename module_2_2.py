first = int(input('введите число'))
second = int(input('введите число'))
third = int(input('введите число'))

if first == second == third:
    print(3)
if first == second or first == third or second == third:
    print(2)
else:
    print(0)