import time 

num1 = int(input("Digite um número: "))

while (num1 <= 0):
    print("Tente outra vez")
    num1 = int(input("Digite um número: "))
   

if num1 % 2 == 0:
    print(' ""P-A-R!"" ')


elif num1 % 2 != 0:
    print("Tente outra vez")

time.sleep(10)

