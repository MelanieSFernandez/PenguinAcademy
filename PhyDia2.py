number = 70
bingo = False
while(bingo == False):
    number2 = int(input("Ingrese un numero"))
    if number2 > number:
        print("Ingrese un valor menor")
    if number2 < number:
        print("Ingrese un valor mayor")
    if number2 == number:
        bingo = True
        print("Lo lograste")












##################Dia3
for varnumeros in range(0,101):
    if varnumeros%3==0 and varnumeros%5==0:
        print(varnumeros,"FizzBuzz")
    elif varnumeros%5==0:
        print(varnumeros,"Buzz")
    elif varnumeros%3==0:
        print(varnumeros,"Fizz")
    else:
        print(varnumeros)
    

