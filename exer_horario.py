"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Que horas sao agr?'))

if hora < 11:
    print('Bom dia ')
elif hora > 11 and hora <=17:
    print('Boa tarde')
elif hora >17 and hora <=23:
    print('Boa noite')
else:
    print('Voce digitou uma hora inválida')            