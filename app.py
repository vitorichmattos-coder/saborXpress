import os

restaurantes=[{'nome':'Romanelle','Categoria':'Pizzaria','ativo':False},
            {'nome':'SushiDan','Categoria':'Japonês','ativo':True},
            {'nome':'Instancia','Categoria':'Churrascaria','ativo':False}]



def exibir_nome_do_programa():
    print("\n𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n")

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
                cadastrar_novo_restaurante()    
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
                alternar_estado_rest()
        elif opcao_escolhida ==4:
                fechar_app()
        else:
            opcao_invalida()

    except: 
         opcao_invalida()

def exibir_menu():
    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar estado do Restaurante')
    print('4. Sair \n')



def voltar_menu():
     input('\n Aperte uma tecla para voltar para o menu ')
     main()

def exibir_subtitulo(texto):
     os.system('cls')
     
     linha ='*' * (len(texto))
     print(linha)
     print(texto)
     print(linha)
     print()

     
    


def cadastrar_novo_restaurante():
    "'Essa função cadastra novos restaurantes '"
     
    exibir_subtitulo('Cadastrar restaurante: ')

    nome_do_restaurante= input('Digite o nome do restaurante que desja cadastrar: \n ')
    categ_restaurante=input (f'\nDigite a categoria do restaurente {nome_do_restaurante} que deseja cadastrar \n')

    dados_do_novo_restaurante={'nome':nome_do_restaurante,'Categoria':categ_restaurante,'ativo':False}


    restaurantes.append(dados_do_novo_restaurante)

    print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso !')
     
    voltar_menu()
 
  

     
def listar_restaurantes():

    "'Essa função lista os restaurantes cadastrado'"
    exibir_subtitulo('lista de reataurantes')
    
    print(f'{'Nome do restaurante:'.ljust(21)} | {'Categoria:'.ljust(20)} | ({'Status'})\n')
    for restaurante in restaurantes:
         nome_restaurante = restaurante['nome']
         categ_restaurante = restaurante['Categoria']
         ativo= 'ativado' if restaurante['ativo']else 'Desativado'
         print(f' {categ_restaurante.ljust(20)} | {nome_restaurante.ljust(20)} | ({ativo})')


    voltar_menu()


def alternar_estado_rest():
  "'Essa função alterna o status dos restaurantes (ativado ou desastivado) '"
  exibir_subtitulo("alternado estado")  

  nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: \n ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
   if nome_do_restaurante == restaurante['nome']:
       restaurante_encontrado =True
       restaurante['ativo']= not restaurante['ativo']
       mensagem = f' \n O restaurente {nome_do_restaurante} foi ativado com sucesso ' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso '
       print(mensagem)
  if not restaurante_encontrado:
   print('O restaurante não foi encontrado')

  

  voltar_menu()

def fechar_app():
     "'Essa função fecha o programa '"
     exibir_subtitulo('Fechando o aplicativo...')
     


def opcao_invalida():
    print(' \n Opção Invalida ! \n')
    voltar_menu()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()
