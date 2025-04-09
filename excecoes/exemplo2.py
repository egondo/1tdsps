if __name__ == "__main__":
    try:
        a = float(input("A: "))
        b = float(input("B: "))

        quociente = a / b
        
        
    except ZeroDivisionError as e:
        print("Divisao por zero!")
    
    except ValueError as v:
        print("Erro na conversao")

    else:    
        print(f"{a}/{b} = {quociente}")
    print("Bom dia!")