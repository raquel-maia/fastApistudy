# FastAPI User Management API

## Descrição

Este projeto é um exemplo de API de gerenciamento de usuários construída com FastAPI. A API permite criar, listar, buscar e deletar usuários. Cada usuário possui um identificador único (UUID), nome, sobrenome, e-mail e uma função (como admin, aluna ou instrutora). Feito com base no curso da WomakersCode de BackEnd com Python 

## Estrutura do Projeto

### Arquivos Principais

- **app.py**: Contém as rotas e a lógica principal da API.
- **models.py**: Define os modelos de dados usados na API.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

Você pode instalar as dependências usando o seguinte comando:

```bash
pip install fastapi uvicorn

## Como executar

    uvicorn app:app --reload

    A aplicação estará disponível em 
    http://127.0.0.1:8000.


## Modelos de Dados

User

id: UUID (opcional, gerado automaticamente)
first_name: string (obrigatório)
last_name: string (obrigatório)
email: string (obrigatório)
role: Lista de roles (obrigatório)
Role
role_1: "admin"
role_2: "aluna"
role_3: "instrutora"

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.