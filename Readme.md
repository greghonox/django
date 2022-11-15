# Praticando conceitos de *Django Framework com Python 3.10*.

## O que vamos ver aqui?
### 1. Criação de cadastro simples.
### 2. Consulta de cadastro simples.
### 3. Conexão com banco de dados.
### 4. Migração de modelos de tabelas. (__Veja o histórico do github__)
### 5. Criação de __graficos com bootstrap__.
### 6. Esboço de testes unitários.

## Requisito para rodar projeto
### 1. Ter python <= 3.8.
### 2. Instalar o *requirements.txt*.
### 3. Noção de __Makefile__ e comandos linux.


## Historico do github
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/github_screenshot.png)

## Para começar, __Comandos abaixo funcionan apenas em sistema unix__.

```python
make create-venv
make install-requirements
make run
```

## Acessando o sistema:
[sistema de eventos](http://127.0.0.1:8000/query_metherelogic)

## Você  vera as telas abaixo:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/github_screenshot.png)

## Para cadastrar eventos:
[sistema de eventos cadastros](http://127.0.0.1:8000/register_metherelogic)

## Consultar a tela cadastro:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/register.png)

## Para consultar eventos:
[sistema de eventos consultar](http://127.0.0.1:8000/query_metherelogic)

## Consultar a tela cadastro:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/query.png)

## Admin do django
### Primeiro faça o login para entrar no admin django
[admin django](http://127.0.0.1:8000/admin)

## Credenciais para acesso:
```python
usuario: gregorio
senha: 123
```

## Tela de login:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/login.png)

## Para cadastrar eventos admin:
[sistema de eventos cadastros](http://127.0.0.1:8000/admin/core/eventmetherologic/add/)

## Consultar a tela cadastro admin:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/register_admin.png)

## Para consultar eventos admin:
[sistema de eventos consultar](http://127.0.0.1:8000/admin/core/eventmetherologic/)

## Consultar a tela cadastro admin:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/query_admin.png)

## Inicio de esquema de testes:
![Grafico](https://github.com/greghonox/HidroMar/blob/main/resources/unitary_tests.png)