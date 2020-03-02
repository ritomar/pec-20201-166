# Entrada de Dados
PRECO_PAO = 0.12
PRECO_BROA = 1.50
POUPANCA = 0.10

qtd_paes = int(input("Quantidade de pães vendidos: "))
qtd_broas = int(input("Quantidade de broas vendidas: "))

# Processamento
total_vendido = (qtd_paes * PRECO_PAO) + (qtd_broas * PRECO_BROA)
valor_poupanca = total_vendido * POUPANCA

# Saída de dados
print(f'Total vendido: {total_vendido:.2f}')
print(f'Valor para poupança: {valor_poupanca:.2f}')


