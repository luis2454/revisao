repertir = "s"
while repertir == "s":

    num = int(input("digite um numero : "))
    if num > 0:
     if num %2 == 0 :
         print(f"e par e positivo ")

     else:
         print(f" e impar e positivo")
    else:
     if num % 2 == 0:
         print(f"e par e negativo")
     else :
         print(" e impar e negativo")
    repertir = input("repita o numero")



