import json
import os
#Criação das classe

#-----------------------------------------CLASSES DO APP--------------------------------------------
class DataBase:
    def __init__(self):
        self.arquivo = "bd.json"
    def verificar(self):
        if not os.path.exists(self.arquivo):
            begin = {"0": {"Nome":"Duplo P", "Telefone":"922770270", "Endereço":"Benguela/Navegante",}}
            with open(self.arquivo,"w") as arquivo:
                json.dump(begin,arquivo, indent=8)

    def addBd(self,dic):
        with open(self.arquivo, "r") as arquivo:
                dados = json.load(arquivo)
        id = int(self.pegar()) + 1
        dados[str(id)] = dic 
        with open(self.arquivo,"w") as arquivo:
            json.dump(dados, arquivo, indent=8)
        
    def pegar(self):
        with open(self.arquivo, "r") as arquivo:
                dados = json.load(arquivo)
                chaves = list(dados.keys())     
        return chaves[-1]
        
    def surchBd(self):
        self.verificar()
        try:
            with open(self.arquivo, "r") as arquivo:
                dados = json.load(arquivo)
            return dados
        except FileNotFoundError:
            return "NO FOUND"
            
class Agenda:
    def __init__(self):
        self.bd = DataBase()
    def add(self, contato:dict):
        self.bd.verificar()
        self.bd.addBd(contato)
        return "Adionado com Sucesso"
    
    def surch_all(self):
        for chave, valor in self.bd.surchBd().items():
            print(f"Id: {chave}")
            print(f"Nome: {valor["Nome"]}\tTelefone: {valor["Telefone"]}\tEndereço: {valor["Endereço"]}\n")
        
    def delete(self, id: str):
        valores = self.bd.surchBd()
        for chave, __ in valores.items():
            if id == chave:
                x = valores.pop(chave)
                self.gravar(valores)
                return x
        return "NO FOUND"
    def gravar(self,dados):
         with open(self.bd.arquivo,"w") as arq:
            json.dump(dados,arq, indent=8)
    def verId(self, id):
        valores = self.bd.surchBd()
        if str(id) in valores.keys(): 
            return True
        return False
        
    def update(self,id , contato:dict):
        valores = self.bd.surchBd()
        for chave, dic in valores.items():
            if id == chave:
                valores[chave]["Nome"] = contato["Nome"]
                valores[chave]["Telefone"] = contato["Telefone"]
                valores[chave]["Endereço"] = contato["Endereço"]
                self.gravar(valores)
                return f"Nome: {valores[chave]["Nome"]}, Telefone: {valores[chave]["Telefone"]}, Endereço: {valores[chave]["Endereço"]}"
        return "NO FOUND"
        

                
        
        
    
    