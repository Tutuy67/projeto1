import os
restaurantes=[{"nome": "tutuy food", "categoria": "food","ativo":False},
              {"nome": "tutuy fode truki", "categoria": "truck","ativo":True},
              {"nome": "tutuy sushi de flango kalalio", "categoria": "japones","ativo":False}
             ]

def nome_do_restaurante():
    print('𝒕𝒖𝒕𝒖𝒚 𝒇𝒐𝒐𝒅\n')


###################################################################################################################################################################################################################   


def exibir_opções():
    print('1-cadastrar restaurante')
    print('2-listar restaurante')                                                                                            #mostra opçoes no prompt
    print('3-Ativar restaurante')
    print('4-sair\n')
    
    
###################################################################################################################################################################################################################    


def encerrando_programa(): 
      os.system('cls')                                                                                                       #tela de encerramento de programa
      print("encerrando programa")
      
      
###################################################################################################################################################################################################################   


def  voltar_ao_menu_principal():
   input("\nDigite qualquer tecla para voltar ao menu principal")                                                            #tela de volta ao menu principal
   main() 
   
    
###################################################################################################################################################################################################################      


def exibir_subtitulo(texto):
      os.system("cls")
      print(texto)                                                                                                           #variavel para exibição de texto
      print()
      
      
###################################################################################################################################################################################################################          


def cadstrar_novo_restaurante():
      os.system("cls")
      print("cadastro de novos restaurantes\n")
      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
      restaurantes.append(nome_do_restaurante)                                                                                # tela de cadastro de novo restaurante
      print(f"o restaurante {nome_do_restaurante}  foi cadastrado com sucesso")
      voltar_ao_menu_principal()
      main()
      
      
###################################################################################################################################################################################################################         


def listar_restaurantes():
   exibir_subtitulo("Listando os restaurantes")
   
   for restaurante in restaurantes:
       nome_do_restaurante = restaurante["nome"]                                                                               #variável (mostra de lista de restaurantes)
       print(f".{nome_do_restaurante}")   
      
      
###################################################################################################################################################################################################################        


# def ativar_restaurante():
#os.system("cls")
#print("ativando restaurante")                                                                                                  #Variável (ativa restaurantes)

    
###################################################################################################################################################################################################################          


def escolher_op():

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
         print ('ativar restaurante')
      elif opcao_escolhida == 4:    
         encerrando_programa()
      else:
         opcao_invalida()
   except:
        opcao_invalida() 
        
           
###################################################################################################################################################################################################################           


def    opcao_invalida():
       print("opção invalida\n")                                                                                                #variável
       voltar_ao_menu_principal()
       
       
###################################################################################################################################################################################################################          


def encerrando_programa(): 
   exibir_subtitulo("Encerrando programa")                                                                                      #variável
   
   
###################################################################################################################################################################################################################   


def cadastrar_novo_restaurante():
   exibir_subtitulo("Cadastro de novos restaurantes")                                                                          #variável
   
   
###################################################################################################################################################################################################################   
          

def main():
        os.system('cls')
        nome_do_restaurante()
        exibir_opções()                                                                                                       #Volta tela 
        escolher_op()
        
if __name__ == "__main__":
        main()
        
###################################################################################################################################################################################################################   