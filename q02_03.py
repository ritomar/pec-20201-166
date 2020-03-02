# Entrada de dados
total_conta = float(input("Total da conta: "))

# Processamento
total_1 = total_conta // 3
total_2 = total_conta // 3
total_3 = total_conta - (total_1 + total_2)

# Saída de dados
print(f'Total Carlos: {total_1:.2f}')
print(f'Total André: {total_2:.2f}')
print(f'Total Felipe: {total_3:.2f}')
