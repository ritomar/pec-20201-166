# Entrada de dados
cotacao_dolar = float(input("Valor do dólar hoje: "))
qtd_dolares = float(input("Quantos dólares você tem?\n"))

# Processamento
valor_em_reais = cotacao_dolar * qtd_dolares

# Saída de dados
print(f'Você tem R${valor_em_reais:.2f}')

