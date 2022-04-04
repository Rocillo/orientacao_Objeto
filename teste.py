from pkg_resources import compatible_platforms


def cria_conta(numero, titular, saldo, limite):
   conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
   return conta
def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
def saca(conta,valor):
    conta["saldo"] -= valor
def deposita(conta, valor): 
    conta ["saldo"] += valor

numero = int(input('Digite o numero da sua conta: '))
titular = input('Digite o nome do tiutlar: ').upper()
saldo = 1000.0
limite = 1000.0
conta = cria_conta(numero,titular,saldo,limite)
extrato(conta)
""