import json
import sys
from app.infrastructure.files.Leitura import Leitura
from app.infrastructure.db.postgres.PostgresUtility import PostgresUtility
from app.utils.GeneralUtility import GeneralUtility

def processo():

    #Importa o arquivo de configuração com os parametros
    with open('app/conf/config.json', 'r') as f:
        config = json.load(f)

    # Ler os dados
    # Obs: Splita quando estiver mais de um espaço em branco
    df = Leitura().read_file(path=config['file_path'], file_name=config['file_name'], extension=config['file_extension'],
                             header_names=config['file_headers'])

    # Transformar dados
    # Adiciona colunas para validar CPF e CNPJ.
    print("Transformando dados...")
    df['cpf_valido'] = df['cpf'].apply(GeneralUtility().validate_cpf)
    print("Terminou transformação de dados...")

    #Escrever dados
    PostgresUtility().escrever_df_postgres(df, config['table_name'])

if __name__ == '__main__':
    try:
        print("Iniciando processo...")
        processo()
        print("Processo finalizado com sucesso!")
    except Exception as err:
        print(f"Erro ao executar o pipeline: {err}.")
        raise err