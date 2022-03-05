# PyStack Week 3.0

Sistema desenvolvido na PyStack Week 3.0

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
(env) pip install django
(env) pip install pillow

(env) pip freeze > requirements.txt
(env) pip install -r requirements.txt
```
### Criar projeto
```
(env) django-admin startproject freelaway .
```
