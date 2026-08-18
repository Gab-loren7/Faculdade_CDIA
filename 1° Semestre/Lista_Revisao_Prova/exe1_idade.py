'''
1. Escreva um programa que leia a idade de uma pessoa e informe:
• “Criança” (0–12)
• “Adolescente” (13–17)
• “Adulto” (18–59)
• “Idoso” (60+)
'''

idade = int(input('Digite a sua idade: '))


def informe_idade():
    if idade >= 0 and idade <= 12:
        print('\u2022 “Criança”\t (0–12)')
    elif idade >= 13 and idade <= 17:
        print('\u2022 “Adolescente”\t (13–17)')
    elif idade >= 18 and idade <= 59:
        print('\u2022 “Adulto”\t (18–59)')
    else:
        print('\u2022 “Idoso”\t (60+)')
informe_idade()
        