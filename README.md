# Agenda Python

Uma agenda simples desenvolvida em Python para gerenciar seus contatos.

## Funcionalidades

* **Adicionar contatos:** Permite adicionar novos contatos com nome, telefone e endereço.
* **Atualizar contatos:** Permite modificar os dados de contatos existentes.
* **Consultar contatos:** Permite buscar todos os contatos.
* **Excluir contatos:** Permite remover contatos da agenda.

## Tecnologias

* **Python:** Linguagem de programação principal.
* **colorama:** para adicionar cor no terminal.

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <https://github.com/Duplo-P/Agenda.git>
## Como Utilizar

**1. Iniciar a Agenda:**

**2. Menu Principal:**
Ao iniciar a agenda, um menu com as opções disponíveis será apresentado:

    1 - Adicionar Contato: Digite o número correspondente para adicionar um novo contato.
    2 - Atualizar Contato: Digite o número correspondente para modificar um contato existente.
    3 - Procurar Contato: Apresenta todos os contato da agenda.
    4 - Apagar Contato: Digite o número correspondente para remover um contato.
    5 - Ajuda: apresenta um manual de instrução.
    6 - Sair: Digite o número correspondente para encerrar a agenda.

**3. Seguir as Instruções:**

A cada opção escolhida, o programa irá solicitar as informações necessárias para realizar a ação.
Siga as instruções na tela para inserir os dados corretamente.

## Composição do projecto

O projecto é composto por 4 arquivos, a sitar:
**main.py:** é o arquivo principal onde encontramos as funções que dão vida e imagem ao programa.
**modulo.py:** é o arquivo aonde podemos encontrar as duas classes principais, a class Agenda e a class DataBase que foi o intermédiario com o nosso suposto database.
**requirements.txt:** esse arquivo é aonde podemos encontrar as nossas dependencias, que no nosso caso foi o colorama.
**intrunctions.txt:** esse é orquivo que utilizamos para importar as instrunções de ajuda do nosso programa. 

## Guia com imagem
## Nota
**Nota:** Para base de dados utilizamos arquivos json, para armazenar os contactos.
