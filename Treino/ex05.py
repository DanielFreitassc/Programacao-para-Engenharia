for numero in range(1,101):
    if numero >1:
        primo = True 
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                primo = False
                break
        if primo:
            print(numero)
                            