#потрібно щоб числа у рядку стали в стовпчик .
number = int(input('Enter a number: '))
variant1 = number // 1000
variant2 = number % 1000 // 100
variant3 = number % 100 // 10
variant4 = number % 10
print1 = (variant1)
print2 = (variant2)
print3 = (variant3)
print4 = (variant4)
print( variant1, variant2, variant3, variant4, sep="\n")
