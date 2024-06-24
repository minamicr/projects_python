
def nota_conceito(valor):
    if (valor > 10.0):
        return "Nota inválida"
    elif (valor > 9.1):
        return "A"
    elif (valor > 8.1):
        return "A-"
    elif (valor > 7.1):
        return "B"
    elif (valor > 6.1):
        return "B-"
    elif (valor > 5.1):
        return "C"
    elif (valor > 4.1):
        return "C-"
    elif (valor > 3.1):
        return "D"
    elif (valor > 2.1):
        return "D-"
    elif (valor > 1.1):
        return "E"
    elif (valor > 0.1):
        return "E-"
    else:
        return("Nota inválida")

if __name__ == '__main__':
    nota = input("Por favor, informe a nota:")
    if nota.isnumeric:
        print("Nota " + nota_conceito(float(nota)))