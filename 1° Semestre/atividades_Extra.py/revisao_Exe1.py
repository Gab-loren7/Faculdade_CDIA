'''
Implemente uma função chamada buscar, que recebe duas strings origem e subs, devolvendo o índice
da primeira ocorrência de subs em origem. Se não encontrar, deve retornar -1

Obs: não use a função pronta “find” do python. O desafio é fazer sua própria versão.

Ex: buscar(“dificilmasviavel”, “mas”) deve retornar 7
buscar(“dificilmasviavel”, “masz”) deve retornar -1

'''
def buscar(strOrigem, strSubs):
    contador = -1
    conterSub = strOrigem.count(strSubs)
    if conterSub == True:
        arraySubs = list(strSubs)
        for i in strOrigem:
            contador += 1
            if i == arraySubs[0]:
                print(contador)
                break
    else:
        print('-1')

buscar('Sofia Linda','Linda')
