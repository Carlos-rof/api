# Projeto Django - Consumindo APIs do site newsapi - 1.0.0
Este projeto Django tem como objetivo consumir APIs do site https://newsapi.org/ para buscar artigos e exibir informações como o nome do autor, título do artigo e descrição.

## Configuração do Ambiente
* Certifique-se de ter o Python instalado em seu sistema. Recomenda-se usar o Python 3.
* Crie um ambiente virtual para isolar as dependências do projeto:
    **python -m venv meuambiente**
* Ative o ambiente virtual:
    No Windows: **meuambiente\Scripts\activate**
    No Linux/Mac: **source meuambiente/bin/activate**
* Clone o repositório do projeto:
    **git clone https://github.com/seu-usuario/projeto-django-api.git**
* Acesse o diretório do projeto:
    **cd projeto-django-api**
* Instale as dependências do projeto:
    **pip install -r requirements.txt**

## Executando o Projeto
* Execute as migrações para criar o banco de dados:
    **python manage.py makemigrations**
    **python manage.py migrate**
* Inicie o servidor de desenvolvimento:
    **python manage.py runserver**
* Acesse o projeto no navegador em http://localhost:8000/ e verifique se as APIs estão sendo consumidas corretamente e as informações estão sendo exibidas.

## Considerações Finais
Este projeto Django demonstra como consumir APIs do site https://newsapi.org/ para buscar artigos e exibir informações como nome do autor, título do artigo e descrição.