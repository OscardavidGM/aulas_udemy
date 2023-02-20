def factorial(n):
    print(f"Calculando el factorial de {n}")
    if n == 0 or n == 1:
        print(f"factorial de {n} = 1")
        return 1 
    else:
        fat = n * factorial(n - 1)
       
        print(n, fat)
    return fat 

factorial(4)           