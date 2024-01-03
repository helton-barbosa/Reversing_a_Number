aux = number = int(input('Entre com um número inteiro: '))
rev = 0

while number != 0:
    last_digit = number % 10
    number //= 10
    rev = rev * 10 + last_digit

print(f'O inverso do número {aux} é {rev}')
