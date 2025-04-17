peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
calculo_imc = peso/(altura*altura)
if calculo_imc < 18.5:
    print("abaixo do peso")
elif calculo_imc > 18.6 and calculo_imc < 24.9:
    print("peso ideal parabens")
elif calculo_imc > 25.0 and calculo_imc < 29.9:
    print("levemente  acima do peso")
elif calculo_imc  > 30.0 and calculo_imc < 34.9:
    print("obesidade grau 1")
elif calculo_imc > 35.0 and calculo_imc < 39.9:
    print("obesidade grau 2")
elif calculo_imc >= 40:
    print("obesidade grau 3")
else :
    print("va ao medico urgente")
