import os
restaurantes=[{"nome": "tutuy food", "categoria": "food","ativo":False},
              {"nome": "tutuy fode truki", "categoria": "truck","ativo":True},
              {"nome": "tutuy sushi de flango", "categoria": "japones","ativo":False}
             ]

def nome_do_restaurante():
   """Essa função é responsável por demonstrar o nome do restaurante"""
   print('𝒕𝒖𝒕𝒖𝒚 𝒇𝒐𝒐𝒅\n')


###################################################################################################################################################################################################################   


def exibir_opções():
   """Essa função é responsável por mostrar opções"""
   print('1-cadastrar restaurante')
   print('2-listar restaurante')                                                                                            #mostra opçoes no prompt
   print('3-Alternar estado do restaurante')
   print('4-sair\n')
    
    
###################################################################################################################################################################################################################    


def encerrando_programa(): 
   """Essa função é responsável por encerramento do programa"""
   os.system('cls')                                                                                                       #tela de encerramento de programa
   print("encerrando programa")
      
      
###################################################################################################################################################################################################################   


def  voltar_ao_menu_principal():
   """Essa função é responsável por voltar ao menu"""
   input("\nDigite qualquer tecla para voltar ao menu principal")                                                            #tela de volta ao menu principal
   main() 
   
    
###################################################################################################################################################################################################################      


def exibir_subtitulo(texto):
   """Essa função é responsável por exibir o titulo"""
   os.system("cls")
   linha = "-" * (len(texto))                                                                                                          #variavel para exibição de titulo'
   print(linha)
   print(texto)
   print(linha)
   print()
      
      
###################################################################################################################################################################################################################          


def cadstrar_novo_restaurante():
   
   """Essa função é responsável por cadastrar novo restaurante"""
   
   exibir_subtitulo("Cadastro de novos restaurantes")                                                                          #variável de cadastrar
   
   nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
   categoria = input(f"Digite o nome da categoria do restaureante {nome_do_restaurante}: ")
   dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo":False}
   restaurantes.append(dados_do_restaurante)
   print(f"o restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
   
   voltar_ao_menu_principal()
   
###################################################################################################################################################################################################################       


def listar_restaurantes():
   """Essa função é responsável por listar os restaurantes"""
   exibir_subtitulo("Listando os restaurantes")
  
   for restaurante in restaurantes:
       nome_do_restaurante = restaurante ["nome"] 
       categoria = restaurante ["categoria"]
       ativo = "ativado" if restaurante ["ativo"] else "desativado"                                                                                       #variável (mostra de lista de restaurantes)
       print(f" - {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
       
   voltar_ao_menu_principal()       
    
      
###################################################################################################################################################################################################################        
     

def alternar_estado_restaurante():
   """Essa função é responsável por alterar o estado do restaurante"""
   exibir_subtitulo("alternando estado do restaurante")
   nome_do_restaurante = input("Digite o nome do restaurante que deseja alternar o estado")
   restaurante_encontrado = False  

   for restaurante in restaurantes:
      if nome_do_restaurante == restaurante ["nome"]:                                                                            #variável (ativa o restaurante)
         restaurante_encontrado = True
         restaurante ["ativo"] = not restaurante ["ativo"]
         mensagem = f"o restaurante {nome_do_restaurante} foi ativado com sucesso" if restaurante ["ativo"] else f"o restaurante {nome_do_restaurante} foi desativado com sucesso"
         print(mensagem)
   if not restaurante_encontrado:
      print("o restaurante nao foi encontrado")
      
      voltar_ao_menu_principal()               
         
###################################################################################################################################################################################################################   

   
def escolher_op():
   """Essa função é responsável por escolha das opções"""

   try:
      opcao_escolhida= int(input('digite uma opcao:'))
      print(f'voce escolheu a opcao:{opcao_escolhida}\n')
   
      if opcao_escolhida == 1:
         cadstrar_novo_restaurante()
         print ('cadastrar restaurante')
      elif opcao_escolhida == 2:                                                                                              #escolha de opçoes no prompt
         listar_restaurantes()
         print('listar restaurante')
      elif opcao_escolhida == 3:
         alternar_estado_restaurante()
      elif opcao_escolhida == 4:    
         encerrando_programa()
      else:
         opcao_invalida()
   except:
        opcao_invalida() 
        
           
###################################################################################################################################################################################################################           


def    opcao_invalida():
   """Essa função é responsável por invalidar uma escolha"""
   print("opção invalida\n")                                                                                                #variável
   voltar_ao_menu_principal()
       
       
###################################################################################################################################################################################################################          


def encerrando_programa():
   """Essa função é responsável por encerrar programa subtitulo"""
   exibir_subtitulo("Encerrando programa")                                                                                      #variável
   
   
###################################################################################################################################################################################################################   
         
def main():
   """Essa função é responsável por voltar tela"""
   os.system('cls')
   nome_do_restaurante()
   exibir_opções()                                                                                                       #Volta tela 
   escolher_op()
        
if __name__ == "__main__":
        main()
        
###################################################################################################################################################################################################################   