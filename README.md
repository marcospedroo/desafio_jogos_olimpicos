# Desafio Jogos Olimpicos

Neste repositório, você encontrará a solução para o desafio dos Jogos Olímpicos, que consiste na criação de uma API onde
são possíveis as seguintes operações:

1. Criar uma competição
2. Cadastrar resultados para uma competição, 
3. Finalizar uma competição.
4. Retornar o ranking da competição, exibindo a posição final de cada atleta.

## Como executar

1. Criar um virtualenv com Python 3.8 - `virtualenv env`
2. Ativar o virtualenv utilizando - `source env/bin/activate`
3. Instalar as bibliotecas necessárias - `pip install -r requirements.txt`
4. Criar o banco de dados local na estrutura correta - `python manage.py migrate`
5. Iniciar o servidor local - `python manage.py runserver`

## Rotas e payloads

Para este projeto, utilizamos as seguintes rotas:

Para listar todas as competições cadastradas
```
GET http://127.0.0.1:8000/competicoes/
```
Para listar todos os resultados de uma competição específica
```
GET http://127.0.0.1:8000/competicoes/<str:nome_da_competicao>
```

Para iniciar uma competição
```
POST http://127.0.0.1:8000/iniciar_competicao

{
    "nome": "Nome da Competicao",
    "tipo": "L"
}
```

Para adicionar dados a uma competição existente
```
POST http://127.0.0.1:8000/inserir_resultado

{
    "competicao": "Nome da Competicao",
    "atleta": "Nome do Atleta",
    "value": 1000.0,
    "unidade": "m"
}
```

Para finalizar uma competição
```
POST http://127.0.0.1:8000/finalizar_competicao

{
    "nome": "Nome da Competicao"
}
```
