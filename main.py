import os

options = {
  "0" : "sair",
  "1" : "criar_tarefa",
  "2" : "listar_tarefas",
  "3" : "editar_tarefa",
  "4" : "remover_tarefa",
}

tarefas = [["Minha tarefa 1", False]]

def __main__():
  """ Fluxo base do programa. Permite mudar de tela """
  inp = "1"

  while inp != "0":
    __print_separator("MENU")
    
    for o in options:
      print(f"\t[{o}] - {options[o]}")
    inp = input("\nDigite a opção desejada: ")
    
    try:
      globals()[options[inp]]()
    except:
      if inp == '0':
        return
      print(f"Input \"{inp}\" não é reconhecido. por favor digite apenas um dos seguintes numeros: {list(options.keys())}")

def criar_tarefa():
  """ Permite cirar uma nova tarefa """
  __print_separator("adicionar")
  
  global tarefas
  nm = input("Digite o nome da tarefa que deseja criar: ")
  tarefas.append([nm, False])
  print("\n Tarefa criada com sucesso!")

def listar_tarefas():
  "lista todas as taredas e permite selecionar uma para editar"
  __print_separator("TAREFAS")

  input = "Digite o numero da tarefa que deseja editar (ou 0 para sair) :"
  editar_tarefa(__select_tarefa(input))

def editar_tarefa(index = None):
  "Muda o status de uma tarefa"

  if index == -1:
    return
  __print_separator("concluir")
  
  if index == None:
    index = __select_tarefa("Digite o numero da tarefa que deseja editar (ou 0 para sair) :")

  global tarefas
  tarefas[index][1] = not tarefas[index][1]
  print(f'\t tarefa "{tarefas[index][0]}" {"" if tarefas[index][1] else "des"}marcada ! '.upper())
  
def remover_tarefa(index = None):
  "Remove uma tarefa"

  if index == -1:
    return
  __print_separator("REMOVER")
  
  if index == None:
    index = __select_tarefa("Digite o numero da tarefa que deseja remover (ou 0 para sair) :")

  if __confirmacao("remover a tarefa "+tarefas[index][0]):
    tarefas.remove(tarefas[index])
    print(f'\t tarefa "{tarefas[index][0]}" removida !')

def __select_tarefa(prompt = ""):
  "seleciona uma tarefa"
  global tarefas
  __print_tarefas()
  
  try:
    inp = int(input(prompt))
  except:
    return __select_tarefa(f"Por favor, digite apenas numeros")
    
  if inp < 0 or inp > len(tarefas)+1:
    return __select_tarefa(f"Não existe tarefa com o numero [{inp}].\n digite um numero entre 1 e {len(tarefas)+1}")
  
  return inp-1

def __print_tarefas():
  "Exibe todas as tarefas"

  global tarefas
  for tarefa in tarefas:
    checkbox = '☑' if tarefa[1] else '☐'
    print(f"\t[{tarefas.index(tarefa)+1}]\t- {checkbox} {tarefa[0]}")
  print('\n')

def __print_separator(name):
  "printa uma separação de tela"
  os.system('clear')
  print(f"______________________________________________________\n\n\t--===  {name.upper()}  ===-- \n")

def __confirmacao(nm_acao = ""):
  "pergunta para o usuario se ele deseja continuar com a ação"
  print("você tem certeza que deseja " + nm_acao + "?")
  i = input("\t digite \"sim\" para confirmar : ")
  
  if i.lower() == "sim":
    return True
  return False

if __name__ == "__main__":
  __main__()