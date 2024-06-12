import time

def hi_everybody(my_list):
    for name in my_list:
        print("Oi,", name)
 
hi_everybody(["Tina", "Gabi", "Jão"])


def criar_lista(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list
 
print(criar_lista(10))




global a = 1
  
def fun():
    a = 2
    print(a)
 
 
fun()
print(a)
 

 



time.sleep