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
Dentro de settings no projeto, inserir o nome do app dentro de INSTALLED_APPS

### Para criar as urls do app:
1. Entrar na pasta do novo app: criar pasta *templates*, criar dentro dela outra pasta, com o mesmo nome do app e criar dentro dele os arquivos HTML.
2. Criar o arquivo *urls.py* dentro da pasta do app, utilizar a extrutura do código abaixo:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```
3. Acessar o views.py e definir a função de renderização do template:
```python
def home(request):
    return render(request, 'home/index.html')
```
4. Dentro da pasta project e dentro de urls.py importar o *include* e inserir dentro do urlpatterns o código abaixo:
```python
path('', include('home.urls')),
```

### Criar outro diretório dentro do mesmo app:
1. Em views dentro do app, repetir o precesso de definir a página.
2. Dentro da pasta do app e dentro de urls.py:
```python
path('pagina2/', views.pagina2),
```
3. Dentro de projects/urls.py:
```python
path('pagina2/', include('home.urls')),
```