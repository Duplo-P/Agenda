from modulo import *
import colorama
from os import system, get_terminal_size

#-----------------------------------------FUNCÕES DO APP----------------------------------------
def menu():
    system("clear")
    agenda = Agenda() 
    while(True):
        print(mudaCor(3,"--BEM VINDO A SUA AGENDA--".center(terminalSize())))
        op = input("1 - Adicionar\n2 - Atualizar\n3 - Procurar\n4 - Apagar\n5 - Ajuda\n6 - Sair\n")
        if op == "1":
            add(agenda)
        elif op == "2":
            update(agenda)
        elif op == "3":
            surch(agenda)
        elif op == "4":
            delete(agenda)
        elif op == "5":
            help()
        elif op == "6":
            system("clear")
            exit(mudaCor(0,"Aplicação Terminada.."))
        else:
            system("clear")
            print(mudaCor(0,"ESCOLHE UMA DAS OPÇÕES VÁLIDAS"))
def pergunta():
    op = input(mudaCor(4,"\nContinuar( Enter ) or Sair( S )? -> ")).upper()
    if op != "S":
        return 1
    system("clear")
    return 0

def mudaCor(cor: int, txt: str):
    if cor == 0:
        return colorama.Fore.RED + txt + colorama.Fore.RESET
    elif cor == 1:
        return colorama.Fore.GREEN + txt + colorama.Fore.RESET
    elif cor == 2:
        return colorama.Fore.BLUE + txt + colorama.Fore.RESET
    elif cor == 3:
        return colorama.Fore.YELLOW + txt + colorama.Fore.RESET
    elif cor == 4:
        return colorama.Fore.CYAN + txt + colorama.Fore.RESET
    elif cor == 5:
        return colorama.Fore.MAGENTA + txt + colorama.Fore.RESET
    else:
        return txt
def terminalSize():
    try:
        largura, _ = get_terminal_size()
        return largura
    except OSError:
        return 80

def add(agenda):
    while(True):
        system("clear")
        print(mudaCor(3, "--ADICIONAR CONTACTO--".center(terminalSize())))
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        contato ={"Nome": nome.lower().title(), "Telefone": telefone,"Endereço": endereco.lower().title()}
        print(mudaCor(1,agenda.add(contato)))
        if pergunta() == 0:
            break
def update(agenda):
    system("clear")
    print(mudaCor(3,"--ATUALIZAR CONTACTO--".center(terminalSize())))
    while(True):
        agenda.surch_all()
        id = input(mudaCor(5,"Id: "))
        nome = input("Novo Nome: ")
        telefone = input("Novo Telefone: ")
        endereco = input("Novo Endereço: ")
        contato ={"Nome": nome.lower().title(), "Telefone": telefone,"Endereço": endereco.lower().title()}
        print(mudaCor(1,agenda.update(id, contato)))

        if pergunta() == 0:
            break
        
def surch(agenda):
    system("clear")
    print(mudaCor(3, "--PROCURAR CONTACTO--".center(terminalSize())))
    agenda.surch_all()
    op = input(mudaCor(4,"Sair ( Enter ). "))
    menu()
    
def delete(agenda):
    system("clear")
    print(mudaCor(3,"--APAGAR--".center(terminalSize())))
    agenda.surch_all()
    dele = input(mudaCor(5,"Digite o id do contacto: "))
    x = agenda.delete(dele)
    system("clear")
    print(mudaCor(0,x["Nome"] + " ELIMINADO"))
    
    
def help():
    system("clear")
    with open("instrunction.txt", "r") as arq:
        ficheiro = arq.read()
        print(ficheiro)
    op = input(mudaCor(4,"Sair ( Enter ). "))
    menu()
#_____________________________________________________TESTE_____________________________________

menu()
        
    