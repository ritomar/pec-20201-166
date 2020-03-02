# Entrada de dados
sua_altura = float(input("Digite sua altura: "))
sua_sombra = float(input("Medida da sua sombra: "))
sombra_predio = float(input("Sombra do prédio: "))

# Processamento
altura_predio = (sua_altura * sombra_predio) / sua_sombra

# Saída de Dados
print(f'A altura do prédio é: {altura_predio:.2f}')


