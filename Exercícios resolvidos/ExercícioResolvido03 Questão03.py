distancia = float(input("Digite a distância que deseja percorrer em km: "))

if distancia <= 200:
  preco = distancia * 0.50
else:
  preco = distancia * 0.45

print(f"O preço da passagem para {distancia:.2f} km é de R$ {preco:.2f}")