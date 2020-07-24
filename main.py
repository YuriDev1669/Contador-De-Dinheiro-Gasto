import os
from time import sleep
from datetime import date
#DEV YURII
ano= date.today().year
dia= date.today().day
mês= date.today().month

def style():
	print("\033[01;33m-"*37)
	TXT = "CONTADOR"
	print(TXT.center(40))
	print("-"*37)
	print(" ")
	
###############	
def fim():
	os.system('clear') or None
	print("\033[01;33m-"*37)
	txt = "Finalizado"
	print(txt.center(40))
	print("-"*37)
##################

def divadd():
	os.system('clear') or None
	abre = open("divida.txt","a+")
	pessoa = input(">> PESSOA:")
	print(" ")
	valor = input(">> VALOR:")
	add = abre.write(f">> {pessoa}    {valor}\n")
	print(" ")
	print(">> ADCIONADO COM SUCESSO")
	print (" ")
	print(f">> {pessoa}  {valor}")
	abre.close()
	sleep(2)
	os.system("clear") or None
	opc3()

###################	
def diver():
	os.system("clear") or None
	abre = open("divida.txt","r")
	abriu = abre.read()
	print(abriu)
	print("-"*37)
	abre.close()
	voltar = int(input(">> CLIQUE (75) PRA VOLTAR:"))
	if voltar == 75:
		opc3()
########################
	
##############
def opc1():
	os.system("clear") or None
	ler = open("lista.txt","r")
	leu = ler.read()
	print(leu)
	print(" ")
	print("-"*37)
	volt = int(input(">> CLIQUE (75) PRA VOLTAR:"))
	if volt == 75:
		os.system("clear") or None
		main()
	else:
		print(">> INVALIDO!!")
		sleep(2)
		opc1()
########################

####################		
def opc2():
	os.system("clear") or None
	add = open("lista.txt","a+")
	preço= input(">> Valor:")
	add.write(f">> {preço}   {dia}/{mês}/{ano}\n")
	add.close()
	print(" ")
	print(">> ADCIONADO COM SUCESSO")
	print(" ")
	print(f">> Valor:{preço}")
	print(" ")
	print(f">> DATA:{dia}/{mês}/{ano}")
	sleep(2.5)
	os.system("clear") or None
	main()
#######################
####################
def opc3():
	os.system('clear') or None
	print("-"*37)
	txt = "DIVIDAS"
	print(txt.center(40))
	print("-"*37)
	print(" ")
	print('''[ 1 ] VER
[ 2 ] ADCIONAR
[ 3 ] MENU''')
	print(" ")
	suaOp = int(input(">> SUA OPCÃO: "))
	if suaOp == 1:
		diver()
	elif suaOp == 2:
		divadd()
	elif suaOp == 3:
		os.system("clear") or None
		main()
	else:
		print(" ")
		print(">> OPCÃO INVÁLIDA!!")
		main()
def opc4():
	os.system("clear") or None
	apaga = open("senha.txt","w+")
	nova = input(">> NOVA SENHA:")
	apaga.write(nova)
	apaga.close()
	print(" ")
	print(">> REDEFINIDO COM SUCESSO!!")
	sleep(2.5)
	os.system("clear") or None
	main()

		

#####################
def main():
	style()
	print('''\033[01;32m[ 1 ] COMPRAS
[ 2 ] ADCIONAR COMPRAS
[ 3 ] DIVIDAS
[ 4 ] REDEFINIR SENHA
[ 5 ] SAIR''')
	print (" ")
	opc = int(input(">> OPÇÃO:"))
	if opc == 1:
		opc1()
	elif opc == 2:
		opc2()
	elif opc == 3:
		opc3()
	elif opc == 4:
		opc4()
	elif opc == 5:
		fim()
	else:
		print(" ")
		print(">> OPCÃO INVÁLIDA!!")
		sleep(1.5)
		os.system("clear") or None
		main()


################
try:
	file = open("senha.txt","rt")
	file.close()
except FileNotFoundError:
	style()
	file2 = open("senha.txt","w+")
	defi2 = input(">> DEFINIR SENHA:")
	file2.write(defi2)
	file2.close()
	main()
else:
	style()
	file3 = open("senha.txt","r")
	mostrar = file3.read()
	senha = input(">> SENHA DE ACESSO:")
	if senha == mostrar:
		os.system("clear") or None
		main()
	else:
		os.system("clear") or None
		print(">> SENHA INCORRETA!!")
		print(" ")
		senha = input(">> SENHA DE ACESSO:")
		if senha == mostrar:
			os.system("clear") or None
			main()
		else:
			os.system("clear") or None
			print(" ")
			print(">> SENHA INCORRETA!!")
			sleep(2)
			fim()
		
