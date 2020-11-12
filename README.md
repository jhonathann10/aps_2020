##Executar
- docker-compose up --build

##Dependencias
- Instalar as bibliotecas que está no requirements.txt.
- Obs: As dependencias são instaladas quando rodamos o docker-compose up.

##Shut down
- docker-compose down

##Arquivo de configuração
- Para flexibilizar a utilização do serviço, foi criado um arquivo de configuração que possui as caracteristicas do arquivo a ser processado.
```
{
    "file_name": "base_teste", // Nome do arquivo a ser processado.
    "file_path": "app/data",   // Caminho do arquivo a ser processado.
    "file_extension": "txt",   // Extensão do arquivo a ser processado.
    "file_headers": ["cpf"] // Cabeçalhos a serem utilizados no arquivo a ser processado
}
```

##Remover imagens e containers
- docker kill <container-id>
- docker rm <container-id>
- docker rmi Image <nome>

##Para acessar o database atraves do psql
- psql -h localhost -p 5434 -U postgres -d aps