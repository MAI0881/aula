'''Dois números inteiros e um resultado para cada operacao'''

print('Digite um número inteiro: ')
n1 = int (input())
print('Digite outro número inteiro: ')
n2 = int (input())

soma = n1+n2
print('A soma dos dois digitos é: ',soma)


sub = n1-n2
print('A subtração do primeiro pelo segundo digito é: ',sub)


mult = n1*n2
print('A multiplicação entre os digitos é: ',mult)


div = n1/n2
print('A divisão entre os digitos é: ',div)


trunc = n1//n2
print ('A divisão truncada entre os digitos é: ',trunc)


resto = n1%n2
print ('O resto da divisão dos digitos é: ',resto)


exp1 = (n1)**2
print('A exponenciação do primeiro digito é: ',exp1)


exp2 = (n2)**2
print('A exponenciação do segundo digito é: ',exp2)
