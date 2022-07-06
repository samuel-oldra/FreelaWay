# Aplicação usando Python e Django 4

## FreelaWay - PyStack Week 3.0

Aplicação para contratação de freelances.

Desenvolvida uma aplicação completa para conectar empresas e freelances.

## Tecnologias e práticas utilizadas
- Python
- Django 4
- SQLite
- Arquitetura MVT

## Funcionalidades
- Autenticação e Cadastro de Usuário
- Listagem, Detalhes e Aceite de Jobs
- Atualização de Perfil, Listagem de Jobs Aceitos e Envio de Arquivos

###

![alt text](https://raw.githubusercontent.com/samuel-oldra/FreelaWay/main/README_IMGS/inscreva-se.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/FreelaWay/main/README_IMGS/logar.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/FreelaWay/main/README_IMGS/encontrar_jobs.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/FreelaWay/main/README_IMGS/encontrar_jobs-detalhes.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/FreelaWay/main/README_IMGS/perfil.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/FreelaWay/main/README_IMGS/perfil-detalhes_envio.png)

## Comandos

### pip
```
pip list --outdate
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
```

### virtualenv (windows)
```
python -m venv env
env\Scripts\activate.bat
env\Scripts\deactivate.bat
```

### Instalar bibliotecas, gravar/instalar requerimentos
```
(env) pip install Django
(env) pip install Pillow

(env) pip freeze > requirements.txt
(env) pip install -r requirements.txt
```

### Criar projeto
```
(env) django-admin startproject freelaway .
```

### Criar apps
```
(env) python manage.py startapp autenticacao
(env) python manage.py startapp jobs
```

### Migrations
```
(env) python manage.py makemigrations
(env) python manage.py migrate
```

### Executar projeto
```
(env) python manage.py runserver
```
