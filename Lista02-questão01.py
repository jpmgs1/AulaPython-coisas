#João Paulo - Redes de Computadores 1v
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nMédia do aluno: {media:.1f}")

if media >= 7:
    print("Aluno: APROVADO.")
else:
    print("Aluno: REPROVADO.")