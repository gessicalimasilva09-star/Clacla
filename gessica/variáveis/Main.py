def main():

    altura= float ( input ("Digite a sua altura: "))
    idade= int (input ("digite a sua idade: "))
    isCasado= input("vc é casado? ")
    sexo= input (" Digite o seu sexo: ")
    nome= input("Digite o seu nome: ")
    peso= float( input("Digite o seu peso:"))
    cpf= input("Digete o seu cpf: ")
    
    print("O ", nome, " mede ", altura, "m de altura, tem ", idade, "anos de idade")
    print("É do sexo", sexo, "pesa", peso, "e seu cpf É:",cpf)

    if isCasado == "S" or isCasado == "s":
        print("O ", nome, "é casado")
    elif isCasado == "Sou" or isCasado == "sou":
        print("Ele é casado")
    else:
        print("O ", nome, " não é casado") 


    return 0
main()
