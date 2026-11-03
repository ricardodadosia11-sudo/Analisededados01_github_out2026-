valor_salario = float(input('Salario inicial: '))
percentual = float(input('informe o digito para percentual: '))

percentual = percentual / 100

aumento_percentual  = int(input('informe o aumento percentual de aumento: '))

valor_final = valor_salario * (valor_salario * aumento_percentual / 100)

print(f'Salario inicial: {valor_salario}')
print(f'percentual de aumento: {aumento_percentual:.2f}')
print(f'valor aumento: {valor_final - valor_final:.2f}')
print(f'Salario final: {valor_final:.2f}')



