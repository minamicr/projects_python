
score = float(input("Informe a nota do aluno:"))

if (score > 10.0 or score < 0.0):
    print("Nota inválida")
elif (score <= 10.0 and score >= 9.1):
    print("Nota A")
elif (score <= 9.0 and score >= 8.1):
    print("Nota A-")
elif (score <= 8.0 and score >= 7.1):
    print("Nota B")
elif (score <= 7.0 and score >= 6.1):
    print("Nota B-")
elif (score <= 6.0 and score >= 5.1):
    print("Nota C")
elif (score <= 5.0 and score >= 4.1):
    print("Nota C-")
elif (score <= 4.0 and score >= 3.1):
    print("Nota D")
elif (score <= 3.0 and score >= 2.1):
    print("Nota D-")
elif (score <= 2.0 and score >= 1.1):
    print("Nota E")
elif (score <= 1.0 and score >= 0.0):
    print("Nota E-")
