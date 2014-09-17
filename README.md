## Configuración


### Instalar `python social auth`

* [Instalación](http://python-social-auth.readthedocs.org/en/latest/installing.html)


### Agregar los siguientes valores a settings.py


* Agregar `socialregister.users` a `INSTALLED_APPS`


* Definir la tupla `AUTHENTICATION_BACKENDS`, siempre debe incluir el backend `django.contrib.auth.backends.ModelBackend`

* Definir la tupla `SOCIAL_AUTH_PIPELINE`

| setting                                    | descripción                |
|--------------------------------------------|----------------------------|
| `SOCIAL_AUTH_LOGIN_REDIRECT_URL = '<url>'` | Redirige al usuario una vez terminado el proceso de autenticación |
| `SOCIAL_AUTH_LOGIN_ERROR_URL = '<url>'`    | Redirige al usuario en caso de error de autenticación |
| `SOCIAL_AUTH_LOGIN_URL = '<url>'`          | Se utiliza como una retrollamada para `LOGIN_ERROR_URL` |
| `AUTH_USER_MODEL = '<user_model>`          | Establece el modelo de usuario |
| `SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = <boolean>` | Define que el nombre de usuario sera el email |


## Configuración para autenticacion con `Facebook`

* `SOCIAL_AUTH_FACEBOOK_KEY = '<key>'`
* `SOCIAL_AUTH_FACEBOOK_SECRET = '<secret>'`
* `SOCIAL_AUTH_FACEBOOK_SCOPE = [<scope>]`
