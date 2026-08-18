# Foco: Operadores Lógicos e Precedência

valorAdmin = "Gabriel"
valorChaveAcesso = 123
statusSistemaManutencao = False

AdminRecebido = input("Qual o Usuário?\n")
ChaveRecebido = int(input("Qual a Chave?\n"))


if statusSistemaManutencao == True:
    print("Sistema está Indisponivel para Manutenção!")
elif valorAdmin == AdminRecebido or valorChaveAcesso == ChaveRecebido:
    print("Usuário Logado! ✅")
else:
    print("Usuário Negado! ❌")
