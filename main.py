lista = []

while True:
  print("ESCOLHA UMA DAS OPÇÕES \n 1-ADICIONAR\n 2-ATUALIZAR\n 3-REMOVER\n 4-ENCERRAR")
  opc = int(input("Digite a opção que deseja: \n"))
  if opc == 1:
    usuario = input("Digite o item que deseja inserir na lista de compras\n")
    lista.append(usuario)
    continuar = input("Deseja continuar ? S/N\n").strip().upper()
    
    if continuar == "N":
      break
    elif continuar == "S":
      continue


  if opc == 2:
    print(f" no momento temos esses items na nossa lista\n {lista}\nPela posicao me informe qual voce deseja alterar")
    posicao = int(input("Digite qual posição da lista de compras deseja alterar: "))
    novoItem = input("Digite o novo item: ")
    lista[posicao] = novoItem
    print(lista)
    continuar = input("Deseja continuar ? S/N\n").strip().upper()
    if continuar == "N":
      break
    elif continuar == "S":
      continue
    
  if opc == 3:
    print(f"Temos todos esses items na lista\n {lista}\n Me informe a posição de qual voce deseja remover !")
    posicaoRemover = int(input("Digite a posição: \n"))
    lista.pop(posicaoRemover)
    print(lista)
    continuar = input("Deseja continuar ? S/N\n").strip().upper()
    
    if continuar == "N":
      break
    elif continuar == "S":
      continue
    
  if opc == 4:
    print(f"ENCERRANDO LISTA DE TAREFAS...\nTODOS OS ITEMS DA SUA LISTA SÃO")
    break
    
    
print(lista)