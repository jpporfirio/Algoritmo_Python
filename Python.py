import csv

# Adicionando erro ao codigo, para que o arquivo CSV não seja criado com menos que 5 produtos cadastrados
class QtdInsuficiente(Exception):
    def __str__(self):
        return f'É necessário ter no mínimo 5 produtos cadastrados, adicione mais {(5 - len(produtos))} a lista'


# Lista que guardara os novos produtos adicionados
produtos = []

# Loop while, para que o programa só seja encerrado caso solicitado pelo usuário
while True:
    try:
        # Para que o usuário repita até digitar um valor válido
        while True:
            cadastro = input('Deseja cadastrar um novo produto (\033[34mSIM\033[m ou \033[31mNAO\033[m): ').strip().upper().replace(' ', '')
            # O loop é encerrado quando o usuário digita um valor válido
            if cadastro in ('NÃO', 'NAO', 'SIM'):
                break
            # Caso o usuário digite um valor inválido é exibida a mensagem do ocorrido, e o pergunta é feita novamente
            else:
                print('Você digitou um valor inválido')

        # Variavél que inicia/encerra o loop while
        continuar_add = 'SIM'

        # Verificando se o usuário deseja cadastrar algum produto
        if cadastro == 'SIM':

            while continuar_add == 'SIM':
                print('Por gentileza, forneça as seguintes informações.')
                # Criando um dicionário para receber os novos produtos cadastrados
                produtos_add = {}

                # Perguntado e adicionando as informações de cadastro do produto
                produtos_add['ds_produto'] = input('Descrição do produto: ')
                produtos_add['vl_produto'] = input('Valor do produto: R$').replace(',', '.')
                produtos_add['tp_embalagem'] = input('Embalagem do produto: ')

                # Adicionando o dicionário de informações a lista
                produtos.append(produtos_add)
                #
                continuar_add = input(
                    'Se desejar adicionar mais um produto (\033[34mSIM\033[m ou '
                    '\033[31mNAO\033[m): ').strip().upper().replace(' ', '')

            # Verificando se a lista possui mais de 5 produtos
            if len(produtos) < 5:
                raise QtdInsuficiente
            # Perguntando se o usuário deseja salvar os dados
            salvar_dados = input('Deseja salvar os dados fornecidos em um arquivo CSV (\033[34mSIM\033[m ou '
                                 '\033[31mNAO\033[m): ').strip().upper().replace(' ', '')

            if salvar_dados == 'SIM':

                # Nome do arquivo CSV
                nome_arquivo = "1_5_arquivo_produto.csv"

                # Abrir o arquivo CSV em modo de escrita
                with open(nome_arquivo, 'w', newline='') as arquivo_csv:

                    # Criar o escritor CSV
                    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=["ds_produto", "vl_produto", "tp_embalagem"])

                    # Escrever o cabeçalho
                    escritor_csv.writeheader()

                    # Escrever as informações dos produtos
                    for produto in produtos:
                        escritor_csv.writerow(produto)

                print('\033[3;34mArquivo "1_5_arquivo_produto.csv" foi gerado com o cadastro dos produtos')


            # Caso a usuário não queira cadastrar produtos
            elif cadastro in ('NAO', 'NÃO'):
                print('Tudo bem! Estarei disponível quando desejar cadastrar algum produto.')

        # Encerra o loop while (o loop somente é quando todas as condições são estabelecidas e o arquivo CSV
        break

    # Mensagem de erro caso o usuário entre com um valor inválido
    except ValueError as error:
        print(f' \033[31mPor favor entre com um valor compativel ao campo:\033[m"{error}" \n  TENTE ADICIONAR NOVAMENTE!')

    # Mensagem de erro caso o usuário não adicione a quantidade necessária na lista
    except QtdInsuficiente as error:
        print(f'\033[31mNão foi possível adicionar os dados ao arquivo CSV porque: \033[m{error}')

    finally:
        print("Operação concluída.")
