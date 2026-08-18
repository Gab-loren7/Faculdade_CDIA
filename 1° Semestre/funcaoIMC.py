def calc_imc (peso, altura):
    return peso / altura ** 2

IMC = calc_imc(80, 1.74)
print(f"Seu IMC é igual a : {IMC:.1f}")
