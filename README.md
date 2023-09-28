<h1 align="center">Django - Básico - Luiz Miranda</h1>

## O que é Django?
- Framework para desenvolvimento web rápido e limpo
- Utilizado por grandes empresas como Instagram, Youtube, Spotify e Dropbox
- Utiliza o padrão MTV (Model, Template, View)
- Utiliza a linguagem Python

### Instalação e criação do projeto

criar a pasta:
```bash
mkdir django-basico
```
criar ambiente virtual:
```bash
python -m venv venv
```
Instalar o Django:
```bash
pip install django
```
Startar projeto django e criar o manage.py:
```bash
django-admin startproject project .
```
Ligar o Servidor:
```bash
python manage.py runserver
```

### Minha primeira URL
<a href="https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status">🔗 HTTP Codes</a>
<bold> views </bold>e <bold>response</bold> 

#### views
Em um aplicativo da web Django, as views são funções ou classes que controlam o que acontece quando um usuário acessa uma URL específica. As views processam as solicitações HTTP dos usuários e retornam uma resposta apropriada. Elas são o ponto central para a lógica de negócios de um aplicativo web Django.

#### response
No contexto das views do Django, uma resposta (response) é o que a view retorna para o navegador do usuário após processar a solicitação HTTP. O objetivo da resposta é enviar dados de volta ao cliente, que podem ser uma página HTML renderizada, dados JSON, uma imagem, um arquivo para download ou até mesmo um redirecionamento para outra URL.

### app
Criar app:
```bash
python manage.py startapp home
```
