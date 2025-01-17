def sumar(a, b):
    return a + b

def calculo():
    n1 = int(input("dime el primer numero: "))
    n2 = int(input("dime el segundo numero: "))
    resultado = sumar(n1, n2)
    print("la suma de" , n1 , "y" , n2 , "es:", resultado)

calculo()